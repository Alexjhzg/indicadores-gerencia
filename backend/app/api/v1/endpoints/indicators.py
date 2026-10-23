import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_active_user
from app.models.indicator import Indicator
from app.models.department import Department
from app.models.category import Category
from app.models.user import User
from app.schemas.indicator import IndicatorResponse, IndicatorCreate

router = APIRouter()

@router.get("/", response_model=List[IndicatorResponse])
def get_indicators(
    departamento_id: Optional[int] = None,
    activo_solo: bool = True,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Lista los indicadores del catálogo técnico. Puede filtrarse por departamento.
    """
    query = db.query(Indicator)
    
    # Restricción RBAC: Jefes de Unidad (ENCARGADO) solo pueden consultar indicadores de su unidad técnica
    if current_user.rol.nombre == "ENCARGADO" and current_user.departamento_id:
        query = query.filter(Indicator.departamento_id == current_user.departamento_id)
    elif departamento_id is not None:
        query = query.filter(Indicator.departamento_id == departamento_id)

    if activo_solo:
        query = query.filter(Indicator.activo == True)

    indicators = query.order_by(Indicator.codigo).all()
    res = []
    for ind in indicators:
        dept = db.query(Department).filter(Department.id == ind.departamento_id).first()
        cat = db.query(Category).filter(Category.id == ind.categoria_id).first() if ind.categoria_id else None
        
        res.append(IndicatorResponse(
            id=ind.id,
            codigo=ind.codigo,
            nombre=ind.nombre,
            descripcion=ind.descripcion,
            departamento_id=ind.departamento_id,
            categoria_id=ind.categoria_id,
            unidad_medida=ind.unidad_medida,
            frecuencia=ind.frecuencia,
            tipo_meta=ind.tipo_meta,
            meta_referencial=float(ind.meta_referencial) if ind.meta_referencial is not None else None,
            activo=ind.activo,
            departamento_codigo=dept.codigo if dept else None,
            departamento_nombre=dept.nombre if dept else None,
            categoria_nombre=cat.nombre if cat else None,
            created_at=ind.created_at,
            updated_at=ind.updated_at
        ))
    return res

@router.get("/{indicator_id}", response_model=IndicatorResponse)
def get_indicator_by_id(
    indicator_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtiene la ficha técnica completa de un indicador.
    """
    ind = db.query(Indicator).filter(Indicator.id == indicator_id).first()
    if not ind:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Indicador no encontrado."
        )
    dept = db.query(Department).filter(Department.id == ind.departamento_id).first()
    cat = db.query(Category).filter(Category.id == ind.categoria_id).first() if ind.categoria_id else None
    
    return IndicatorResponse(
        id=ind.id,
        codigo=ind.codigo,
        nombre=ind.nombre,
        descripcion=ind.descripcion,
        departamento_id=ind.departamento_id,
        categoria_id=ind.categoria_id,
        unidad_medida=ind.unidad_medida,
        frecuencia=ind.frecuencia,
        tipo_meta=ind.tipo_meta,
        meta_referencial=float(ind.meta_referencial) if ind.meta_referencial is not None else None,
        activo=ind.activo,
        departamento_codigo=dept.codigo if dept else None,
        departamento_nombre=dept.nombre if dept else None,
        categoria_nombre=cat.nombre if cat else None,
        created_at=ind.created_at,
        updated_at=ind.updated_at
    )
