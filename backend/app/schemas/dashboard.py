from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class DepartmentKpi(BaseModel):
    departamento_id: int
    departamento_codigo: str
    departamento_nombre: str
    total_indicadores: int
    total_mediciones_registradas: int
    mediciones_aprobadas: int
    mediciones_pendientes_aprobacion: int
    porcentaje_cumplimiento_promedio: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)

class DashboardSummaryResponse(BaseModel):
    total_departamentos: int
    cumplimiento_general_estadal: float
    total_indicadores_activos: int
    total_mediciones_aprobadas: int
    departamentos: List[DepartmentKpi]
