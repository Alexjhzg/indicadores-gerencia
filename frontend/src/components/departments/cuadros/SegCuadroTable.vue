<script setup lang="ts">
import { ref } from 'vue';
import { Layers } from 'lucide-vue-next';
import {
  cuadroSEG_Nodos,
  cuadroSEG_Encuestas,
  cuadroSEG_Equipos,
} from '@/data/cuadrosOficiales';

const selectedSegCuadro = ref<'NODOS' | 'ENCUESTAS' | 'EQUIPOS'>('NODOS');
</script>

<template>
  <div class="flex flex-col gap-4">
    <!-- Selector de Cuadros SEGEN -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-mist pb-3">
      <div class="flex items-center gap-2">
        <Layers :size="16" :stroke-width="1.5" class="text-steel shrink-0" />
        <span class="text-xs font-semibold text-steel uppercase tracking-wider">Cuadros Estadísticos SEGEN:</span>
      </div>
      <div class="flex items-center gap-1.5 overflow-x-auto pb-1">
        <button
          type="button"
          class="px-3 py-1.5 rounded-[3px] text-xs font-semibold transition-colors cursor-pointer border-none shrink-0"
          :class="selectedSegCuadro === 'NODOS' ? 'bg-dept-seg text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedSegCuadro = 'NODOS'"
        >
          Cuadro 1: Nodos Municipales
        </button>
        <button
          type="button"
          class="px-3 py-1.5 rounded-[3px] text-xs font-semibold transition-colors cursor-pointer border-none shrink-0"
          :class="selectedSegCuadro === 'ENCUESTAS' ? 'bg-dept-seg text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedSegCuadro = 'ENCUESTAS'"
        >
          Cuadro 2: Encuestas ODK 2026
        </button>
        <button
          type="button"
          class="px-3 py-1.5 rounded-[3px] text-xs font-semibold transition-colors cursor-pointer border-none shrink-0"
          :class="selectedSegCuadro === 'EQUIPOS' ? 'bg-dept-seg text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedSegCuadro = 'EQUIPOS'"
        >
          Cuadro 3: Equipos DMC
        </button>
      </div>
    </div>

    <!-- Cuadro 1: Nodos -->
    <div v-if="selectedSegCuadro === 'NODOS'" class="flex flex-col gap-3">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 4.1. Nodos del SEGEN en el Estado Monagas al mes de agosto 2026
      </div>
      <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
                <th class="py-2.5 px-3">Municipio</th>
                <th class="py-2.5 px-3 text-right">Planificados</th>
                <th class="py-2.5 px-3 text-right">Instalados</th>
                <th class="py-2.5 px-3 text-right">Activos</th>
                <th class="py-2.5 px-3 text-right">Inactivos</th>
                <th class="py-2.5 px-3 text-right">% Operatividad</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist font-medium">
              <tr
                v-for="row in cuadroSEG_Nodos"
                :key="row.municipio"
                class="hover:bg-mist/30 transition-colors"
                :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.municipio === 'TOTAL' }"
              >
                <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.municipio }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.planificados }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.instalados }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-semibold">{{ row.activos }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-steel">{{ row.inactivos }}</td>
                <td class="py-2.5 px-3 text-right font-mono font-semibold">
                  {{ ((row.activos / row.instalados) * 100).toFixed(1) }}%
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Cuadro 2: Encuestas ODK -->
    <div v-else-if="selectedSegCuadro === 'ENCUESTAS'" class="flex flex-col gap-3">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 5. Levantamiento del sistema de encuestas en el SEGEN. Año 2026
      </div>
      <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
                <th class="py-2.5 px-3">Mes</th>
                <th class="py-2.5 px-3 text-right">Conteo Rápido v2</th>
                <th class="py-2.5 px-3 text-right">Coyuntura v2</th>
                <th class="py-2.5 px-3 text-right">Transformación</th>
                <th class="py-2.5 px-3 text-right">Laboral</th>
                <th class="py-2.5 px-3 text-right">Trámites</th>
                <th class="py-2.5 px-3 text-right">Económica ODK</th>
                <th class="py-2.5 px-3 text-right">Educación/Medios</th>
                <th class="py-2.5 px-3 text-right">Servicios ODK</th>
                <th class="py-2.5 px-3 text-right font-bold">Total</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist font-medium">
              <tr
                v-for="row in cuadroSEG_Encuestas"
                :key="row.mes"
                class="hover:bg-mist/30 transition-colors"
                :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.mes === 'TOTAL' }"
              >
                <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.mes }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.conteo_rapido.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.coyuntura_v2.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.transformacion.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.laboral.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.tramites.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.economica_odk.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.educacion_medios.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.servicios_odk.toLocaleString() }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-bold">{{ row.total.toLocaleString() }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Cuadro 3: Equipos DMC -->
    <div v-else class="flex flex-col gap-3">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 4.2. Equipos Tecnológicos en los Nodos del SEGEN al mes de agosto 2026
      </div>
      <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
                <th class="py-2.5 px-3">Ubicación / Condición</th>
                <th class="py-2.5 px-3 text-right">Laptops y MiniPC</th>
                <th class="py-2.5 px-3 text-right">Dispositivos DMC</th>
                <th class="py-2.5 px-3 text-right">Módems Multibam</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist font-medium">
              <tr
                v-for="row in cuadroSEG_Equipos"
                :key="row.condicion"
                class="hover:bg-mist/30 transition-colors"
              >
                <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.condicion }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.laptops }}</td>
                <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-semibold">{{ row.dmc }}</td>
                <td class="py-2.5 px-3 text-right font-mono">{{ row.multibam }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
