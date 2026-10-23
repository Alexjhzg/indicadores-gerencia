<script setup lang="ts">
import { computed } from 'vue';
import { datosSegPorMes } from '@/data/departmentMonthlyData';
import SegFilterBar from './seg/SegFilterBar.vue';
import SegKpiCards from './seg/SegKpiCards.vue';
import SegNodesCard from './seg/SegNodesCard.vue';
import SegOdkSurveysCard from './seg/SegOdkSurveysCard.vue';

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

const currentSegData = computed(() => {
  const key = selectedMes.value in datosSegPorMes ? selectedMes.value : 'Ago';
  return datosSegPorMes[key];
});
const encuestasODK = computed(() => currentSegData.value.encuestas);
</script>

<template>
  <div class="flex flex-col gap-6 w-full min-w-0 max-w-full overflow-hidden">
    <!-- Barra de Filtro de Mes -->
    <SegFilterBar
      v-model:selected-mes="selectedMes"
      :mes-nombre="currentSegData.mesNombre"
    />
    
    <!-- 1. Tarjetas de Resumen de KPIs de Seguimiento y SEGEN -->
    <SegKpiCards :current-seg-data="currentSegData" />

    <!-- 2. Gráficas Especializadas: Red de Nodos y Distribución de Encuestas ODK -->
    <div class="grid grid-cols-1 lg:grid-cols-[1.4fr_1.6fr] gap-4">
      <SegNodesCard />
      <SegOdkSurveysCard
        :mes-nombre="currentSegData.mesNombre"
        :encuestas="encuestasODK"
      />
    </div>
  </div>
</template>
