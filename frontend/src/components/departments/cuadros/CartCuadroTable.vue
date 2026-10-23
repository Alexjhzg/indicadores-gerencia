<script setup lang="ts">
import { Info } from 'lucide-vue-next';
import { cuadroCART, notaMetodologicaCart } from '@/data/cuadrosOficiales';
</script>

<template>
  <div class="flex flex-col gap-4">
    <div class="flex items-center justify-between">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 6. Proyecto Circuitos Comunales — Entidad Monagas, Año 2026
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-dept-cart-light text-dept-cart border border-dept-cart-border rounded-[3px]">
        13 Municipios
      </span>
    </div>

    <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
              <th class="py-2.5 px-3 w-12 text-center">Nº</th>
              <th class="py-2.5 px-3">Municipio</th>
              <th class="py-2.5 px-3 text-right">Total Circuitos Comunales</th>
              <th class="py-2.5 px-3 text-right">Consejos Comunales Conformados</th>
              <th class="py-2.5 px-3 text-right">Comunas Vectorizadas</th>
              <th class="py-2.5 px-3 text-right">% de Vectorización</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-mist font-medium">
            <tr
              v-for="row in cuadroCART"
              :key="row.municipio"
              class="hover:bg-mist/30 transition-colors"
              :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.municipio === 'TOTAL' }"
            >
              <td class="py-2.5 px-3 text-center text-steel font-mono">{{ row.numero }}</td>
              <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.municipio }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.circuitos_total }}</td>
              <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-semibold">{{ row.consejos_comunales.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono text-ink-black font-semibold">{{ row.comunas_vectorizadas }}</td>
              <td class="py-2.5 px-3 text-right font-mono">
                <span
                  class="px-1.5 py-0.5 rounded-xs"
                  :class="row.pct_vectorizacion === 100.0 ? 'bg-signal-blue/10 text-signal-blue' : 'bg-mist text-ink-black'"
                >
                  {{ row.pct_vectorizacion }}%
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Nota Metodológica Oficial de Cartografía e IGVSB -->
    <div class="p-3.5 bg-white border border-ash rounded-[3px] flex items-start gap-2.5 text-xs text-steel leading-relaxed">
      <Info :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0 mt-0.5" />
      <p>
        <strong class="text-ink-black font-semibold">Nota Metodológica Institucional:</strong> {{ notaMetodologicaCart }}
      </p>
    </div>
  </div>
</template>
