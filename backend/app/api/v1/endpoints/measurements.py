import uuid
from typing import List, Optional
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.api.deps import get_db, get_current_active_user, check_department_permission
from app.models.measurement import IndicatorMeasurement, MeasurementStatus
from app.models.indicator import Indicator
from app.models.department import Department
from app.models.municipality import Municipality
from app.models.role import Role
from app.models.user import User
from app.schemas.measurement import (
    MeasurementCreate,
    MeasurementUpdate,
    MeasurementResponse,
    MeasurementBatchItem,
    BatchMeasurementCreate,
    BatchMeasurementResponse,
    UnitCertifyResponse
)
from app.schemas.version import MeasurementVersionResponse, RollbackRequest, VersionDiffResponse
from app.services.versioning_service import VersioningService

router = APIRouter()

def build_measurement_response(m: IndicatorMeasurement, db: Session) -> MeasurementResponse:
    ind = db.query(Indicator).filter(Indicator.id == m.indicador_id).first()
    dept = db.query(Department).filter(Department.id == ind.departamento_id).first() if ind else None
    mun = db.query(Municipality).filter(Municipality.id == m.municipio_id).first() if m.municipio_id else None

    cumplimiento = None
    if m.meta_periodo and float(m.meta_periodo) > 0:
        cumplimiento = round((float(m.valor_registrado) / float(m.meta_periodo)) * 100, 2)

    return MeasurementResponse(
        id=m.id,
        indicador_id=m.indicador_id,
        indicador_codigo=ind.codigo if ind else None,
        indicador_nombre=ind.nombre if ind else None,
        departamento_codigo=dept.codigo if dept else None,
        municipio_id=m.municipio_id,
        municipio_nombre=mun.nombre if mun else "Consolidado Estadal",
        periodo_anio=m.periodo_anio,
        periodo_tipo=m.periodo_tipo,
        periodo_mes=m.periodo_mes,
        valor_registrado=float(m.valor_registrado),
        meta_periodo=float(m.meta_periodo) if m.meta_periodo is not None else None,
        porcentaje_cumplimiento=cumplimiento,
        estado=m.estado,
        version=m.version,
        observaciones=m.observaciones,
        registrado_por=m.registrado_por,
        aprobado_por=m.aprobado_por,
        created_at=m.created_at,
        updated_at=m.updated_at
    )

@router.get("/", response_model=List[MeasurementResponse])
def list_measurements(
    indicador_id: Optional[uuid.UUID] = None,
    departamento_id: Optional[int] = None,
    municipio_id: Optional[int] = None,
    periodo_anio: Optional[int] = Query(None, ge=2000, le=2100),
    periodo_mes: Optional[int] = Query(None, ge=1, le=12),
    estado: Optional[MeasurementStatus] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Lista las mediciones registradas con filtros opcionales de departamento, municipio, año y mes.
    """
    query = db.query(IndicatorMeasurement)

    # Restricción RBAC:
    user_role_name = current_user.rol.nombre if current_user.rol else "ENCARGADO"
    if user_role_name == "ENCARGADO" and current_user.departamento_id:
        query = query.join(Indicator).filter(Indicator.departamento_id == current_user.departamento_id)
    elif user_role_name == "JEFE_AREA":
        assigned_ids = [d.id for d in current_user.departamentos_asignados]
        if not assigned_ids:
            assigned_ids = [d.id for d in db.query(Department).filter(Department.codigo.in_(["CART", "ECO", "SOC", "SEG"])).all()]
        if departamento_id:
            if departamento_id in assigned_ids:
                query = query.join(Indicator).filter(Indicator.departamento_id == departamento_id)
            else:
                return []
        else:
            query = query.join(Indicator).filter(Indicator.departamento_id.in_(assigned_ids))
    elif departamento_id:
        query = query.join(Indicator).filter(Indicator.departamento_id == departamento_id)

    if indicador_id:
        query = query.filter(IndicatorMeasurement.indicador_id == indicador_id)
    if municipio_id is not None:
        query = query.filter(IndicatorMeasurement.municipio_id == municipio_id)
    if periodo_anio:
        query = query.filter(IndicatorMeasurement.periodo_anio == periodo_anio)
    if periodo_mes:
        query = query.filter(IndicatorMeasurement.periodo_mes == periodo_mes)
    if estado:
        query = query.filter(IndicatorMeasurement.estado == estado)

    measurements = query.order_by(IndicatorMeasurement.periodo_anio.desc(), IndicatorMeasurement.periodo_mes.desc()).all()
    return [build_measurement_response(m, db) for m in measurements]

@router.post("/", response_model=MeasurementResponse, status_code=status.HTTP_201_CREATED)
def create_measurement(
    data: MeasurementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Crea una nueva medición en estado inicial BORRADOR. Dispara automáticamente la Versión 1.
    """
    ind = db.query(Indicator).filter(Indicator.id == data.indicador_id).first()
    if not ind:
        raise HTTPException(status_code=404, detail="Indicador no encontrado.")

    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    if not check_department_permission(current_user, ind.departamento_id, role_name, db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permiso para registrar datos en este departamento."
        )

    # Validar que no exista registro previo para el mismo periodo y territorio
    existing = db.query(IndicatorMeasurement).filter(
        IndicatorMeasurement.indicador_id == data.indicador_id,
        IndicatorMeasurement.municipio_id == data.municipio_id,
        IndicatorMeasurement.periodo_anio == data.periodo_anio,
        IndicatorMeasurement.periodo_tipo == data.periodo_tipo,
        IndicatorMeasurement.periodo_mes == data.periodo_mes
    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una medición registrada para este indicador en el periodo y municipio especificados."
        )

    new_measurement = IndicatorMeasurement(
        indicador_id=data.indicador_id,
        municipio_id=data.municipio_id,
        periodo_anio=data.periodo_anio,
        periodo_tipo=data.periodo_tipo,
        periodo_mes=data.periodo_mes,
        valor_registrado=data.valor_registrado,
        meta_periodo=data.meta_periodo,
        estado=MeasurementStatus.BORRADOR,
        observaciones=data.observaciones,
        registrado_por=current_user.id,
        aprobado_por=None
    )
    db.add(new_measurement)
    db.commit()
    db.refresh(new_measurement)

    return build_measurement_response(new_measurement, db)

@router.post("/lote", response_model=BatchMeasurementResponse)
def create_or_update_batch(
    data: BatchMeasurementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Carga masiva o por formulario de mediciones mensuales para una unidad técnica.
    Valida permisos RBAC, actualiza o crea mediciones y genera versionado atómico.
    """
    dept_code = data.departamento_codigo.strip().upper()
    dept = db.query(Department).filter(Department.codigo == dept_code).first()
    if not dept:
        raise HTTPException(status_code=404, detail=f"Unidad técnica con código {dept_code} no encontrada.")

    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    if not check_department_permission(current_user, dept.id, role_name, db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"No tiene permiso para cargar cifras en la {dept.nombre}."
        )

    creados = 0
    actualizados = 0
    resultados = []

    for item in data.mediciones:
        ind = None
        if item.indicador_id:
            ind = db.query(Indicator).filter(Indicator.id == item.indicador_id).first()
        elif item.indicador_codigo:
            ind = db.query(Indicator).filter(
                Indicator.codigo == item.indicador_codigo.strip(),
                Indicator.departamento_id == dept.id
            ).first()

        if not ind:
            continue

        existing = db.query(IndicatorMeasurement).filter(
            IndicatorMeasurement.indicador_id == ind.id,
            IndicatorMeasurement.municipio_id == item.municipio_id,
            IndicatorMeasurement.periodo_anio == data.periodo_anio,
            IndicatorMeasurement.periodo_tipo == data.periodo_tipo,
            IndicatorMeasurement.periodo_mes == data.periodo_mes
        ).first()

        if existing:
            existing.valor_registrado = item.valor_registrado
            if item.meta_periodo is not None:
                existing.meta_periodo = item.meta_periodo
            existing.observaciones = f"Actualizado por {current_user.cedula}: {item.motivo_cambio or data.motivo_general}"
            existing.updated_at = datetime.now(timezone.utc)
            db.flush()
            actualizados += 1
            resultados.append(existing)
        else:
            new_m = IndicatorMeasurement(
                indicador_id=ind.id,
                municipio_id=item.municipio_id,
                periodo_anio=data.periodo_anio,
                periodo_tipo=data.periodo_tipo,
                periodo_mes=data.periodo_mes,
                valor_registrado=item.valor_registrado,
                meta_periodo=item.meta_periodo,
                estado=MeasurementStatus.BORRADOR,
                observaciones=item.observaciones or data.motivo_general,
                registrado_por=current_user.id
            )
            db.add(new_m)
            db.flush()
            creados += 1
            resultados.append(new_m)

    db.commit()

    return BatchMeasurementResponse(
        mensaje=f"Procesamiento exitoso para {dept.nombre}. {creados} mediciones creadas, {actualizados} actualizadas.",
        departamento_codigo=dept.codigo,
        periodo_anio=data.periodo_anio,
        periodo_mes=data.periodo_mes,
        total_procesados=len(resultados),
        total_creados=creados,
        total_actualizados=actualizados,
        mediciones=[build_measurement_response(m, db) for m in resultados]
    )

@router.get("/periodos-disponibles")
def get_available_periods(
    departamento_codigo: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retorna exclusivamente los años y meses que tienen mediciones registradas en la base de datos,
    opcionalmente filtrados por unidad técnica.
    """
    query = (
        db.query(
            IndicatorMeasurement.periodo_anio,
            IndicatorMeasurement.periodo_mes,
            func.count(IndicatorMeasurement.id).label("total_mediciones")
        )
        .join(Indicator, Indicator.id == IndicatorMeasurement.indicador_id)
    )

    if departamento_codigo:
        dept = db.query(Department).filter(Department.codigo == departamento_codigo.strip().upper()).first()
        if dept:
            query = query.filter(Indicator.departamento_id == dept.id)
    else:
        role_name = current_user.rol.nombre if current_user.rol else "ENCARGADO"
        if role_name == "ENCARGADO" and current_user.departamento_id:
            query = query.filter(Indicator.departamento_id == current_user.departamento_id)
        elif role_name == "JEFE_AREA":
            assigned_ids = [d.id for d in current_user.departamentos_asignados]
            if not assigned_ids:
                assigned_ids = [d.id for d in db.query(Department).filter(Department.codigo.in_(["CART", "ECO", "SOC", "SEG"])).all()]
            query = query.filter(Indicator.departamento_id.in_(assigned_ids))

    rows = (
        query.group_by(IndicatorMeasurement.periodo_anio, IndicatorMeasurement.periodo_mes)
        .order_by(IndicatorMeasurement.periodo_anio.desc(), IndicatorMeasurement.periodo_mes.desc())
        .all()
    )

    meses_nombres = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }

    anios_set = sorted(list(set(r.periodo_anio for r in rows)), reverse=True)
    
    periodos = []
    for r in rows:
        periodos.append({
            "anio": r.periodo_anio,
            "mes": r.periodo_mes,
            "mes_nombre": meses_nombres.get(r.periodo_mes, f"Mes {r.periodo_mes}"),
            "total_mediciones": r.total_mediciones
        })

    if not periodos:
        anios_set = [2026]
        periodos = [{"anio": 2026, "mes": 8, "mes_nombre": "Agosto", "total_mediciones": 0}]

    return {
        "departamento_codigo": departamento_codigo,
        "anios": anios_set,
        "periodos": periodos
    }

@router.get("/unidad/{dept_code}")
def get_unit_monthly_measurements(
    dept_code: str,
    periodo_anio: int = Query(2026, ge=2000, le=2100),
    periodo_mes: int = Query(8, ge=1, le=12),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtiene todos los indicadores de la unidad y sus mediciones registradas en el período especificado.
    """
    code = dept_code.strip().upper()
    dept = db.query(Department).filter(Department.codigo == code).first()
    if not dept:
        raise HTTPException(status_code=404, detail=f"Unidad {code} no encontrada.")

    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    if not check_department_permission(current_user, dept.id, role_name, db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Acceso restringido: No tiene autorización sobre la {dept.nombre}."
        )

    indicators = db.query(Indicator).filter(
        Indicator.departamento_id == dept.id,
        Indicator.activo == True
    ).order_by(Indicator.codigo.asc()).all()

    items = []
    total_aprobados = 0
    total_medidos = 0

    for ind in indicators:
        m = db.query(IndicatorMeasurement).filter(
            IndicatorMeasurement.indicador_id == ind.id,
            IndicatorMeasurement.municipio_id == None,
            IndicatorMeasurement.periodo_anio == periodo_anio,
            IndicatorMeasurement.periodo_mes == periodo_mes
        ).first()

        med_data = None
        if m:
            total_medidos += 1
            if m.estado == MeasurementStatus.APROBADO:
                total_aprobados += 1
            med_data = build_measurement_response(m, db)

        items.append({
            "indicador": {
                "id": str(ind.id),
                "codigo": ind.codigo,
                "nombre": ind.nombre,
                "unidad_medida": ind.unidad_medida,
                "frecuencia": ind.frecuencia,
                "meta_referencial": float(ind.meta_referencial) if ind.meta_referencial else None
            },
            "medicion": med_data
        })

    estado_general = "SIN_DATOS"
    if total_medidos > 0:
        if total_aprobados == total_medidos:
            estado_general = "CERTIFICADO"
        elif total_aprobados > 0:
            estado_general = "PARCIALMENTE_CERTIFICADO"
        else:
            estado_general = "BORRADOR"

    return {
        "departamento_codigo": dept.codigo,
        "departamento_nombre": dept.nombre,
        "periodo_anio": periodo_anio,
        "periodo_mes": periodo_mes,
        "estado_general": estado_general,
        "total_indicadores": len(indicators),
        "total_medidos": total_medidos,
        "total_aprobados": total_aprobados,
        "items": items
    }

@router.post("/unidad/{dept_code}/certificar", response_model=UnitCertifyResponse)
def certify_unit_monthly_measurements(
    dept_code: str,
    periodo_anio: int = Query(2026, ge=2000, le=2100),
    periodo_mes: int = Query(8, ge=1, le=12),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Certifica y aprueba en bloque todas las mediciones de la unidad en el período indicado.
    """
    code = dept_code.strip().upper()
    dept = db.query(Department).filter(Department.codigo == code).first()
    if not dept:
        raise HTTPException(status_code=404, detail=f"Unidad {code} no encontrada.")

    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    if not check_department_permission(current_user, dept.id, role_name, db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Solo el personal autorizado de la {dept.nombre} o Gerencia puede certificar las cifras."
        )

    measurements = (
        db.query(IndicatorMeasurement)
        .join(Indicator)
        .filter(
            Indicator.departamento_id == dept.id,
            IndicatorMeasurement.periodo_anio == periodo_anio,
            IndicatorMeasurement.periodo_mes == periodo_mes
        )
        .all()
    )

    if not measurements:
        raise HTTPException(
            status_code=400,
            detail=f"No hay mediciones registradas para {dept.nombre} en el período {periodo_mes}/{periodo_anio} para certificar."
        )

    for m in measurements:
        m.estado = MeasurementStatus.APROBADO
        m.aprobado_por = current_user.id
        m.observaciones = f"Certificado oficialmente por {current_user.nombre_completo} ({current_user.cedula})"
        m.updated_at = datetime.now(timezone.utc)

    db.commit()

    return UnitCertifyResponse(
        mensaje=f"Se han certificado exitosamente {len(measurements)} indicadores de la {dept.nombre} para el período {periodo_mes}/{periodo_anio}.",
        departamento_codigo=dept.codigo,
        periodo_anio=periodo_anio,
        periodo_mes=periodo_mes,
        total_certificados=len(measurements),
        certificados_por=f"{current_user.nombre_completo} ({current_user.cedula})"
    )

@router.put("/{measurement_id}", response_model=MeasurementResponse)
def update_measurement(
    measurement_id: uuid.UUID,
    data: MeasurementUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Actualiza el valor de una medición existente. Exige un motivo de cambio y genera una nueva versión en el historial.
    """
    m = db.query(IndicatorMeasurement).filter(IndicatorMeasurement.id == measurement_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Medición no encontrada.")

    ind = db.query(Indicator).filter(Indicator.id == m.indicador_id).first()
    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    if not check_department_permission(current_user, ind.departamento_id, role_name, db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permiso para modificar mediciones de este departamento."
        )

    if data.valor_registrado is not None:
        m.valor_registrado = data.valor_registrado
    if data.meta_periodo is not None:
        m.meta_periodo = data.meta_periodo
    
    # El motivo de cambio alimenta la observación y el snapshot de versión
    m.observaciones = f"Modificado por {current_user.cedula}: {data.motivo_cambio}"
    m.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(m)
    return build_measurement_response(m, db)

@router.post("/{measurement_id}/aprobar", response_model=MeasurementResponse)
def approve_measurement(
    measurement_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Permite al Encargado de la unidad certificar y pasar la medición a estado APROBADO, haciéndola oficial.
    """
    m = db.query(IndicatorMeasurement).filter(IndicatorMeasurement.id == measurement_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Medición no encontrada.")

    ind = db.query(Indicator).filter(Indicator.id == m.indicador_id).first()
    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    if not check_department_permission(current_user, ind.departamento_id, role_name):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo el personal autorizado de esta unidad puede aprobar la medición."
        )

    m.estado = MeasurementStatus.APROBADO
    m.aprobado_por = current_user.id
    m.observaciones = f"Aprobado y certificado oficialmente por {current_user.nombre_completo} ({current_user.cedula})"
    m.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(m)
    return build_measurement_response(m, db)

@router.get("/{measurement_id}/versiones", response_model=List[MeasurementVersionResponse])
def get_versions(
    measurement_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtiene el historial completo de versiones de una medición (snapshots inmutables).
    """
    versions = VersioningService.get_measurement_versions(db, measurement_id)
    res = []
    for v in versions:
        u = db.query(User).filter(User.id == v.modificado_por).first() if v.modificado_por else None
        cumplimiento = None
        if v.meta_periodo and float(v.meta_periodo) > 0:
            cumplimiento = round((float(v.valor_registrado) / float(v.meta_periodo)) * 100, 2)

        res.append(MeasurementVersionResponse(
            id=v.id,
            medicion_id=v.medicion_id,
            numero_version=v.numero_version,
            valor_registrado=float(v.valor_registrado),
            meta_periodo=float(v.meta_periodo) if v.meta_periodo is not None else None,
            porcentaje_cumplimiento=cumplimiento,
            estado=v.estado,
            tipo_accion=v.tipo_accion,
            motivo_cambio=v.motivo_cambio,
            modificado_por=v.modificado_por,
            modificado_por_nombre=u.nombre_completo if u else None,
            modificado_por_cedula=u.cedula if u else None,
            created_at=v.created_at
        ))
    return res

@router.post("/{measurement_id}/revertir", response_model=dict)
def rollback_measurement(
    measurement_id: uuid.UUID,
    rollback_data: RollbackRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Ejecuta el Rollback atómico a una versión histórica sana.
    """
    m = db.query(IndicatorMeasurement).filter(IndicatorMeasurement.id == measurement_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Medición no encontrada.")

    ind = db.query(Indicator).filter(Indicator.id == m.indicador_id).first()
    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    if not check_department_permission(current_user, ind.departamento_id, role_name):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permiso para ejecutar reversiones en este departamento."
        )

    try:
        result = VersioningService.rollback_measurement_version(
            db=db,
            measurement_id=measurement_id,
            target_version=rollback_data.version_destino,
            user_id=current_user.id,
            reason=rollback_data.motivo
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{measurement_id}/diff", response_model=VersionDiffResponse)
def get_version_diff(
    measurement_id: uuid.UUID,
    version_from: int = Query(..., ge=1),
    version_to: int = Query(..., ge=1),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Compara dos versiones de una medición para identificar qué causó la alteración de las estadísticas.
    """
    try:
        diff = VersioningService.get_version_diff(
            db=db,
            measurement_id=measurement_id,
            version_from=version_from,
            version_to=version_to
        )
        return diff
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
