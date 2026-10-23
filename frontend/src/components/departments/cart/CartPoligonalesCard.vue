<script setup lang="ts">
import { Compass } from 'lucide-vue-next';
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <Compass :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Estado de Validación Vectorial
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Completitud de poligonales cartográficas cerradas en Monagas
      </p>
    </div>

    <div class="flex flex-col gap-4 my-4">
      <!-- Circuito 100% Pleno -->
      <div class="flex flex-col gap-1">
        <div class="flex items-center justify-between text-xs font-semibold">
          <span class="text-ink-black">100% Vectorizado (Pleno)</span>
          <span class="text-signal-blue font-mono">177 Circuitos (88.9%)</span>
        </div>
        <div class="w-full h-3 bg-mist rounded-sm overflow-hidden">
          <div class="h-full bg-signal-blue" style="width: 88.9%"></div>
        </div>
      </div>

      <!-- Circuito Parcial -->
      <div class="flex flex-col gap-1">
        <div class="flex items-center justify-between text-xs font-semibold">
          <span class="text-ink-black">Avance Parcial (33% - 93%)</span>
          <span class="text-steel font-mono">18 Circuitos (9.0%)</span>
        </div>
        <div class="w-full h-3 bg-mist rounded-sm overflow-hidden">
          <div class="h-full bg-steel" style="width: 9.0%"></div>
        </div>
      </div>

      <!-- Pendiente -->
      <div class="flex flex-col gap-1">
        <div class="flex items-center justify-between text-xs font-semibold">
          <span class="text-ink-black">Pendiente por Iniciar</span>
          <span class="text-steel font-mono">4 Circuitos (2.0%)</span>
        </div>
        <div class="w-full h-3 bg-mist rounded-sm overflow-hidden">
          <div class="h-full bg-ash" style="width: 2.0%"></div>
        </div>
      </div>
    </div>

    <div class="flex items-center justify-between pt-3 border-t border-mist text-xs">
      <span class="text-steel font-medium">Total Circuitos Electorales:</span>
      <span class="text-ink-black font-semibold">199 Circuitos Comunales</span>
    </div>
  </div>
</template>
