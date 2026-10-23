import uuid
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    cedula: str
    nombre_completo: str
    rol_id: int
    departamento_id: Optional[int] = None
    activo: bool = True

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: uuid.UUID
    rol_nombre: Optional[str] = None
    departamento_codigo: Optional[str] = None
    departamento_nombre: Optional[str] = None
    departamentos_codigos: List[str] = []
    ultimo_ingreso: Optional[datetime] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

