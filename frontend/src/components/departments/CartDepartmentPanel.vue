<script setup lang="ts">
import CartKpiCards from './cart/CartKpiCards.vue';
import CartPoligonalesCard from './cart/CartPoligonalesCard.vue';
import CartMunicipalitiesCard from './cart/CartMunicipalitiesCard.vue';

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
    <!-- 1. Tarjetas Resumen de KPIs Cartográficos -->
    <CartKpiCards />

    <!-- 2. Gráficas Especializadas: Estado de Poligonales y Ranking Municipal -->
    <div class="grid grid-cols-1 lg:grid-cols-[1fr_1.8fr] gap-4">
      <CartPoligonalesCard />
      <CartMunicipalitiesCard />
    </div>
  </div>
</template>
