<script setup lang="ts">
import { Radio } from 'lucide-vue-next';

const nodosMunicipales = [
  { nombre: 'Maturín', activos: 23, instalados: 49, tasa: '46.9%' },
  { nombre: 'Piar', activos: 5, instalados: 9, tasa: '55.6%' },
  { nombre: 'Cedeño', activos: 3, instalados: 8, tasa: '37.5%' },
  { nombre: 'Libertador', activos: 2, instalados: 7, tasa: '28.6%' },
  { nombre: 'Caripe', activos: 2, instalados: 6, tasa: '33.3%' },
  { nombre: 'Bolívar', activos: 2, instalados: 5, tasa: '40.0%' },
  { nombre: 'Acosta', activos: 2, instalados: 9, tasa: '22.2%' },
  { nombre: 'Ezequiel Zamora', activos: 2, instalados: 3, tasa: '66.7%' },
  { nombre: 'Punceres', activos: 3, instalados: 3, tasa: '100.0%' },
  { nombre: 'Santa Bárbara', activos: 2, instalados: 2, tasa: '100.0%' },
  { nombre: 'Sotillo', activos: 2, instalados: 2, tasa: '100.0%' },
  { nombre: 'Aguasay', activos: 1, instalados: 2, tasa: '50.0%' },
  { nombre: 'Uracoa', activos: 1, instalados: 1, tasa: '100.0%' },
];
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <Radio :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Red Territorial de Nodos SEGEN (106 Nodos Instalados)
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Monitoreo de transmisión activa vs nodos en incidencia técnica
      </p>
    </div>

    <div class="flex flex-col gap-3 my-4">
      <div class="flex items-center justify-between text-xs font-semibold">
        <span class="text-ink-black">Tasa de Conectividad Estadal</span>
        <span class="text-signal-blue font-mono">50 Activos (47.17%)</span>
      </div>
      <div class="w-full h-3 bg-mist rounded-sm overflow-hidden flex">
        <div class="h-full bg-signal-blue" style="width: 47.17%"></div>
        <div class="h-full bg-ash" style="width: 52.83%"></div>
      </div>
      <div class="flex justify-between text-[11px] text-steel">
        <div class="flex items-center gap-1.5">
          <span class="w-2.5 h-2.5 bg-signal-blue rounded-xs"></span>
          <span>50 Activos en línea</span>
        </div>
        <div class="flex items-center gap-1.5">
          <span class="w-2.5 h-2.5 bg-ash rounded-xs"></span>
          <span>56 Con soporte técnico</span>
        </div>
      </div>
    </div>

    <!-- Scroll municipal de nodos -->
    <div class="flex flex-col gap-1.5 max-h-[160px] overflow-y-auto pr-1 border-t border-mist pt-2 text-xs">
      <div
        v-for="mun in nodosMunicipales"
        :key="mun.nombre"
        class="flex items-center justify-between py-1 px-1.5 hover:bg-mist/40 rounded-xs"
      >
        <span class="text-ink-black font-medium">{{ mun.nombre }}</span>
        <div class="flex items-center gap-2">
          <span class="text-steel font-mono">{{ mun.activos }} / {{ mun.instalados }}</span>
          <span class="font-semibold text-signal-blue font-mono">{{ mun.tasa }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
