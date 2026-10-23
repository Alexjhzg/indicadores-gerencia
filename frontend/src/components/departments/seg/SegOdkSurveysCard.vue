<script setup lang="ts">
import { FileCheck2 } from 'lucide-vue-next';

export interface OdkSurveyItem {
  tipo: string;
  cantidad: number;
  porcentaje: string;
  meta: string;
}

defineProps<{
  mesNombre: string;
  encuestas: OdkSurveyItem[];
}>();
</script>

<template>
  <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
    <div class="flex items-start justify-between mb-3">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <FileCheck2 :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
          <h3 class="text-base font-semibold text-ink-black">
            Captura Digital por Investigación
          </h3>
        </div>
        <p class="text-xs font-normal text-steel">
          Volumen de cuestionarios electrónicos capturados en la plataforma SEGEN en {{ mesNombre }}
        </p>
      </div>
      <span class="text-xs font-semibold px-2 py-0.5 bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px]">
        Superó Meta (25k)
      </span>
    </div>

    <div class="flex flex-col gap-3 my-2">
      <div
        v-for="enc in encuestas"
        :key="enc.tipo"
        class="flex flex-col gap-1 text-xs"
      >
        <div class="flex items-center justify-between font-semibold">
          <span class="text-ink-black truncate max-w-[280px]">{{ enc.tipo }}</span>
          <div class="flex items-center gap-2 shrink-0">
            <span class="text-ink-black">{{ enc.cantidad.toLocaleString() }}</span>
            <span class="text-signal-blue font-mono text-[11px]">({{ enc.porcentaje }})</span>
          </div>
        </div>
        <div class="w-full h-2 bg-mist rounded-xs overflow-hidden">
          <div
            class="h-full bg-signal-blue"
            :style="{ width: enc.porcentaje }"
          ></div>
        </div>
      </div>
    </div>

    <div class="flex items-center justify-between pt-3 border-t border-mist text-xs text-steel font-medium">
      <span>Fuerza Territorial Activa: <strong class="text-ink-black">208 funcionarios</strong> (99.0% despliegue)</span>
      <span class="text-signal-blue font-semibold">ODK Plataforma Operativa</span>
    </div>
  </div>
</template>
