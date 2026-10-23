from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.config import settings
from app.core.database import get_db
from app.api.v1.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API REST del Sistema de Indicadores de Gestión para el Instituto Nacional de Estadística (INE) - Gerencia Estadal Monagas.",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_origin_regex=r"https://.*\.onrender\.com",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enrutador principal v1
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["Sistema"])
def root():
    return {
        "sistema": settings.PROJECT_NAME,
        "institucion": "Instituto Nacional de Estadística (INE)",
        "estado": "Monagas (Entidad 16)",
        "version": "1.0.0",
        "docs": f"{settings.API_V1_STR}/docs",
    }

@app.get("/health", tags=["Sistema"], status_code=status.HTTP_200_OK)
def health_check(db: Session = Depends(get_db)):
    """
    Verifica la conectividad activa con el motor PostgreSQL y la salud del sistema.
    """
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "entidad": "16 - Monagas",
            "municipios": 13
        }
    except Exception as e:
        return {
            "status": "degraded",
            "database": f"error: {str(e)}"
        }
