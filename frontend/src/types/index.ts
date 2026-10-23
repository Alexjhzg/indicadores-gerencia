// Definiciones de tipos para el Sistema de Indicadores INE Monagas

export type RolUsuario = 'ADMIN' | 'GERENTE' | 'ENCARGADO' | 'JEFE_AREA';

export type DepartamentoId = 'ECO' | 'SOC' | 'DEM' | 'CART' | 'SEG' | 'SEEM';

export type EstadoMedicion = 'BORRADOR' | 'APROBADO';

export interface Usuario {
  cedula: string;
  nombres: string;
  apellidos: string;
  rol_id: RolUsuario;
  departamento_id: DepartamentoId | null;
  departamentos_codigos?: DepartamentoId[];
  activo: boolean;
}

export interface Departamento {
  id: DepartamentoId;
  nombre: string;
  descripcion?: string;
  orden?: number;
}

export interface Municipio {
  codigo_dpt: string; // Ej: '1601' a '1613'
  nombre: string;
  estado_id: number;
}

export interface Indicador {
  id: number;
  codigo: string; // Ej: 'ECO-IP-01'
  nombre: string;
  descripcion?: string;
  departamento_id: DepartamentoId;
  unidad_medida: string;
  periodicidad: string;
  meta_anual?: number | null;
  fuente_origen?: string;
  activo: boolean;
}

export interface Medicion {
  id: number;
  indicador_id: number;
  periodo_mes: number;
  periodo_anio: number;
  municipio_codigo?: string | null;
  valor_numerico: number;
  meta_esperada?: number | null;
  porcentaje_cumplimiento?: number | null;
  estado: EstadoMedicion;
  justificacion?: string;
  version_actual: number;
  created_at?: string;
  updated_at?: string;
}

export interface ResumenDivision {
  departamento_id: DepartamentoId;
  nombre: string;
  total_indicadores: number;
  mediciones_cargadas: number;
  promedio_cumplimiento: number;
  alertas: number;
}

export interface ResumenDashboard {
  periodo_mes: number;
  periodo_anio: number;
  cumplimiento_global: number;
  total_municipios: number;
  total_departamentos: number;
  total_indicadores_certificados: number;
  divisiones: ResumenDivision[];
}
