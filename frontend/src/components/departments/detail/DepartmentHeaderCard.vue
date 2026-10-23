<script setup lang="ts">
import { Calendar } from 'lucide-vue-next';

export interface DepartmentMeta {
  nombre: string;
  desc: string;
  coordinacion: string;
  indicadores: number;
  colorName: string;
  badgeClass: string;
  activeBtnClass: string;
  borderTopClass: string;
  lightTagClass: string;
  accentHex: string;
}

defineProps<{
  deptCode: string;
  currentDept: DepartmentMeta;
  indicatorsCount: number;
}>();
</script>

<template>
  <section
    class="bg-white border border-ash border-t-[3.5px] rounded-[3px] p-6 max-md:p-4.5 flex flex-col gap-4 transition-all"
    :class="currentDept.borderTopClass"
  >
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span
          class="text-xs font-semibold px-2.5 py-0.5 rounded-[3px] transition-colors"
          :class="currentDept.badgeClass"
        >
          {{ deptCode }}
        </span>
        <span
          class="text-xs font-semibold px-2 py-0.5 rounded-[3px] border transition-colors"
          :class="currentDept.lightTagClass"
        >
          {{ deptCode === 'SEEM' ? 'COORDINACIÓN' : 'UNIDAD DE ESTADÍSTICA' }} · INE MONAGAS (ENTIDAD 16)
        </span>
      </div>
      <div class="flex items-center gap-1.5 text-xs font-semibold px-2 py-0.5 bg-mist text-steel border border-ash rounded-[3px]">
        <Calendar :size="13" :stroke-width="1.5" class="shrink-0" />
        <span>Datos Oficiales: Agosto 2026</span>
      </div>
    </div>

    <h1 class="text-2xl max-md:text-xl font-semibold text-ink-black tracking-tight leading-snug">
      {{ currentDept.nombre }}
    </h1>
    <p class="text-[15px] font-normal text-steel leading-relaxed max-w-3xl">
      {{ currentDept.desc }}
    </p>

    <div class="flex flex-col sm:flex-row gap-6 sm:gap-10 pt-4 border-t border-mist">
      <div class="flex flex-col gap-0.5">
        <span class="text-xs font-semibold text-steel">
          {{ deptCode === 'SEEM' ? 'Coordinador Responsable:' : (['DEM', 'SEG'].includes(deptCode) ? 'Jefa de Unidad:' : 'Jefe de Unidad:') }}
        </span>
        <span class="text-sm font-semibold text-ink-black">{{ currentDept.coordinacion }}</span>
      </div>
      <div class="flex flex-col gap-0.5">
        <span class="text-xs font-semibold text-steel">Indicadores Oficiales:</span>
        <span class="text-sm font-semibold text-ink-black">{{ indicatorsCount }} métricas</span>
      </div>
      <div class="flex flex-col gap-0.5">
        <span class="text-xs font-semibold text-steel">Ámbito Territorial:</span>
        <span class="text-sm font-semibold text-ink-black">13 Municipios de Monagas</span>
      </div>
    </div>
  </section>
</template>
