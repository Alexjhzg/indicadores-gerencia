<script setup lang="ts">
import { cuadroDEM } from '@/data/cuadrosOficiales';
</script>

<template>
  <div class="flex flex-col gap-4">
    <div class="flex items-center justify-between">
      <div class="text-xs font-semibold text-steel uppercase tracking-wider">
        Cuadro LA 2. Estadísticas Vitales según el total de boletas recibidas, codificadas y transcritas por año (2018 - 2026)
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-dept-dem-light text-dept-dem border border-dept-dem-border rounded-[3px]">
        Al 31/08/2026 · 0 Rezago
      </span>
    </div>

    <div class="bg-white border border-ash rounded-[3px] overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
              <th class="py-2.5 px-3">Año</th>
              <th class="py-2.5 px-3 text-right">Nacimientos</th>
              <th class="py-2.5 px-3 text-right">Defunciones</th>
              <th class="py-2.5 px-3 text-right">Matrimonios</th>
              <th class="py-2.5 px-3 text-right">Unión Estable</th>
              <th class="py-2.5 px-3 text-right">Divorcios</th>
              <th class="py-2.5 px-3 text-right">Suicidios</th>
              <th class="py-2.5 px-3 text-right">Total Recolectado</th>
              <th class="py-2.5 px-3 text-right">Transcrito</th>
              <th class="py-2.5 px-3 text-right">Por Transcribir (Rezago)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-mist font-medium">
            <tr
              v-for="row in cuadroDEM"
              :key="row.anio"
              class="hover:bg-mist/30 transition-colors"
              :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.anio === 'TOTALES' }"
            >
              <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.anio }}</td>
              <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-semibold">{{ row.nacimientos.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.defunciones.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.matrimonios.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.uniones.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.divorcios.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.suicidios }}</td>
              <td class="py-2.5 px-3 text-right font-mono text-ink-black font-semibold">{{ row.total_recolectado.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono font-semibold">{{ row.transcritas.toLocaleString() }}</td>
              <td class="py-2.5 px-3 text-right font-mono">
                <span class="px-1.5 py-0.5 rounded-xs bg-signal-blue/10 text-signal-blue font-semibold">
                  {{ row.por_transcribir }} (0 Rezago)
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
