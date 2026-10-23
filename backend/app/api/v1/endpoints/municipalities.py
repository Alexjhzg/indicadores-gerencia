from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_active_user
from app.models.municipality import Municipality
from app.models.user import User
from app.schemas.municipality import MunicipalityResponse

router = APIRouter()

@router.get("/", response_model=List[MunicipalityResponse])
def get_municipalities(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Lista los 13 municipios del Estado Monagas con su código INE oficial DPT (1601 al 1613).
    """
    return db.query(Municipality).order_by(Municipality.id).all()
