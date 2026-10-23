from typing import Optional
from pydantic import BaseModel

class LoginRequest(BaseModel):
    cedula: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    user_id: Optional[str] = None
    rol: Optional[str] = None
    departamento_id: Optional[int] = None
