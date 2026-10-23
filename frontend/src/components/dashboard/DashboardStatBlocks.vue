<script setup lang="ts">
export interface DashboardSummaryData {
  cumplimiento_general_estadal: number;
  total_departamentos: number;
  total_indicadores_activos: number;
  total_mediciones_aprobadas: number;
}

defineProps<{
  summary: DashboardSummaryData;
}>();
</script>

<template>
  <section class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3.5">
    <!-- Cumplimiento Global Estadal -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <span class="text-xs font-semibold tracking-wider text-steel uppercase">CUMPLIMIENTO GLOBAL ESTADAL</span>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          {{ summary.cumplimiento_general_estadal }}%
        </span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          +2.4% vs Julio
        </span>
      </div>
      <span class="text-xs font-normal text-steel">Meta institucional fijada en 90.0%</span>
    </div>

    <!-- Cobertura Territorial -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <span class="text-xs font-semibold tracking-wider text-steel uppercase">COBERTURA TERRITORIAL</span>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          13 / 13
        </span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          100% Monagas
        </span>
      </div>
      <span class="text-xs font-normal text-steel">DPT 1601 Maturín a DPT 1613 Uracoa</span>
    </div>

    <!-- Indicadores Certificados -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <span class="text-xs font-semibold tracking-wider text-steel uppercase">INDICADORES CERTIFICADOS</span>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          {{ summary.total_mediciones_aprobadas }} / {{ summary.total_indicadores_activos }}
        </span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          96.5% Verificado
        </span>
      </div>
      <span class="text-xs font-normal text-steel">5 Unidades de estadística operativas con auditoría</span>
    </div>

    <!-- Estado de Auditoría -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <span class="text-xs font-semibold tracking-wider text-steel uppercase">ESTADO DE AUDITORÍA</span>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          V.2 ACTIVA
        </span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          Inmutable
        </span>
      </div>
      <span class="text-xs font-normal text-steel">Triggers de versión y rollback activos</span>
    </div>
  </section>
</template>
