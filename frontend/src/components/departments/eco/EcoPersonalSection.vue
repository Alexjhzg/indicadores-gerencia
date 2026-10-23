<script setup lang="ts">
import { Users } from 'lucide-vue-next';
import type { EconomicasMesData } from '@/data/departmentMonthlyData';

defineProps<{
  currentMesData: EconomicasMesData;
}>();

const selectedMes = defineModel<string>('selectedMes', { required: true });

const historialPersonal = [
  { mes: 'Ene', planif: 18, efec: 14, pct: '77.8%' },
  { mes: 'Feb', planif: 18, efec: 16, pct: '88.9%' },
  { mes: 'Mar', planif: 18, efec: 15, pct: '83.3%' },
  { mes: 'Abr', planif: 18, efec: 15, pct: '83.3%' },
  { mes: 'May', planif: 18, efec: 16, pct: '88.9%' },
  { mes: 'Jun', planif: 12, efec: 11, pct: '91.7%' },
  { mes: 'Jul', planif: 8, efec: 8, pct: '100.0%' },
  { mes: 'Ago', planif: 5, efec: 5, pct: '100.0%' },
];
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div class="pb-3 border-b border-mist">
      <div class="flex items-center gap-2 mb-1">
        <span class="font-mono text-xs font-semibold text-white bg-dept-eco px-2 py-0.5 rounded-[3px]">
          ECO-PRE-01
        </span>
        <Users :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Total Personal Levantamiento Encuesta (Operaciones de Campo)
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Planificado: {{ currentMesData.planif_personal }} · Efectivo: {{ currentMesData.efec_personal }} · Efectividad: {{ currentMesData.pct_personal }} (Mes activo: {{ currentMesData.mesNombre }})
      </p>
    </div>

    <!-- Tabla compacta del despliegue mensual de personal -->
    <div class="my-3 overflow-x-auto w-full min-w-0">
      <div class="grid grid-cols-8 gap-1 text-center min-w-[320px]">
        <button
          v-for="item in historialPersonal"
          :key="item.mes"
          type="button"
          class="border rounded-[3px] p-2 flex flex-col items-center justify-between gap-1 transition-all cursor-pointer border-none"
          :class="item.mes === selectedMes ? 'border-2 border-dept-eco bg-dept-eco-light/50 font-bold' : 'border-mist bg-white hover:bg-mist/40'"
          @click="selectedMes = item.mes"
        >
          <span class="text-[10px] font-semibold uppercase text-steel">{{ item.mes }}</span>
          <span class="text-xs font-mono font-semibold text-ink-black">{{ item.efec }}/{{ item.planif }}</span>
          <span class="text-[10px] font-mono text-signal-blue font-semibold">{{ item.pct }}</span>
        </button>
      </div>
    </div>

    <div class="pt-3 border-t border-mist text-xs text-steel font-medium flex items-center justify-between">
      <span>Acumulado 2026: <strong>100 de 115 personal</strong> (86.96% anual)</span>
      <span class="text-dept-eco font-semibold">{{ currentMesData.mesNombre }}: {{ currentMesData.pct_personal }} Efectividad</span>
    </div>
  </div>
</template>
