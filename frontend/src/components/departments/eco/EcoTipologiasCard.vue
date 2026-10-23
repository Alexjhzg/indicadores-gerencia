<script setup lang="ts">
import { Store, CheckCircle2 } from 'lucide-vue-next';
import type { EconomicasMesData } from '@/data/departmentMonthlyData';

defineProps<{
  currentMesData: EconomicasMesData;
}>();
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between gap-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-mist">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="font-mono text-xs font-semibold text-white bg-dept-eco px-2 py-0.5 rounded-[3px]">
            ECO-CAN-01
          </span>
          <Store :size="16" :stroke-width="1.5" class="text-dept-eco shrink-0" />
          <h3 class="text-base font-semibold text-ink-black">
            Total Establecimientos con Encuesta Efectiva en el Levantamiento de Precios CAN
          </h3>
        </div>
        <p class="text-xs font-normal text-steel">
          Muestra de {{ currentMesData.planif_locales }} establecimientos comerciales planificados investigados al {{ currentMesData.pct_locales }} en {{ currentMesData.mesNombre }}
        </p>
      </div>
      <span class="inline-flex items-center gap-1 text-xs font-semibold px-2 py-0.5 bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px] shrink-0">
        <CheckCircle2 :size="13" :stroke-width="1.5" />
        <span>{{ currentMesData.pct_locales }} Efectividad Total</span>
      </span>
    </div>

    <!-- Desglose por Tipologías de Comercio -->
    <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-2.5">
      <div
        v-for="tip in currentMesData.tipologias"
        :key="tip.nombre"
        class="border border-ash rounded-[3px] p-3 flex flex-col justify-between gap-2 bg-white hover:border-ink-black transition-colors"
      >
        <div>
          <div class="flex items-center justify-between mb-1">
            <span class="text-xs font-semibold text-dept-eco">{{ tip.porcentaje }}</span>
            <span class="text-xs font-medium text-steel">{{ tip.locales }} locales</span>
          </div>
          <h4 class="text-xs font-semibold text-ink-black leading-snug">{{ tip.nombre }}</h4>
        </div>
        <div class="flex items-center justify-between pt-1.5 border-t border-mist text-[11px]">
          <span class="text-steel font-medium">Cotizaciones:</span>
          <span class="font-semibold text-ink-black">{{ tip.cotizaciones }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
