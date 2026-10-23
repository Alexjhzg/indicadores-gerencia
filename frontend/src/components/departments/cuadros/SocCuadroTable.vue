<script setup lang="ts">
import { ref } from 'vue';
import { Layers } from 'lucide-vue-next';
import { cuadroSOC_EHM, cuadroSOC_ESCA } from '@/data/cuadrosOficiales';

const selectedSocCuadro = ref<'EHM' | 'ESCA'>('EHM');
</script>

<template>
  <div class="flex flex-col gap-4">
    <!-- Selector de Cuadros EHM vs ESCA -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-mist pb-3">
      <div class="flex items-center gap-2">
        <Layers :size="16" :stroke-width="1.5" class="text-steel shrink-0" />
        <span class="text-xs font-semibold text-steel uppercase tracking-wider">Seleccionar Cuadro Oficial:</span>
      </div>
      <div class="flex items-center gap-1.5">
        <button
          type="button"
          class="px-3.5 py-1.5 rounded-[3px] text-xs font-semibold transition-colors cursor-pointer border-none"
          :class="selectedSocCuadro === 'EHM' ? 'bg-dept-soc text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedSocCuadro = 'EHM'"
        >
          Cuadro 1: Encuesta de Hogares (EHM)
        </button>
        <button
          type="button"
          class="px-3.5 py-1.5 rounded-[3px] text-xs font-semibold transition-colors cursor-pointer border-none"
          :class="selectedSocCuadro === 'ESCA' ? 'bg-dept-soc text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedSocCuadro = 'ESCA'"
        >
          Cuadro 2: Consumo de Alimentos (ESCA)
        </button>
      </div>
    </div>

    <!-- Cuadro EHM -->
    <div v-if="selectedSocCuadro === 'EHM'" class="flex flex-col gap-3">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 1.1. Estado MONAGAS — Levantamiento de la Encuesta de Hogares por Muestreo (EHM), Año 2026
      </div>
      <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
                <th class="py-2.5 px-3">Periodo</th>
                <th class="py-2.5 px-3 text-right">Controles Planif.</th>
                <th class="py-2.5 px-3 text-right">Controles Lev.</th>
                <th class="py-2.5 px-3 text-right">% Levantamiento</th>
                <th class="py-2.5 px-3 text-right">Viv. Planif.</th>
                <th class="py-2.5 px-3 text-right">Viv. Efectivas</th>
                <th class="py-2.5 px-3 text-right">Tipo A (Rechazo)</th>
                <th class="py-2.5 px-3 text-right">Tipo B (Desoc.)</th>
                <th class="py-2.5 px-3 text-right">Tipo C (Destr.)</th>
                <th class="py-2.5 px-3 text-right">% No Respuesta</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist font-medium">
              <tr
                v-for="row in cuadroSOC_EHM"
                :key="row.periodo"
                class="hover:bg-mist/30 transition-colors"
                :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.periodo === 'TOTAL' }"
              >
                <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.periodo }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.controles_planificados }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-semibold">{{ row.controles_levantados }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.pct_levantamiento }}%</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.viviendas_planificadas }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-ink-black font-semibold">{{ row.viviendas_efectivas }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.tipo_a }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.tipo_b }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.tipo_c }}</td>
                <td class="py-2.5 px-3 text-right font-mono">
                  <span
                    class="px-1.5 py-0.5 rounded-xs"
                    :class="row.pct_no_respuesta <= 15.0 ? 'bg-signal-blue/10 text-signal-blue' : 'bg-mist text-ink-black font-semibold'"
                  >
                    {{ row.pct_no_respuesta }}%
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Cuadro ESCA -->
    <div v-else class="flex flex-col gap-3">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 1.2. Estado MONAGAS — Levantamiento de la Encuesta de Seguimiento al Consumo de Alimentos (ESCA), Año 2026
      </div>
      <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
                <th class="py-2.5 px-3">Periodo</th>
                <th class="py-2.5 px-3 text-right">Controles Planif.</th>
                <th class="py-2.5 px-3 text-right">Controles Lev.</th>
                <th class="py-2.5 px-3 text-right">% Levantamiento</th>
                <th class="py-2.5 px-3 text-right">Viv. Planif.</th>
                <th class="py-2.5 px-3 text-right">Viv. Efectivas</th>
                <th class="py-2.5 px-3 text-right">Tipo A (Rechazo)</th>
                <th class="py-2.5 px-3 text-right">Tipo B (Desoc.)</th>
                <th class="py-2.5 px-3 text-right">Tipo C (Destr.)</th>
                <th class="py-2.5 px-3 text-right">% No Respuesta</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist font-medium">
              <tr
                v-for="row in cuadroSOC_ESCA"
                :key="row.periodo"
                class="hover:bg-mist/30 transition-colors"
                :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.periodo === 'TOTAL' }"
              >
                <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.periodo }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.controles_planificados }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-semibold">{{ row.controles_levantados }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.pct_levantamiento }}%</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.viviendas_planificadas }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-ink-black font-semibold">{{ row.viviendas_efectivas }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.tipo_a }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.tipo_b }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.tipo_c }}</td>
                <td class="py-2.5 px-3 text-right font-mono">
                  <span
                    class="px-1.5 py-0.5 rounded-xs"
                    :class="row.pct_no_respuesta <= 20.0 ? 'bg-signal-blue/10 text-signal-blue' : 'bg-mist text-ink-black font-semibold'"
                  >
                    {{ row.pct_no_respuesta }}%
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
