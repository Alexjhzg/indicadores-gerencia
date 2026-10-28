<script setup lang="ts">
import { computed, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useIndicatorsStore } from '@/stores/indicators';
import { useAuthStore } from '@/stores/auth';
import { BarChart3, FileSpreadsheet } from 'lucide-vue-next';

import EcoDepartmentPanel from '@/components/departments/EcoDepartmentPanel.vue';
import SocDepartmentPanel from '@/components/departments/SocDepartmentPanel.vue';
import DemDepartmentPanel from '@/components/departments/DemDepartmentPanel.vue';
import CartDepartmentPanel from '@/components/departments/CartDepartmentPanel.vue';
import SegDepartmentPanel from '@/components/departments/SegDepartmentPanel.vue';
import SeemDepartmentPanel from '@/components/departments/SeemDepartmentPanel.vue';
import CuadrosOficialesView from '@/components/departments/CuadrosOficialesView.vue';

import DepartmentNavHeader from '@/components/departments/detail/DepartmentNavHeader.vue';
import DepartmentHeaderCard, { type DepartmentMeta } from '@/components/departments/detail/DepartmentHeaderCard.vue';
import DepartmentIndicatorsCatalog from '@/components/departments/detail/DepartmentIndicatorsCatalog.vue';
import { getDynamicIndicatorMeasurement, mesesDisponibles } from '@/data/departmentMonthlyData';

const route = useRoute();
const router = useRouter();
const indicatorsStore = useIndicatorsStore();
const authStore = useAuthStore();

const searchQuery = ref('');
const activeViewMode = ref<'CUADROS' | 'GRAFICOS'>('GRAFICOS');
const selectedMonth = ref<string>('Ago');
const selectedSemana = ref<string>('TODAS');

const selectedMonthName = computed(() => {
  const m = mesesDisponibles.find((mes) => mes.id === selectedMonth.value);
  return m ? m.nombre : 'Agosto';
});

const deptCode = computed(() => (route.params.id as string || 'ECO').toUpperCase());

const departmentInfo: Record<string, DepartmentMeta> = {
  ECO: {
    nombre: 'Unidad de Estadísticas Económicas',
    desc: 'Gerencia de Precios, Directorio de Tipologías y Canasta Alimentaria Normativa (CAN) en 25 comunas del estado Monagas.',
    coordinacion: 'Wilfredo Rojas',
    indicadores: 5,
    colorName: 'Verde Esmeralda',
    badgeClass: 'bg-dept-eco text-white',
    activeBtnClass: 'bg-dept-eco text-white',
    borderTopClass: 'border-t-dept-eco',
    lightTagClass: 'bg-dept-eco-light text-dept-eco border-dept-eco-border',
    accentHex: '#15803d',
  },
  SOC: {
    nombre: 'Unidad de Estadísticas Sociales',
    desc: 'Encuesta de Hogares por Muestreo (EHM) y Encuesta de Seguimiento al Consumo de Alimentos (ESCA) con control muestral de no respuesta.',
    coordinacion: 'Rubén Alejandro',
    indicadores: 6,
    colorName: 'Azul Zafiro',
    badgeClass: 'bg-dept-soc text-white',
    activeBtnClass: 'bg-dept-soc text-white',
    borderTopClass: 'border-t-dept-soc',
    lightTagClass: 'bg-dept-soc-light text-dept-soc border-dept-soc-border',
    accentHex: '#1d4ed8',
  },
  DEM: {
    nombre: 'Unidad de Demografía y Población',
    desc: 'Registro continuo de hechos vitales (Nacimientos, Defunciones, Nupcialidad) y flujo informático de boletas sin rezago.',
    coordinacion: 'Cledys Bastardo',
    indicadores: 5,
    colorName: 'Borgoña Censal',
    badgeClass: 'bg-dept-dem text-white',
    activeBtnClass: 'bg-dept-dem text-white',
    borderTopClass: 'border-t-dept-dem',
    lightTagClass: 'bg-dept-dem-light text-dept-dem border-dept-dem-border',
    accentHex: '#991b1b',
  },
  CART: {
    nombre: 'Unidad de Cartografía',
    desc: 'Proyecto Circuitos Comunales, delimitación de consejos comunales y vectorización territorial con IGVSB en los 13 Municipios.',
    coordinacion: 'Henri Guevara',
    indicadores: 4,
    colorName: 'Ámbar Ocre',
    badgeClass: 'bg-dept-cart text-white',
    activeBtnClass: 'bg-dept-cart text-white',
    borderTopClass: 'border-t-dept-cart',
    lightTagClass: 'bg-dept-cart-light text-dept-cart border-dept-cart-border',
    accentHex: '#b45309',
  },
  SEG: {
    nombre: 'Unidad de SEGEN',
    desc: 'Red territorial de 106 nodos, parque tecnológico DMC, cuestionarios electrónicos ODK y despliegue territorial en los 13 municipios.',
    coordinacion: 'Johana Larez',
    indicadores: 6,
    colorName: 'Pizarra Tecnológica',
    badgeClass: 'bg-dept-seg text-white',
    activeBtnClass: 'bg-dept-seg text-white',
    borderTopClass: 'border-t-dept-seg',
    lightTagClass: 'bg-dept-seg-light text-dept-seg border-dept-seg-border',
    accentHex: '#4338ca',
  },
  SEEM: {
    nombre: 'Coordinación de SEEM',
    desc: 'Seguimiento, Evaluación, Educación Metodológica y Comités de Coordinación Estadística (CCEE) del estado Monagas.',
    coordinacion: 'Luis Velásquez',
    indicadores: 4,
    colorName: 'Teal Institucional',
    badgeClass: 'bg-teal-700 text-white',
    activeBtnClass: 'bg-teal-700 text-white',
    borderTopClass: 'border-t-teal-700',
    lightTagClass: 'bg-teal-50 text-teal-800 border-teal-200',
    accentHex: '#0f766e',
  },
};

const currentDept = computed<DepartmentMeta>(() => {
  return departmentInfo[deptCode.value] || {
    nombre: `Unidad ${deptCode.value}`,
    desc: 'Unidad técnica operativa de la Gerencia Estadal Monagas',
    coordinacion: 'Jefe de Unidad Técnica Operativa',
    indicadores: 5,
    colorName: 'Institucional',
    badgeClass: 'bg-ink-black text-white',
    activeBtnClass: 'bg-ink-black text-white',
    borderTopClass: 'border-t-ink-black',
    lightTagClass: 'bg-mist text-steel border-ash',
    accentHex: '#000000',
  };
});

onMounted(async () => {
  // Aislamiento estricto: Si es Jefe de Unidad y está en un departamento ajeno, redirigir al suyo
  if (authStore.isEncargado && authStore.userDept && deptCode.value !== authStore.userDept) {
    router.replace(`/departamentos/${authStore.userDept}`);
    return;
  }

  if (indicatorsStore.indicators.length === 0) {
    await indicatorsStore.fetchIndicators();
  }
  if (indicatorsStore.measurements.length === 0) {
    await indicatorsStore.fetchMeasurements();
  }
});

const deptIndicators = computed(() => {
  return indicatorsStore.indicators.filter(
    (i) => i.departamento_codigo === deptCode.value
  );
});

const filteredIndicators = computed(() => {
  if (!searchQuery.value.trim()) return deptIndicators.value;
  const q = searchQuery.value.toLowerCase().trim();
  return deptIndicators.value.filter(
    (ind) =>
      ind.codigo.toLowerCase().includes(q) ||
      ind.nombre.toLowerCase().includes(q) ||
      (ind.descripcion && ind.descripcion.toLowerCase().includes(q))
  );
});

const getMeasurement = (indId: string, indCode: string) => {
  const dynamic = getDynamicIndicatorMeasurement(
    deptCode.value,
    indCode,
    selectedMonth.value,
    selectedSemana.value
  );
  if (dynamic) {
    return {
      valor_registrado: dynamic.valor_registrado,
      meta_periodo: dynamic.meta_periodo,
      cumplimientoTexto: dynamic.cumplimientoTexto,
      cumplimientoClass: dynamic.cumplimientoClass,
      periodoLabel: dynamic.periodoLabel,
      unidad_medida: dynamic.unidad_medida,
    };
  }
  const fallback = indicatorsStore.measurements.find(
    (m) =>
      (!m.municipio_id || m.municipio_id === null) &&
      (m.indicador_id === indId || m.indicador_codigo === indCode)
  );
  if (fallback) {
    return {
      valor_registrado: fallback.valor_registrado,
      meta_periodo: fallback.meta_periodo,
      cumplimientoTexto: 'Certificado',
      cumplimientoClass: 'text-signal-blue',
      periodoLabel: `${selectedMonthName.value} 2026`,
      unidad_medida: '',
    };
  }
  return null;
};

const goBack = () => {
  if (authStore.isEncargado || authStore.isJefeArea) {
    router.push('/operaciones');
  } else {
    router.push('/dashboard');
  }
};

const selectDept = (code: string) => {
  if (authStore.isEncargado && authStore.userDept && code !== authStore.userDept) {
    return;
  }
  if (authStore.isJefeArea && !authStore.allowedDepts.includes(code as any)) {
    return;
  }
  router.push(`/departamentos/${code}`);
};
</script>

<template>
  <div class="py-10 max-md:py-5 max-md:pb-24 pb-24 w-full max-w-full overflow-x-hidden">
    <div class="max-w-[1440px] mx-auto px-10 max-md:px-4 flex flex-col gap-8 max-md:gap-5 w-full min-w-0">
      
      <!-- 1. Barra Superior de Navegación y Selectores Departamentales -->
      <DepartmentNavHeader
        :dept-code="deptCode"
        :department-info="departmentInfo"
        @back="goBack"
        @select-dept="selectDept"
      />

      <!-- 2. Tarjeta de Cabecera Oficial de la Unidad Técnica -->
      <DepartmentHeaderCard
        :dept-code="deptCode"
        :current-dept="currentDept"
        :indicators-count="deptIndicators.length || currentDept.indicadores"
      />

      <!-- Selector de Modo de Visualización: Cuadros Oficiales vs Gráficos e Indicadores -->
      <div class="grid grid-cols-2 sm:flex sm:items-center gap-1.5 sm:gap-2 border-b border-ash pb-1 w-full">
        <button
          type="button"
          class="inline-flex items-center justify-center gap-1.5 sm:gap-2 px-2.5 sm:px-4 py-2 sm:py-2.5 text-xs sm:text-sm font-semibold rounded-[3px] transition-colors cursor-pointer border-none text-center sm:shrink-0"
          :class="activeViewMode === 'CUADROS' ? (currentDept.activeBtnClass || 'bg-ink-black text-white') : 'bg-mist text-steel hover:text-ink-black'"
          @click="activeViewMode = 'CUADROS'"
        >
          <FileSpreadsheet :size="16" :stroke-width="1.5" class="shrink-0" />
          <span class="hidden sm:inline">Cuadros del Informe Mensual (Matriz Oficial)</span>
          <span class="sm:hidden">Cuadros Oficiales</span>
        </button>

        <button
          type="button"
          class="inline-flex items-center justify-center gap-1.5 sm:gap-2 px-2.5 sm:px-4 py-2 sm:py-2.5 text-xs sm:text-sm font-semibold rounded-[3px] transition-colors cursor-pointer border-none text-center sm:shrink-0"
          :class="activeViewMode === 'GRAFICOS' ? (currentDept.activeBtnClass || 'bg-ink-black text-white') : 'bg-mist text-steel hover:text-ink-black'"
          @click="activeViewMode = 'GRAFICOS'"
        >
          <BarChart3 :size="16" :stroke-width="1.5" class="shrink-0" />
          <span class="hidden sm:inline">Gráficos y Fichas de Indicadores</span>
          <span class="sm:hidden">Gráficos e Indicadores</span>
        </button>
      </div>

      <!-- VISTA 1: CUADROS OFICIALES REPLICADOS DEL INFORME MENSUAL EXCEL -->
      <section v-if="activeViewMode === 'CUADROS'" class="flex flex-col gap-4">
        <CuadrosOficialesView :dept-code="deptCode" />
      </section>

      <!-- VISTA 2: TABLERO ANALÍTICO Y FICHAS TÉCNICAS -->
      <template v-else>
        <!-- 3. Panel Especializado de Indicadores y Gráficos por Departamento -->
        <section class="flex flex-col gap-4">
          <div class="flex items-center gap-2 text-ink-black">
            <BarChart3 :size="18" :stroke-width="1.5" class="shrink-0 text-signal-blue" />
            <h2 class="text-lg font-semibold tracking-tight">Tablero Analítico y Visualizaciones Especializadas</h2>
          </div>

          <EcoDepartmentPanel
            v-if="deptCode === 'ECO'"
            v-model:selected-mes="selectedMonth"
            v-model:selected-semana="selectedSemana"
            :indicators="deptIndicators"
          />
          <SocDepartmentPanel
            v-else-if="deptCode === 'SOC'"
            v-model:selected-mes="selectedMonth"
            :indicators="deptIndicators"
          />
          <DemDepartmentPanel
            v-else-if="deptCode === 'DEM'"
            :indicators="deptIndicators"
          />
          <CartDepartmentPanel
            v-else-if="deptCode === 'CART'"
            :indicators="deptIndicators"
          />
          <SegDepartmentPanel
            v-else-if="deptCode === 'SEG'"
            v-model:selected-mes="selectedMonth"
            :indicators="deptIndicators"
          />
          <SeemDepartmentPanel
            v-else-if="deptCode === 'SEEM'"
            v-model:selected-mes="selectedMonth"
            :indicators="deptIndicators"
          />
        </section>

        <!-- 4. Catálogo Detallado de Fichas Técnicas de Indicadores -->
        <DepartmentIndicatorsCatalog
          v-model:selected-month="selectedMonth"
          v-model:search-query="searchQuery"
          :selected-month-name="selectedMonthName"
          :filtered-indicators="filteredIndicators"
          :active-btn-class="currentDept.activeBtnClass"
          :get-measurement="getMeasurement"
        />
      </template>

    </div>
  </div>
</template>
