<script setup lang="ts">
import { CheckCircle2 } from 'lucide-vue-next';

export interface IndicatorData {
  id: string;
  codigo: string;
  nombre: string;
  descripcion?: string;
  frecuencia?: string;
  meta_referencial?: number | null;
  unidad_medida?: string;
  categoria_nombre?: string;
}

export interface MeasurementDisplay {
  valor_registrado: string | number;
  meta_periodo: string | number;
  cumplimientoTexto: string;
  cumplimientoClass: string;
  periodoLabel: string;
  unidad_medida?: string;
}

defineProps<{
  indicator: IndicatorData;
  measurement: MeasurementDisplay | null;
  selectedMonth: string;
}>();
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between min-h-[220px] hover:border-ink-black transition-colors">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="font-mono text-xs font-semibold text-signal-blue bg-signal-blue/10 px-2 py-0.5 rounded-[3px]">
          {{ indicator.codigo }}
        </span>
        <span class="text-xs font-semibold text-steel">
          {{ indicator.frecuencia || 'Mensual' }}
        </span>
      </div>

      <h3 class="text-base font-semibold text-ink-black leading-snug mb-1.5">
        {{ indicator.nombre }}
      </h3>
      <p class="text-sm font-normal text-steel leading-relaxed mb-4 grow line-clamp-3">
        {{ indicator.descripcion || 'Sin descripción técnica adicional.' }}
      </p>
    </div>

    <div class="flex flex-col gap-2.5 pt-3 border-t border-mist">
      <!-- Cifra Real y Cumplimiento Dinámico según Mes -->
      <div
        v-if="measurement"
        class="flex items-center justify-between bg-mist/40 p-2 rounded-[3px]"
      >
        <div class="flex flex-col">
          <span class="text-[11px] font-medium text-steel">
            Cifra Real {{ selectedMonth }} 2026:
          </span>
          <span class="text-sm font-semibold text-ink-black font-mono">
            {{ measurement.valor_registrado }} {{ measurement.unidad_medida || indicator.unidad_medida }}
          </span>
        </div>
        <div class="flex flex-col items-end">
          <span class="text-[11px] font-medium text-steel">Meta Período:</span>
          <span class="text-xs font-semibold text-steel font-mono">
            {{ measurement.meta_periodo || indicator.meta_referencial }} {{ measurement.unidad_medida || indicator.unidad_medida }}
          </span>
        </div>
      </div>

      <div class="flex items-center justify-between">
        <div
          class="flex items-center gap-1 text-xs font-semibold"
          :class="measurement?.cumplimientoClass || 'text-signal-blue'"
        >
          <CheckCircle2 :size="15" :stroke-width="1.5" class="shrink-0" />
          <span>{{ measurement?.cumplimientoTexto || 'Certificado' }}</span>
        </div>
        <span class="text-xs text-steel font-normal">
          {{ indicator.categoria_nombre || 'Indicador Oficial' }}
        </span>
      </div>
    </div>
  </div>
</template>
