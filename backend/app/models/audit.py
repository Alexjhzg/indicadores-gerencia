from sqlalchemy import Column, BigInteger, String, Text, Numeric, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base

class MeasurementAudit(Base):
    __tablename__ = "auditoria_mediciones"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    medicion_id = Column(UUID(as_uuid=True), ForeignKey("mediciones_indicador.id", ondelete="CASCADE"), nullable=False)
    valor_anterior = Column(Numeric(16, 4), nullable=True)
    valor_nuevo = Column(Numeric(16, 4), nullable=True)
    estado_anterior = Column(String(30), nullable=True)
    estado_nuevo = Column(String(30), nullable=True)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False)
    justificacion = Column(Text, nullable=False)
    fecha_cambio = Column(DateTime(timezone=True), server_default=func.now())

    medicion = relationship("IndicatorMeasurement", back_populates="auditorias")
    usuario = relationship("User", back_populates="auditorias")
