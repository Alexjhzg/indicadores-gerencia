from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Municipality(Base):
    __tablename__ = "municipios"

    id = Column(Integer, primary_key=True, index=True)
    codigo_ine = Column(String(10), nullable=False, unique=True, index=True)
    nombre = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    mediciones = relationship("IndicatorMeasurement", back_populates="municipio")
