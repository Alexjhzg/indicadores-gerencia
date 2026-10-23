<script setup lang="ts">
import { Search } from 'lucide-vue-next';
import type { DepartmentSummaryMeta } from './DashboardDepartmentCards.vue';

export interface DashboardIndicatorItem {
  id: string;
  codigo: string;
  nombre: string;
  departamento_codigo: string;
  frecuencia?: string;
  meta_referencial?: number | null;
  unidad_medida?: string;
}

defineProps<{
  indicators: DashboardIndicatorItem[];
  departments: DepartmentSummaryMeta[];
  totalIndicatorsCount: number;
  getDeptBadgeClass: (codigo: string) => string;
  getDeptCount: (codigo: string) => number;
}>();

const emit = defineEmits<{
  (e: 'navigate', codigo: string): void;
  (e: 'filterDept', codigo: string): void;
}>();

const activeFilter = defineModel<string>('activeFilter', { default: 'TODOS' });
const searchQuery = defineModel<string>('searchQuery', { default: '' });
</script>

<template>
  <section class="bg-white border border-ash rounded-[3px] p-5 flex flex-col gap-4">
    <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3">
      <div>
        <h3 class="text-base font-semibold text-ink-black">Catálogo Oficial de Indicadores Registrados</h3>
        <p class="text-xs font-normal text-steel">
          Mostrando {{ indicators.length }} de {{ totalIndicatorsCount }} indicadores técnicos vigentes
        </p>
      </div>

      <div class="flex flex-wrap items-center gap-2">
        <!-- Buscador Rápido -->
        <div class="relative w-full sm:w-60">
          <Search :size="14" :stroke-width="1.5" class="absolute left-3 top-1/2 -translate-y-1/2 text-steel" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Buscar indicador o código..."
            class="w-full pl-8 pr-3 py-1 text-xs font-medium border border-ash rounded-[3px] bg-white text-ink-black focus:outline-none focus:border-signal-blue"
          />
        </div>

        <!-- Filtros por Unidad de Estadística -->
        <div class="flex items-center gap-1.5 overflow-x-auto pb-1 max-w-full">
          <button
            type="button"
            class="px-2.5 py-1 rounded-[3px] text-xs font-semibold transition-all cursor-pointer shrink-0 border-none"
            :class="activeFilter === 'TODOS' ? 'bg-ink-black text-white' : 'bg-mist text-steel hover:text-ink-black'"
            @click="emit('filterDept', 'TODOS')"
          >
            Todos ({{ totalIndicatorsCount }})
          </button>
          <button
            v-for="dept in departments"
            :key="dept.codigo"
            type="button"
            class="px-2.5 py-1 rounded-[3px] text-xs font-semibold transition-all cursor-pointer shrink-0 border-none"
            :class="activeFilter === dept.codigo ? (dept.activeBtnClass || 'bg-ink-black text-white') : 'bg-mist text-steel hover:text-ink-black'"
            @click="emit('filterDept', dept.codigo)"
          >
            {{ dept.codigo }} ({{ getDeptCount(dept.codigo) }})
          </button>
        </div>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full border-collapse text-left text-[15px]">
        <thead>
          <tr class="border-b-[1.5px] border-ash text-xs font-semibold text-steel">
            <th class="py-3 px-3">CÓDIGO</th>
            <th class="py-3 px-3">INDICADOR TÉCNICO</th>
            <th class="py-3 px-3">UNIDAD / COORD.</th>
            <th class="py-3 px-3">FRECUENCIA</th>
            <th class="py-3 px-3">META REFERENCIAL</th>
            <th class="py-3 px-3">ESTADO</th>
            <th class="py-3 px-3">ACCIÓN</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-mist">
          <tr
            v-for="ind in indicators"
            :key="ind.id"
            class="hover:bg-black/[0.02] transition-colors"
          >
            <td class="py-3 px-3 font-mono text-xs font-semibold text-ink-black">
              {{ ind.codigo }}
            </td>
            <td class="py-3 px-3 font-medium text-ink-black max-w-[380px]">
              {{ ind.nombre }}
            </td>
            <td class="py-3 px-3">
              <span
                class="inline-flex items-center px-2 py-0.5 text-xs font-semibold rounded-[3px] transition-colors"
                :class="getDeptBadgeClass(ind.departamento_codigo)"
              >
                {{ ind.departamento_codigo }}
              </span>
            </td>
            <td class="py-3 px-3 text-xs text-steel">
              {{ ind.frecuencia || 'Mensual' }}
            </td>
            <td class="py-3 px-3 font-semibold text-ink-black text-sm tabular-nums">
              {{ ind.meta_referencial ?? '100.00' }} {{ ind.unidad_medida }}
            </td>
            <td class="py-3 px-3">
              <span class="inline-flex items-center px-2 py-0.5 text-xs font-semibold bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px]">
                Certificado
              </span>
            </td>
            <td class="py-3 px-3">
              <button
                type="button"
                class="text-xs font-semibold text-ink-black border-b-[1.5px] border-ink-black pb-[1px] hover:opacity-70 transition-opacity cursor-pointer bg-transparent border-t-0 border-l-0 border-r-0 p-0"
                @click="emit('navigate', ind.departamento_codigo)"
              >
                Detalle
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>
