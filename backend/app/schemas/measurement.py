import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.models.indicator import FrequencyType
from app.models.measurement import MeasurementStatus

class MeasurementCreate(BaseModel):
    indicador_id: uuid.UUID
    municipio_id: Optional[int] = None
    periodo_anio: int = Field(..., ge=2000, le=2100)
    periodo_tipo: FrequencyType = FrequencyType.MENSUAL
    periodo_mes: int = Field(..., ge=1, le=12)
    valor_registrado: float
    meta_periodo: Optional[float] = None
    observaciones: Optional[str] = None

class MeasurementUpdate(BaseModel):
    valor_registrado: Optional[float] = None
    meta_periodo: Optional[float] = None
    observaciones: Optional[str] = None
    motivo_cambio: str = Field(..., min_length=5, description="Justificación obligatoria de la modificación")

class MeasurementResponse(BaseModel):
    id: uuid.UUID
    indicador_id: uuid.UUID
    indicador_codigo: Optional[str] = None
    indicador_nombre: Optional[str] = None
    departamento_codigo: Optional[str] = None
    municipio_id: Optional[int] = None
    municipio_nombre: Optional[str] = None
    periodo_anio: int
    periodo_tipo: FrequencyType
    periodo_mes: int
    valor_registrado: float
    meta_periodo: Optional[float] = None
    porcentaje_cumplimiento: Optional[float] = None
    estado: MeasurementStatus
    version: int
    observaciones: Optional[str] = None
    registrado_por: uuid.UUID
    aprobado_por: Optional[uuid.UUID] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class MeasurementBatchItem(BaseModel):
    indicador_codigo: Optional[str] = None
    indicador_id: Optional[uuid.UUID] = None
    municipio_id: Optional[int] = None
    valor_registrado: float
    meta_periodo: Optional[float] = None
    observaciones: Optional[str] = None
    motivo_cambio: Optional[str] = None

class BatchMeasurementCreate(BaseModel):
    departamento_codigo: str
    periodo_anio: int = Field(..., ge=2000, le=2100)
    periodo_mes: int = Field(..., ge=1, le=12)
    periodo_tipo: FrequencyType = FrequencyType.MENSUAL
    motivo_general: Optional[str] = "Carga mensual de cifras oficiales"
    mediciones: list[MeasurementBatchItem]

class BatchMeasurementResponse(BaseModel):
    mensaje: str
    departamento_codigo: str
    periodo_anio: int
    periodo_mes: int
    total_procesados: int
    total_creados: int
    total_actualizados: int
    mediciones: list[MeasurementResponse]

class UnitCertifyResponse(BaseModel):
    mensaje: str
    departamento_codigo: str
    periodo_anio: int
    periodo_mes: int
    total_certificados: int
    certificados_por: str

