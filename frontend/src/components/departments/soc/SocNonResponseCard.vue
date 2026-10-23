<script setup lang="ts">
import { computed } from 'vue';
import { AlertTriangle } from 'lucide-vue-next';
import type { SocialesMesData } from '@/data/departmentMonthlyData';

const props = defineProps<{
  currentSocData: SocialesMesData;
}>();

const ehmNoRespNum = computed(() => parseFloat(props.currentSocData.no_resp) || 20.49);
const ehmDiff = computed(() => (ehmNoRespNum.value - 15.0).toFixed(2));
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <AlertTriangle :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Tasa de No Respuesta por Rechazo o Ausencia (Tipo A)
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Control de calidad de la muestra frente a los umbrales máximos tolerados por el INE ({{ currentSocData.mesNombre }})
      </p>
    </div>

    <div class="flex flex-col gap-5 my-4">
      <!-- Barra EHM -->
      <div class="flex flex-col gap-1.5">
        <div class="flex items-center justify-between text-xs font-semibold">
          <span class="text-ink-black">EHM: Tasa de No Respuesta</span>
          <span class="text-signal-blue font-mono">{{ currentSocData.no_resp }} ({{ Math.round((currentSocData.ehm_viv_efec * ehmNoRespNum) / 80) }} viviendas aprox.)</span>
        </div>
        <div class="relative w-full h-3 bg-mist rounded-sm overflow-hidden">
          <div class="h-full bg-signal-blue" :style="{ width: `${Math.min(ehmNoRespNum, 100)}%` }"></div>
          <!-- Línea meta 15% -->
          <div
            class="absolute top-0 bottom-0 w-[2px] bg-ink-black"
            style="left: 15%"
            title="Umbral Máximo INE: 15.0%"
          ></div>
        </div>
        <div class="flex justify-between text-[11px] text-steel">
          <span>Umbral tolerado: ≤ 15.0%</span>
          <span class="font-semibold text-ink-black">
            {{ parseFloat(ehmDiff) > 0 ? `+${ehmDiff}% sobre el límite` : 'Dentro del umbral' }}
          </span>
        </div>
      </div>

      <!-- Barra ESCA -->
      <div class="flex flex-col gap-1.5">
        <div class="flex items-center justify-between text-xs font-semibold">
          <span class="text-ink-black">ESCA: Tasa de No Respuesta</span>
          <span class="text-signal-blue font-mono">28.35% (55 viviendas)</span>
        </div>
        <div class="relative w-full h-3 bg-mist rounded-sm overflow-hidden">
          <div class="h-full bg-signal-blue" style="width: 28.35%"></div>
          <!-- Línea meta 20% -->
          <div
            class="absolute top-0 bottom-0 w-[2px] bg-ink-black"
            style="left: 20%"
            title="Umbral Máximo INE: 20.0%"
          ></div>
        </div>
        <div class="flex justify-between text-[11px] text-steel">
          <span>Umbral tolerado: ≤ 20.0%</span>
          <span class="font-semibold text-ink-black">+8.35% sobre el límite</span>
        </div>
      </div>
    </div>

    <div class="p-3 bg-mist/60 border border-mist rounded-[3px] text-xs text-steel leading-relaxed">
      <strong class="text-ink-black font-semibold">Causas Principales:</strong> Ausencia prolongada de jefes de hogar en jornada laboral y rechazos en urbanizaciones privadas. Requiere refuerzo de re-visitas en fines de semana.
    </div>
  </div>
</template>
