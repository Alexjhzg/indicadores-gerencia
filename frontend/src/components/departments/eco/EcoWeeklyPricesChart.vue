<script setup lang="ts">
import { computed } from 'vue';
import { TrendingUp } from 'lucide-vue-next';
import type { EconomicasMesData } from '@/data/departmentMonthlyData';

const props = defineProps<{
  currentMesData: EconomicasMesData;
  displayPreciosEfec: number;
  displayMetaPrecios: number;
  displayCumplimientoPrecios: string;
}>();

const selectedSemana = defineModel<string>('selectedSemana', { required: true });

// Coordenadas reactivas para el gráfico SVG de semanas
const semanaPoints = computed(() => {
  const sList = props.currentMesData.semanas;
  return sList.map((s, idx) => {
    const x = 100 + idx * 130;
    // Escala vertical: min 450 -> y=145, max -> y=40
    const minP = 450;
    const maxP = Math.max(...sList.map(item => item.precios), s.meta) + 40;
    const norm = (s.precios - minP) / (maxP - minP);
    const y = Math.round(145 - norm * 95);
    return {
      id: s.id,
      nombre: s.nombre,
      precios: s.precios,
      meta: s.meta,
      x,
      y,
      isSelected: selectedSemana.value === s.id,
    };
  });
});

const polylinePoints = computed(() => {
  return semanaPoints.value.map(p => `${p.x},${p.y}`).join(' ');
});

const polygonPoints = computed(() => {
  const pts = semanaPoints.value;
  if (!pts.length) return '';
  return `${pts[0].x},165 ${polylinePoints.value} ${pts[pts.length - 1].x},165`;
});
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div class="flex items-start justify-between mb-4 pb-3 border-b border-mist">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="font-mono text-xs font-semibold text-white bg-dept-eco px-2 py-0.5 rounded-[3px]">
            ECO-CAN-02
          </span>
          <TrendingUp :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
          <h3 class="text-base font-semibold text-ink-black">
            Total Precios Levantados Reales Efectivos
          </h3>
        </div>
        <p class="text-xs font-normal text-steel">
          Captura semanal de cotizaciones CAN en {{ currentMesData.mesNombre }} 2026 (Haz clic en un punto para filtrar por semana)
        </p>
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px] shrink-0">
        Meta Mes: {{ currentMesData.meta_precios_mes.toLocaleString() }}
      </span>
    </div>

    <div class="w-full min-w-0 overflow-hidden">
      <svg viewBox="0 0 600 200" class="w-full h-[180px] max-md:h-[150px] max-w-full">
        <line x1="40" y1="30" x2="570" y2="30" stroke="#f0f0f0" stroke-dasharray="4" />
        <line x1="40" y1="75" x2="570" y2="75" stroke="#f0f0f0" stroke-dasharray="4" />
        <line x1="40" y1="120" x2="570" y2="120" stroke="#f0f0f0" stroke-dasharray="4" />
        <line x1="40" y1="165" x2="570" y2="165" stroke="#d1d4d5" />

        <text x="10" y="34" font-size="10" font-weight="600" fill="#424647">700</text>
        <text x="10" y="79" font-size="10" font-weight="600" fill="#424647">550</text>
        <text x="10" y="124" font-size="10" font-weight="600" fill="#424647">450</text>
        <text x="10" y="169" font-size="10" font-weight="600" fill="#424647">0</text>

        <line x1="40" y1="75" x2="570" y2="75" stroke="#2749ff" stroke-dasharray="6" stroke-width="1.2" opacity="0.6" />
        <text x="500" y="70" font-size="10" font-weight="600" fill="#2749ff">Meta Técnica</text>

        <polygon
          :points="polygonPoints"
          fill="rgba(39, 73, 255, 0.08)"
        />

        <polyline
          :points="polylinePoints"
          fill="none"
          stroke="#2749ff"
          stroke-width="2.5"
        />

        <g
          v-for="p in semanaPoints"
          :key="p.id"
          class="cursor-pointer"
          @click="selectedSemana = (selectedSemana === p.id ? 'TODAS' : p.id)"
        >
          <!-- Anillo resaltador si la semana está seleccionada -->
          <circle
            v-if="p.isSelected"
            :cx="p.x"
            :cy="p.y"
            r="8.5"
            fill="none"
            stroke="#2749ff"
            stroke-width="2"
            opacity="0.4"
          />
          <circle
            :cx="p.x"
            :cy="p.y"
            :r="p.isSelected ? 5.5 : 4.5"
            :fill="p.isSelected ? '#15803d' : '#2749ff'"
            stroke="#ffffff"
            stroke-width="2"
          />
          <text
            :x="p.x"
            :y="p.y - 12"
            font-size="11"
            :font-weight="p.isSelected ? '700' : '600'"
            text-anchor="middle"
            :fill="p.isSelected ? '#15803d' : '#000000'"
          >
            {{ p.precios }}
          </text>
          <text
            :x="p.x"
            y="182"
            font-size="10"
            :font-weight="p.isSelected ? '700' : '600'"
            text-anchor="middle"
            :fill="p.isSelected ? '#15803d' : '#424647'"
          >
            {{ p.nombre }}
          </text>
        </g>
      </svg>
    </div>

    <div class="flex items-center justify-between pt-3 border-t border-mist text-xs text-steel font-medium">
      <span>
        {{ selectedSemana === 'TODAS' ? `Total ${currentMesData.mesNombre}:` : `Semana ${selectedSemana} (${currentMesData.mesNombre}):` }}
        <strong class="text-ink-black">{{ displayPreciosEfec.toLocaleString() }} precios</strong>
        (Meta: {{ displayMetaPrecios.toLocaleString() }})
      </span>
      <span class="text-signal-blue font-semibold">Cumplimiento: {{ displayCumplimientoPrecios }}</span>
    </div>
  </div>
</template>
