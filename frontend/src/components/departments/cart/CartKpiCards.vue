<script setup lang="ts">
// KPIs de resumen para la Unidad de Cartografía
</script>

<template>
  <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3.5">
    <!-- Vectorización Comunal -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Vectorización Comunal</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          97.99% Meta
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          195 / 199
        </span>
        <span class="text-xs font-semibold text-steel">circuitos</span>
      </div>
      <span class="text-xs font-normal text-steel">Solo 4 circuitos en proceso de cierre</span>
    </div>

    <!-- Consejos Georreferenciados -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Consejos Georreferenciados</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          Base Territorial
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          1,361
        </span>
        <span class="text-xs font-semibold text-steel">consejos</span>
      </div>
      <span class="text-xs font-normal text-steel">100% integrados al marco cartográfico IGVSB</span>
    </div>

    <!-- Cierre Pleno al 100% -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Cierre Pleno al 100%</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          88.9% Total
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          177
        </span>
        <span class="text-xs font-semibold text-steel">circuitos plenos</span>
      </div>
      <span class="text-xs font-normal text-steel">18 parciales con avance entre 33% y 93%</span>
    </div>

    <!-- Cobertura Municipal -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Cobertura Municipal</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          13 / 13
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          100%
        </span>
        <span class="text-xs font-semibold text-steel">Monagas</span>
      </div>
      <span class="text-xs font-normal text-steel">Totalidad de municipios con cartografía activa</span>
    </div>
  </div>
</template>
