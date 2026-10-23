/**
 * Matriz oficial de datos mensuales por departamento y sincronización
 * de mediciones para las Fichas Técnicas de Indicadores Oficiales (2026).
 */

export interface DynamicMeasurement {
  valor_registrado: string | number;
  meta_periodo: string | number;
  cumplimientoTexto: string;
  cumplimientoClass: string;
  periodoLabel: string;
  unidad_medida?: string;
}

export const mesesDisponibles = [
  { id: 'Ene', nombre: 'Enero', nombreCorto: 'Ene' },
  { id: 'Feb', nombre: 'Febrero', nombreCorto: 'Feb' },
  { id: 'Mar', nombre: 'Marzo', nombreCorto: 'Mar' },
  { id: 'Abr', nombre: 'Abril', nombreCorto: 'Abr' },
  { id: 'May', nombre: 'Mayo', nombreCorto: 'May' },
  { id: 'Jun', nombre: 'Junio', nombreCorto: 'Jun' },
  { id: 'Jul', nombre: 'Julio', nombreCorto: 'Jul' },
  { id: 'Ago', nombre: 'Agosto', nombreCorto: 'Ago' },
] as const;

export type MesId = typeof mesesDisponibles[number]['id'];

// ==========================================
// 1. UNIDAD DE ESTADÍSTICAS ECONÓMICAS (ECO)
// ==========================================
export interface EconomicaSemanaData {
  id: string;
  nombre: string;
  precios: number;
  meta: number;
  sin_error: number;
  pct_calidad: string;
}

export interface EconomicaTipologiaData {
  nombre: string;
  locales: number;
  porcentaje: string;
  cotizaciones: number;
}

export interface EconomicasMesData {
  mesNombre: string;
  planif_personal: number;
  efec_personal: number;
  pct_personal: string;
  directorio: number;
  acumulado_directorio: number;
  comunas: number;
  nodos: number;
  planif_locales: number;
  efec_locales: number;
  pct_locales: string;
  precios_efec: number;
  meta_precios_mes: number;
  precios_sin_error: number;
  pct_precios_calidad: string;
  tiempo_prom: number;
  semanas: EconomicaSemanaData[];
  tipologias: EconomicaTipologiaData[];
}

export const datosEconomicasPorMes: Record<string, EconomicasMesData> = {
  Ene: {
    mesNombre: 'Enero',
    planif_personal: 18,
    efec_personal: 14,
    pct_personal: '77.8%',
    directorio: 211,
    acumulado_directorio: 211,
    comunas: 23,
    nodos: 15,
    planif_locales: 48,
    efec_locales: 48,
    pct_locales: '100.0%',
    precios_efec: 2340,
    meta_precios_mes: 2340,
    precios_sin_error: 2275,
    pct_precios_calidad: '97.22%',
    tiempo_prom: 743.8,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 585, meta: 585, sin_error: 569, pct_calidad: '97.26%' },
      { id: '2', nombre: 'Semana 2', precios: 585, meta: 585, sin_error: 568, pct_calidad: '97.09%' },
      { id: '3', nombre: 'Semana 3', precios: 585, meta: 585, sin_error: 569, pct_calidad: '97.26%' },
      { id: '4', nombre: 'Semana 4', precios: 585, meta: 585, sin_error: 569, pct_calidad: '97.26%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 16, porcentaje: '33.3%', cotizaciones: 890 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 14, porcentaje: '29.2%', cotizaciones: 650 },
      { nombre: 'Mercados Municipales y Libres', locales: 9, porcentaje: '18.8%', cotizaciones: 440 },
      { nombre: 'Carnicerías y Charcuterías', locales: 9, porcentaje: '18.8%', cotizaciones: 360 },
    ],
  },
  Feb: {
    mesNombre: 'Febrero',
    planif_personal: 18,
    efec_personal: 16,
    pct_personal: '88.9%',
    directorio: 143,
    acumulado_directorio: 354,
    comunas: 22,
    nodos: 15,
    planif_locales: 48,
    efec_locales: 48,
    pct_locales: '100.0%',
    precios_efec: 2340,
    meta_precios_mes: 2340,
    precios_sin_error: 2325,
    pct_precios_calidad: '99.36%',
    tiempo_prom: 1042.8,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 580, meta: 585, sin_error: 576, pct_calidad: '99.31%' },
      { id: '2', nombre: 'Semana 2', precios: 585, meta: 585, sin_error: 581, pct_calidad: '99.32%' },
      { id: '3', nombre: 'Semana 3', precios: 585, meta: 585, sin_error: 582, pct_calidad: '99.49%' },
      { id: '4', nombre: 'Semana 4', precios: 590, meta: 585, sin_error: 586, pct_calidad: '99.32%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 16, porcentaje: '33.3%', cotizaciones: 890 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 14, porcentaje: '29.2%', cotizaciones: 650 },
      { nombre: 'Mercados Municipales y Libres', locales: 9, porcentaje: '18.8%', cotizaciones: 440 },
      { nombre: 'Carnicerías y Charcuterías', locales: 9, porcentaje: '18.8%', cotizaciones: 360 },
    ],
  },
  Mar: {
    mesNombre: 'Marzo',
    planif_personal: 18,
    efec_personal: 15,
    pct_personal: '83.3%',
    directorio: 84,
    acumulado_directorio: 438,
    comunas: 22,
    nodos: 14,
    planif_locales: 50,
    efec_locales: 50,
    pct_locales: '100.0%',
    precios_efec: 2340,
    meta_precios_mes: 2340,
    precios_sin_error: 2320,
    pct_precios_calidad: '99.15%',
    tiempo_prom: 1043.8,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 580, meta: 585, sin_error: 575, pct_calidad: '99.14%' },
      { id: '2', nombre: 'Semana 2', precios: 585, meta: 585, sin_error: 580, pct_calidad: '99.15%' },
      { id: '3', nombre: 'Semana 3', precios: 585, meta: 585, sin_error: 580, pct_calidad: '99.15%' },
      { id: '4', nombre: 'Semana 4', precios: 590, meta: 585, sin_error: 585, pct_calidad: '99.15%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 17, porcentaje: '34.0%', cotizaciones: 890 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 15, porcentaje: '30.0%', cotizaciones: 650 },
      { nombre: 'Mercados Municipales y Libres', locales: 9, porcentaje: '18.0%', cotizaciones: 440 },
      { nombre: 'Carnicerías y Charcuterías', locales: 9, porcentaje: '18.0%', cotizaciones: 360 },
    ],
  },
  Abr: {
    mesNombre: 'Abril',
    planif_personal: 18,
    efec_personal: 15,
    pct_personal: '83.3%',
    directorio: 50,
    acumulado_directorio: 488,
    comunas: 21,
    nodos: 13,
    planif_locales: 50,
    efec_locales: 49,
    pct_locales: '98.0%',
    precios_efec: 2336,
    meta_precios_mes: 2340,
    precios_sin_error: 2324,
    pct_precios_calidad: '99.49%',
    tiempo_prom: 1044.8,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 584, meta: 585, sin_error: 581, pct_calidad: '99.49%' },
      { id: '2', nombre: 'Semana 2', precios: 584, meta: 585, sin_error: 581, pct_calidad: '99.49%' },
      { id: '3', nombre: 'Semana 3', precios: 584, meta: 585, sin_error: 581, pct_calidad: '99.49%' },
      { id: '4', nombre: 'Semana 4', precios: 584, meta: 585, sin_error: 581, pct_calidad: '99.49%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 17, porcentaje: '34.0%', cotizaciones: 885 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 15, porcentaje: '30.0%', cotizaciones: 650 },
      { nombre: 'Mercados Municipales y Libres', locales: 9, porcentaje: '18.0%', cotizaciones: 440 },
      { nombre: 'Carnicerías y Charcuterías', locales: 8, porcentaje: '16.0%', cotizaciones: 361 },
    ],
  },
  May: {
    mesNombre: 'Mayo',
    planif_personal: 18,
    efec_personal: 16,
    pct_personal: '88.9%',
    directorio: 122,
    acumulado_directorio: 610,
    comunas: 23,
    nodos: 15,
    planif_locales: 49,
    efec_locales: 49,
    pct_locales: '100.0%',
    precios_efec: 2340,
    meta_precios_mes: 2340,
    precios_sin_error: 2328,
    pct_precios_calidad: '99.49%',
    tiempo_prom: 3347.0,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 585, meta: 585, sin_error: 582, pct_calidad: '99.49%' },
      { id: '2', nombre: 'Semana 2', precios: 585, meta: 585, sin_error: 582, pct_calidad: '99.49%' },
      { id: '3', nombre: 'Semana 3', precios: 585, meta: 585, sin_error: 582, pct_calidad: '99.49%' },
      { id: '4', nombre: 'Semana 4', precios: 585, meta: 585, sin_error: 582, pct_calidad: '99.49%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 17, porcentaje: '34.7%', cotizaciones: 890 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 14, porcentaje: '28.6%', cotizaciones: 650 },
      { nombre: 'Mercados Municipales y Libres', locales: 9, porcentaje: '18.4%', cotizaciones: 440 },
      { nombre: 'Carnicerías y Charcuterías', locales: 9, porcentaje: '18.4%', cotizaciones: 360 },
    ],
  },
  Jun: {
    mesNombre: 'Junio',
    planif_personal: 12,
    efec_personal: 11,
    pct_personal: '91.7%',
    directorio: 143,
    acumulado_directorio: 753,
    comunas: 22,
    nodos: 16,
    planif_locales: 47,
    efec_locales: 47,
    pct_locales: '100.0%',
    precios_efec: 2340,
    meta_precios_mes: 2340,
    precios_sin_error: 2328,
    pct_precios_calidad: '99.49%',
    tiempo_prom: 2697.0,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 580, meta: 585, sin_error: 577, pct_calidad: '99.48%' },
      { id: '2', nombre: 'Semana 2', precios: 585, meta: 585, sin_error: 582, pct_calidad: '99.49%' },
      { id: '3', nombre: 'Semana 3', precios: 585, meta: 585, sin_error: 582, pct_calidad: '99.49%' },
      { id: '4', nombre: 'Semana 4', precios: 590, meta: 585, sin_error: 587, pct_calidad: '99.49%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 16, porcentaje: '34.0%', cotizaciones: 890 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 14, porcentaje: '29.8%', cotizaciones: 650 },
      { nombre: 'Mercados Municipales y Libres', locales: 9, porcentaje: '19.1%', cotizaciones: 440 },
      { nombre: 'Carnicerías y Charcuterías', locales: 8, porcentaje: '17.0%', cotizaciones: 360 },
    ],
  },
  Jul: {
    mesNombre: 'Julio',
    planif_personal: 8,
    efec_personal: 8,
    pct_personal: '100.0%',
    directorio: 281,
    acumulado_directorio: 1034,
    comunas: 22,
    nodos: 16,
    planif_locales: 58,
    efec_locales: 56,
    pct_locales: '96.6%',
    precios_efec: 2795,
    meta_precios_mes: 2800,
    precios_sin_error: 2791,
    pct_precios_calidad: '99.86%',
    tiempo_prom: 3382.0,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 690, meta: 700, sin_error: 689, pct_calidad: '99.86%' },
      { id: '2', nombre: 'Semana 2', precios: 700, meta: 700, sin_error: 699, pct_calidad: '99.86%' },
      { id: '3', nombre: 'Semana 3', precios: 705, meta: 700, sin_error: 704, pct_calidad: '99.86%' },
      { id: '4', nombre: 'Semana 4', precios: 700, meta: 700, sin_error: 699, pct_calidad: '99.86%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 20, porcentaje: '35.7%', cotizaciones: 1050 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 16, porcentaje: '28.6%', cotizaciones: 780 },
      { nombre: 'Mercados Municipales y Libres', locales: 10, porcentaje: '17.9%', cotizaciones: 510 },
      { nombre: 'Carnicerías y Charcuterías', locales: 10, porcentaje: '17.9%', cotizaciones: 455 },
    ],
  },
  Ago: {
    mesNombre: 'Agosto',
    planif_personal: 5,
    efec_personal: 5,
    pct_personal: '100.0%',
    directorio: 44,
    acumulado_directorio: 1078,
    comunas: 25,
    nodos: 16,
    planif_locales: 34,
    efec_locales: 34,
    pct_locales: '100.0%',
    precios_efec: 2145,
    meta_precios_mes: 2200,
    precios_sin_error: 2131,
    pct_precios_calidad: '99.35%',
    tiempo_prom: 3240.0,
    semanas: [
      { id: '1', nombre: 'Semana 1', precios: 520, meta: 550, sin_error: 516, pct_calidad: '99.23%' },
      { id: '2', nombre: 'Semana 2', precios: 540, meta: 550, sin_error: 537, pct_calidad: '99.44%' },
      { id: '3', nombre: 'Semana 3', precios: 535, meta: 550, sin_error: 531, pct_calidad: '99.25%' },
      { id: '4', nombre: 'Semana 4', precios: 550, meta: 550, sin_error: 547, pct_calidad: '99.45%' },
    ],
    tipologias: [
      { nombre: 'Supermercados e Hipermercados', locales: 12, porcentaje: '35.3%', cotizaciones: 820 },
      { nombre: 'Abastos y Bodegas Tradicionales', locales: 10, porcentaje: '29.4%', cotizaciones: 580 },
      { nombre: 'Mercados Municipales y Libres', locales: 6, porcentaje: '17.6%', cotizaciones: 410 },
      { nombre: 'Carnicerías y Charcuterías', locales: 6, porcentaje: '17.6%', cotizaciones: 335 },
    ],
  },
};

// ==========================================
// 2. UNIDAD DE SEGEN (SEG)
// ==========================================
export const datosSegPorMes: Record<string, {
  mesNombre: string;
  totalEncuestas: number;
  pctMeta: string;
  encuestas: { tipo: string; cantidad: number; porcentaje: string; meta: string }[];
}> = {
  Ene: {
    mesNombre: 'Enero',
    totalEncuestas: 26789,
    pctMeta: '107.2%',
    encuestas: [
      { tipo: 'Conteo Rápido v2 (Estructuras)', cantidad: 0, porcentaje: '0.0%', meta: '15,000' },
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 10981, porcentaje: '41.0%', meta: '10,000' },
      { tipo: 'Económica ODK V2', cantidad: 5272, porcentaje: '19.7%', meta: '5,000' },
      { tipo: 'Educación, Medios y Lectura', cantidad: 5276, porcentaje: '19.7%', meta: '5,000' },
      { tipo: 'Servicios ODK', cantidad: 5260, porcentaje: '19.6%', meta: '5,000' },
    ],
  },
  Feb: {
    mesNombre: 'Febrero',
    totalEncuestas: 28084,
    pctMeta: '112.3%',
    encuestas: [
      { tipo: 'Conteo Rápido v2 (Estructuras)', cantidad: 0, porcentaje: '0.0%', meta: '15,000' },
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 11276, porcentaje: '40.1%', meta: '10,000' },
      { tipo: 'Consulta Laboral 2026', cantidad: 3713, porcentaje: '13.2%', meta: '3,500' },
      { tipo: 'Educación, Medios y Lectura', cantidad: 4368, porcentaje: '15.6%', meta: '4,000' },
      { tipo: 'Servicios y Económica ODK', cantidad: 8727, porcentaje: '31.1%', meta: '8,000' },
    ],
  },
  Mar: {
    mesNombre: 'Marzo',
    totalEncuestas: 29869,
    pctMeta: '119.5%',
    encuestas: [
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 8773, porcentaje: '29.4%', meta: '8,000' },
      { tipo: 'Consulta Laboral 2026', cantidad: 8308, porcentaje: '27.8%', meta: '8,000' },
      { tipo: 'Económica ODK V2', cantidad: 4248, porcentaje: '14.2%', meta: '4,000' },
      { tipo: 'Educación y Medios', cantidad: 4196, porcentaje: '14.0%', meta: '4,000' },
      { tipo: 'Servicios ODK', cantidad: 4344, porcentaje: '14.5%', meta: '4,000' },
    ],
  },
  Abr: {
    mesNombre: 'Abril',
    totalEncuestas: 33369,
    pctMeta: '133.5%',
    encuestas: [
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 10355, porcentaje: '31.0%', meta: '10,000' },
      { tipo: 'Consulta Laboral 2026', cantidad: 9656, porcentaje: '28.9%', meta: '9,000' },
      { tipo: 'Económica ODK V2', cantidad: 4495, porcentaje: '13.5%', meta: '4,000' },
      { tipo: 'Educación y Medios', cantidad: 4473, porcentaje: '13.4%', meta: '4,000' },
      { tipo: 'Servicios ODK', cantidad: 4390, porcentaje: '13.2%', meta: '4,000' },
    ],
  },
  May: {
    mesNombre: 'Mayo',
    totalEncuestas: 27624,
    pctMeta: '110.5%',
    encuestas: [
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 8344, porcentaje: '30.2%', meta: '8,000' },
      { tipo: 'Consulta Laboral 2026', cantidad: 7796, porcentaje: '28.2%', meta: '7,000' },
      { tipo: 'Servicios ODK', cantidad: 4310, porcentaje: '15.6%', meta: '4,000' },
      { tipo: 'Económica ODK V2', cantidad: 3865, porcentaje: '14.0%', meta: '3,500' },
      { tipo: 'Otras Investigaciones ODK', cantidad: 3309, porcentaje: '12.0%', meta: '3,000' },
    ],
  },
  Jun: {
    mesNombre: 'Junio',
    totalEncuestas: 38946,
    pctMeta: '155.8%',
    encuestas: [
      { tipo: 'Conteo Rápido v2 (Estructuras)', cantidad: 21604, porcentaje: '55.5%', meta: '15,000' },
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 6420, porcentaje: '16.5%', meta: '6,000' },
      { tipo: 'Trámites Adm. ODK', cantidad: 2946, porcentaje: '7.6%', meta: '2,500' },
      { tipo: 'Consulta Laboral 2026', cantidad: 2746, porcentaje: '7.1%', meta: '2,500' },
      { tipo: 'Económica y Educación ODK', cantidad: 5230, porcentaje: '13.4%', meta: '5,000' },
    ],
  },
  Jul: {
    mesNombre: 'Julio',
    totalEncuestas: 39036,
    pctMeta: '156.1%',
    encuestas: [
      { tipo: 'Conteo Rápido v2 (Estructuras)', cantidad: 21587, porcentaje: '55.3%', meta: '15,000' },
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 5853, porcentaje: '15.0%', meta: '5,500' },
      { tipo: 'Consulta Laboral 2026', cantidad: 3062, porcentaje: '7.8%', meta: '3,000' },
      { tipo: 'Económica ODK V2', cantidad: 3006, porcentaje: '7.7%', meta: '3,000' },
      { tipo: 'Otras Investigaciones ODK', cantidad: 5528, porcentaje: '14.2%', meta: '5,000' },
    ],
  },
  Ago: {
    mesNombre: 'Agosto',
    totalEncuestas: 28147,
    pctMeta: '112.6%',
    encuestas: [
      { tipo: 'Conteo Rápido v2 (Estructuras)', cantidad: 14281, porcentaje: '50.7%', meta: '15,000' },
      { tipo: 'Encuesta de Coyuntura Social', cantidad: 3227, porcentaje: '11.5%', meta: '3,000' },
      { tipo: 'Consulta Laboral y Ocupación', cantidad: 2591, porcentaje: '9.2%', meta: '2,500' },
      { tipo: 'Captura Económica ODK', cantidad: 2558, porcentaje: '9.1%', meta: '2,500' },
      { tipo: 'Otras Investigaciones Territoriales', cantidad: 5490, porcentaje: '19.5%', meta: '5,000' },
    ],
  },
};

// ==========================================
// 3. UNIDAD DE ESTADÍSTICAS SOCIALES (SOC)
// ==========================================
export interface SocialesMesData {
  mesNombre: string;
  ehm_efec: number;
  ehm_planif: number;
  ehm_pct: string;
  ehm_viv_meta: number;
  ehm_viv_efec: number;
  esca_efec: number;
  esca_planif: number;
  esca_pct: string;
  esca_viv_meta: number;
  esca_viv_efec: number;
  no_resp: string;
}

export const datosSocialesPorMes: Record<string, SocialesMesData> = {
  Ene: { mesNombre: 'Enero', ehm_efec: 10, ehm_planif: 13, ehm_pct: '76.92%', ehm_viv_meta: 152, ehm_viv_efec: 78, esca_efec: 17, esca_planif: 23, esca_pct: '73.91%', esca_viv_meta: 260, esca_viv_efec: 120, no_resp: '24.2%' },
  Feb: { mesNombre: 'Febrero', ehm_efec: 11, ehm_planif: 13, ehm_pct: '84.62%', ehm_viv_meta: 168, ehm_viv_efec: 88, esca_efec: 18, esca_planif: 23, esca_pct: '78.26%', esca_viv_meta: 270, esca_viv_efec: 128, no_resp: '22.8%' },
  Mar: { mesNombre: 'Marzo', ehm_efec: 10, ehm_planif: 15, ehm_pct: '66.67%', ehm_viv_meta: 145, ehm_viv_efec: 79, esca_efec: 17, esca_planif: 23, esca_pct: '73.91%', esca_viv_meta: 265, esca_viv_efec: 122, no_resp: '23.4%' },
  Abr: { mesNombre: 'Abril', ehm_efec: 11, ehm_planif: 13, ehm_pct: '84.62%', ehm_viv_meta: 165, ehm_viv_efec: 74, esca_efec: 18, esca_planif: 23, esca_pct: '78.26%', esca_viv_meta: 275, esca_viv_efec: 130, no_resp: '24.1%' },
  May: { mesNombre: 'Mayo', ehm_efec: 14, ehm_planif: 17, ehm_pct: '82.35%', ehm_viv_meta: 215, ehm_viv_efec: 123, esca_efec: 20, esca_planif: 23, esca_pct: '86.96%', esca_viv_meta: 285, esca_viv_efec: 145, no_resp: '19.5%' },
  Jun: { mesNombre: 'Junio', ehm_efec: 12, ehm_planif: 13, ehm_pct: '92.31%', ehm_viv_meta: 189, ehm_viv_efec: 101, esca_efec: 21, esca_planif: 23, esca_pct: '91.30%', esca_viv_meta: 290, esca_viv_efec: 148, no_resp: '18.2%' },
  Jul: { mesNombre: 'Julio', ehm_efec: 6, ehm_planif: 9, ehm_pct: '66.67%', ehm_viv_meta: 91, ehm_viv_efec: 59, esca_efec: 15, esca_planif: 23, esca_pct: '65.22%', esca_viv_meta: 220, esca_viv_efec: 105, no_resp: '26.1%' },
};

// ==========================================
// 4. SEEM (SEGUIMIENTO, EVALUACIÓN, EDUCACIÓN Y COMITÉS)
// ==========================================
export interface SeemTallerItem {
  nombre: string;
  participantes: number;
  tipo: 'Sede Regional' | 'Territorial / Campo';
  fecha: string;
}

export interface SeemMesaTecnicaItem {
  nombre: string;
  ente: string;
  participantes: number;
  fecha: string;
  acuerdos: string;
}

export interface SeemMesData {
  mesNombre: string;
  totalCapacitados: number;
  metaCapacitados: number;
  totalTalleres: number;
  metaTalleres: number;
  capacitadosSede: number;
  capacitadosCampo: number;
  totalMesasCCEE: number;
  participantesCCEE: number;
  talleres: SeemTallerItem[];
  mesas: SeemMesaTecnicaItem[];
}

export const datosSeemPorMes: Record<string, SeemMesData> = {
  Ene: {
    mesNombre: 'Enero',
    totalCapacitados: 42,
    metaCapacitados: 50,
    totalTalleres: 2,
    metaTalleres: 3,
    capacitadosSede: 36,
    capacitadosCampo: 6,
    totalMesasCCEE: 0,
    participantesCCEE: 0,
    talleres: [
      { nombre: 'Inducción General Marco Estadístico', participantes: 25, tipo: 'Sede Regional', fecha: '15/01/2026' },
      { nombre: 'Taller de Operaciones en Campo', participantes: 17, tipo: 'Territorial / Campo', fecha: '22/01/2026' },
    ],
    mesas: [],
  },
  Feb: {
    mesNombre: 'Febrero',
    totalCapacitados: 58,
    metaCapacitados: 60,
    totalTalleres: 3,
    metaTalleres: 3,
    capacitadosSede: 48,
    capacitadosCampo: 10,
    totalMesasCCEE: 1,
    participantesCCEE: 5,
    talleres: [
      { nombre: 'Captura Digital ODK y DMC', participantes: 28, tipo: 'Sede Regional', fecha: '10/02/2026' },
      { nombre: 'Muestreo y Segmentación Territorial', participantes: 20, tipo: 'Sede Regional', fecha: '18/02/2026' },
      { nombre: 'Enlace de Nodos SEGEN Municipales', participantes: 10, tipo: 'Territorial / Campo', fecha: '25/02/2026' },
    ],
    mesas: [
      { nombre: 'Mesa Técnica Instalación CCEE 2026', ente: 'Gobernación de Monagas', participantes: 5, fecha: '12/02/2026', acuerdos: 'Cronograma interinstitucional 2026' },
    ],
  },
  Mar: {
    mesNombre: 'Marzo',
    totalCapacitados: 65,
    metaCapacitados: 70,
    totalTalleres: 3,
    metaTalleres: 4,
    capacitadosSede: 52,
    capacitadosCampo: 13,
    totalMesasCCEE: 0,
    participantesCCEE: 0,
    talleres: [
      { nombre: 'Metodología EHM y No Respuesta', participantes: 30, tipo: 'Sede Regional', fecha: '14/03/2026' },
      { nombre: 'Estructuras de Directorio Comercial', participantes: 22, tipo: 'Sede Regional', fecha: '20/03/2026' },
      { nombre: 'Actualización Cartográfica Local', participantes: 13, tipo: 'Territorial / Campo', fecha: '27/03/2026' },
    ],
    mesas: [],
  },
  Abr: {
    mesNombre: 'Abril',
    totalCapacitados: 72,
    metaCapacitados: 80,
    totalTalleres: 4,
    metaTalleres: 4,
    capacitadosSede: 58,
    capacitadosCampo: 14,
    totalMesasCCEE: 1,
    participantesCCEE: 6,
    talleres: [
      { nombre: 'Supervisión de Calidad en Encuestas', participantes: 25, tipo: 'Sede Regional', fecha: '08/04/2026' },
      { nombre: 'Consumo de Alimentos ESCA', participantes: 20, tipo: 'Sede Regional', fecha: '16/04/2026' },
      { nombre: 'Operatividad de Dispositivos Móviles', participantes: 14, tipo: 'Territorial / Campo', fecha: '23/04/2026' },
      { nombre: 'Codificación y Consistencia Vital', participantes: 13, tipo: 'Sede Regional', fecha: '29/04/2026' },
    ],
    mesas: [
      { nombre: 'Mesa de Coordinación de Estadísticas de Salud', ente: 'Dirección Regional de Salud', participantes: 6, fecha: '17/04/2026', acuerdos: 'Revisión de certificados EV-25' },
    ],
  },
  May: {
    mesNombre: 'Mayo',
    totalCapacitados: 89,
    metaCapacitados: 90,
    totalTalleres: 4,
    metaTalleres: 5,
    capacitadosSede: 71,
    capacitadosCampo: 18,
    totalMesasCCEE: 0,
    participantesCCEE: 0,
    talleres: [
      { nombre: 'Protocolo de Precios CAN', participantes: 32, tipo: 'Sede Regional', fecha: '07/05/2026' },
      { nombre: 'Vectorización de Circuitos Comunales', participantes: 24, tipo: 'Sede Regional', fecha: '15/05/2026' },
      { nombre: 'Despliegue Conteo Rápido v2', participantes: 18, tipo: 'Territorial / Campo', fecha: '21/05/2026' },
      { nombre: 'Sistemas de Respaldo y Auditoría', participantes: 15, tipo: 'Sede Regional', fecha: '28/05/2026' },
    ],
    mesas: [],
  },
  Jun: {
    mesNombre: 'Junio',
    totalCapacitados: 110,
    metaCapacitados: 100,
    totalTalleres: 5,
    metaTalleres: 5,
    capacitadosSede: 92,
    capacitadosCampo: 18,
    totalMesasCCEE: 1,
    participantesCCEE: 7,
    talleres: [
      { nombre: 'Coyuntura Social y ODK', participantes: 35, tipo: 'Sede Regional', fecha: '05/06/2026' },
      { nombre: 'Validación de Datos Geográficos', participantes: 27, tipo: 'Sede Regional', fecha: '12/06/2026' },
      { nombre: 'Técnicas de Entrevista en Hogares', participantes: 18, tipo: 'Territorial / Campo', fecha: '19/06/2026' },
      { nombre: 'Normas de Registros Civiles', participantes: 16, tipo: 'Sede Regional', fecha: '25/06/2026' },
      { nombre: 'Gestión Operativa de Nodos', participantes: 14, tipo: 'Sede Regional', fecha: '30/06/2026' },
    ],
    mesas: [
      { nombre: 'Mesa Técnica Sector Social y Comunas', ente: 'Ministerio de Comunas / Fundacomunal', participantes: 7, fecha: '18/06/2026', acuerdos: 'Validación de 195 comunas' },
    ],
  },
  Jul: {
    mesNombre: 'Julio',
    totalCapacitados: 122,
    metaCapacitados: 120,
    totalTalleres: 5,
    metaTalleres: 6,
    capacitadosSede: 104,
    capacitadosCampo: 18,
    totalMesasCCEE: 0,
    participantesCCEE: 0,
    talleres: [
      { nombre: 'Formación de Supervisores SEGEN', participantes: 38, tipo: 'Sede Regional', fecha: '09/07/2026' },
      { nombre: 'Control de Cobertura Cartográfica', participantes: 26, tipo: 'Sede Regional', fecha: '16/07/2026' },
      { nombre: 'Levantamiento de Hechos Vitales', participantes: 22, tipo: 'Sede Regional', fecha: '22/07/2026' },
      { nombre: 'Protocolo de Seguridad en DMC', participantes: 18, tipo: 'Territorial / Campo', fecha: '28/07/2026' },
      { nombre: 'Análisis de Datos Intermedios', participantes: 18, tipo: 'Sede Regional', fecha: '31/07/2026' },
    ],
    mesas: [],
  },
  Ago: {
    mesNombre: 'Agosto',
    totalCapacitados: 145,
    metaCapacitados: 150,
    totalTalleres: 7,
    metaTalleres: 10,
    capacitadosSede: 129,
    capacitadosCampo: 16,
    totalMesasCCEE: 1,
    participantesCCEE: 6,
    talleres: [
      { nombre: 'Inducción Metodológica ODK v2', participantes: 32, tipo: 'Sede Regional', fecha: '04/08/2026' },
      { nombre: 'Cuestionarios EHM y Flujo de Controles', participantes: 25, tipo: 'Sede Regional', fecha: '07/08/2026' },
      { nombre: 'Mesa de Registros Vitales y Defunciones', participantes: 21, tipo: 'Sede Regional', fecha: '11/08/2026' },
      { nombre: 'Levantamiento Normativo Precios CAN', participantes: 23, tipo: 'Sede Regional', fecha: '14/08/2026' },
      { nombre: 'Vectorización Cartográfica IGVSB', participantes: 18, tipo: 'Sede Regional', fecha: '19/08/2026' },
      { nombre: 'Seguridad en Dispositivos DMC y Nodos', participantes: 16, tipo: 'Territorial / Campo', fecha: '22/08/2026' },
      { nombre: 'Control de Calidad y Cierre Mensual', participantes: 10, tipo: 'Sede Regional', fecha: '27/08/2026' },
    ],
    mesas: [
      { nombre: 'Mesa Técnica de Registros Vitales', ente: 'Dirección Regional de Salud / CNE Monagas', participantes: 6, fecha: '11/08/2026', acuerdos: 'Sincronización mensual de actas de defunción y reducción de rezago en hospitales de Maturín' },
    ],
  },
};

// ==========================================
// 5. RESOLVEDOR DINÁMICO DE MEDICIONES
// ==========================================
export function getDynamicIndicatorMeasurement(
  deptCode: string,
  indCode: string,
  selectedMonthId: string = 'Ago',
  selectedSemanaId: string = 'TODAS'
): DynamicMeasurement | null {
  const mesKey = selectedMonthId in datosEconomicasPorMes ? selectedMonthId : 'Ago';

  // Resoluciones para la Unidad de Estadísticas Económicas (ECO)
  if (deptCode === 'ECO') {
    const eco = datosEconomicasPorMes[mesKey];
    if (!eco) return null;

    switch (indCode) {
      case 'ECO-PRE-01':
        return {
          valor_registrado: `${eco.efec_personal} / ${eco.planif_personal}`,
          meta_periodo: `${eco.planif_personal}`,
          cumplimientoTexto: `${eco.pct_personal} Efect.`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${eco.mesNombre} 2026`,
          unidad_medida: 'personas',
        };

      case 'ECO-DIR-01':
        return {
          valor_registrado: eco.directorio,
          meta_periodo: 50,
          cumplimientoTexto: `Acum. ${eco.acumulado_directorio.toLocaleString()}`,
          cumplimientoClass: 'text-dept-eco font-semibold',
          periodoLabel: `${eco.mesNombre} 2026`,
          unidad_medida: 'locales',
        };

      case 'ECO-CAN-04':
        return {
          valor_registrado: eco.comunas,
          meta_periodo: 25,
          cumplimientoTexto: `${eco.nodos} Nodos SEGEN`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${eco.mesNombre} 2026`,
          unidad_medida: 'comunas',
        };

      case 'ECO-PRE-02':
        return {
          valor_registrado: eco.planif_locales,
          meta_periodo: eco.planif_locales,
          cumplimientoTexto: '100% Planificado',
          cumplimientoClass: 'text-dept-eco font-semibold',
          periodoLabel: `${eco.mesNombre} 2026`,
          unidad_medida: 'establecimientos',
        };

      case 'ECO-CAN-01':
        return {
          valor_registrado: `${eco.efec_locales} / ${eco.planif_locales}`,
          meta_periodo: `${eco.planif_locales}`,
          cumplimientoTexto: `${eco.pct_locales} Efect.`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${eco.mesNombre} 2026`,
          unidad_medida: 'locales',
        };

      case 'ECO-CAN-02': {
        const hasSemana = selectedSemanaId !== 'TODAS';
        const semana = hasSemana ? eco.semanas.find(s => s.id === selectedSemanaId) : null;
        const valor = semana ? semana.precios : eco.precios_efec;
        const meta = semana ? semana.meta : eco.meta_precios_mes;
        const pct = ((valor / meta) * 100).toFixed(1) + '%';
        return {
          valor_registrado: valor.toLocaleString(),
          meta_periodo: meta.toLocaleString(),
          cumplimientoTexto: `${pct} Meta`,
          cumplimientoClass: valor >= meta ? 'text-dept-eco font-semibold' : 'text-signal-blue',
          periodoLabel: hasSemana ? `${eco.mesNombre} 2026 (Sem ${selectedSemanaId})` : `${eco.mesNombre} 2026`,
          unidad_medida: 'precios',
        };
      }

      case 'ECO-CAN-03': {
        const hasSemana = selectedSemanaId !== 'TODAS';
        const semana = hasSemana ? eco.semanas.find(s => s.id === selectedSemanaId) : null;
        const pct = semana ? semana.pct_calidad : eco.pct_precios_calidad;
        const limpios = semana ? semana.sin_error : eco.precios_sin_error;
        return {
          valor_registrado: pct,
          meta_periodo: '≥ 99.0%',
          cumplimientoTexto: `${limpios.toLocaleString()} sin errores`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: hasSemana ? `${eco.mesNombre} 2026 (Sem ${selectedSemanaId})` : `${eco.mesNombre} 2026`,
          unidad_medida: 'limpios',
        };
      }
    }
  }

  // Resoluciones para la Unidad de SEGEN (SEG)
  if (deptCode === 'SEG') {
    const segKey = selectedMonthId in datosSegPorMes ? selectedMonthId : 'Ago';
    const seg = datosSegPorMes[segKey];
    if (!seg) return null;

    switch (indCode) {
      case 'SEG-ENC-01':
        return {
          valor_registrado: seg.totalEncuestas.toLocaleString(),
          meta_periodo: '25,000',
          cumplimientoTexto: `${seg.pctMeta} Meta`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seg.mesNombre} 2026`,
          unidad_medida: 'encuestas',
        };

      case 'SEG-ENC-02': {
        const conteo = seg.encuestas.find(e => e.tipo.includes('Conteo Rápido'))?.cantidad || 0;
        return {
          valor_registrado: conteo.toLocaleString(),
          meta_periodo: '15,000',
          cumplimientoTexto: conteo > 0 ? 'Conteo Rápido v2' : 'En preparación',
          cumplimientoClass: conteo > 0 ? 'text-signal-blue' : 'text-steel',
          periodoLabel: `${seg.mesNombre} 2026`,
          unidad_medida: 'encuestas',
        };
      }

      case 'SEG-ENC-03': {
        const coyuntura = seg.encuestas.find(e => e.tipo.includes('Coyuntura'))?.cantidad || 0;
        const laboral = seg.encuestas.find(e => e.tipo.includes('Laboral'))?.cantidad || 0;
        const suma = coyuntura + laboral;
        return {
          valor_registrado: suma.toLocaleString(),
          meta_periodo: '8,000',
          cumplimientoTexto: 'Coyuntura y Laboral',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seg.mesNombre} 2026`,
          unidad_medida: 'encuestas',
        };
      }

      case 'SEG-NOD-01':
        return {
          valor_registrado: '47.17%',
          meta_periodo: '≥ 80.0%',
          cumplimientoTexto: '50 / 106 Activos',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seg.mesNombre} 2026`,
          unidad_medida: '%',
        };

      case 'SEG-NOD-02':
        return {
          valor_registrado: '108.16%',
          meta_periodo: '100.0%',
          cumplimientoTexto: '106 Instalados',
          cumplimientoClass: 'text-dept-eco font-semibold',
          periodoLabel: `${seg.mesNombre} 2026`,
          unidad_medida: '%',
        };

      case 'SEG-PAR-01':
        return {
          valor_registrado: '315',
          meta_periodo: '350',
          cumplimientoTexto: '90.0% Meta',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seg.mesNombre} 2026`,
          unidad_medida: 'equipos',
        };

      case 'SEG-PER-01':
        return {
          valor_registrado: '208 / 210',
          meta_periodo: '210',
          cumplimientoTexto: '99.0% Despliegue',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seg.mesNombre} 2026`,
          unidad_medida: 'personas',
        };
    }
  }

  // Resoluciones para la Coordinación de SEEM (Capacitación y Comités CCEE)
  if (deptCode === 'SEEM') {
    const seemKey = selectedMonthId in datosSeemPorMes ? selectedMonthId : 'Ago';
    const seem = datosSeemPorMes[seemKey];
    if (!seem) return null;

    switch (indCode) {
      case 'SEEM-CAP-01':
        return {
          valor_registrado: seem.totalCapacitados.toLocaleString(),
          meta_periodo: seem.metaCapacitados.toLocaleString(),
          cumplimientoTexto: `${seem.capacitadosSede} sede + ${seem.capacitadosCampo} campo`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seem.mesNombre} 2026`,
          unidad_medida: 'personas',
        };

      case 'SEEM-CAP-02':
        return {
          valor_registrado: seem.totalTalleres,
          meta_periodo: seem.metaTalleres,
          cumplimientoTexto: `${seem.talleres.length} talleres ejecutados`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seem.mesNombre} 2026`,
          unidad_medida: 'talleres',
        };

      case 'SEEM-COM-01':
        return {
          valor_registrado: seem.totalMesasCCEE,
          meta_periodo: 2,
          cumplimientoTexto: seem.mesas.length > 0 ? 'Mesa de Registros Vitales' : 'Sin mesas en el mes',
          cumplimientoClass: seem.totalMesasCCEE > 0 ? 'text-dept-eco font-semibold' : 'text-steel',
          periodoLabel: `${seem.mesNombre} 2026`,
          unidad_medida: 'mesas',
        };

      case 'SEEM-COM-02':
        return {
          valor_registrado: seem.participantesCCEE,
          meta_periodo: 10,
          cumplimientoTexto: 'Salud, CNE e INE Monagas',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${seem.mesNombre} 2026`,
          unidad_medida: 'personas',
        };
    }
  }

  // Resoluciones para la Unidad de Cartografía (CART - Circuitos Comunales)
  if (deptCode === 'CART') {
    switch (indCode) {
      case 'CART-CIR-01':
        return {
          valor_registrado: '97.99%',
          meta_periodo: '100.0%',
          cumplimientoTexto: '195 de 199 Circuitos',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: 'Agosto 2026',
          unidad_medida: '%',
        };
      case 'CART-CIR-02':
        return {
          valor_registrado: '1,361',
          meta_periodo: '1,361',
          cumplimientoTexto: '100% Georreferenciados',
          cumplimientoClass: 'text-dept-eco font-semibold',
          periodoLabel: 'Agosto 2026',
          unidad_medida: 'consejos',
        };
      case 'CART-CIR-03':
        return {
          valor_registrado: '177',
          meta_periodo: '199',
          cumplimientoTexto: '88.9% al 100% Cierre',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: 'Agosto 2026',
          unidad_medida: 'circuitos',
        };
      case 'CART-MUN-01':
        return {
          valor_registrado: '13',
          meta_periodo: '13',
          cumplimientoTexto: '100% Cobertura Municipal',
          cumplimientoClass: 'text-dept-eco font-semibold',
          periodoLabel: 'Agosto 2026',
          unidad_medida: 'municipios',
        };
    }
  }

  // Resoluciones para la Unidad de Estadísticas Sociales (SOC)
  if (deptCode === 'SOC') {
    const socKey = selectedMonthId in datosSocialesPorMes ? selectedMonthId : 'Ago';
    const soc = datosSocialesPorMes[socKey];
    if (!soc) return null;

    switch (indCode) {
      case 'SOC-EHM-01':
      case 'SOC-EAM-01':
        return {
          valor_registrado: soc.ehm_pct,
          meta_periodo: '100.0%',
          cumplimientoTexto: `${soc.ehm_efec} de ${soc.ehm_planif} controles`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${soc.mesNombre} 2026`,
          unidad_medida: '%',
        };
      case 'SOC-EHM-02':
      case 'SOC-EAM-02':
        return {
          valor_registrado: soc.ehm_viv_efec,
          meta_periodo: soc.ehm_viv_meta,
          cumplimientoTexto: `${soc.ehm_viv_efec} viviendas efectivas`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${soc.mesNombre} 2026`,
          unidad_medida: 'viviendas',
        };
      case 'SOC-EHM-03':
        return {
          valor_registrado: soc.no_resp,
          meta_periodo: '≤ 15.0%',
          cumplimientoTexto: 'Monitoreo No Respuesta',
          cumplimientoClass: parseFloat(soc.no_resp) <= 15 ? 'text-dept-eco' : 'text-signal-blue',
          periodoLabel: `${soc.mesNombre} 2026`,
          unidad_medida: '%',
        };
      case 'SOC-ESCA-01':
        return {
          valor_registrado: soc.esca_pct,
          meta_periodo: '100.0%',
          cumplimientoTexto: `${soc.esca_efec} de ${soc.esca_planif} controles`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${soc.mesNombre} 2026`,
          unidad_medida: '%',
        };
      case 'SOC-ESCA-02':
        return {
          valor_registrado: soc.esca_viv_efec,
          meta_periodo: soc.esca_viv_meta,
          cumplimientoTexto: `${soc.esca_viv_efec} viviendas efectivas`,
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${soc.mesNombre} 2026`,
          unidad_medida: 'viviendas',
        };
      case 'SOC-ESCA-03':
        return {
          valor_registrado: '28.35%',
          meta_periodo: '≤ 20.0%',
          cumplimientoTexto: 'Monitoreo No Respuesta ESCA',
          cumplimientoClass: 'text-signal-blue',
          periodoLabel: `${soc.mesNombre} 2026`,
          unidad_medida: '%',
        };
    }
  }

  return null;
}
