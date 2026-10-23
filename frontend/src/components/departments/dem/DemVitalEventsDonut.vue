<script setup lang="ts">
import { PieChart } from 'lucide-vue-next';

export interface HechoVitalItem {
  tipo: string;
  cantidad: number;
  porcentaje: string;
  color: string;
}

const hechosVitales: HechoVitalItem[] = [
  { tipo: 'Nacimientos Registrados', cantidad: 6972, porcentaje: '67.7%', color: '#2749ff' },
  { tipo: 'Defunciones Registradas', cantidad: 1987, porcentaje: '19.3%', color: '#424647' },
  { tipo: 'Nupcialidad y Uniones Estables', cantidad: 1339, porcentaje: '13.0%', color: '#9da3a5' },
];
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <PieChart :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Estructura de Hechos Vitales Registrados (Monagas 2026)
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Proporción de boletas procesadas por naturaleza del hecho demográfico
      </p>
    </div>

    <div class="flex flex-col sm:flex-row items-center justify-center gap-6 my-4">
      <!-- Donut SVG -->
      <div class="relative w-36 h-36 shrink-0 flex items-center justify-center">
        <svg viewBox="0 0 100 100" class="w-full h-full -rotate-90">
          <!-- Fondo gris total -->
          <circle cx="50" cy="50" r="38" fill="none" stroke="#ededed" stroke-width="12" />
          <!-- Nacimientos: 67.7% de 238.76 = 161.64 -->
          <circle
            cx="50"
            cy="50"
            r="38"
            fill="none"
            stroke="#2749ff"
            stroke-width="12"
            stroke-dasharray="238.76"
            stroke-dashoffset="77.12"
          />
          <!-- Defunciones: 19.3% de 238.76 = 46.08, desplazado 161.64 -->
          <circle
            cx="50"
            cy="50"
            r="38"
            fill="none"
            stroke="#424647"
            stroke-width="12"
            stroke-dasharray="46.08 192.68"
            stroke-dashoffset="-161.64"
          />
          <!-- Nupcialidad: 13.0% de 238.76 = 31.04, desplazado 207.72 -->
          <circle
            cx="50"
            cy="50"
            r="38"
            fill="none"
            stroke="#9da3a5"
            stroke-width="12"
            stroke-dasharray="31.04 207.72"
            stroke-dashoffset="-207.72"
          />
        </svg>
        <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
          <span class="text-xl font-semibold text-ink-black tracking-tight leading-none">
            10,298
          </span>
          <span class="text-[9px] font-semibold text-steel uppercase tracking-wider mt-0.5">
            Actas Principales
          </span>
        </div>
      </div>

      <!-- Leyenda con Datos de Alto Contraste -->
      <div class="flex flex-col gap-2.5 w-full sm:w-auto">
        <div
          v-for="h in hechosVitales"
          :key="h.tipo"
          class="flex items-center justify-between sm:justify-start gap-4 text-xs"
        >
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-xs shrink-0" :style="{ backgroundColor: h.color }"></span>
            <span class="text-steel font-medium">{{ h.tipo }}</span>
          </div>
          <div class="flex items-center gap-1.5 font-semibold text-ink-black">
            <span>{{ h.cantidad.toLocaleString() }}</span>
            <span class="text-steel font-normal">({{ h.porcentaje }})</span>
          </div>
        </div>
      </div>
    </div>

    <div class="flex items-center justify-between pt-3 border-t border-mist text-xs text-steel font-medium">
      <span>Fuente: Registros Civiles y Red Hospitalaria de Monagas</span>
      <span class="text-signal-blue font-semibold">100% Verificado</span>
    </div>
  </div>
</template>
