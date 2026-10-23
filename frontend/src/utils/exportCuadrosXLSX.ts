import * as XLSX from 'xlsx';
import {
  cuadroECO,
  cuadroSOC_EHM,
  cuadroSOC_ESCA,
  cuadroDEM,
  cuadroCART,
  cuadroSEG_Nodos,
  cuadroSEG_Encuestas,
  cuadroSEG_Equipos,
  cuadroSEEM_Capacitacion,
} from '@/data/cuadrosOficiales';

export function exportCuadroXLSX(deptCode: string) {
  const wb = XLSX.utils.book_new();
  let filename = `INE_Monagas_${deptCode}_Cuadro_Oficial.xlsx`;

  if (deptCode === 'ECO') {
    filename = 'INE_Monagas_ECO_Levantamiento_CAN_2026.xlsx';
    const data = cuadroECO.map((r) => ({
      'Mes': r.mes,
      'Personal Planificado': r.personal_planificado,
      'Personal Levantamiento': r.personal_levantamiento,
      '% Efectividad Personal': `${r.pct_efectividad_personal}%`,
      'Establecimientos Implantados': r.establecimientos_implantados,
      'Comunas CAN': r.comunas_can,
      'Nodos CAN': r.nodos_can,
      'Establecimientos Planificados': r.establecimientos_planificados,
      'Establecimientos Efectivos': r.establecimientos_efectivos,
      '% Efectividad CAN': `${r.pct_efectividad_can}%`,
    }));
    const ws = XLSX.utils.json_to_sheet(data);
    XLSX.utils.book_append_sheet(wb, ws, 'Levantamiento CAN');
  } else if (deptCode === 'SOC') {
    filename = 'INE_Monagas_SOC_Estadisticas_Sociales_2026.xlsx';
    
    // Pestaña 1: EHM
    const dataEHM = cuadroSOC_EHM.map((r) => ({
      'Período': r.periodo,
      'Controles Planificados': r.controles_planificados,
      'Controles Levantados': r.controles_levantados,
      '% Levantamiento': `${r.pct_levantamiento}%`,
      'Viviendas Planificadas': r.viviendas_planificadas,
      'Viviendas Efectivas': r.viviendas_efectivas,
      'Tipo A': r.tipo_a,
      'Tipo B': r.tipo_b,
      'Tipo C': r.tipo_c,
      '% No Respuesta': `${r.pct_no_respuesta}%`,
    }));
    const wsEHM = XLSX.utils.json_to_sheet(dataEHM);
    XLSX.utils.book_append_sheet(wb, wsEHM, 'EHM - Hogares');

    // Pestaña 2: ESCA
    const dataESCA = cuadroSOC_ESCA.map((r) => ({
      'Período': r.periodo,
      'Controles Planificados': r.controles_planificados,
      'Controles Levantados': r.controles_levantados,
      '% Levantamiento': `${r.pct_levantamiento}%`,
      'Viviendas Planificadas': r.viviendas_planificadas,
      'Viviendas Efectivas': r.viviendas_efectivas,
      'Tipo A': r.tipo_a,
      'Tipo B': r.tipo_b,
      'Tipo C': r.tipo_c,
      '% No Respuesta': `${r.pct_no_respuesta}%`,
    }));
    const wsESCA = XLSX.utils.json_to_sheet(dataESCA);
    XLSX.utils.book_append_sheet(wb, wsESCA, 'ESCA - Consumo');
  } else if (deptCode === 'DEM') {
    filename = 'INE_Monagas_DEM_Estadisticas_Vitales_2018_2026.xlsx';
    const data = cuadroDEM.map((r) => ({
      'Año': r.anio,
      'Nacimientos': r.nacimientos,
      'Defunciones': r.defunciones,
      'Matrimonios': r.matrimonios,
      'Unión Estable': r.uniones,
      'Divorcios': r.divorcios,
      'Suicidios': r.suicidios,
      'Total Boletas Recolectadas': r.total_recolectado,
      'Boletas Transcritas': r.transcritas,
      'Pendientes por Transcribir': r.por_transcribir,
    }));
    const ws = XLSX.utils.json_to_sheet(data);
    XLSX.utils.book_append_sheet(wb, ws, 'Estadísticas Vitales');
  } else if (deptCode === 'CART') {
    filename = 'INE_Monagas_CART_Circuitos_Comunales_2026.xlsx';
    const data = cuadroCART.map((r) => ({
      'Nº': r.numero,
      'Municipio': r.municipio,
      'Total Circuitos': r.circuitos_total,
      'Consejos Comunales': r.consejos_comunales,
      'Comunas Vectorizadas': r.comunas_vectorizadas,
      '% Vectorización': `${r.pct_vectorizacion}%`,
    }));
    const ws = XLSX.utils.json_to_sheet(data);
    XLSX.utils.book_append_sheet(wb, ws, 'Circuitos Comunales');
  } else if (deptCode === 'SEG') {
    filename = 'INE_Monagas_SEG_Estructura_y_Nodos_2026.xlsx';

    // Pestaña 1: Nodos
    const dataNodos = cuadroSEG_Nodos.map((r) => ({
      'Municipio': r.municipio,
      'Planificados': r.planificados,
      'Instalados': r.instalados,
      'Activos': r.activos,
      'Inactivos': r.inactivos,
    }));
    const wsNodos = XLSX.utils.json_to_sheet(dataNodos);
    XLSX.utils.book_append_sheet(wb, wsNodos, 'Nodos Municipales');

    // Pestaña 2: Encuestas ODK
    const dataEnc = cuadroSEG_Encuestas.map((r) => ({
      'Mes': r.mes,
      'Conteo Rápido v2': r.conteo_rapido,
      'Coyuntura v2': r.coyuntura_v2,
      'Transformación Estado': r.transformacion,
      'Consulta Laboral': r.laboral,
      'Trámites': r.tramites,
      'Económica ODK': r.economica_odk,
      'Educación y Medios': r.educacion_medios,
      'Servicios ODK': r.servicios_odk,
      'Total Encuestas': r.total,
    }));
    const wsEnc = XLSX.utils.json_to_sheet(dataEnc);
    XLSX.utils.book_append_sheet(wb, wsEnc, 'Encuestas ODK');

    // Pestaña 3: Equipos Tecnológicos
    const dataEq = cuadroSEG_Equipos.map((r) => ({
      'Condición': r.condicion,
      'Laptops y MiniPC': r.laptops,
      'DMC': r.dmc,
      'Multibam': r.multibam,
    }));
    const wsEq = XLSX.utils.json_to_sheet(dataEq);
    XLSX.utils.book_append_sheet(wb, wsEq, 'Equipos DMC');
  } else if (deptCode === 'SEEM') {
    filename = 'INE_Monagas_SEEM_Capacitacion_y_Comites_2026.xlsx';

    // Pestaña 1: Capacitación (LA 8)
    const dataCap = cuadroSEEM_Capacitacion.map((r) => ({
      'Plan de Formación': r.plan,
      'Tipo': r.tipo,
      'Personal INE': r.personal_ine,
      'Coord. Municipal': r.coord_municipal,
      'Coord. Nodo': r.coord_nodo,
      'Supervisor': r.supervisor,
      'Encuestador': r.encuestador,
      'Total': r.total,
    }));
    const wsCap = XLSX.utils.json_to_sheet(dataCap);
    XLSX.utils.book_append_sheet(wb, wsCap, 'LA 8 - Capacitación');

    // Pestaña 2: Comités CCEE (LA 9)
    const dataCom = [
      {
        'Actividad': 'Mesa Técnica de Registros Vitales y Estadísticas de Salud',
        'Ente Convocante': 'Dirección Regional de Salud / CNE / INE',
        'Participantes INE': 2,
        'Participantes Externos': 4,
        'Total Delegados': 6,
        'Fecha': '11/08/2026',
        'Acuerdos': 'Sincronización mensual de actas de defunción y reducción de rezago en hospitales de Maturín'
      }
    ];
    const wsCom = XLSX.utils.json_to_sheet(dataCom);
    XLSX.utils.book_append_sheet(wb, wsCom, 'LA 9 - Comités CCEE');
  }

  // Guardar archivo binario Excel (.xlsx)
  XLSX.writeFile(wb, filename);
}

export function exportConsolidadoXLSX(indicators: any[], summary?: any) {
  const wb = XLSX.utils.book_new();
  const filename = 'INE_Monagas_Consolidado_Indicadores_2026.xlsx';

  // Pestaña 1: Resumen General
  const resumenData = [
    { 'Métrica Institucional': 'Institución', 'Detalle': 'Instituto Nacional de Estadística (INE)' },
    { 'Métrica Institucional': 'Entidad Federal', 'Detalle': 'Estado Monagas (Entidad 16)' },
    { 'Métrica Institucional': 'Período', 'Detalle': 'Agosto 2026' },
    { 'Métrica Institucional': 'Total Unidades Técnicas', 'Detalle': 6 },
    { 'Métrica Institucional': 'Total Indicadores Normativos', 'Detalle': indicators.length },
    { 'Métrica Institucional': 'Cumplimiento General Estadal', 'Detalle': summary?.cumplimiento_general_estadal ? `${summary.cumplimiento_general_estadal}%` : '94.2%' },
  ];
  const wsResumen = XLSX.utils.json_to_sheet(resumenData);
  XLSX.utils.book_append_sheet(wb, wsResumen, 'Resumen Ejecutivo');

  // Pestaña 2: Indicadores
  const indicadoresData = indicators.map((i) => ({
    'Código': i.codigo,
    'Unidad Técnica': i.departamento_codigo,
    'Nombre del Indicador': i.nombre,
    'Categoría': i.categoria_nombre || i.departamento_nombre || 'Oficial',
    'Frecuencia': i.frecuencia || 'Mensual',
    'Unidad de Medida': i.unidad_medida || 'Unidad',
    'Meta Referencial': i.meta_referencial ?? '100%',
    'Descripción': i.descripcion || '',
  }));
  const wsIndicadores = XLSX.utils.json_to_sheet(indicadoresData);
  XLSX.utils.book_append_sheet(wb, wsIndicadores, 'Indicadores Oficiales');

  // Guardar archivo binario Excel (.xlsx)
  XLSX.writeFile(wb, filename);
}

/**
 * Recrea y descarga el libro Excel original oficial analizado:
 * "Cuadros Informe Mensual de Gestion Gerencias Estadales MONAGAS AGOSTO 2026.xlsx"
 * contentivo de las 9 matrices oficiales del INE Monagas.
 */
export function downloadInformeGestionOficial() {
  const link = document.createElement('a');
  link.href = '/Cuadros_Informe_Mensual_de_Gestion_Gerencias_Estadales_MONAGAS_AGOSTO_2026.xlsx';
  link.setAttribute('download', 'Cuadros Informe Mensual de Gestion Gerencias Estadales MONAGAS AGOSTO 2026.xlsx');
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

