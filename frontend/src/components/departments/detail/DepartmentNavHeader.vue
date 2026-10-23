<script setup lang="ts">
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { ArrowLeft, ArrowRight, ShieldCheck, FileSpreadsheet } from 'lucide-vue-next';

defineProps<{
  deptCode: string;
  departmentInfo: Record<string, { activeBtnClass?: string }>;
}>();

const emit = defineEmits<{
  (e: 'back'): void;
  (e: 'selectDept', code: string): void;
}>();

const router = useRouter();
const authStore = useAuthStore();

const isJefeArea = computed(() => authStore.isJefeArea);
const isGerente = computed(() => authStore.isGerente);

const availableDeptCodes = computed(() => {
  if (isGerente.value) {
    return ['ECO', 'SOC', 'DEM', 'CART', 'SEG', 'SEEM'];
  }
  if (isJefeArea.value) {
    return authStore.allowedDepts;
  }
  return [];
});

const goToOperations = () => {
  router.push('/operaciones');
};
</script>

<template>
  <div class="flex items-center justify-between gap-2.5 py-1 sm:py-2.5 w-full">
    <!-- Si es Gerente o Admin: Volver al Resumen Ejecutivo -->
    <button
      v-if="isGerente"
      type="button"
      class="inline-flex items-center gap-1.5 text-xs sm:text-sm font-semibold text-ink-black border-b-[1.5px] border-ink-black pb-[1px] hover:opacity-75 transition-opacity cursor-pointer bg-transparent border-t-0 border-l-0 border-r-0 p-0 shrink-0"
      @click="emit('back')"
    >
      <ArrowLeft :size="16" :stroke-width="1.5" class="shrink-0" />
      <span class="max-sm:hidden">Volver al Resumen Ejecutivo</span>
      <span class="sm:hidden">Resumen</span>
    </button>

    <!-- Si es Jefe de Unidad o Jefe de Área: Enlace a Carga de Cifras Operativa -->
    <button
      v-else
      type="button"
      class="inline-flex items-center gap-1.5 text-xs sm:text-sm font-semibold text-signal-blue border-b-[1.5px] border-signal-blue pb-[1px] hover:opacity-75 transition-opacity cursor-pointer bg-transparent border-t-0 border-l-0 border-r-0 p-0 shrink-0"
      @click="goToOperations"
    >
      <FileSpreadsheet :size="15" :stroke-width="1.5" class="shrink-0" />
      <span>Ir al Panel de Carga Operativa</span>
      <ArrowRight :size="13" :stroke-width="1.5" class="shrink-0" />
    </button>

    <!-- Selector de Unidades Técnicas (Para Gerente con 6 unidades o Jefe de Área con sus 4 unidades) -->
    <div v-if="isGerente || isJefeArea" class="flex items-center gap-1.5 overflow-x-auto pb-0.5 max-w-full">
      <button
        v-for="code in availableDeptCodes"
        :key="code"
        type="button"
        class="px-3.5 max-sm:px-2.5 py-1.5 max-sm:py-1 rounded-[3px] text-xs font-semibold transition-all cursor-pointer shrink-0 border-none"
        :class="code === deptCode ? (departmentInfo[code]?.activeBtnClass || 'bg-ink-black text-white') : 'bg-mist text-steel hover:text-ink-black'"
        @click="emit('selectDept', code)"
      >
        {{ code }}
      </button>
    </div>

    <!-- Indicador Fijo de Unidad Asignada para el Jefe de Unidad (Encargado único) -->
    <div v-else class="flex items-center gap-2 shrink-0">
      <span
        class="inline-flex items-center gap-1.5 px-3 py-1 rounded-[3px] text-xs font-semibold"
        :class="departmentInfo[deptCode]?.activeBtnClass || 'bg-ink-black text-white'"
      >
        <ShieldCheck :size="14" :stroke-width="1.5" />
        <span>Unidad Asignada Exclusiva ({{ deptCode }})</span>
      </span>
    </div>
  </div>
</template>
