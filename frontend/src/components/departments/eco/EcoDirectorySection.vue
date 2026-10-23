<script setup lang="ts">
import { Building2 } from 'lucide-vue-next';
import type { EconomicasMesData } from '@/data/departmentMonthlyData';

defineProps<{
  currentMesData: EconomicasMesData;
}>();

const selectedMes = defineModel<string>('selectedMes', { required: true });

// Datos del historial del directorio
const historialDirectorio = [
  { mes: 'Ene', valor: 211, height: 70, y: 65 },
  { mes: 'Feb', valor: 143, height: 47, y: 88 },
  { mes: 'Mar', valor: 84, height: 28, y: 107 },
  { mes: 'Abr', valor: 50, height: 17, y: 118 },
  { mes: 'May', valor: 122, height: 40, y: 95 },
  { mes: 'Jun', valor: 143, height: 47, y: 88 },
  { mes: 'Jul', valor: 281, height: 93, y: 42 },
  { mes: 'Ago', valor: 44, height: 15, y: 120 },
];
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div class="flex items-start justify-between mb-1 pb-3 border-b border-mist">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="font-mono text-xs font-semibold text-white bg-dept-eco px-2 py-0.5 rounded-[3px]">
            ECO-DIR-01
          </span>
          <Building2 :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
          <h3 class="text-base font-semibold text-ink-black">
            Total Establecimientos Implantados Directorio de Tipologías de Precios
          </h3>
        </div>
        <p class="text-xs font-normal text-steel">
          Incorporación mensual de locales comerciales y tipologías al marco muestral
        </p>
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-dept-eco-light text-dept-eco border border-dept-eco-border rounded-[3px] shrink-0">
        {{ currentMesData.mesNombre }}: {{ currentMesData.directorio }} Locales
      </span>
    </div>

    <!-- Gráfico SVG de Barras Mensuales (Ene - Ago 2026) -->
    <div class="w-full my-2 min-w-0 overflow-hidden">
      <svg viewBox="0 0 540 160" class="w-full h-[140px] max-md:h-[120px] max-w-full">
        <line x1="30" y1="20" x2="520" y2="20" stroke="#f0f0f0" stroke-dasharray="3" />
        <line x1="30" y1="60" x2="520" y2="60" stroke="#f0f0f0" stroke-dasharray="3" />
        <line x1="30" y1="100" x2="520" y2="100" stroke="#f0f0f0" stroke-dasharray="3" />
        <line x1="30" y1="135" x2="520" y2="135" stroke="#d1d4d5" />

        <text x="5" y="24" font-size="9" font-weight="600" fill="#686c6d">300</text>
        <text x="5" y="64" font-size="9" font-weight="600" fill="#686c6d">200</text>
        <text x="5" y="104" font-size="9" font-weight="600" fill="#686c6d">100</text>
        <text x="15" y="139" font-size="9" font-weight="600" fill="#686c6d">0</text>

        <g
          v-for="(item, idx) in historialDirectorio"
          :key="item.mes"
          class="cursor-pointer"
          @click="selectedMes = item.mes"
        >
          <rect
            :x="50 + idx * 60"
            :y="item.y"
            width="30"
            :height="item.height"
            :fill="item.mes === selectedMes ? '#15803d' : '#2749ff'"
            rx="1.5"
          />
          <text
            :x="65 + idx * 60"
            :y="item.y - 7"
            font-size="10"
            font-weight="600"
            text-anchor="middle"
            :fill="item.mes === selectedMes ? '#15803d' : '#000000'"
          >
            {{ item.valor }}
          </text>
          <text
            :x="65 + idx * 60"
            y="150"
            font-size="10"
            :font-weight="item.mes === selectedMes ? '700' : '500'"
            text-anchor="middle"
            :fill="item.mes === selectedMes ? '#15803d' : '#686c6d'"
          >
            {{ item.mes }}
          </text>
        </g>
      </svg>
    </div>

    <div class="pt-3 border-t border-mist text-xs text-steel font-medium flex items-center justify-between">
      <span>Meta Mensual: 50 locales</span>
      <span class="font-semibold text-ink-black">Acumulado a {{ currentMesData.mesNombre }}: {{ currentMesData.acumulado_directorio.toLocaleString() }} establecimientos</span>
    </div>
  </div>
</template>
