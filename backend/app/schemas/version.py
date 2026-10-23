import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class MeasurementVersionResponse(BaseModel):
    id: int
    medicion_id: uuid.UUID
    numero_version: int
    valor_registrado: float
    meta_periodo: Optional[float] = None
    porcentaje_cumplimiento: Optional[float] = None
    estado: str
    tipo_accion: str
    motivo_cambio: Optional[str] = None
    modificado_por: Optional[uuid.UUID] = None
    modificado_por_nombre: Optional[str] = None
    modificado_por_cedula: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class RollbackRequest(BaseModel):
    version_destino: int = Field(..., ge=1, description="Número de versión histórica a la que se desea regresar")
    motivo: str = Field(..., min_length=5, description="Motivo justificado de la reversión")

class VersionDiffResponse(BaseModel):
    medicion_id: str
    version_base: int
    version_comparada: int
    diferencias: dict
