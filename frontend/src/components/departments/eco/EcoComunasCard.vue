<script setup lang="ts">
import { MapPin } from 'lucide-vue-next';
import type { EconomicasMesData } from '@/data/departmentMonthlyData';

defineProps<{
  currentMesData: EconomicasMesData;
}>();
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div class="pb-3 border-b border-mist">
      <div class="flex items-center gap-2 mb-1">
        <span class="font-mono text-xs font-semibold text-white bg-dept-eco px-2 py-0.5 rounded-[3px]">
          ECO-CAN-04
        </span>
        <MapPin :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Total Comunas con Levantamiento CAN
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Cobertura territorial en circuitos comunales y articulación con la red de nodos SEGEN en {{ currentMesData.mesNombre }}
      </p>
    </div>

    <div class="flex flex-col gap-3 my-4">
      <div class="bg-mist p-3 rounded-[3px] flex items-center justify-between">
        <div class="flex flex-col">
          <span class="text-xs font-medium text-steel">Comunas con Monitoreo CAN:</span>
          <span class="text-xl font-semibold text-ink-black">{{ currentMesData.comunas }} Comunas</span>
        </div>
        <span class="text-xs font-semibold px-2 py-0.5 bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px]">
          100% Meta
        </span>
      </div>

      <div class="bg-mist p-3 rounded-[3px] flex items-center justify-between">
        <div class="flex flex-col">
          <span class="text-xs font-medium text-steel">Nodos SEGEN Vinculados:</span>
          <span class="text-xl font-semibold text-ink-black">{{ currentMesData.nodos }} Nodos Activos</span>
        </div>
        <span class="text-xs font-semibold px-2 py-0.5 bg-mist text-ink-black rounded-[3px]">
          Despliegue Territorial
        </span>
      </div>
    </div>

    <div class="pt-3 border-t border-mist text-xs text-steel font-medium flex items-center justify-between">
      <span>Cobertura de Monitoreo de Precios</span>
      <span class="font-semibold text-ink-black">Monagas Entidad 16 ({{ currentMesData.mesNombre }})</span>
    </div>
  </div>
</template>
