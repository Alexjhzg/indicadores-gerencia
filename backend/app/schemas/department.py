from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class DepartmentResponse(BaseModel):
    id: int
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    activo: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
