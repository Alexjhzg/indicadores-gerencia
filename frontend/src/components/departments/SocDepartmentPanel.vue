<script setup lang="ts">
import { ref, computed } from 'vue';
import { datosSocialesPorMes } from '@/data/departmentMonthlyData';
import SocFilterBar from './soc/SocFilterBar.vue';
import SocKpiCards from './soc/SocKpiCards.vue';
import SocComparisonBarChart from './soc/SocComparisonBarChart.vue';
import SocNonResponseCard from './soc/SocNonResponseCard.vue';
import SocHouseholdStructureCard from './soc/SocHouseholdStructureCard.vue';

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

const selectedMes = defineModel<string>('selectedMes', { default: 'Ago' });
const activeSubprogram = ref<'TODOS' | 'EHM' | 'ESCA'>('TODOS');

const currentSocData = computed(() => {
  const mes = selectedMes.value;
  if (mes && mes in datosSocialesPorMes) {
    return datosSocialesPorMes[mes];
  }
  return datosSocialesPorMes['Ago'] || Object.values(datosSocialesPorMes)[0];
});
</script>

<template>
  <div class="flex flex-col gap-6 w-full min-w-0 max-w-full overflow-hidden">
    <!-- Filtros de Período (Mes) y Subprogramas Sociales (Consolidado, EHM, ESCA) -->
    <SocFilterBar
      v-model:selected-mes="selectedMes"
      v-model:active-subprogram="activeSubprogram"
    />

    <!-- 1. Tarjetas Resumen de Indicadores Sociales (EHM y ESCA) -->
    <SocKpiCards
      :current-soc-data="currentSocData"
      :active-subprogram="activeSubprogram"
    />

    <!-- 2. Gráficas Comparativas y Monitoreo de No Respuesta Tipo A -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
      <SocComparisonBarChart :current-soc-data="currentSocData" />
      <SocNonResponseCard :current-soc-data="currentSocData" />
    </div>

    <!-- 3. Composición de Muestra de Hogares Entrevistados vs Rechazos -->
    <SocHouseholdStructureCard :current-soc-data="currentSocData" />
  </div>
</template>
