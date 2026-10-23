<script setup lang="ts">
import { computed } from 'vue';
import { Home } from 'lucide-vue-next';
import type { SocialesMesData } from '@/data/departmentMonthlyData';

const props = defineProps<{
  currentSocData: SocialesMesData;
}>();

const noRespPct = computed(() => parseFloat(props.currentSocData.no_resp) || 20.49);
const efecPct = computed(() => (100 - noRespPct.value).toFixed(1));
const totalEhmViv = computed(() => Math.round(props.currentSocData.ehm_viv_efec / (parseFloat(efecPct.value) / 100)));
const tipoAViv = computed(() => totalEhmViv.value - props.currentSocData.ehm_viv_efec);
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col gap-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <Home :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
          <h3 class="text-base font-semibold text-ink-black">
            Estructura Muestral de Hogares: Entrevistas Efectivas vs Rechazos (Tipo A)
          </h3>
        </div>
        <span class="text-xs font-normal text-steel">
          Detalle del volumen de viviendas investigadas en los sectores muestrales de Monagas
        </span>
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-mist text-ink-black rounded-[3px] self-start sm:self-auto">
        Monagas · {{ currentSocData.mesNombre }} 2026
      </span>
    </div>

    <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-4">
      <!-- Panel EHM -->
      <div class="border border-mist rounded-[3px] p-4 flex flex-col gap-3">
        <div class="flex items-center justify-between">
          <h4 class="text-sm font-semibold text-ink-black">Encuesta EHM (Hogares)</h4>
          <span class="text-xs font-semibold text-steel">{{ totalEhmViv }} Viviendas Totales</span>
        </div>
        <div class="flex items-center gap-4 text-xs">
          <div class="flex items-center gap-1.5">
            <span class="w-3 h-3 bg-signal-blue rounded-sm"></span>
            <span class="text-ink-black font-semibold">{{ currentSocData.ehm_viv_efec }} Efectivas ({{ efecPct }}%)</span>
          </div>
          <div class="flex items-center gap-1.5">
            <span class="w-3 h-3 bg-ash rounded-sm"></span>
            <span class="text-steel font-medium">{{ tipoAViv }} Tipo A ({{ noRespPct }}%)</span>
          </div>
        </div>
        <div class="w-full h-2 bg-mist rounded-sm overflow-hidden flex">
          <div class="h-full bg-signal-blue" :style="{ width: `${efecPct}%` }"></div>
          <div class="h-full bg-ash" :style="{ width: `${noRespPct}%` }"></div>
        </div>
      </div>

      <!-- Panel ESCA -->
      <div class="border border-mist rounded-[3px] p-4 flex flex-col gap-3">
        <div class="flex items-center justify-between">
          <h4 class="text-sm font-semibold text-ink-black">Encuesta ESCA (Consumo Alimentario)</h4>
          <span class="text-xs font-semibold text-steel">194 Viviendas Totales</span>
        </div>
        <div class="flex items-center gap-4 text-xs">
          <div class="flex items-center gap-1.5">
            <span class="w-3 h-3 bg-signal-blue rounded-sm"></span>
            <span class="text-ink-black font-semibold">139 Efectivas (71.6%)</span>
          </div>
          <div class="flex items-center gap-1.5">
            <span class="w-3 h-3 bg-ash rounded-sm"></span>
            <span class="text-steel font-medium">55 Tipo A (28.4%)</span>
          </div>
        </div>
        <div class="w-full h-2 bg-mist rounded-sm overflow-hidden flex">
          <div class="h-full bg-signal-blue" style="width: 71.6%"></div>
          <div class="h-full bg-ash" style="width: 28.4%"></div>
        </div>
      </div>
    </div>
  </div>
</template>
