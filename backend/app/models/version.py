from sqlalchemy import Column, BigInteger, String, Text, Numeric, ForeignKey, DateTime, Integer, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base

class MeasurementVersion(Base):
    __tablename__ = "versiones_medicion"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    medicion_id = Column(UUID(as_uuid=True), ForeignKey("mediciones_indicador.id", ondelete="CASCADE"), nullable=False, index=True)
    numero_version = Column(Integer, nullable=False)
    valor_registrado = Column(Numeric(16, 4), nullable=False)
    meta_periodo = Column(Numeric(16, 4), nullable=True)
    estado = Column(String(30), nullable=False)
    observaciones = Column(Text, nullable=True)
    tipo_accion = Column(String(20), nullable=False, default="MODIFICACION") # CREACION, MODIFICACION, REVERSION, APROBACION
    motivo_cambio = Column(Text, nullable=True)
    modificado_por = Column(UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    __table_args__ = (
        UniqueConstraint("medicion_id", "numero_version", name="uk_medicion_version"),
    )

    medicion = relationship("IndicatorMeasurement", back_populates="versiones")
    usuario = relationship("User")
