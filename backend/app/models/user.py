import uuid
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime, Table, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base

usuario_departamentos = Table(
    "usuario_departamentos",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("usuario_id", UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False),
    Column("departamento_id", Integer, ForeignKey("departamentos.id", ondelete="CASCADE"), nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
)

class User(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cedula = Column(String(20), nullable=False, unique=True, index=True)
    nombre_completo = Column(String(150), nullable=False)
    password_hash = Column(String(255), nullable=False)
    rol_id = Column(Integer, ForeignKey("roles.id", ondelete="RESTRICT"), nullable=False)
    departamento_id = Column(Integer, ForeignKey("departamentos.id", ondelete="SET NULL"), nullable=True)
    activo = Column(Boolean, default=True)
    ultimo_ingreso = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    rol = relationship("Role", back_populates="usuarios")
    departamento = relationship("Department", back_populates="usuarios")
    departamentos_asignados = relationship("Department", secondary=usuario_departamentos, backref="supervisores")
    mediciones_registradas = relationship("IndicatorMeasurement", foreign_keys="[IndicatorMeasurement.registrado_por]", back_populates="usuario_registrador")
    mediciones_aprobadas = relationship("IndicatorMeasurement", foreign_keys="[IndicatorMeasurement.aprobado_por]", back_populates="usuario_aprobador")
    auditorias = relationship("MeasurementAudit", back_populates="usuario")

