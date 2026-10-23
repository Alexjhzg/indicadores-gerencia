import uuid
import enum
from sqlalchemy import Column, String, Text, Integer, Numeric, ForeignKey, Enum as SQLEnum, DateTime, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.indicator import FrequencyType

class MeasurementStatus(str, enum.Enum):
    BORRADOR = "BORRADOR"
    ENVIADO = "ENVIADO"
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"

class IndicatorMeasurement(Base):
    __tablename__ = "mediciones_indicador"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    indicador_id = Column(UUID(as_uuid=True), ForeignKey("indicadores.id", ondelete="CASCADE"), nullable=False, index=True)
    municipio_id = Column(Integer, ForeignKey("municipios.id", ondelete="SET NULL"), nullable=True, index=True)
    periodo_anio = Column(Integer, nullable=False, index=True)
    periodo_tipo = Column(SQLEnum(FrequencyType, name="tipo_frecuencia"), nullable=False)
    periodo_mes = Column(Integer, nullable=False)
    valor_registrado = Column(Numeric(16, 4), nullable=False)
    meta_periodo = Column(Numeric(16, 4), nullable=True)
    estado = Column(SQLEnum(MeasurementStatus, name="estado_medicion"), nullable=False, default=MeasurementStatus.BORRADOR, index=True)
    observaciones = Column(Text, nullable=True)
    registrado_por = Column(UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False)
    aprobado_por = Column(UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="SET NULL"), nullable=True)
    version = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("indicador_id", "municipio_id", "periodo_anio", "periodo_tipo", "periodo_mes", name="uk_medicion_periodo"),
    )

    indicador = relationship("Indicator", back_populates="mediciones")
    municipio = relationship("Municipality", back_populates="mediciones")
    usuario_registrador = relationship("User", foreign_keys=[registrado_por], back_populates="mediciones_registradas")
    usuario_aprobador = relationship("User", foreign_keys=[aprobado_por], back_populates="mediciones_aprobadas")
    auditorias = relationship("MeasurementAudit", back_populates="medicion", cascade="all, delete-orphan")
    versiones = relationship("MeasurementVersion", back_populates="medicion", cascade="all, delete-orphan", order_by="desc(MeasurementVersion.numero_version)")
