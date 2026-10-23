import uuid
from sqlalchemy import Column, String, Text, Boolean, Integer, Numeric, ForeignKey, Enum, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base

class FrequencyType(str, enum.Enum):
    MENSUAL = "MENSUAL"
    TRIMESTRAL = "TRIMESTRAL"
    SEMESTRAL = "SEMESTRAL"
    ANUAL = "ANUAL"

class TargetOrientationType(str, enum.Enum):
    ASCENDENTE = "ASCENDENTE"
    DESCENDENTE = "DESCENDENTE"
    RANGO = "RANGO"

class Indicator(Base):
    __tablename__ = "indicadores"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codigo = Column(String(30), nullable=False, unique=True, index=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=True)
    departamento_id = Column(Integer, ForeignKey("departamentos.id", ondelete="RESTRICT"), nullable=False, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="SET NULL"), nullable=True)
    unidad_medida = Column(String(50), nullable=False)
    frecuencia = Column(Enum(FrequencyType, name="tipo_frecuencia"), nullable=False, default=FrequencyType.MENSUAL)
    tipo_meta = Column(Enum(TargetOrientationType, name="tipo_orientacion_meta"), nullable=False, default=TargetOrientationType.ASCENDENTE)
    meta_referencial = Column(Numeric(14, 4), nullable=True)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    departamento = relationship("Department", back_populates="indicadores")
    categoria = relationship("Category", back_populates="indicadores")
    mediciones = relationship("IndicatorMeasurement", back_populates="indicador", cascade="all, delete-orphan")
