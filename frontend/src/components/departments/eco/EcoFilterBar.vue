<script setup lang="ts">
import { Calendar, Clock } from 'lucide-vue-next';

defineProps<{
  activePeriodLabel: string;
}>();

const selectedMes = defineModel<string>('selectedMes', { required: true });
const selectedSemana = defineModel<string>('selectedSemana', { required: true });

const mesesDisponibles = [
  { id: 'Ene', nombre: 'Enero', nombreCorto: 'Ene' },
  { id: 'Feb', nombre: 'Febrero', nombreCorto: 'Feb' },
  { id: 'Mar', nombre: 'Marzo', nombreCorto: 'Mar' },
  { id: 'Abr', nombre: 'Abril', nombreCorto: 'Abr' },
  { id: 'May', nombre: 'Mayo', nombreCorto: 'May' },
  { id: 'Jun', nombre: 'Junio', nombreCorto: 'Jun' },
  { id: 'Jul', nombre: 'Julio', nombreCorto: 'Jul' },
  { id: 'Ago', nombre: 'Agosto', nombreCorto: 'Ago' },
];

const semanasDisponibles = [
  { id: 'TODAS', label: 'Todas las Semanas' },
  { id: '1', label: 'Semana 1' },
  { id: '2', label: 'Semana 2' },
  { id: '3', label: 'Semana 3' },
  { id: '4', label: 'Semana 4' },
];
</script>

<template>
  <div class="flex flex-col gap-2 w-full min-w-0">
    <!-- Barra de Filtros: Mes y Semanas -->
    <div class="bg-white border border-ash rounded-[3px] p-3.5 flex flex-col md:flex-row md:items-center justify-between gap-3.5 w-full min-w-0 overflow-hidden">
      <!-- Selector de Meses -->
      <div class="flex flex-col sm:flex-row sm:items-center gap-2 w-full md:w-auto min-w-0">
        <div class="flex items-center gap-1.5 text-xs font-semibold text-steel uppercase tracking-wider shrink-0">
          <Calendar :size="15" :stroke-width="1.5" class="text-dept-eco shrink-0" />
          <span>Filtro de Mes:</span>
        </div>
        <div class="inline-flex rounded-[3px] border border-ash p-0.5 bg-mist/60 overflow-x-auto max-w-full min-w-0">
          <button
            v-for="mes in mesesDisponibles"
            :key="mes.id"
            type="button"
            class="px-2.5 py-1 text-xs font-semibold rounded-[3px] transition-colors cursor-pointer border-none shrink-0"
            :class="selectedMes === mes.id ? 'bg-dept-eco text-white' : 'text-steel hover:text-ink-black bg-transparent'"
            @click="selectedMes = mes.id"
          >
            {{ mes.nombreCorto }}
          </button>
        </div>
      </div>

      <!-- Selector de Semanas -->
      <div class="flex flex-col sm:flex-row sm:items-center gap-2 w-full md:w-auto min-w-0">
        <div class="flex items-center gap-1.5 text-xs font-semibold text-steel uppercase tracking-wider shrink-0">
          <Clock :size="15" :stroke-width="1.5" class="text-signal-blue shrink-0" />
          <span>Filtro de Semanas:</span>
        </div>
        <div class="inline-flex rounded-[3px] border border-ash p-0.5 bg-mist/60 overflow-x-auto max-w-full min-w-0">
          <button
            v-for="sem in semanasDisponibles"
            :key="sem.id"
            type="button"
            class="px-2.5 py-1 text-xs font-semibold rounded-[3px] transition-colors cursor-pointer border-none shrink-0"
            :class="selectedSemana === sem.id ? 'bg-signal-blue text-white' : 'text-steel hover:text-ink-black bg-transparent'"
            @click="selectedSemana = sem.id"
          >
            <span class="sm:hidden">{{ sem.id === 'TODAS' ? 'Todas' : `Sem ${sem.id}` }}</span>
            <span class="hidden sm:inline">{{ sem.label }}</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Indicador de Contexto Activo -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 px-1 text-xs text-steel font-medium w-full min-w-0">
      <div class="flex items-center gap-2 min-w-0">
        <span class="inline-block w-2 h-2 rounded-full bg-dept-eco shrink-0"></span>
        <span class="truncate">Período Seleccionado: <strong class="text-ink-black">{{ activePeriodLabel }}</strong></span>
      </div>
      <span class="text-[11px] text-steel shrink-0">Fuente: Informe Mensual de Gestión (Gerencia de Precios)</span>
    </div>
  </div>
</template>
