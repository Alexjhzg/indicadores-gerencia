<script setup lang="ts">
export interface SegDepartmentData {
  mesNombre: string;
  totalEncuestas: number;
  pctMeta: string;
}

defineProps<{
  currentSegData: SegDepartmentData;
}>();
</script>

<template>
  <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3.5">
    <!-- Operatividad Nodos -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Operatividad Nodos</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          50 / 106
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          47.17%
        </span>
        <span class="text-xs font-semibold text-steel">activos</span>
      </div>
      <span class="text-xs font-normal text-steel">56 nodos con intermitencia de enlace en campo</span>
    </div>

    <!-- Encuestas ODK -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Encuestas ODK {{ currentSegData.mesNombre }}</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          {{ currentSegData.pctMeta }} Meta
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          {{ currentSegData.totalEncuestas.toLocaleString() }}
        </span>
        <span class="text-xs font-semibold text-steel">formularios</span>
      </div>
      <span class="text-xs font-normal text-steel">{{ currentSegData.mesNombre }}: {{ currentSegData.totalEncuestas.toLocaleString() }} formularios levantados</span>
    </div>

    <!-- Equipos DMC en Campo -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Equipos DMC en Campo</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          90.0% Meta
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          315
        </span>
        <span class="text-xs font-semibold text-steel">dispositivos</span>
      </div>
      <span class="text-xs font-normal text-steel">+ 48 laptops y estaciones MiniPC operativas</span>
    </div>

    <!-- Fuerza Territorial -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Fuerza Territorial</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          99.0% Despliegue
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          208 / 210
        </span>
        <span class="text-xs font-semibold text-steel">funcionarios</span>
      </div>
      <span class="text-xs font-normal text-steel">Coordinadores, supervisores y encuestadores</span>
    </div>
  </div>
</template>
