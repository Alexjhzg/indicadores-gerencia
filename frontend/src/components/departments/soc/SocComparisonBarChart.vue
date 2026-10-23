<script setup lang="ts">
import { computed } from 'vue';
import { BarChart3 } from 'lucide-vue-next';
import type { SocialesMesData } from '@/data/departmentMonthlyData';

const props = defineProps<{
  currentSocData: SocialesMesData;
}>();

const scaleFactor = 4.8;
const baselineY = 150;

const ehmPlanifHeight = computed(() => Math.round(props.currentSocData.ehm_planif * scaleFactor));
const ehmPlanifY = computed(() => baselineY - ehmPlanifHeight.value);

const ehmEfecHeight = computed(() => Math.round(props.currentSocData.ehm_efec * scaleFactor));
const ehmEfecY = computed(() => baselineY - ehmEfecHeight.value);

const escaPlanifHeight = computed(() => Math.round(props.currentSocData.esca_planif * scaleFactor));
const escaPlanifY = computed(() => baselineY - escaPlanifHeight.value);

const escaEfecHeight = computed(() => Math.round(props.currentSocData.esca_efec * scaleFactor));
const escaEfecY = computed(() => baselineY - escaEfecHeight.value);
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <BarChart3 :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Cobertura Operativa de Muestra: EHM vs ESCA
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Comparación de sectores y controles de muestra programados vs ejecutados en {{ currentSocData.mesNombre }} 2026
      </p>
    </div>

    <div class="my-4">
      <svg viewBox="0 0 500 180" class="w-full h-[170px]">
        <!-- Cuadrícula -->
        <line x1="50" y1="20" x2="470" y2="20" stroke="#f0f0f0" stroke-dasharray="4" />
        <line x1="50" y1="65" x2="470" y2="65" stroke="#f0f0f0" stroke-dasharray="4" />
        <line x1="50" y1="110" x2="470" y2="110" stroke="#f0f0f0" stroke-dasharray="4" />
        <line x1="50" y1="150" x2="470" y2="150" stroke="#d1d4d5" />

        <text x="15" y="24" font-size="10" font-weight="600" fill="#424647">25</text>
        <text x="15" y="69" font-size="10" font-weight="600" fill="#424647">15</text>
        <text x="15" y="114" font-size="10" font-weight="600" fill="#424647">5</text>
        <text x="15" y="154" font-size="10" font-weight="600" fill="#424647">0</text>

        <!-- Grupo EHM -->
        <rect x="110" :y="ehmPlanifY" width="36" :height="ehmPlanifHeight" fill="#ededed" rx="2" />
        <text x="128" :y="ehmPlanifY - 8" font-size="11" font-weight="600" text-anchor="middle" fill="#424647">
          {{ currentSocData.ehm_planif }}
        </text>

        <rect x="152" :y="ehmEfecY" width="36" :height="ehmEfecHeight" fill="#2749ff" rx="2" />
        <text x="170" :y="ehmEfecY - 8" font-size="11" font-weight="600" text-anchor="middle" fill="#2749ff">
          {{ currentSocData.ehm_efec }}
        </text>

        <text x="150" y="168" font-size="11" font-weight="600" text-anchor="middle" fill="#000000">
          EHM ({{ currentSocData.ehm_pct }})
        </text>

        <!-- Grupo ESCA -->
        <rect x="300" :y="escaPlanifY" width="36" :height="escaPlanifHeight" fill="#ededed" rx="2" />
        <text x="318" :y="escaPlanifY - 8" font-size="11" font-weight="600" text-anchor="middle" fill="#424647">
          {{ currentSocData.esca_planif }}
        </text>

        <rect x="342" :y="escaEfecY" width="36" :height="escaEfecHeight" fill="#2749ff" rx="2" />
        <text x="360" :y="escaEfecY - 8" font-size="11" font-weight="600" text-anchor="middle" fill="#2749ff">
          {{ currentSocData.esca_efec }}
        </text>

        <text x="340" y="168" font-size="11" font-weight="600" text-anchor="middle" fill="#000000">
          ESCA ({{ currentSocData.esca_pct }})
        </text>
      </svg>
    </div>

    <div class="flex items-center justify-between pt-3 border-t border-mist text-xs">
      <div class="flex items-center gap-4">
        <div class="flex items-center gap-1.5">
          <span class="w-3 h-3 bg-mist rounded-sm"></span>
          <span class="text-steel font-medium">Planificados</span>
        </div>
        <div class="flex items-center gap-1.5">
          <span class="w-3 h-3 bg-signal-blue rounded-sm"></span>
          <span class="text-ink-black font-semibold">Levantados</span>
        </div>
      </div>
      <span class="text-steel font-medium">Cobertura Monagas {{ currentSocData.mesNombre }}</span>
    </div>
  </div>
</template>
