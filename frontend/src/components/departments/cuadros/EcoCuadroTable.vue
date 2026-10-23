<script setup lang="ts">
import { cuadroECO } from '@/data/cuadrosOficiales';
</script>

<template>
  <div class="flex flex-col gap-4">
    <div class="flex items-center justify-between">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 3. Levantamiento de Proyectos CAN, Complementaria y Directorio de Establecimientos (2026)
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-dept-eco-light text-dept-eco border border-dept-eco-border rounded-[3px]">
        Gerencia de Precios
      </span>
    </div>

    <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
              <th class="py-2.5 px-3">Mes</th>
              <th class="py-2.5 px-3 text-right">Personal Planif.</th>
              <th class="py-2.5 px-3 text-right">Personal Efec.</th>
              <th class="py-2.5 px-3 text-right">% Efect. Pers.</th>
              <th class="py-2.5 px-3 text-right">Estab. Implantados</th>
              <th class="py-2.5 px-3 text-right">Comunas CAN</th>
              <th class="py-2.5 px-3 text-right">Nodos CAN</th>
              <th class="py-2.5 px-3 text-right">Estab. Planif.</th>
              <th class="py-2.5 px-3 text-right">Estab. Efec.</th>
              <th class="py-2.5 px-3 text-right">% Efect. CAN</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-mist font-medium">
            <tr
              v-for="row in cuadroECO"
              :key="row.mes"
              class="hover:bg-mist/30 transition-colors"
              :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.mes === 'TOTAL' }"
            >
              <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.mes }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.personal_planificado }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.personal_levantamiento }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.pct_efectividad_personal }}%</td>
              <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-semibold">{{ row.establecimientos_implantados }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.comunas_can }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.nodos_can }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.establecimientos_planificados }}</td>
              <td class="py-2.5 px-3 text-right font-mono text-ink-black font-semibold">{{ row.establecimientos_efectivos }}</td>
              <td class="py-2.5 px-3 text-right font-mono">
                <span
                  class="px-1.5 py-0.5 rounded-xs"
                  :class="row.pct_efectividad_can === 100.0 ? 'bg-signal-blue/10 text-signal-blue' : 'bg-mist text-ink-black'"
                >
                  {{ row.pct_efectividad_can }}%
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
