<script setup lang="ts">
import { Layers, ChevronRight } from 'lucide-vue-next';

export interface DepartmentSummaryMeta {
  codigo: string;
  nombre: string;
  descripcion: string;
  total_indicadores: number;
  meta_ref: string;
  badgeClass: string;
  activeBtnClass: string;
  borderTop: string;
  barColor: string;
  lightTag: string;
}

defineProps<{
  departments: DepartmentSummaryMeta[];
  activeFilter?: string;
  getDeptCount: (codigo: string) => number;
}>();

const emit = defineEmits<{
  (e: 'selectDept', codigo: string): void;
}>();
</script>

<template>
  <section class="flex flex-col gap-4">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2 text-ink-black">
        <Layers :size="18" :stroke-width="1.5" class="shrink-0" />
        <h2 class="text-xl font-semibold tracking-tight">UNIDADES Y COORDINACIÓN</h2>
      </div>
      <span class="text-xs font-medium text-steel hidden sm:inline">
        Seleccione una unidad o coordinación para acceder directamente a sus indicadores
      </span>
    </div>

    <!-- Carrusel deslizable en móvil, Grid 6 columnas en Desktop -->
    <div class="grid grid-cols-6 max-xl:grid-cols-3 max-lg:grid-cols-2 max-md:flex max-md:overflow-x-auto max-md:snap-x max-md:snap-mandatory gap-3 pb-2">
      <div
        v-for="dept in departments"
        :key="dept.codigo"
        class="bg-white border border-ash border-t-[3.5px] rounded-[3px] p-4.5 flex flex-col justify-between min-h-[190px] max-md:min-w-[260px] max-md:shrink-0 max-md:snap-start hover:border-carbon transition-all cursor-pointer"
        :class="[dept.borderTop, { 'ring-1 ring-carbon': activeFilter === dept.codigo }]"
        @click="emit('selectDept', dept.codigo)"
      >
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] transition-colors" :class="dept.badgeClass">
            {{ dept.codigo }}
          </span>
          <span class="text-xs font-semibold text-steel">
            {{ getDeptCount(dept.codigo) || dept.total_indicadores }} Indicadores
          </span>
        </div>

        <h3 class="text-base font-semibold text-ink-black leading-snug mb-1">
          {{ dept.nombre }}
        </h3>
        <p class="text-xs font-normal text-steel leading-relaxed mb-3 grow">
          {{ dept.descripcion }}
        </p>

        <div class="flex flex-col gap-1 mb-3">
          <div class="flex justify-between text-xs font-semibold">
            <span class="text-steel">Cumplimiento:</span>
            <span class="text-ink-black">{{ dept.meta_ref }}</span>
          </div>
          <div class="w-full h-1 bg-mist rounded-sm overflow-hidden">
            <div
              class="h-full transition-all"
              :class="dept.barColor"
              :style="{ width: dept.meta_ref }"
            ></div>
          </div>
        </div>

        <div class="flex justify-end pt-1">
          <span class="inline-flex items-center gap-1 text-xs font-semibold text-ink-black hover:opacity-75 transition-opacity">
            <span>Ver Unidad</span>
            <ChevronRight :size="14" :stroke-width="1.5" class="shrink-0" />
          </span>
        </div>
      </div>
    </div>
  </section>
</template>
