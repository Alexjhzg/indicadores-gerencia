<script setup lang="ts">
import { computed } from 'vue';
import { datosEconomicasPorMes } from '@/data/departmentMonthlyData';
import EcoFilterBar from './eco/EcoFilterBar.vue';
import EcoKpiCards from './eco/EcoKpiCards.vue';
import EcoPersonalSection from './eco/EcoPersonalSection.vue';
import EcoDirectorySection from './eco/EcoDirectorySection.vue';
import EcoComunasCard from './eco/EcoComunasCard.vue';
import EcoTipologiasCard from './eco/EcoTipologiasCard.vue';
import EcoWeeklyPricesChart from './eco/EcoWeeklyPricesChart.vue';
import EcoQualityDonutChart from './eco/EcoQualityDonutChart.vue';

interface IndicatorItem {
  id: string;
  codigo: string;
  nombre: string;
  descripcion: string;
  meta_referencial: number | null;
  unidad_medida: string;
}

defineProps<{
  indicators: IndicatorItem[];
}>();

// ==========================================
// SELECTORES DE PERÍODO (MES Y SEMANA) CON DEFINE_MODEL
// ==========================================
const selectedMes = defineModel<string>('selectedMes', { default: 'Ago' });
const selectedSemana = defineModel<string>('selectedSemana', { default: 'TODAS' });

// Objeto reactivo del mes seleccionado
const currentMesData = computed(() => datosEconomicasPorMes[selectedMes.value]);

// Objeto reactivo de la semana seleccionada
const currentSemanaData = computed(() => {
  if (selectedSemana.value === 'TODAS') return null;
  return currentMesData.value.semanas.find(s => s.id === selectedSemana.value) || null;
});

// Resumen del período activo
const activePeriodLabel = computed(() => {
  if (selectedSemana.value === 'TODAS') {
    return `${currentMesData.value.mesNombre} 2026 · Mes Completo`;
  }
  return `${currentMesData.value.mesNombre} 2026 · Semana ${selectedSemana.value}`;
});

// Métricas de calidad y precios calculadas reactivamente
const displayCalidadPct = computed(() => {
  return currentSemanaData.value
    ? currentSemanaData.value.pct_calidad
    : currentMesData.value.pct_precios_calidad;
});

const displayPreciosSinError = computed(() => {
  return currentSemanaData.value
    ? currentSemanaData.value.sin_error
    : currentMesData.value.precios_sin_error;
});

const displayPreciosEfec = computed(() => {
  return currentSemanaData.value
    ? currentSemanaData.value.precios
    : currentMesData.value.precios_efec;
});

const displayMetaPrecios = computed(() => {
  return currentSemanaData.value
    ? currentSemanaData.value.meta
    : currentMesData.value.meta_precios_mes;
});

const displayCumplimientoPrecios = computed(() => {
  const efec = displayPreciosEfec.value;
  const meta = displayMetaPrecios.value;
  return ((efec / meta) * 100).toFixed(1) + '%';
});
</script>

<template>
  <div class="flex flex-col gap-6 w-full min-w-0 max-w-full overflow-hidden">
    <!-- Barra de Filtros: Meses y Semanas con indicador de período -->
    <EcoFilterBar
      v-model:selected-mes="selectedMes"
      v-model:selected-semana="selectedSemana"
      :active-period-label="activePeriodLabel"
    />

    <!-- 1. Tarjetas de Resumen en orden de hoja técnica (ECO-PRE-01 a ECO-CAN-03) -->
    <EcoKpiCards
      :current-mes-data="currentMesData"
      :display-cumplimiento-precios="displayCumplimientoPrecios"
      :display-precios-efec="displayPreciosEfec"
      :display-meta-precios="displayMetaPrecios"
      :display-calidad-pct="displayCalidadPct"
      :display-precios-sin-error="displayPreciosSinError"
      :selected-semana="selectedSemana"
    />

    <!-- 2. Sección: Personal en Levantamiento (ECO-PRE-01) y Directorio de Establecimientos (ECO-DIR-01) -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
      <EcoPersonalSection
        v-model:selected-mes="selectedMes"
        :current-mes-data="currentMesData"
      />
      <EcoDirectorySection
        v-model:selected-mes="selectedMes"
        :current-mes-data="currentMesData"
      />
    </div>

    <!-- 3. Sección: Cobertura Comunal (ECO-CAN-04) y Tipologías Comerciales Efectivas (ECO-CAN-01) -->
    <div class="grid grid-cols-1 lg:grid-cols-[1.1fr_1.9fr] gap-4">
      <EcoComunasCard :current-mes-data="currentMesData" />
      <EcoTipologiasCard :current-mes-data="currentMesData" />
    </div>

    <!-- 4. Sección: Captura Semanal de Precios (ECO-CAN-02) y Control de Calidad Donut (ECO-CAN-03) -->
    <div class="grid grid-cols-1 lg:grid-cols-[1.8fr_1.2fr] gap-4">
      <EcoWeeklyPricesChart
        v-model:selected-semana="selectedSemana"
        :current-mes-data="currentMesData"
        :display-precios-efec="displayPreciosEfec"
        :display-meta-precios="displayMetaPrecios"
        :display-cumplimiento-precios="displayCumplimientoPrecios"
      />
      <EcoQualityDonutChart
        :active-period-label="activePeriodLabel"
        :display-calidad-pct="displayCalidadPct"
        :display-precios-sin-error="displayPreciosSinError"
        :display-precios-efec="displayPreciosEfec"
      />
    </div>
  </div>
</template>
