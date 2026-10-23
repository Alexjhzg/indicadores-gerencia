from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_active_user
from app.core.security import verify_password, create_access_token
from app.models.user import User
from app.models.role import Role
from app.models.department import Department
from app.schemas.auth import LoginRequest, Token
from app.schemas.user import UserResponse

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    Autentica un usuario mediante su Cédula de Identidad y contraseña, retornando un token JWT.
    """
    clean_cedula = login_data.cedula.strip().upper()
    digits = clean_cedula.replace("V-", "").replace("V", "").strip()
    cedula_variants = list(set([clean_cedula, f"V-{digits}", digits]))
    user = db.query(User).filter(User.cedula.in_(cedula_variants)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cédula o contraseña incorrecta.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Permitir autenticación si la contraseña ingresada coincide con la cédula (con o sin V-) o con el hash almacenado
    pwd_clean = login_data.password.strip().upper()
    pwd_digits = pwd_clean.replace("V-", "").replace("V", "").strip()
    is_cedula_password = (pwd_digits == digits and len(digits) >= 6) or (pwd_clean in cedula_variants)
    is_hash_valid = verify_password(login_data.password, user.password_hash)

    if not (is_cedula_password or is_hash_valid):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cédula o contraseña incorrecta.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo en el sistema INE."
        )

    # Actualizar último ingreso
    user.ultimo_ingreso = datetime.now(timezone.utc)
    db.commit()

    role = db.query(Role).filter(Role.id == user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"

    token_payload = {
        "sub": user.cedula,
        "user_id": str(user.id),
        "rol": role_name,
        "departamento_id": user.departamento_id
    }
    access_token = create_access_token(data=token_payload)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_current_user(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Obtiene los datos del usuario autenticado actualmente en sesión.
    """
    role = db.query(Role).filter(Role.id == current_user.rol_id).first()
    role_name = role.nombre if role else "ENCARGADO"
    dept = db.query(Department).filter(Department.id == current_user.departamento_id).first() if current_user.departamento_id else None

    # Determinar departamentos permitidos para el usuario
    if role_name in ["ADMIN", "GERENTE"]:
        dept_codes = [d.codigo for d in db.query(Department).filter(Department.activo == True).order_by(Department.id).all()]
    elif role_name == "JEFE_AREA":
        dept_codes = [d.codigo for d in current_user.departamentos_asignados]
        if not dept_codes:
            # Fallback a sus 4 unidades asignadas si aún no se han poblado en BD
            dept_codes = ["CART", "ECO", "SOC", "SEG"]
    elif dept:
        dept_codes = [dept.codigo]
    else:
        dept_codes = []

    primary_dept_code = dept.codigo if dept else (dept_codes[0] if dept_codes else None)
    primary_dept_name = dept.nombre if dept else (
        db.query(Department).filter(Department.codigo == primary_dept_code).first().nombre if primary_dept_code else None
    )

    return UserResponse(
        id=current_user.id,
        cedula=current_user.cedula,
        nombre_completo=current_user.nombre_completo,
        rol_id=current_user.rol_id,
        departamento_id=current_user.departamento_id,
        activo=current_user.activo,
        rol_nombre=role_name,
        departamento_codigo=primary_dept_code,
        departamento_nombre=primary_dept_name,
        departamentos_codigos=dept_codes,
        ultimo_ingreso=current_user.ultimo_ingreso,
        created_at=current_user.created_at
    )

