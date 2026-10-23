<script setup lang="ts">
import { ref } from 'vue';
import { Layers, GraduationCap, Building2 } from 'lucide-vue-next';
import {
  cuadroSEEM_Capacitacion,
  cuadroSEEM_Comites,
} from '@/data/cuadrosOficiales';

const selectedSeemCuadro = ref<'CAPACITACION' | 'COMITES'>('CAPACITACION');
</script>

<template>
  <div class="flex flex-col gap-4">
    <!-- Selector de Cuadros SEEM -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-mist pb-3">
      <div class="flex items-center gap-2">
        <Layers :size="16" :stroke-width="1.5" class="text-steel shrink-0" />
        <span class="text-xs font-semibold text-steel uppercase tracking-wider">Cuadros Estadísticos SEEM:</span>
      </div>
      <div class="flex items-center gap-1.5 overflow-x-auto pb-1">
        <button
          type="button"
          class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-[3px] text-xs font-semibold transition-colors cursor-pointer border-none shrink-0"
          :class="selectedSeemCuadro === 'CAPACITACION' ? 'bg-teal-700 text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedSeemCuadro = 'CAPACITACION'"
        >
          <GraduationCap :size="14" :stroke-width="1.5" />
          <span>Cuadro LA 8: Capacitación</span>
        </button>
        <button
          type="button"
          class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-[3px] text-xs font-semibold transition-colors cursor-pointer border-none shrink-0"
          :class="selectedSeemCuadro === 'COMITES' ? 'bg-teal-700 text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedSeemCuadro = 'COMITES'"
        >
          <Building2 :size="14" :stroke-width="1.5" />
          <span>Cuadro LA 9: Comités CCEE</span>
        </button>
      </div>
    </div>

    <!-- Cuadro LA 8: Capacitación -->
    <div v-if="selectedSeemCuadro === 'CAPACITACION'" class="flex flex-col gap-3">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 8. Planes de Formación y Talleres Ejecutados en el Estado Monagas · Agosto 2026
      </div>
      <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
                <th class="py-2.5 px-3">Plan / Taller de Formación</th>
                <th class="py-2.5 px-3 text-center">Tipo</th>
                <th class="py-2.5 px-3 text-right">Personal INE</th>
                <th class="py-2.5 px-3 text-right">Coord. Mun.</th>
                <th class="py-2.5 px-3 text-right">Coord. Nodo</th>
                <th class="py-2.5 px-3 text-right">Supervisores</th>
                <th class="py-2.5 px-3 text-right">Encuestadores</th>
                <th class="py-2.5 px-3 text-right">Total</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist font-medium">
              <tr
                v-for="(row, idx) in cuadroSEEM_Capacitacion"
                :key="idx"
                class="hover:bg-mist/30 transition-colors"
                :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.plan.includes('TOTAL') }"
              >
                <td class="py-2.5 px-3 font-semibold text-ink-black max-w-sm">{{ row.plan }}</td>
                <td class="py-2.5 px-3 text-center text-steel font-mono">{{ row.tipo }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.personal_ine }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.coord_municipal }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.coord_nodo }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.supervisor }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.encuestador }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-bold">{{ row.total }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Cuadro LA 9: Comités CCEE -->
    <div v-else-if="selectedSeemCuadro === 'COMITES'" class="flex flex-col gap-3">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 9. Sesiones del Comité de Coordinación Estadística (CCEE) · Estado Monagas
      </div>
      <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
                <th class="py-2.5 px-3">Actividad / Mesa Técnica</th>
                <th class="py-2.5 px-3">Ente Convocante / Aliados</th>
                <th class="py-2.5 px-3 text-center">Fecha</th>
                <th class="py-2.5 px-3 text-right">Delegados INE</th>
                <th class="py-2.5 px-3 text-right">Delegados Externos</th>
                <th class="py-2.5 px-3 text-right">Total Participantes</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist font-medium">
              <tr
                v-for="(row, idx) in cuadroSEEM_Comites"
                :key="idx"
                class="hover:bg-mist/30 transition-colors"
              >
                <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.actividad }}</td>
                <td class="py-2.5 px-3 text-steel">{{ row.ente_convocante }}</td>
                <td class="py-2.5 px-3 text-center font-mono text-[11px] text-steel">{{ row.fecha }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.participantes_ine }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.participantes_externos }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-bold">{{ row.total }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Detalle de Acuerdos -->
      <div
        v-for="(row, idx) in cuadroSEEM_Comites"
        :key="idx"
        class="bg-canvas border border-ash rounded-[3px] p-4 text-xs"
      >
        <span class="font-semibold text-ink-black block mb-1">Acuerdos suscritos en acta oficial ({{ row.fecha }}):</span>
        <p class="text-steel leading-relaxed">{{ row.acuerdos }}</p>
      </div>
    </div>
  </div>
</template>
