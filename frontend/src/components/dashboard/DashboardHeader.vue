<script setup lang="ts">
import { Calendar, Download } from 'lucide-vue-next';

defineEmits<{
  (e: 'exportXlsx'): void;
}>();
</script>

<template>
  <section class="flex flex-col md:flex-row md:items-end justify-between pb-5 border-b border-ash gap-4">
    <div>
      <div class="inline-flex items-center gap-1.5 text-xs font-semibold text-steel mb-1.5 tracking-wider">
        <Calendar :size="14" :stroke-width="1.5" class="shrink-0" />
        <span>INFORME MENSUAL DE GESTIÓN · AGOSTO 2026</span>
      </div>
      <h1 class="text-[32px] max-md:text-[22px] font-semibold text-ink-black tracking-tight leading-tight">
        MONAGAS / CONTROL DE INDICADORES
      </h1>
      <p class="text-[15px] font-medium text-steel mt-1">
        Consolidado estadal de las 5 unidades de estadística en los 13 municipios
      </p>
    </div>

    <div class="flex items-center gap-2.5">
      <button
        type="button"
        class="inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-signal-blue text-white rounded-[3px] text-[15px] font-semibold hover:opacity-90 transition-opacity cursor-pointer border-none"
        title="Descargar el Informe Mensual de Gestión analizado en formato Excel (.xlsx)"
        @click="$emit('exportXlsx')"
      >
        <Download :size="16" :stroke-width="1.5" class="shrink-0" />
        <span>Descargar Informe de Gestión (.xlsx)</span>
      </button>
    </div>
  </section>
</template>
