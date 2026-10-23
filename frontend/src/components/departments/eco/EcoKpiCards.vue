<script setup lang="ts">
import type { EconomicasMesData } from '@/data/departmentMonthlyData';

defineProps<{
  currentMesData: EconomicasMesData;
  displayCumplimientoPrecios: string;
  displayPreciosEfec: number;
  displayMetaPrecios: number;
  displayCalidadPct: string;
  displayPreciosSinError: number;
  selectedSemana: string;
}>();
</script>

<template>
  <div class="grid grid-cols-6 max-xl:grid-cols-3 max-md:grid-cols-2 max-sm:grid-cols-1 gap-3">
    <!-- 1.1 ECO-PRE-01 -->
    <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col justify-between gap-2 hover:border-ink-black transition-colors">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-mono text-[10px] font-semibold text-white bg-dept-eco px-1.5 py-0.5 rounded-[3px]">
            ECO-PRE-01
          </span>
          <span class="text-[10px] font-semibold px-1.5 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
            {{ currentMesData.pct_personal }} Efect.
          </span>
        </div>
        <h4 class="text-xs font-semibold tracking-tight text-steel uppercase line-clamp-2">
          Total Personal Levantamiento Encuesta
        </h4>
      </div>
      <div>
        <div class="flex items-baseline gap-1">
          <span class="text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentMesData.efec_personal }} / {{ currentMesData.planif_personal }}
          </span>
          <span class="text-xs font-semibold text-steel">personas</span>
        </div>
        <span class="text-[10px] font-normal text-steel">
          Planif: {{ currentMesData.planif_personal }} · Efec: {{ currentMesData.efec_personal }} ({{ currentMesData.mesNombre }})
        </span>
      </div>
    </div>

    <!-- 1.2 ECO-DIR-01 -->
    <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col justify-between gap-2 hover:border-ink-black transition-colors">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-mono text-[10px] font-semibold text-white bg-dept-eco px-1.5 py-0.5 rounded-[3px]">
            ECO-DIR-01
          </span>
          <span class="text-[10px] font-semibold px-1.5 py-0.5 rounded-[3px] bg-dept-eco-light text-dept-eco border border-dept-eco-border">
            Directorio
          </span>
        </div>
        <h4 class="text-xs font-semibold tracking-tight text-steel uppercase line-clamp-2">
          Total Establecimientos Implantados Directorio
        </h4>
      </div>
      <div>
        <div class="flex items-baseline gap-1">
          <span class="text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentMesData.directorio }}
          </span>
          <span class="text-xs font-semibold text-steel">locales</span>
        </div>
        <span class="text-[10px] font-normal text-steel">Acumulado a {{ currentMesData.mesNombre }}: {{ currentMesData.acumulado_directorio.toLocaleString() }}</span>
      </div>
    </div>

    <!-- 1.3 ECO-CAN-04 -->
    <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col justify-between gap-2 hover:border-ink-black transition-colors">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-mono text-[10px] font-semibold text-white bg-dept-eco px-1.5 py-0.5 rounded-[3px]">
            ECO-CAN-04
          </span>
          <span class="text-[10px] font-semibold px-1.5 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
            100% Meta
          </span>
        </div>
        <h4 class="text-xs font-semibold tracking-tight text-steel uppercase line-clamp-2">
          Total Comunas con Levantamiento CAN
        </h4>
      </div>
      <div>
        <div class="flex items-baseline gap-1">
          <span class="text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentMesData.comunas }}
          </span>
          <span class="text-xs font-semibold text-steel">comunas</span>
        </div>
        <span class="text-[10px] font-normal text-steel">{{ currentMesData.nodos }} nodos SEGEN articulados</span>
      </div>
    </div>

    <!-- 1.4 ECO-CAN-01 -->
    <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col justify-between gap-2 hover:border-ink-black transition-colors">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-mono text-[10px] font-semibold text-white bg-dept-eco px-1.5 py-0.5 rounded-[3px]">
            ECO-CAN-01
          </span>
          <span class="text-[10px] font-semibold px-1.5 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
            {{ currentMesData.pct_locales }} Efect.
          </span>
        </div>
        <h4 class="text-xs font-semibold tracking-tight text-steel uppercase line-clamp-2">
          Total Establecimientos Encuesta Efectiva CAN
        </h4>
      </div>
      <div>
        <div class="flex items-baseline gap-1">
          <span class="text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentMesData.efec_locales }} / {{ currentMesData.planif_locales }}
          </span>
          <span class="text-xs font-semibold text-steel">locales</span>
        </div>
        <span class="text-[10px] font-normal text-steel">{{ currentMesData.pct_locales }} locales planificados</span>
      </div>
    </div>

    <!-- 1.5 ECO-CAN-02 -->
    <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col justify-between gap-2 hover:border-ink-black transition-colors">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-mono text-[10px] font-semibold text-white bg-dept-eco px-1.5 py-0.5 rounded-[3px]">
            ECO-CAN-02
          </span>
          <span class="text-[10px] font-semibold px-1.5 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
            {{ displayCumplimientoPrecios }} Meta
          </span>
        </div>
        <h4 class="text-xs font-semibold tracking-tight text-steel uppercase line-clamp-2">
          Total Precios Levantados Reales Efectivos
        </h4>
      </div>
      <div>
        <div class="flex items-baseline gap-1">
          <span class="text-[24px] font-semibold text-ink-black tracking-tight">
            {{ displayPreciosEfec.toLocaleString() }}
          </span>
          <span class="text-xs font-semibold text-steel">/ {{ displayMetaPrecios.toLocaleString() }}</span>
        </div>
        <span class="text-[10px] font-normal text-steel">
          {{ selectedSemana === 'TODAS' ? `Total ${currentMesData.mesNombre}: ${displayPreciosEfec.toLocaleString()} precios` : `Semana ${selectedSemana}: ${displayPreciosEfec} precios` }}
        </span>
      </div>
    </div>

    <!-- 1.6 ECO-CAN-03 -->
    <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col justify-between gap-2 hover:border-ink-black transition-colors">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-mono text-[10px] font-semibold text-white bg-dept-eco px-1.5 py-0.5 rounded-[3px]">
            ECO-CAN-03
          </span>
          <span class="text-[10px] font-semibold px-1.5 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
            Excelente
          </span>
        </div>
        <h4 class="text-xs font-semibold tracking-tight text-steel uppercase line-clamp-2">
          Total Precios Levantados Reales (Sin Errores)
        </h4>
      </div>
      <div>
        <div class="flex items-baseline gap-1">
          <span class="text-[24px] font-semibold text-ink-black tracking-tight">
            {{ displayCalidadPct }}
          </span>
          <span class="text-xs font-semibold text-steel">limpios</span>
        </div>
        <span class="text-[10px] font-normal text-steel">
          {{ displayPreciosSinError.toLocaleString() }} precios sin incidencias
        </span>
      </div>
    </div>
  </div>
</template>
