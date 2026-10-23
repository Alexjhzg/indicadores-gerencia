<script setup lang="ts">
import { Cpu, CheckCircle2 } from 'lucide-vue-next';
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <Cpu :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <h3 class="text-base font-semibold text-ink-black">
          Digitalización y Flujo Informático de Boletas
        </h3>
      </div>
      <p class="text-xs font-normal text-steel">
        Control de digitación y estado de transcripción sin rezago en el sistema
      </p>
    </div>

    <div class="flex flex-col gap-4 my-3">
      <!-- Barra de digitalización -->
      <div class="flex flex-col gap-1.5">
        <div class="flex items-center justify-between text-xs font-semibold">
          <span class="text-ink-black">Boletas Transcritas en Sistema</span>
          <span class="text-signal-blue font-mono">11,023 / 11,615 (94.90%)</span>
        </div>
        <div class="w-full h-3 bg-mist rounded-sm overflow-hidden">
          <div class="h-full bg-signal-blue" style="width: 94.9%"></div>
        </div>
        <div class="flex justify-between text-[11px] text-steel">
          <span>Meta operativa: 100.0%</span>
          <span class="font-semibold text-ink-black">592 boletas en flujo regular</span>
        </div>
      </div>

      <!-- Estructura de Nupcialidad -->
      <div class="border border-mist rounded-[3px] p-3.5 flex flex-col gap-2 bg-mist/30">
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold text-ink-black">Desglose de Nupcialidad (1,339 Actos)</span>
          <span class="text-xs font-semibold text-signal-blue">Agosto 2026</span>
        </div>
        <div class="grid grid-cols-2 gap-3 pt-1">
          <div class="flex flex-col">
            <span class="text-[11px] text-steel font-medium">Matrimonios Civiles:</span>
            <span class="text-sm font-semibold text-ink-black">790 actos (59.0%)</span>
          </div>
          <div class="flex flex-col">
            <span class="text-[11px] text-steel font-medium">Uniones Estables de Hecho:</span>
            <span class="text-sm font-semibold text-ink-black">549 actos (41.0%)</span>
          </div>
        </div>
      </div>
    </div>

    <div class="flex items-center gap-2 text-xs font-semibold text-signal-blue pt-3 border-t border-mist">
      <CheckCircle2 :size="15" :stroke-width="1.5" class="shrink-0" />
      <span>Mesa Técnica Interinstitucional con CNE y Salud Activa</span>
    </div>
  </div>
</template>
