import * as XLSX from 'xlsx';
import type { DepartamentoId } from '@/types';

export interface IndicatorTemplateRow {
  codigo: string;
  nombre: string;
  unidad_medida: string;
  meta: number;
}

export const UNIT_INDICATORS_CONFIG: Record<DepartamentoId, {
  unitName: string;
  chiefTitle: string;
  indicators: IndicatorTemplateRow[];
}> = {
  ECO: {
    unitName: 'Unidad de Estadísticas Económicas',
    chiefTitle: 'Wilfredo Rojas · Jefe de Unidad de Estadísticas Económicas',
    indicators: [
      { codigo: 'ECO-CAN-01', nombre: 'Total Establecimientos con Encuesta Efectiva en Precios CAN', unidad_medida: '%', meta: 100 },
      { codigo: 'ECO-CAN-02', nombre: 'Total Precios Levantados Reales Efectivos', unidad_medida: 'Precios', meta: 2200 },
      { codigo: 'ECO-CAN-03', nombre: 'Total Precios Levantados Reales (Sin Errores)', unidad_medida: '%', meta: 99 },
      { codigo: 'ECO-CAN-04', nombre: 'Total Comunas con Levantamiento CAN', unidad_medida: 'Comunas', meta: 25 },
      { codigo: 'ECO-DIR-01', nombre: 'Total Establecimientos Implantados Directorio de Tipologías', unidad_medida: 'Locales', meta: 50 },
      { codigo: 'ECO-PRE-01', nombre: 'Total Personal Levantamiento Encuesta', unidad_medida: 'Personas', meta: 5 },
      { codigo: 'ECO-PRE-02', nombre: 'Total Establecimientos Planificados para Levantamiento CAN', unidad_medida: 'Establecimientos', meta: 34 },
    ],
  },
  SOC: {
    unitName: 'Unidad de Estadísticas Sociales',
    chiefTitle: 'Rubén Alejandro · Jefe de Unidad de Estadísticas Sociales',
    indicators: [
      { codigo: 'SOC-EAM-01', nombre: 'Efectividad Operativa de Sectores EAM', unidad_medida: 'Sectores', meta: 13 },
      { codigo: 'SOC-EAM-02', nombre: 'Viviendas Efectivas EAM', unidad_medida: 'Viviendas', meta: 172 },
      { codigo: 'SOC-EHM-01', nombre: 'Tasa de Levantamiento de Controles EHM', unidad_medida: '%', meta: 100 },
      { codigo: 'SOC-EHM-02', nombre: 'Viviendas Efectivas Entrevistadas EHM', unidad_medida: 'Viviendas', meta: 172 },
      { codigo: 'SOC-EHM-03', nombre: 'Tasa de No Respuesta EHM', unidad_medida: '%', meta: 15 },
      { codigo: 'SOC-ESCA-01', nombre: 'Tasa de Levantamiento de Controles ESCA', unidad_medida: '%', meta: 100 },
      { codigo: 'SOC-ESCA-02', nombre: 'Viviendas Efectivas Entrevistadas ESCA', unidad_medida: 'Viviendas', meta: 287 },
      { codigo: 'SOC-ESCA-03', nombre: 'Tasa de No Respuesta ESCA', unidad_medida: '%', meta: 20 },
    ],
  },
  DEM: {
    unitName: 'Unidad de Demografía y Población',
    chiefTitle: 'Cledys Bastardo · Jefa de Unidad de Demografía y Población',
    indicators: [
      { codigo: 'DEM-VIT-01', nombre: 'Volumen Total de Boletas Vitales Recolectadas', unidad_medida: 'Boletas', meta: 25000 },
      { codigo: 'DEM-VIT-02', nombre: 'Cantidad de Nacimientos Registrados', unidad_medida: 'Actas', meta: 15000 },
      { codigo: 'DEM-VIT-03', nombre: 'Cantidad de Defunciones Registradas', unidad_medida: 'Actas', meta: 4000 },
      { codigo: 'DEM-VIT-04', nombre: 'Registro de Nupcialidad y Uniones Estables', unidad_medida: 'Actas', meta: 3000 },
      { codigo: 'DEM-VIT-05', nombre: 'Tasa de Transcripción y Digitalización Vital', unidad_medida: '%', meta: 100 },
    ],
  },
  CART: {
    unitName: 'Unidad de Cartografía',
    chiefTitle: 'Henri Guevara · Jefe de Unidad de Cartografía',
    indicators: [
      { codigo: 'CART-CIR-01', nombre: 'Tasa de Vectorización de Circuitos Comunales', unidad_medida: '%', meta: 100 },
      { codigo: 'CART-CIR-02', nombre: 'Consejos Comunales Georreferenciados', unidad_medida: 'Consejos', meta: 1361 },
      { codigo: 'CART-CIR-03', nombre: 'Completitud Vectorial Plena (100%)', unidad_medida: 'Circuitos', meta: 199 },
      { codigo: 'CART-MUN-01', nombre: 'Cobertura Cartográfica por Municipio', unidad_medida: 'Municipios', meta: 13 },
      { codigo: 'CART-VEC-01', nombre: 'Comunas y Circuitos Vectorizados', unidad_medida: 'Comunas', meta: 199 },
    ],
  },
  SEG: {
    unitName: 'Unidad de SEGEN',
    chiefTitle: 'Johana Larez · Jefa de Unidad de SEGEN',
    indicators: [
      { codigo: 'SEG-NOD-01', nombre: 'Tasa de Operatividad de Nodos SEGEN', unidad_medida: '%', meta: 80 },
      { codigo: 'SEG-NOD-02', nombre: 'Cumplimiento de Despliegue de Nodos', unidad_medida: '%', meta: 100 },
      { codigo: 'SEG-PAR-01', nombre: 'Disponibilidad de Dispositivos Móviles (DMC)', unidad_medida: 'Equipos', meta: 350 },
      { codigo: 'SEG-PER-01', nombre: 'Despliegue de Fuerza Territorial SEGEN', unidad_medida: 'Personas', meta: 210 },
      { codigo: 'SEG-ENC-01', nombre: 'Volumen Mensual de Encuestas Digitales SEGEN', unidad_medida: 'Encuestas', meta: 25000 },
      { codigo: 'SEG-ENC-02', nombre: 'Captura Formulario Intercensal Conteo Rápido', unidad_medida: 'Encuestas', meta: 15000 },
    ],
  },
  SEEM: {
    unitName: 'Coordinación de SEEM',
    chiefTitle: 'Luis Velásquez · Coordinador de SEEM',
    indicators: [
      { codigo: 'SEEM-CAP-01', nombre: 'Personal Capacitado en Actividades Formativas', unidad_medida: 'Personas', meta: 150 },
      { codigo: 'SEEM-CAP-02', nombre: 'Talleres y Actividades de Formación Ejecutadas', unidad_medida: 'Talleres', meta: 10 },
      { codigo: 'SEEM-COM-01', nombre: 'Mesas Técnicas y Sesiones de Comités Estadales (CCEE)', unidad_medida: 'Mesas', meta: 2 },
      { codigo: 'SEEM-COM-02', nombre: 'Participantes en Mesas Técnicas CCEE', unidad_medida: 'Personas', meta: 10 },
    ],
  },
};

export function downloadUnitExcelTemplate(deptCode: DepartamentoId, mesNombre: string, anio: number = 2026): void {
  const config = UNIT_INDICATORS_CONFIG[deptCode];
  if (!config) return;

  const headerRows = [
    ['INSTITUTO NACIONAL DE ESTADÍSTICA (INE) - GERENCIA ESTADAL MONAGAS'],
    [`PLANTILLA OFICIAL DE CARGA MENSUAL · ${config.unitName.toUpperCase()}`],
    [`Período: ${mesNombre} ${anio} · Responsable: ${config.chiefTitle}`],
    [''],
    ['Código Indicador', 'Nombre del Indicador', 'Unidad de Medida', 'Meta Oficial', 'Valor Reportado (Mes)', 'Observación Técnica'],
  ];

  const dataRows = config.indicators.map((ind) => [
    ind.codigo,
    ind.nombre,
    ind.unidad_medida,
    ind.meta,
    ind.meta, // Valor sugerido / meta por defecto
    `Carga oficial ${mesNombre} ${anio}`,
  ]);

  const allRows = [...headerRows, ...dataRows];

  const ws = XLSX.utils.aoa_to_sheet(allRows);

  ws['!cols'] = [
    { wch: 18 }, // Código
    { wch: 55 }, // Nombre
    { wch: 18 }, // Unidad
    { wch: 15 }, // Meta
    { wch: 24 }, // Valor Reportado
    { wch: 40 }, // Observación
  ];

  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, `Carga_${deptCode}`);

  const fileName = `Plantilla_Carga_${deptCode}_${mesNombre}_${anio}.xlsx`;
  XLSX.writeFile(wb, fileName);
}
