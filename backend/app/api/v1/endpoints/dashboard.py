from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.api.deps import get_db, get_current_active_user
from app.models.user import User
from app.schemas.dashboard import DashboardSummaryResponse, DepartmentKpi

router = APIRouter()

@router.get("/resumen", response_model=DashboardSummaryResponse)
def get_dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retorna el resumen ejecutivo consolidado del estado Monagas y el desglose de los 5 departamentos clave.
    Acceso restringido exclusivamente a Gerente y Administrador.
    """
    if current_user.rol.nombre == "ENCARGADO":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso restringido: El Resumen Ejecutivo está reservado para la Gerencia Estadal. Los Jefes de Unidad solo tienen acceso a su propia unidad técnica."
        )
    query = text("""
        SELECT 
            departamento_id,
            departamento_codigo,
            departamento_nombre,
            total_indicadores,
            total_mediciones_registradas,
            mediciones_aprobadas,
            mediciones_pendientes_aprobacion,
            porcentaje_cumplimiento_promedio
        FROM v_dashboard_central_resumen
        ORDER BY departamento_id;
    """)
    rows = db.execute(query).fetchall()

    dept_kpis = []
    total_cumplimiento = 0.0
    depts_con_cumplimiento = 0
    total_indicadores = 0
    total_aprobadas = 0

    for r in rows:
        cumplimiento = float(r.porcentaje_cumplimiento_promedio) if r.porcentaje_cumplimiento_promedio is not None else None
        if cumplimiento is not None:
            total_cumplimiento += cumplimiento
            depts_con_cumplimiento += 1

        total_indicadores += r.total_indicadores
        total_aprobadas += r.mediciones_aprobadas

        dept_kpis.append(DepartmentKpi(
            departamento_id=r.departamento_id,
            departamento_codigo=r.departamento_codigo,
            departamento_nombre=r.departamento_nombre,
            total_indicadores=r.total_indicadores,
            total_mediciones_registradas=r.total_mediciones_registradas,
            mediciones_aprobadas=r.mediciones_aprobadas,
            mediciones_pendientes_aprobacion=r.mediciones_pendientes_aprobacion,
            porcentaje_cumplimiento_promedio=cumplimiento
        ))

    promedio_global = round(total_cumplimiento / depts_con_cumplimiento, 2) if depts_con_cumplimiento > 0 else 0.0

    return DashboardSummaryResponse(
        total_departamentos=len(dept_kpis),
        cumplimiento_general_estadal=promedio_global,
        total_indicadores_activos=total_indicadores,
        total_mediciones_aprobadas=total_aprobadas,
        departamentos=dept_kpis
    )
