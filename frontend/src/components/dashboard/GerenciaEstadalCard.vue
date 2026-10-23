<script setup lang="ts">
import { Building, ShieldCheck } from 'lucide-vue-next';
import { cuadroGerenciaEstadal_Personal } from '@/data/cuadrosOficiales';
</script>

<template>
  <section class="bg-white border border-ash rounded-[3px] p-5 flex flex-col gap-4">
    <!-- Encabezado de la Gerencia Estadal -->
    <div class="flex items-start justify-between flex-wrap gap-2">
      <div class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-[3px] bg-ink-black text-white flex items-center justify-center shrink-0">
          <Building :size="18" :stroke-width="1.5" />
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h3 class="text-base font-semibold text-ink-black">
              Gerencia Estadal Monagas · Informe de Gestión Institucional
            </h3>
            <span class="text-[11px] font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
              LA 10. Gerencia Estadal
            </span>
          </div>
          <p class="text-xs text-steel">
            Planta de personal activa, condición laboral y paridad de género en la sede regional (Entidad 16 · Agosto 2026)
          </p>
        </div>
      </div>

      <div class="flex items-center gap-1.5">
        <span class="text-xs font-semibold px-2.5 py-1 bg-mist text-ink-black rounded-[3px] inline-flex items-center gap-1.5">
          <ShieldCheck :size="14" :stroke-width="1.5" class="text-signal-blue" />
          <span>Sede Maturín · Despacho Gerencial</span>
        </span>
      </div>
    </div>

    <!-- Bloques de Estadísticas de Personal -->
    <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3">
      <!-- Total Planta -->
      <div class="p-3.5 bg-canvas border border-mist rounded-[3px] flex flex-col gap-1">
        <span class="text-[11px] font-semibold text-steel uppercase tracking-wider">Total Planta INE</span>
        <div class="flex items-baseline gap-2">
          <span class="text-2xl font-bold text-ink-black">54</span>
          <span class="text-xs text-steel font-medium">trabajadores</span>
        </div>
        <span class="text-[11px] text-steel">44 en funciones activas + 10 jubilados</span>
      </div>

      <!-- Contratados -->
      <div class="p-3.5 bg-canvas border border-mist rounded-[3px] flex flex-col gap-1">
        <span class="text-[11px] font-semibold text-steel uppercase tracking-wider">Personal Contratado</span>
        <div class="flex items-baseline gap-2">
          <span class="text-2xl font-bold text-ink-black">39</span>
          <span class="text-xs text-signal-blue font-semibold">72.2% Planta</span>
        </div>
        <span class="text-[11px] text-steel">18 Masculino / 21 Femenino</span>
      </div>

      <!-- Fijos -->
      <div class="p-3.5 bg-canvas border border-mist rounded-[3px] flex flex-col gap-1">
        <span class="text-[11px] font-semibold text-steel uppercase tracking-wider">Personal Fijo</span>
        <div class="flex items-baseline gap-2">
          <span class="text-2xl font-bold text-ink-black">5</span>
          <span class="text-xs text-dept-eco font-semibold">Carrera</span>
        </div>
        <span class="text-[11px] text-steel">2 Masculino / 3 Femenino</span>
      </div>

      <!-- Jubilados -->
      <div class="p-3.5 bg-canvas border border-mist rounded-[3px] flex flex-col gap-1">
        <span class="text-[11px] font-semibold text-steel uppercase tracking-wider">Personal Jubilado</span>
        <div class="flex items-baseline gap-2">
          <span class="text-2xl font-bold text-ink-black">10</span>
          <span class="text-xs text-steel font-medium">Previsión</span>
        </div>
        <span class="text-[11px] text-steel">4 Masculino / 6 Femenino</span>
      </div>
    </div>

    <!-- Tabla Oficial de Personal por Género y Condición (LA 10) -->
    <div class="border border-mist rounded-[3px] overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="bg-mist text-ink-black border-b border-ash font-semibold text-[11px] uppercase tracking-wider">
              <th class="py-2.5 px-3">Condición del Personal</th>
              <th class="py-2.5 px-3 text-right">Masculino</th>
              <th class="py-2.5 px-3 text-right">Femenino</th>
              <th class="py-2.5 px-3 text-right">Total Dotación</th>
              <th class="py-2.5 px-3 text-right">% Paridad</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-mist font-medium">
            <tr
              v-for="row in cuadroGerenciaEstadal_Personal"
              :key="row.condicion"
              class="hover:bg-mist/30 transition-colors"
              :class="{ 'bg-signal-blue/5 font-bold text-ink-black border-t-2 border-ash': row.condicion.includes('TOTAL') }"
            >
              <td class="py-2.5 px-3 font-semibold text-ink-black">{{ row.condicion }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.masculino }}</td>
              <td class="py-2.5 px-3 text-right font-mono">{{ row.femenino }}</td>
              <td class="py-2.5 px-3 text-right font-mono text-signal-blue font-bold">{{ row.total }}</td>
              <td class="py-2.5 px-3 text-right font-mono text-steel">
                {{ ((row.femenino / row.total) * 100).toFixed(1) }}% Fem.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
