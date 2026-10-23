from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    dashboard,
    departments,
    municipalities,
    indicators,
    measurements,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard Ejecutivo"])
api_router.include_router(departments.router, prefix="/departamentos", tags=["Departamentos"])
api_router.include_router(municipalities.router, prefix="/municipios", tags=["Municipios (DPT 1601-1613)"])
api_router.include_router(indicators.router, prefix="/indicadores", tags=["Indicadores Técnicos"])
api_router.include_router(measurements.router, prefix="/mediciones", tags=["Mediciones y Versionamiento"])
