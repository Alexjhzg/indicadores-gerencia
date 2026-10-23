<script setup lang="ts">
// KPIs de resumen para la Unidad de Demografía y Población
</script>

<template>
  <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3.5">
    <!-- Boletas Recolectadas -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Boletas Recolectadas</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          Año 2026
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          11,615
        </span>
        <span class="text-xs font-semibold text-steel">boletas</span>
      </div>
      <span class="text-xs font-normal text-steel">Meta anual de recolección: 25,000 boletas</span>
    </div>

    <!-- Nacimientos Oficiales -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Nacimientos Oficiales</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          60.0% Muestra
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          6,972
        </span>
        <span class="text-xs font-semibold text-steel">recién nacidos</span>
      </div>
      <span class="text-xs font-normal text-steel">Captura continua en hospitales y registros</span>
    </div>

    <!-- Defunciones -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Defunciones</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
          Mortalidad
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          1,987
        </span>
        <span class="text-xs font-semibold text-steel">actas</span>
      </div>
      <span class="text-xs font-normal text-steel">Monitoreo de causas y codificación médica</span>
    </div>

    <!-- Tasa de Digitalización -->
    <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
      <div class="flex items-center justify-between">
        <span class="text-xs font-semibold tracking-wider text-steel uppercase">Tasa de Digitalización</span>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
          Sin Rezago
        </span>
      </div>
      <div class="flex items-baseline gap-2">
        <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
          94.90%
        </span>
        <span class="text-xs font-semibold text-steel">transcrito</span>
      </div>
      <span class="text-xs font-normal text-steel">11,023 boletas procesadas en sistema</span>
    </div>
  </div>
</template>
