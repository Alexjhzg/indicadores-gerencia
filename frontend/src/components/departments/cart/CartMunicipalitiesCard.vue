<script setup lang="ts">
import { ref } from 'vue';
import { BarChart2 } from 'lucide-vue-next';

export interface MunicipioCartografiaItem {
  nombre: string;
  vectorizados: number;
  total: number;
  pct: string;
}

const municipiosCartografia: MunicipioCartografiaItem[] = [
  { nombre: 'Maturín', vectorizados: 90, total: 90, pct: '100.0%' },
  { nombre: 'Caripe', vectorizados: 14, total: 15, pct: '93.3%' },
  { nombre: 'Piar', vectorizados: 12, total: 12, pct: '100.0%' },
  { nombre: 'Libertador', vectorizados: 12, total: 12, pct: '100.0%' },
  { nombre: 'Bolívar', vectorizados: 8, total: 10, pct: '80.0%' },
  { nombre: 'Sotillo', vectorizados: 10, total: 10, pct: '100.0%' },
  { nombre: 'Acosta', vectorizados: 9, total: 9, pct: '100.0%' },
  { nombre: 'Ezequiel Zamora', vectorizados: 9, total: 9, pct: '100.0%' },
  { nombre: 'Aguasay', vectorizados: 8, total: 8, pct: '100.0%' },
  { nombre: 'Cedeño', vectorizados: 7, total: 7, pct: '100.0%' },
  { nombre: 'Uracoa', vectorizados: 7, total: 7, pct: '100.0%' },
  { nombre: 'Púnceres', vectorizados: 6, total: 6, pct: '100.0%' },
  { nombre: 'Santa Bárbara', vectorizados: 3, total: 4, pct: '75.0%' },
];

const selectedMun = ref<string | null>(null);
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div class="flex items-start justify-between mb-3">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <BarChart2 :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
          <h3 class="text-base font-semibold text-ink-black">
            Circuitos Vectorizados por Municipio (13 Municipios)
          </h3>
        </div>
        <p class="text-xs font-normal text-steel">
          Distribución territorial oficial y tasa de completitud comunal
        </p>
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px]">
        195 de 199 Listos
      </span>
    </div>

    <!-- Lista de barras municipales con scroll vertical ordenado -->
    <div class="flex flex-col gap-2 max-h-[250px] overflow-y-auto pr-2">
      <div
        v-for="mun in municipiosCartografia"
        :key="mun.nombre"
        class="p-2 rounded-[3px] transition-colors border border-transparent hover:border-mist cursor-pointer"
        :class="{ 'bg-signal-blue/5 border-signal-blue/20': selectedMun === mun.nombre }"
        @click="selectedMun = selectedMun === mun.nombre ? null : mun.nombre"
      >
        <div class="flex items-center justify-between text-xs font-semibold mb-1">
          <span class="text-ink-black">{{ mun.nombre }}</span>
          <div class="flex items-center gap-2">
            <span class="text-steel">{{ mun.vectorizados }} / {{ mun.total }}</span>
            <span
              class="font-mono text-[11px] px-1.5 py-0.2 rounded-xs"
              :class="mun.pct === '100.0%' ? 'text-signal-blue bg-signal-blue/10' : 'text-ink-black bg-mist'"
            >
              {{ mun.pct }}
            </span>
          </div>
        </div>
        <div class="w-full h-1.5 bg-mist rounded-xs overflow-hidden">
          <div
            class="h-full bg-signal-blue"
            :style="{ width: `${(mun.vectorizados / mun.total) * 100}%` }"
          ></div>
        </div>
      </div>
    </div>

    <div class="flex items-center justify-between pt-3 border-t border-mist text-xs text-steel font-medium">
      <span>Haga clic en un municipio para resaltarlo</span>
      <span class="text-ink-black font-semibold">1,361 Consejos Vinculados</span>
    </div>
  </div>
</template>
