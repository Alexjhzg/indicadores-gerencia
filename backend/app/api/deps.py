import uuid
from typing import Generator, List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import SessionLocal
from app.models.user import User
from app.models.role import Role
from app.schemas.auth import TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

def get_db() -> Generator[Session, None, None]:
    """Provee una sesión de base de datos aislada por request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> User:
    """Valida el token JWT y obtiene el usuario autenticado desde la base de datos."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales de autenticación.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        cedula: str = payload.get("sub")
        if cedula is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.cedula == cedula).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """Verifica que el usuario autenticado esté activo en el sistema."""
    if not current_user.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo en el sistema INE."
        )
    return current_user

def require_roles(allowed_roles: List[str]):
    """Fábrica de dependencias que valida si el rol del usuario está permitido."""
    def role_checker(
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ) -> User:
        user_role = db.query(Role).filter(Role.id == current_user.rol_id).first()
        if not user_role or user_role.nombre not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acceso denegado: Se requiere uno de los siguientes roles: {', '.join(allowed_roles)}"
            )
        return current_user
    return role_checker

def check_department_permission(user: User, department_id: int, user_role_name: str, db: Optional[Session] = None) -> bool:
    """Verifica si el usuario tiene permiso para operar sobre un departamento."""
    # ADMIN y GERENTE tienen alcance global
    if user_role_name in ["ADMIN", "GERENTE"]:
        return True
    # JEFE_AREA tiene permiso sobre sus departamentos asignados (CART, ECO, SOC, SEG)
    if user_role_name == "JEFE_AREA":
        assigned_ids = [d.id for d in user.departamentos_asignados]
        if assigned_ids:
            return department_id in assigned_ids
        if db:
            from app.models.department import Department
            dept = db.query(Department).filter(Department.id == department_id).first()
            if dept and dept.codigo in ["CART", "ECO", "SOC", "SEG"]:
                return True
        return False
    # ENCARGADO solo puede operar sobre su propio departamento
    return user.departamento_id == department_id

