<script setup lang="ts">
import { Calendar, Layers } from 'lucide-vue-next';
import { mesesDisponibles } from '@/data/departmentMonthlyData';

const selectedMes = defineModel<string>('selectedMes', { required: true });
const activeSubprogram = defineModel<'TODOS' | 'EHM' | 'ESCA'>('activeSubprogram', { required: true });
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col md:flex-row md:items-center justify-between gap-3">
    <!-- Selector de Meses -->
    <div class="flex items-center gap-2 flex-wrap">
      <div class="flex items-center gap-1.5 text-xs font-semibold text-steel uppercase tracking-wider shrink-0">
        <Calendar :size="15" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <span>Filtro de Mes:</span>
      </div>
      <div class="inline-flex rounded-[3px] border border-ash p-0.5 bg-mist/60 overflow-x-auto max-w-full">
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

    <!-- Selector de Subprogramas Sociales -->
    <div class="flex items-center gap-2 flex-wrap">
      <div class="flex items-center gap-1.5 text-xs font-semibold text-steel uppercase tracking-wider shrink-0">
        <Layers :size="15" :stroke-width="1.5" class="text-ink-black shrink-0" />
        <span>Subprograma:</span>
      </div>
      <div class="inline-flex rounded-[3px] border border-ash p-0.5 bg-mist/60 overflow-x-auto max-w-full">
        <button
          type="button"
          class="px-2.5 py-1 text-xs font-semibold rounded-[3px] transition-colors cursor-pointer border-none shrink-0"
          :class="activeSubprogram === 'TODOS' ? 'bg-ink-black text-white' : 'text-steel hover:text-ink-black bg-transparent'"
          @click="activeSubprogram = 'TODOS'"
        >
          Consolidado
        </button>
        <button
          type="button"
          class="px-2.5 py-1 text-xs font-semibold rounded-[3px] transition-colors cursor-pointer border-none shrink-0"
          :class="activeSubprogram === 'EHM' ? 'bg-ink-black text-white' : 'text-steel hover:text-ink-black bg-transparent'"
          @click="activeSubprogram = 'EHM'"
        >
          EHM
        </button>
        <button
          type="button"
          class="px-2.5 py-1 text-xs font-semibold rounded-[3px] transition-colors cursor-pointer border-none shrink-0"
          :class="activeSubprogram === 'ESCA' ? 'bg-ink-black text-white' : 'text-steel hover:text-ink-black bg-transparent'"
          @click="activeSubprogram = 'ESCA'"
        >
          ESCA
        </button>
      </div>
    </div>
  </div>
</template>
