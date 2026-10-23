<script setup lang="ts">
import type { SocialesMesData } from '@/data/departmentMonthlyData';

defineProps<{
  currentSocData: SocialesMesData;
  activeSubprogram: 'TODOS' | 'EHM' | 'ESCA';
}>();
</script>

<template>
  <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3.5">
    <!-- Controles Levantados EHM -->
    <div
      v-if="activeSubprogram === 'TODOS' || activeSubprogram === 'EHM'"
      class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors"
    >
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Levantamiento EHM</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          {{ currentSocData.ehm_efec }} / {{ currentSocData.ehm_planif }} Controles
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          {{ currentSocData.ehm_pct }}
        </span>
        <span class="text-xs font-semibold text-steel">cobertura</span>
      </div>
      <span class="text-xs font-normal text-steel">
        {{ currentSocData.mesNombre }}: {{ currentSocData.ehm_efec }} controles levantados
      </span>
    </div>

    <!-- Viviendas Efectivas EHM -->
    <div
      v-if="activeSubprogram === 'TODOS' || activeSubprogram === 'EHM'"
      class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors"
    >
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Viviendas EHM</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          Meta: {{ currentSocData.ehm_viv_meta }}
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          {{ currentSocData.ehm_viv_efec }}
        </span>
        <span class="text-xs font-semibold text-steel">efectivas</span>
      </div>
      <span class="text-xs font-normal text-steel">
        {{ currentSocData.mesNombre }}: {{ currentSocData.ehm_viv_efec }} hogares entrevistados
      </span>
    </div>

    <!-- Controles Levantados ESCA -->
    <div
      v-if="activeSubprogram === 'TODOS' || activeSubprogram === 'ESCA'"
      class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors"
    >
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Levantamiento ESCA</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          {{ currentSocData.esca_efec }} / {{ currentSocData.esca_planif }} Controles
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          {{ currentSocData.esca_pct }}
        </span>
        <span class="text-xs font-semibold text-steel">cobertura</span>
      </div>
      <span class="text-xs font-normal text-steel">
        {{ currentSocData.mesNombre }}: {{ currentSocData.esca_efec }} controles levantados
      </span>
    </div>

    <!-- Viviendas Efectivas ESCA -->
    <div
      v-if="activeSubprogram === 'TODOS' || activeSubprogram === 'ESCA'"
      class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors"
    >
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Viviendas ESCA</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          Meta: {{ currentSocData.esca_viv_meta }}
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          {{ currentSocData.esca_viv_efec }}
        </span>
        <span class="text-xs font-semibold text-steel">efectivas</span>
      </div>
      <span class="text-xs font-normal text-steel">
        {{ currentSocData.mesNombre }}: {{ currentSocData.esca_viv_efec }} hogares registrados
      </span>
    </div>
  </div>
</template>
