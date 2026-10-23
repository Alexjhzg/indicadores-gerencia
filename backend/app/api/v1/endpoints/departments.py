from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_active_user
from app.models.department import Department
from app.models.user import User
from app.schemas.department import DepartmentResponse

router = APIRouter()

@router.get("/", response_model=List[DepartmentResponse])
def get_departments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Lista todos los departamentos oficiales del INE Monagas (ECO, SOC, DEM, CART, SEG).
    Para Jefes de Unidad (ENCARGADO), solo devuelve su propia unidad asignada.
    """
    query = db.query(Department).filter(Department.activo == True)
    if current_user.rol.nombre == "ENCARGADO" and current_user.departamento_id:
        query = query.filter(Department.id == current_user.departamento_id)
    return query.order_by(Department.id).all()
