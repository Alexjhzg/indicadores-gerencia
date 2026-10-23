<script setup lang="ts">
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useIndicatorsStore } from '@/stores/indicators';
import DashboardHeader from '@/components/dashboard/DashboardHeader.vue';
import DashboardDepartmentCards, { type DepartmentSummaryMeta } from '@/components/dashboard/DashboardDepartmentCards.vue';
import DashboardStatBlocks, { type DashboardSummaryData } from '@/components/dashboard/DashboardStatBlocks.vue';
import DashboardPerformanceCharts from '@/components/dashboard/DashboardPerformanceCharts.vue';
import DashboardIndicatorsTable from '@/components/dashboard/DashboardIndicatorsTable.vue';
import GerenciaEstadalCard from '@/components/dashboard/GerenciaEstadalCard.vue';
import { downloadInformeGestionOficial } from '@/utils/exportCuadrosXLSX';

const router = useRouter();
const indicatorsStore = useIndicatorsStore();

const activeFilter = ref<string>('TODOS');
const searchQuery = ref<string>('');

const handleExportConsolidado = () => {
  downloadInformeGestionOficial();
};

onMounted(async () => {
  await Promise.all([
    indicatorsStore.fetchDashboardSummary(),
    indicatorsStore.fetchIndicators(),
    indicatorsStore.fetchMeasurements(),
    indicatorsStore.fetchDepartments(),
  ]);
});

// Metadatos oficiales para las 6 unidades técnicas del INE Monagas
const departmentMeta: DepartmentSummaryMeta[] = [
  {
    codigo: 'ECO',
    nombre: 'Estadísticas Económicas',
    descripcion: 'Precios CAN, Directorio Comercial y 25 Comunas',
    total_indicadores: 5,
    meta_ref: '98.5%',
    badgeClass: 'bg-dept-eco text-white',
    activeBtnClass: 'bg-dept-eco text-white',
    borderTop: 'border-t-dept-eco',
    barColor: 'bg-dept-eco',
    lightTag: 'bg-dept-eco-light text-dept-eco border border-dept-eco-border',
  },
  {
    codigo: 'SOC',
    nombre: 'Estadísticas Sociales',
    descripcion: 'Encuestas EHM y ESCA con monitoreo de no respuesta',
    total_indicadores: 6,
    meta_ref: '95.0%',
    badgeClass: 'bg-dept-soc text-white',
    activeBtnClass: 'bg-dept-soc text-white',
    borderTop: 'border-t-dept-soc',
    barColor: 'bg-dept-soc',
    lightTag: 'bg-dept-soc-light text-dept-soc border border-dept-soc-border',
  },
  {
    codigo: 'DEM',
    nombre: 'Demografía y Población',
    descripcion: 'Estadísticas Vitales continuas y transcripción sin rezago',
    total_indicadores: 5,
    meta_ref: '92.3%',
    badgeClass: 'bg-dept-dem text-white',
    activeBtnClass: 'bg-dept-dem text-white',
    borderTop: 'border-t-dept-dem',
    barColor: 'bg-dept-dem',
    lightTag: 'bg-dept-dem-light text-dept-dem border border-dept-dem-border',
  },
  {
    codigo: 'CART',
    nombre: 'Cartografía y Territorio',
    descripcion: '199 Circuitos Comunales y 1.361 Consejos Georreferenciados',
    total_indicadores: 4,
    meta_ref: '97.9%',
    badgeClass: 'bg-dept-cart text-white',
    activeBtnClass: 'bg-dept-cart text-white',
    borderTop: 'border-t-dept-cart',
    barColor: 'bg-dept-cart',
    lightTag: 'bg-dept-cart-light text-dept-cart border border-dept-cart-border',
  },
  {
    codigo: 'SEG',
    nombre: 'Unidad de SEGEN',
    descripcion: '106 Nodos territoriales, 315 DMC y encuestas ODK',
    total_indicadores: 6,
    meta_ref: '91.2%',
    badgeClass: 'bg-dept-seg text-white',
    activeBtnClass: 'bg-dept-seg text-white',
    borderTop: 'border-t-dept-seg',
    barColor: 'bg-dept-seg',
    lightTag: 'bg-dept-seg-light text-dept-seg border border-dept-seg-border',
  },
  {
    codigo: 'SEEM',
    nombre: 'Coordinación de SEEM',
    descripcion: 'Capacitación Metodológica y Comités Estadales (CCEE)',
    total_indicadores: 4,
    meta_ref: '96.7%',
    badgeClass: 'bg-teal-700 text-white',
    activeBtnClass: 'bg-teal-700 text-white',
    borderTop: 'border-t-teal-700',
    barColor: 'bg-teal-700',
    lightTag: 'bg-teal-50 text-teal-800 border border-teal-200',
  },
];

const getDeptBadgeClass = (codigo: string) => {
  const map: Record<string, string> = {
    ECO: 'bg-dept-eco text-white',
    SOC: 'bg-dept-soc text-white',
    DEM: 'bg-dept-dem text-white',
    CART: 'bg-dept-cart text-white',
    SEG: 'bg-dept-seg text-white',
    SEEM: 'bg-teal-700 text-white',
  };
  return map[codigo] || 'bg-mist text-ink-black';
};

const getDeptCount = (codigo: string) => {
  return indicatorsStore.indicators.filter((i) => i.departamento_codigo === codigo).length;
};

const summary = computed<DashboardSummaryData>(() => indicatorsStore.dashboardSummary || {
  cumplimiento_general_estadal: 94.2,
  total_departamentos: 6,
  total_indicadores_activos: indicatorsStore.indicators.length || 30,
  total_mediciones_aprobadas: 30,
});

const navigateToDepartment = (codigo: string) => {
  router.push(`/departamentos/${codigo}`);
};

const filterByDept = (codigo: string) => {
  activeFilter.value = codigo;
  indicatorsStore.setSelectedDepartment(codigo as any);
};

const displayIndicators = computed(() => {
  let list = indicatorsStore.indicators;
  if (activeFilter.value !== 'TODOS') {
    list = list.filter((i) => i.departamento_codigo === activeFilter.value);
  }
  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase().trim();
    list = list.filter(
      (i) =>
        i.codigo.toLowerCase().includes(q) ||
        i.nombre.toLowerCase().includes(q) ||
        (i.descripcion && i.descripcion.toLowerCase().includes(q))
    );
  }
  return list;
});
</script>

<template>
  <div class="py-10 max-md:py-5 pb-20">
    <div class="max-w-[1440px] mx-auto px-10 max-md:px-4 flex flex-col gap-10 max-md:gap-6">
      
      <!-- 1. Cabecera Ejecutiva -->
      <DashboardHeader @export-xlsx="handleExportConsolidado" />

      <!-- 2. Arquitectura "Unit-First": Tarjetas de las 5 Unidades Técnicas -->
      <DashboardDepartmentCards
        :departments="departmentMeta"
        :active-filter="activeFilter"
        :get-dept-count="getDeptCount"
        @select-dept="navigateToDepartment"
      />

      <!-- 3. Stat Blocks & Métricas Globales -->
      <DashboardStatBlocks :summary="summary" />

      <!-- 4. Visualizaciones Gráficas SVG en Signal Blue -->
      <DashboardPerformanceCharts :global-compliance="summary.cumplimiento_general_estadal" />

      <!-- 5. Información de Gestión Institucional y Talento Humano (LA 10. Gerencia Estadal) -->
      <GerenciaEstadalCard />

      <!-- 6. Tabla de Indicadores con Buscador y Filtro Departamental -->
      <DashboardIndicatorsTable
        v-model:active-filter="activeFilter"
        v-model:search-query="searchQuery"
        :indicators="displayIndicators"
        :departments="departmentMeta"
        :total-indicators-count="indicatorsStore.indicators.length"
        :get-dept-badge-class="getDeptBadgeClass"
        :get-dept-count="getDeptCount"
        @navigate="navigateToDepartment"
        @filter-dept="filterByDept"
      />

    </div>
  </div>
</template>
