<script setup lang="ts">
import { computed } from 'vue';
import { ShieldCheck } from 'lucide-vue-next';

const props = defineProps<{
  activePeriodLabel: string;
  displayCalidadPct: string;
  displayPreciosSinError: number;
  displayPreciosEfec: number;
}>();

// Cálculo reactivo del Donut Gauge de Calidad
const donutOffset = computed(() => {
  const pct = parseFloat(props.displayCalidadPct) || 99.35;
  const circumference = 251.32;
  return (circumference * (1 - pct / 100)).toFixed(2);
});
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div class="pb-3 border-b border-mist">
      <div class="flex items-center gap-2 mb-1">
        <span class="font-mono text-xs font-semibold text-white bg-dept-eco px-2 py-0.5 rounded-[3px]">
          ECO-CAN-03
        </span>
        <ShieldCheck :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Total Precios Levantados Reales (Sin Errores)
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Control de consistencia estadística en {{ activePeriodLabel }}
      </p>
    </div>

    <div class="flex items-center justify-center my-3">
      <div class="relative w-36 h-36 flex items-center justify-center">
        <svg viewBox="0 0 100 100" class="w-full h-full -rotate-90">
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="none"
            stroke="#ededed"
            stroke-width="10"
          />
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="none"
            stroke="#2749ff"
            stroke-width="10"
            stroke-dasharray="251.32"
            :stroke-dashoffset="donutOffset"
            stroke-linecap="round"
            class="transition-all duration-500"
          />
        </svg>
        <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
          <span class="text-2xl font-semibold text-ink-black tracking-tight leading-none">
            {{ displayCalidadPct }}
          </span>
          <span class="text-[10px] font-semibold text-steel uppercase tracking-wider mt-1">
            Efectividad
          </span>
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-2 pt-3 border-t border-mist text-xs">
      <div class="flex items-center justify-between">
        <span class="text-steel font-medium">Precios Sin Errores:</span>
        <span class="font-semibold text-ink-black">{{ displayPreciosSinError.toLocaleString() }} precios</span>
      </div>
      <div class="flex items-center justify-between">
        <span class="text-steel font-medium">Incidencias Subsanadas:</span>
        <span class="font-semibold text-signal-blue">
          {{ (displayPreciosEfec - displayPreciosSinError).toLocaleString() }} casos ({{ (100 - parseFloat(displayCalidadPct)).toFixed(2) }}%)
        </span>
      </div>
      <div class="flex items-center justify-between">
        <span class="text-steel font-medium">Meta Institucional INE:</span>
        <span class="font-semibold text-ink-black">≥ 99.00%</span>
      </div>
    </div>
  </div>
</template>
