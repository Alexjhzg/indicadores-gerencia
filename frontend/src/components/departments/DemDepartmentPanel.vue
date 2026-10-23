<script setup lang="ts">
import DemKpiCards from './dem/DemKpiCards.vue';
import DemVitalEventsDonut from './dem/DemVitalEventsDonut.vue';
import DemDigitalizationCard from './dem/DemDigitalizationCard.vue';

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
</script>

<template>
  <div class="flex flex-col gap-8 w-full min-w-0 max-w-full overflow-hidden">
    <!-- 1. Tarjetas de Resumen de KPIs Demográficos -->
    <DemKpiCards />

    <!-- 2. Gráficas Especializadas: Donut de Hechos Vitales y Tasa de Digitalización -->
    <div class="grid grid-cols-1 lg:grid-cols-[1.5fr_1.5fr] gap-4">
      <DemVitalEventsDonut />
      <DemDigitalizationCard />
    </div>
  </div>
</template>
