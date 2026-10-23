<script setup lang="ts">
import { Calendar } from 'lucide-vue-next';
import { mesesDisponibles } from '@/data/departmentMonthlyData';

defineProps<{
  mesNombre: string;
}>();

const selectedMes = defineModel<string>('selectedMes', { required: true });
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col md:flex-row md:items-center justify-between gap-3 w-full min-w-0 overflow-hidden">
    <div class="flex items-center gap-2 flex-wrap min-w-0 max-w-full">
      <div class="flex items-center gap-1.5 text-xs font-semibold text-steel uppercase tracking-wider shrink-0">
        <Calendar :size="15" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <span>Filtro de Mes (SEGEN):</span>
      </div>
      <div class="inline-flex rounded-[3px] border border-ash p-0.5 bg-mist/60 overflow-x-auto max-w-full min-w-0">
        <button
          v-for="m in mesesDisponibles"
          :key="m.id"
          type="button"
          class="px-2.5 py-1 text-xs font-semibold rounded-[3px] transition-colors cursor-pointer border-none shrink-0"
          :class="selectedMes === m.id ? 'bg-signal-blue text-white' : 'text-steel hover:text-ink-black bg-transparent'"
          @click="selectedMes = m.id"
        >
          {{ m.nombreCorto }}
        </button>
      </div>
    </div>
    <div class="text-xs text-steel font-medium">
      Período: <strong class="text-ink-black">{{ mesNombre }} 2026</strong>
    </div>
  </div>
</template>
