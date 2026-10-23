<script setup lang="ts">
import { Search } from 'lucide-vue-next';
import IndicatorCard, { type IndicatorData, type MeasurementDisplay } from './IndicatorCard.vue';
import { mesesDisponibles } from '@/data/departmentMonthlyData';

defineProps<{
  selectedMonthName: string;
  filteredIndicators: IndicatorData[];
  activeBtnClass?: string;
  getMeasurement: (indId: string, indCode: string) => MeasurementDisplay | null;
}>();

const selectedMonth = defineModel<string>('selectedMonth', { required: true });
const searchQuery = defineModel<string>('searchQuery', { default: '' });
</script>

<template>
  <section class="flex flex-col gap-4 pt-4 border-t border-mist">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
      <div>
        <div class="flex items-center gap-2">
          <h2 class="text-base font-semibold text-ink-black">
            Fichas Técnicas de Indicadores Oficiales ({{ filteredIndicators.length }})
          </h2>
          <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black border border-ash">
            {{ selectedMonthName }} 2026
          </span>
        </div>
        <span class="text-xs font-normal text-steel">
          Registro normativo del Informe Mensual de Gestión con valores reales de {{ selectedMonthName }} 2026
        </span>
      </div>

      <!-- Selector rápido de meses para las fichas y buscador -->
      <div class="flex flex-col sm:flex-row sm:items-center gap-2.5">
        <div class="inline-flex rounded-[3px] border border-ash p-0.5 bg-mist/60 overflow-x-auto max-w-full">
          <button
            v-for="m in mesesDisponibles"
            :key="m.id"
            type="button"
            class="px-2 py-1 text-[11px] font-semibold rounded-[3px] transition-colors cursor-pointer border-none shrink-0"
            :class="selectedMonth === m.id ? (activeBtnClass || 'bg-ink-black text-white') : 'text-steel hover:text-ink-black bg-transparent'"
            @click="selectedMonth = m.id"
          >
            {{ m.nombreCorto }}
          </button>
        </div>

        <!-- Buscador de indicadores -->
        <div class="relative w-full sm:w-64">
          <Search :size="15" :stroke-width="1.5" class="absolute left-3 top-1/2 -translate-y-1/2 text-steel" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Buscar por código o nombre..."
            class="w-full pl-9 pr-3 py-1.5 text-xs font-medium border border-ash rounded-[3px] bg-white text-ink-black focus:outline-none focus:border-signal-blue"
          />
        </div>
      </div>
    </div>

    <!-- Grid de Indicadores con Mediciones Reales -->
    <div class="grid grid-cols-3 max-lg:grid-cols-2 max-md:grid-cols-1 gap-4">
      <IndicatorCard
        v-for="ind in filteredIndicators"
        :key="ind.id"
        :indicator="ind"
        :measurement="getMeasurement(ind.id, ind.codigo)"
        :selected-month="selectedMonth"
      />
    </div>
  </section>
</template>
