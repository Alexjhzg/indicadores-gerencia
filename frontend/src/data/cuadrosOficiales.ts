/**
 * Datos oficiales extraídos directamente del documento fuente del INE:
 * "Cuadros Informe Mensual de Gestion Gerencias Estadales MONAGAS AGOSTO 2026.xlsx"
 * Entidad 16 - Estado Monagas
 */

export interface CuadroRowEco {
  mes: string;
  personal_planificado: number;
  personal_levantamiento: number;
  pct_efectividad_personal: number;
  establecimientos_implantados: number;
  comunas_can: number;
  nodos_can: number;
  establecimientos_planificados: number;
  establecimientos_efectivos: number;
  pct_efectividad_can: number;
}

export const cuadroECO: CuadroRowEco[] = [
  { mes: 'Enero', personal_planificado: 18, personal_levantamiento: 14, pct_efectividad_personal: 77.78, establecimientos_implantados: 211, comunas_can: 23, nodos_can: 15, establecimientos_planificados: 48, establecimientos_efectivos: 48, pct_efectividad_can: 100.0 },
  { mes: 'Febrero', personal_planificado: 18, personal_levantamiento: 16, pct_efectividad_personal: 88.89, establecimientos_implantados: 143, comunas_can: 22, nodos_can: 15, establecimientos_planificados: 48, establecimientos_efectivos: 48, pct_efectividad_can: 100.0 },
  { mes: 'Marzo', personal_planificado: 18, personal_levantamiento: 15, pct_efectividad_personal: 83.33, establecimientos_implantados: 84, comunas_can: 22, nodos_can: 14, establecimientos_planificados: 50, establecimientos_efectivos: 50, pct_efectividad_can: 100.0 },
  { mes: 'Abril', personal_planificado: 18, personal_levantamiento: 15, pct_efectividad_personal: 83.33, establecimientos_implantados: 50, comunas_can: 21, nodos_can: 13, establecimientos_planificados: 50, establecimientos_efectivos: 49, pct_efectividad_can: 98.0 },
  { mes: 'Mayo', personal_planificado: 18, personal_levantamiento: 16, pct_efectividad_personal: 88.89, establecimientos_implantados: 122, comunas_can: 23, nodos_can: 15, establecimientos_planificados: 49, establecimientos_efectivos: 49, pct_efectividad_can: 100.0 },
  { mes: 'Junio', personal_planificado: 12, personal_levantamiento: 11, pct_efectividad_personal: 91.67, establecimientos_implantados: 143, comunas_can: 22, nodos_can: 16, establecimientos_planificados: 47, establecimientos_efectivos: 47, pct_efectividad_can: 100.0 },
  { mes: 'Julio', personal_planificado: 8, personal_levantamiento: 8, pct_efectividad_personal: 100.0, establecimientos_implantados: 281, comunas_can: 22, nodos_can: 16, establecimientos_planificados: 58, establecimientos_efectivos: 56, pct_efectividad_can: 96.55 },
  { mes: 'Agosto', personal_planificado: 5, personal_levantamiento: 5, pct_efectividad_personal: 100.0, establecimientos_implantados: 44, comunas_can: 25, nodos_can: 16, establecimientos_planificados: 34, establecimientos_efectivos: 34, pct_efectividad_can: 100.0 },
  { mes: 'TOTAL', personal_planificado: 115, personal_levantamiento: 100, pct_efectividad_personal: 86.96, establecimientos_implantados: 1078, comunas_can: 180, nodos_can: 120, establecimientos_planificados: 384, establecimientos_efectivos: 381, pct_efectividad_can: 99.22 }
];

export interface CuadroRowSoc {
  periodo: string;
  controles_planificados: number;
  controles_levantados: number;
  pct_levantamiento: number;
  viviendas_planificadas: number;
  viviendas_efectivas: number;
  tipo_a: number;
  tipo_b: number;
  tipo_c: number;
  pct_no_respuesta: number;
}

export const cuadroSOC_EHM: CuadroRowSoc[] = [
  { periodo: 'Enero', controles_planificados: 13, controles_levantados: 10, pct_levantamiento: 76.92, viviendas_planificadas: 152, viviendas_efectivas: 78, tipo_a: 45, tipo_b: 24, tipo_c: 5, pct_no_respuesta: 36.59 },
  { periodo: 'Febrero', controles_planificados: 13, controles_levantados: 11, pct_levantamiento: 84.62, viviendas_planificadas: 168, viviendas_efectivas: 88, tipo_a: 40, tipo_b: 29, tipo_c: 11, pct_no_respuesta: 31.25 },
  { periodo: 'Marzo', controles_planificados: 15, controles_levantados: 10, pct_levantamiento: 66.67, viviendas_planificadas: 145, viviendas_efectivas: 79, tipo_a: 28, tipo_b: 29, tipo_c: 5, pct_no_respuesta: 25.23 },
  { periodo: 'Abril', controles_planificados: 13, controles_levantados: 11, pct_levantamiento: 84.62, viviendas_planificadas: 165, viviendas_efectivas: 74, tipo_a: 47, tipo_b: 38, tipo_c: 6, pct_no_respuesta: 38.84 },
  { periodo: 'Mayo', controles_planificados: 17, controles_levantados: 14, pct_levantamiento: 82.35, viviendas_planificadas: 215, viviendas_efectivas: 123, tipo_a: 49, tipo_b: 37, tipo_c: 6, pct_no_respuesta: 28.49 },
  { periodo: 'Junio', controles_planificados: 13, controles_levantados: 12, pct_levantamiento: 92.31, viviendas_planificadas: 189, viviendas_efectivas: 101, tipo_a: 46, tipo_b: 34, tipo_c: 8, pct_no_respuesta: 31.29 },
  { periodo: 'Julio', controles_planificados: 9, controles_levantados: 6, pct_levantamiento: 66.67, viviendas_planificadas: 91, viviendas_efectivas: 59, tipo_a: 11, tipo_b: 17, tipo_c: 4, pct_no_respuesta: 15.71 },
  { periodo: 'Agosto', controles_planificados: 13, controles_levantados: 11, pct_levantamiento: 84.62, viviendas_planificadas: 172, viviendas_efectivas: 97, tipo_a: 25, tipo_b: 37, tipo_c: 13, pct_no_respuesta: 20.49 },
  { periodo: 'TOTAL', controles_planificados: 106, controles_levantados: 85, pct_levantamiento: 80.19, viviendas_planificadas: 1297, viviendas_efectivas: 699, tipo_a: 291, tipo_b: 245, tipo_c: 58, pct_no_respuesta: 29.39 }
];

export const cuadroSOC_ESCA: CuadroRowSoc[] = [
  { periodo: 'Enero', controles_planificados: 22, controles_levantados: 19, pct_levantamiento: 86.36, viviendas_planificadas: 287, viviendas_efectivas: 102, tipo_a: 133, tipo_b: 42, tipo_c: 10, pct_no_respuesta: 56.60 },
  { periodo: 'Febrero', controles_planificados: 24, controles_levantados: 20, pct_levantamiento: 83.33, viviendas_planificadas: 288, viviendas_efectivas: 129, tipo_a: 92, tipo_b: 55, tipo_c: 12, pct_no_respuesta: 41.63 },
  { periodo: 'Marzo', controles_planificados: 24, controles_levantados: 17, pct_levantamiento: 70.83, viviendas_planificadas: 258, viviendas_efectivas: 150, tipo_a: 59, tipo_b: 37, tipo_c: 13, pct_no_respuesta: 28.37 },
  { periodo: 'Abril', controles_planificados: 23, controles_levantados: 19, pct_levantamiento: 82.61, viviendas_planificadas: 277, viviendas_efectivas: 160, tipo_a: 61, tipo_b: 50, tipo_c: 6, pct_no_respuesta: 27.60 },
  { periodo: 'Mayo', controles_planificados: 29, controles_levantados: 24, pct_levantamiento: 82.76, viviendas_planificadas: 357, viviendas_efectivas: 203, tipo_a: 69, tipo_b: 64, tipo_c: 21, pct_no_respuesta: 25.37 },
  { periodo: 'Junio', controles_planificados: 18, controles_levantados: 13, pct_levantamiento: 72.22, viviendas_planificadas: 182, viviendas_efectivas: 92, tipo_a: 50, tipo_b: 29, tipo_c: 11, pct_no_respuesta: 35.21 },
  { periodo: 'Julio', controles_planificados: 17, controles_levantados: 15, pct_levantamiento: 88.24, viviendas_planificadas: 234, viviendas_efectivas: 134, tipo_a: 33, tipo_b: 49, tipo_c: 18, pct_no_respuesta: 19.76 },
  { periodo: 'Agosto', controles_planificados: 23, controles_levantados: 19, pct_levantamiento: 82.61, viviendas_planificadas: 287, viviendas_efectivas: 139, tipo_a: 55, tipo_b: 69, tipo_c: 24, pct_no_respuesta: 28.35 },
  { periodo: 'TOTAL', controles_planificados: 180, controles_levantados: 146, pct_levantamiento: 81.11, viviendas_planificadas: 4341, viviendas_efectivas: 1109, tipo_a: 552, tipo_b: 395, tipo_c: 115, pct_no_respuesta: 33.23 }
];

export interface CuadroRowDem {
  anio: string;
  nacimientos: number;
  defunciones: number;
  matrimonios: number;
  uniones: number;
  divorcios: number;
  suicidios: number;
  total_recolectado: number;
  transcritas: number;
  por_transcribir: number;
}

export const cuadroDEM: CuadroRowDem[] = [
  { anio: '2018', nacimientos: 20871, defunciones: 4785, matrimonios: 2169, uniones: 2213, divorcios: 768, suicidios: 33, total_recolectado: 31475, transcritas: 30839, por_transcribir: 0 },
  { anio: '2019', nacimientos: 21163, defunciones: 3964, matrimonios: 2303, uniones: 1476, divorcios: 460, suicidios: 32, total_recolectado: 30145, transcritas: 29398, por_transcribir: 0 },
  { anio: '2020', nacimientos: 14840, defunciones: 3797, matrimonios: 1133, uniones: 434, divorcios: 178, suicidios: 46, total_recolectado: 20749, transcritas: 20428, por_transcribir: 0 },
  { anio: '2021', nacimientos: 12740, defunciones: 4787, matrimonios: 2131, uniones: 547, divorcios: 461, suicidios: 27, total_recolectado: 21192, transcritas: 20693, por_transcribir: 0 },
  { anio: '2022', nacimientos: 17144, defunciones: 4217, matrimonios: 2275, uniones: 1349, divorcios: 734, suicidios: 33, total_recolectado: 26485, transcritas: 25752, por_transcribir: 0 },
  { anio: '2023', nacimientos: 15618, defunciones: 3279, matrimonios: 1996, uniones: 1088, divorcios: 697, suicidios: 33, total_recolectado: 23759, transcritas: 22711, por_transcribir: 0 },
  { anio: '2024', nacimientos: 13292, defunciones: 3354, matrimonios: 1956, uniones: 1106, divorcios: 1117, suicidios: 32, total_recolectado: 21940, transcritas: 20857, por_transcribir: 0 },
  { anio: '2025', nacimientos: 12418, defunciones: 3394, matrimonios: 1821, uniones: 1101, divorcios: 1073, suicidios: 37, total_recolectado: 20863, transcritas: 19844, por_transcribir: 0 },
  { anio: '2026', nacimientos: 6972, defunciones: 1987, matrimonios: 790, uniones: 549, divorcios: 704, suicidios: 21, total_recolectado: 11615, transcritas: 11023, por_transcribir: 0 },
  { anio: 'TOTALES', nacimientos: 135058, defunciones: 33564, matrimonios: 16574, uniones: 9863, divorcios: 6192, suicidios: 294, total_recolectado: 208223, transcritas: 201545, por_transcribir: 0 }
];

export interface CuadroRowCart {
  numero: string | number;
  municipio: string;
  circuitos_total: number;
  consejos_comunales: number;
  comunas_vectorizadas: number;
  pct_vectorizacion: number;
}

export const cuadroCART: CuadroRowCart[] = [
  { numero: 1, municipio: 'Acosta', circuitos_total: 9, consejos_comunales: 58, comunas_vectorizadas: 9, pct_vectorizacion: 100.0 },
  { numero: 2, municipio: 'Aguasay', circuitos_total: 8, consejos_comunales: 37, comunas_vectorizadas: 8, pct_vectorizacion: 100.0 },
  { numero: 3, municipio: 'Bolívar', circuitos_total: 10, consejos_comunales: 67, comunas_vectorizadas: 8, pct_vectorizacion: 80.0 },
  { numero: 4, municipio: 'Caripe', circuitos_total: 15, consejos_comunales: 88, comunas_vectorizadas: 14, pct_vectorizacion: 93.33 },
  { numero: 5, municipio: 'Cedeño', circuitos_total: 7, consejos_comunales: 62, comunas_vectorizadas: 7, pct_vectorizacion: 100.0 },
  { numero: 6, municipio: 'Ezequiel Zamora', circuitos_total: 9, consejos_comunales: 91, comunas_vectorizadas: 9, pct_vectorizacion: 100.0 },
  { numero: 7, municipio: 'Libertador', circuitos_total: 12, consejos_comunales: 87, comunas_vectorizadas: 12, pct_vectorizacion: 100.0 },
  { numero: 8, municipio: 'Maturín', circuitos_total: 90, consejos_comunales: 638, comunas_vectorizadas: 90, pct_vectorizacion: 100.0 },
  { numero: 9, municipio: 'Piar', circuitos_total: 12, consejos_comunales: 77, comunas_vectorizadas: 12, pct_vectorizacion: 100.0 },
  { numero: 10, municipio: 'Punceres', circuitos_total: 6, consejos_comunales: 45, comunas_vectorizadas: 6, pct_vectorizacion: 100.0 },
  { numero: 11, municipio: 'Santa Bárbara', circuitos_total: 4, consejos_comunales: 22, comunas_vectorizadas: 3, pct_vectorizacion: 75.0 },
  { numero: 12, municipio: 'Sotillo', circuitos_total: 10, consejos_comunales: 53, comunas_vectorizadas: 10, pct_vectorizacion: 100.0 },
  { numero: 13, municipio: 'Uracoa', circuitos_total: 7, consejos_comunales: 36, comunas_vectorizadas: 7, pct_vectorizacion: 100.0 },
  { numero: '', municipio: 'TOTAL', circuitos_total: 199, consejos_comunales: 1361, comunas_vectorizadas: 195, pct_vectorizacion: 97.99 }
];

export const notaMetodologicaCart = `Las poligonales de las comunas y circuitos comunales de los municipios: Maturín, Caripe y Ezequiel Zamora, fueron vectorizadas por el IGVSB, con información suministradas por voceros de cada una de esas OBPP. Los municipios restantes fueron cartografiados tanto las comunas, circuitos comunales y los consejos comunales agregados a esas OBPP, por la Unidad de Cartografía Estadística de INE Monagas, con información proveniente de los nodos, Fundacomunal y Cuadrante de Paz. De las 199 comunas y circuitos comunales, 177 de ellas están 100% vectorizadas con sus consejos comunales, 18 tienen un avance entre 33 al 93% completadas y 4 tienen 0% de avance.`;

export interface CuadroRowSegNodo {
  municipio: string;
  planificados: number;
  instalados: number;
  activos: number;
  inactivos: number;
}

export const cuadroSEG_Nodos: CuadroRowSegNodo[] = [
  { municipio: 'Acosta', planificados: 9, instalados: 9, activos: 2, inactivos: 7 },
  { municipio: 'Aguasay', planificados: 2, instalados: 2, activos: 1, inactivos: 1 },
  { municipio: 'Bolívar', planificados: 5, instalados: 5, activos: 2, inactivos: 3 },
  { municipio: 'Caripe', planificados: 6, instalados: 6, activos: 2, inactivos: 4 },
  { municipio: 'Cedeño', planificados: 8, instalados: 8, activos: 3, inactivos: 5 },
  { municipio: 'Ezequiel Zamora', planificados: 3, instalados: 3, activos: 2, inactivos: 1 },
  { municipio: 'Libertador', planificados: 7, instalados: 7, activos: 2, inactivos: 5 },
  { municipio: 'Maturín', planificados: 40, instalados: 49, activos: 23, inactivos: 26 },
  { municipio: 'Piar', planificados: 9, instalados: 9, activos: 5, inactivos: 4 },
  { municipio: 'Punceres', planificados: 3, instalados: 3, activos: 3, inactivos: 0 },
  { municipio: 'Santa Bárbara', planificados: 2, instalados: 2, activos: 2, inactivos: 0 },
  { municipio: 'Sotillo', planificados: 2, instalados: 2, activos: 2, inactivos: 0 },
  { municipio: 'Uracoa', planificados: 2, instalados: 1, activos: 1, inactivos: 0 },
  { municipio: 'TOTAL', planificados: 98, instalados: 106, activos: 50, inactivos: 56 }
];

export interface CuadroRowSegEncuesta {
  mes: string;
  conteo_rapido: number;
  coyuntura_v2: number;
  transformacion: number;
  laboral: number;
  tramites: number;
  economica_odk: number;
  educacion_medios: number;
  servicios_odk: number;
  total: number;
}

export const cuadroSEG_Encuestas: CuadroRowSegEncuesta[] = [
  { mes: 'Enero', conteo_rapido: 0, coyuntura_v2: 10981, transformacion: 0, laboral: 0, tramites: 0, economica_odk: 5272, educacion_medios: 5276, servicios_odk: 5260, total: 26789 },
  { mes: 'Febrero', conteo_rapido: 0, coyuntura_v2: 11276, transformacion: 0, laboral: 3713, tramites: 0, economica_odk: 4362, educacion_medios: 4368, servicios_odk: 4363, total: 28082 },
  { mes: 'Marzo', conteo_rapido: 0, coyuntura_v2: 8773, transformacion: 0, laboral: 8308, tramites: 0, economica_odk: 4248, educacion_medios: 4196, servicios_odk: 4147, total: 29672 },
  { mes: 'Abril', conteo_rapido: 0, coyuntura_v2: 10355, transformacion: 0, laboral: 9656, tramites: 0, economica_odk: 4495, educacion_medios: 4473, servicios_odk: 4517, total: 33496 },
  { mes: 'Mayo', conteo_rapido: 2238, coyuntura_v2: 8344, transformacion: 0, laboral: 7796, tramites: 248, economica_odk: 3865, educacion_medios: 3813, servicios_odk: 4310, total: 30614 },
  { mes: 'Junio', conteo_rapido: 21604, coyuntura_v2: 6420, transformacion: 0, laboral: 2746, tramites: 2946, economica_odk: 2616, educacion_medios: 2614, servicios_odk: 2597, total: 41543 },
  { mes: 'Julio', conteo_rapido: 21587, coyuntura_v2: 5853, transformacion: 2578, laboral: 3062, tramites: 0, economica_odk: 3006, educacion_medios: 2966, servicios_odk: 2990, total: 42042 },
  { mes: 'Agosto', conteo_rapido: 14281, coyuntura_v2: 3227, transformacion: 2957, laboral: 2591, tramites: 0, economica_odk: 2558, educacion_medios: 2573, servicios_odk: 2527, total: 30714 },
  { mes: 'TOTAL', conteo_rapido: 59710, coyuntura_v2: 65229, transformacion: 5535, laboral: 37872, tramites: 3194, economica_odk: 30422, educacion_medios: 30279, servicios_odk: 30711, total: 262952 }
];

export interface CuadroRowSegEquipo {
  condicion: string;
  laptops: number;
  dmc: number;
  multibam: number | string;
}

export const cuadroSEG_Equipos: CuadroRowSegEquipo[] = [
  { condicion: 'En la Gerencia', laptops: 29, dmc: 9, multibam: 52 },
  { condicion: 'En campo', laptops: 48, dmc: 315, multibam: '—' },
  { condicion: 'Dañadas', laptops: 18, dmc: 472, multibam: '—' },
  { condicion: 'Robadas', laptops: 2, dmc: 73, multibam: 5 },
  { condicion: 'En equipo INE', laptops: 24, dmc: 9, multibam: '—' }
];

// ==============================================================
// LA 8. Coordinación de SEEM (Capacitación y Educación Metodológica)
// ==============================================================
export interface CuadroRowCapacitacion {
  plan: string;
  tipo: string;
  personal_ine: number;
  coord_municipal: number;
  coord_nodo: number;
  supervisor: number;
  encuestador: number;
  total: number;
}

export const cuadroSEEM_Capacitacion: CuadroRowCapacitacion[] = [
  { plan: 'Capacitación metodológica ESCA al equipo SEGEN (nodos 16060 y 16102) Municipio Bolívar', tipo: 'Taller', personal_ine: 0, coord_municipal: 1, coord_nodo: 2, supervisor: 2, encuestador: 0, total: 5 },
  { plan: 'Capacitación metodológica ESCA al equipo SEGEN (nodo 16064) Municipio Caripe', tipo: 'Taller', personal_ine: 0, coord_municipal: 1, coord_nodo: 2, supervisor: 2, encuestador: 0, total: 5 },
  { plan: 'Capacitación metodológica ESCA al equipo SEGEN (nodos 16087, 16089, 16077) Municipio Púnceres', tipo: 'Taller', personal_ine: 0, coord_municipal: 1, coord_nodo: 2, supervisor: 2, encuestador: 1, total: 6 },
  { plan: 'Doble terremoto y respuesta del Estado: La vida y protección como prioridad', tipo: 'Taller', personal_ine: 34, coord_municipal: 0, coord_nodo: 0, supervisor: 0, encuestador: 0, total: 34 },
  { plan: '¿Cambio o crisis climática? Desafíos para la humanidad', tipo: 'Taller', personal_ine: 30, coord_municipal: 0, coord_nodo: 0, supervisor: 0, encuestador: 0, total: 30 },
  { plan: 'De los ACA Comunitarios al presupuesto Nacional: El poder obediencial', tipo: 'Taller', personal_ine: 32, coord_municipal: 0, coord_nodo: 0, supervisor: 0, encuestador: 0, total: 32 },
  { plan: 'Formación e inclusión laboral. Oleada en sector construcción', tipo: 'Taller', personal_ine: 33, coord_municipal: 0, coord_nodo: 0, supervisor: 0, encuestador: 0, total: 33 },
  { plan: 'TOTAL CAPACITADOS AGOSTO 2026', tipo: 'Taller', personal_ine: 129, coord_municipal: 3, coord_nodo: 6, supervisor: 6, encuestador: 1, total: 145 }
];

export interface CuadroRowComite {
  actividad: string;
  ente_convocante: string;
  participantes_ine: number;
  participantes_externos: number;
  total: number;
  fecha: string;
  acuerdos: string;
}

export const cuadroSEEM_Comites: CuadroRowComite[] = [
  {
    actividad: 'Mesa Técnica de Registros Vitales y Estadísticas de Salud',
    ente_convocante: 'Dirección Regional de Salud / CNE Monagas / INE',
    participantes_ine: 2,
    participantes_externos: 4,
    total: 6,
    fecha: '11/08/2026',
    acuerdos: 'Sincronización mensual de actas de defunción y reducción de rezago en hospitales de Maturín'
  }
];

// ==============================================================
// LA 10. Gerencia Estadal (Talento Humano Sede Regional Monagas)
// ==============================================================
export interface CuadroRowGerenciaPersonal {
  condicion: string;
  masculino: number;
  femenino: number;
  total: number;
}

export const cuadroGerenciaEstadal_Personal: CuadroRowGerenciaPersonal[] = [
  { condicion: 'Personal Fijo', masculino: 2, femenino: 3, total: 5 },
  { condicion: 'Personal Contratado', masculino: 18, femenino: 21, total: 39 },
  { condicion: 'Personal Jubilado', masculino: 4, femenino: 6, total: 10 },
  { condicion: 'TOTAL PLANTA INE MONAGAS', masculino: 24, femenino: 30, total: 54 }
];
