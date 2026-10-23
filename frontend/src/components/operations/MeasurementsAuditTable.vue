<script setup lang="ts">
import { RotateCcw } from 'lucide-vue-next';

export interface MeasurementRow {
  id: string;
  indicador_codigo: string;
  indicador_nombre: string;
  municipio_nombre?: string;
  valor_registrado: string | number;
  meta_periodo?: string | number | null;
  porcentaje_cumplimiento?: number | null;
  version: number;
  estado: string;
}

defineProps<{
  measurements: MeasurementRow[];
}>();

const emit = defineEmits<{
  (e: 'rollback', item: MeasurementRow): void;
}>();
</script>

<template>
  <section class="bg-white border border-ash rounded-[3px] p-5 flex flex-col gap-4">
    <div class="flex items-center justify-between">
      <h3 class="text-base font-semibold text-ink-black">Mediciones Registradas en Sistema (Agosto 2026)</h3>
      <span class="text-xs font-semibold text-steel">{{ measurements.length }} Registros</span>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full border-collapse text-left text-[15px]">
        <thead>
          <tr class="border-b-[1.5px] border-ash text-xs font-semibold text-steel">
            <th class="py-3 px-3">CÓDIGO</th>
            <th class="py-3 px-3">INDICADOR</th>
            <th class="py-3 px-3">MUNICIPIO</th>
            <th class="py-3 px-3">VALOR REGISTRADO</th>
            <th class="py-3 px-3">META</th>
            <th class="py-3 px-3">CUMPLIMIENTO</th>
            <th class="py-3 px-3">VERSIÓN</th>
            <th class="py-3 px-3">ESTADO</th>
            <th class="py-3 px-3">AUDITORÍA</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-mist">
          <tr v-for="m in measurements" :key="m.id" class="hover:bg-black/[0.02] transition-colors">
            <td class="py-3 px-3 font-mono text-xs font-semibold text-ink-black">
              {{ m.indicador_codigo }}
            </td>
            <td class="py-3 px-3 font-medium text-ink-black max-w-[320px]">
              {{ m.indicador_nombre }}
            </td>
            <td class="py-3 px-3 text-xs text-steel">
              {{ m.municipio_nombre || 'Estadal' }}
            </td>
            <td class="py-3 px-3 font-semibold text-ink-black tabular-nums">
              {{ m.valor_registrado }}
            </td>
            <td class="py-3 px-3 font-medium text-steel tabular-nums">
              {{ m.meta_periodo ?? '—' }}
            </td>
            <td class="py-3 px-3">
              <span class="inline-flex items-center px-2 py-0.5 text-xs font-semibold bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px]">
                {{ m.porcentaje_cumplimiento ? `${m.porcentaje_cumplimiento}%` : '100%' }}
              </span>
            </td>
            <td class="py-3 px-3">
              <span class="inline-flex items-center px-2 py-0.5 text-xs font-semibold bg-mist text-ink-black rounded-[3px]">
                V.{{ m.version }}
              </span>
            </td>
            <td class="py-3 px-3">
              <span class="inline-flex items-center px-2 py-0.5 text-xs font-semibold bg-mist text-ink-black rounded-[3px]">
                {{ m.estado }}
              </span>
            </td>
            <td class="py-3 px-3">
              <button
                type="button"
                class="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold text-ink-black border border-ash rounded-[3px] hover:border-signal-blue hover:text-signal-blue transition-colors cursor-pointer bg-white"
                title="Reversión atómica segura"
                @click="emit('rollback', m)"
              >
                <RotateCcw :size="13" :stroke-width="1.5" class="shrink-0" />
                <span>Rollback</span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>
