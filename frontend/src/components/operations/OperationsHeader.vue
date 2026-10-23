<script setup lang="ts">
import { FileSpreadsheet, UploadCloud, History } from 'lucide-vue-next';

defineProps<{
  activeTab: 'UPLOAD' | 'AUDIT';
}>();

defineEmits<{
  (e: 'changeTab', tab: 'UPLOAD' | 'AUDIT'): void;
}>();
</script>

<template>
  <div class="flex flex-col md:flex-row md:items-end justify-between pb-5 border-b border-ash gap-4">
    <div>
      <div class="inline-flex items-center gap-1.5 text-xs font-semibold text-steel mb-1.5 tracking-wider">
        <FileSpreadsheet :size="14" :stroke-width="1.5" class="shrink-0" />
        <span>CENTRO DE GESTIÓN OPERATIVA · INE MONAGAS (ENTIDAD 16)</span>
      </div>
      <h1 class="text-[32px] max-md:text-[22px] font-semibold text-ink-black tracking-tight leading-tight">
        Panel de Carga y Auditoría Operativa
      </h1>
      <p class="text-[15px] font-medium text-steel mt-1">
        Carga mensual de cifras por Unidad de Estadística, validación Excel (.xlsx) y trazabilidad inmutable
      </p>
    </div>

    <!-- Selector de Pestañas Superiores -->
    <div class="inline-flex p-1 bg-mist border border-ash rounded-[3px] shrink-0">
      <button
        type="button"
        class="inline-flex items-center gap-1.5 px-4 py-2 rounded-[3px] text-xs font-semibold transition-all cursor-pointer border-none"
        :class="
          activeTab === 'UPLOAD'
            ? 'bg-signal-blue text-white'
            : 'bg-transparent text-steel hover:text-ink-black'
        "
        @click="$emit('changeTab', 'UPLOAD')"
      >
        <UploadCloud :size="15" :stroke-width="1.5" />
        <span>Carga de Cifras por Unidad</span>
      </button>

      <button
        type="button"
        class="inline-flex items-center gap-1.5 px-4 py-2 rounded-[3px] text-xs font-semibold transition-all cursor-pointer border-none"
        :class="
          activeTab === 'AUDIT'
            ? 'bg-signal-blue text-white'
            : 'bg-transparent text-steel hover:text-ink-black'
        "
        @click="$emit('changeTab', 'AUDIT')"
      >
        <History :size="15" :stroke-width="1.5" />
        <span>Auditoría de Versiones</span>
      </button>
    </div>
  </div>
</template>
