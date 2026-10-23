import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.indicator import FrequencyType, TargetOrientationType

class IndicatorBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    departamento_id: int
    categoria_id: Optional[int] = None
    unidad_medida: str
    frecuencia: FrequencyType = FrequencyType.MENSUAL
    tipo_meta: TargetOrientationType = TargetOrientationType.ASCENDENTE
    meta_referencial: Optional[float] = None
    activo: bool = True

class IndicatorCreate(IndicatorBase):
    pass

class IndicatorResponse(IndicatorBase):
    id: uuid.UUID
    departamento_codigo: Optional[str] = None
    departamento_nombre: Optional[str] = None
    categoria_nombre: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
