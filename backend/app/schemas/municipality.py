from datetime import datetime
from pydantic import BaseModel, ConfigDict

class MunicipalityResponse(BaseModel):
    id: int
    codigo_ine: str
    nombre: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
