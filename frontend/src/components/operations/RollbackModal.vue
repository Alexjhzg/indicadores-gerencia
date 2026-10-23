<script setup lang="ts">
import type { MeasurementRow } from './MeasurementsAuditTable.vue';

defineProps<{
  show: boolean;
  selectedMeasurement: MeasurementRow | null;
  isSubmitting: boolean;
}>();

const rollbackVersion = defineModel<number>('rollbackVersion', { default: 1 });
const rollbackReason = defineModel<string>('rollbackReason', { default: '' });

const emit = defineEmits<{
  (e: 'close'): void;
  (e: 'confirm'): void;
}>();
</script>

<template>
  <div v-if="show" class="fixed inset-0 bg-black/40 flex items-center justify-center z-50 p-4">
    <div class="bg-white border border-ash rounded-[3px] max-w-lg w-full p-6 relative flex flex-col gap-5">
      <div class="absolute top-0 left-0 right-0 h-[2px] bg-signal-blue rounded-t-[3px]"></div>

      <div>
        <h3 class="text-lg font-semibold text-ink-black">Reversión de Versión (Rollback Atómico)</h3>
        <p class="text-xs font-medium text-steel mt-1">
          Restaura los valores históricos certificados sin perder la trazabilidad de auditoría.
        </p>
      </div>

      <div class="p-3 bg-mist rounded-[3px] text-xs flex flex-col gap-0.5">
        <span class="font-semibold text-steel">Indicador seleccionado:</span>
        <span class="font-semibold text-ink-black">{{ selectedMeasurement?.indicador_codigo }} — {{ selectedMeasurement?.indicador_nombre }}</span>
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-xs font-semibold text-steel">Versión Destino para Restaurar:</label>
        <input
          v-model.number="rollbackVersion"
          type="number"
          min="1"
          class="w-full bg-white border-[1.5px] border-ash rounded-[3px] px-3.5 py-2 text-sm font-medium text-ink-black outline-none focus:border-signal-blue"
        />
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-xs font-semibold text-steel">Motivo de Reversión (Obligatorio para Auditoría):</label>
        <textarea
          v-model="rollbackReason"
          rows="3"
          class="w-full bg-white border-[1.5px] border-ash rounded-[3px] p-3 text-sm font-medium text-ink-black outline-none focus:border-signal-blue resize-none"
          placeholder="Indique la justificación técnica..."
        ></textarea>
      </div>

      <div class="flex flex-col sm:flex-row justify-end gap-2.5 pt-3 border-t border-ash">
        <button
          type="button"
          class="px-4 py-2 text-xs font-semibold bg-mist text-ink-black rounded-[3px] hover:bg-black/10 transition-colors border-none cursor-pointer"
          @click="emit('close')"
        >
          Cancelar
        </button>
        <button
          type="button"
          class="px-4 py-2 text-xs font-semibold bg-signal-blue text-white rounded-[3px] hover:opacity-90 transition-opacity border-none cursor-pointer disabled:opacity-60"
          :disabled="isSubmitting"
          @click="emit('confirm')"
        >
          <span v-if="!isSubmitting">EJECUTAR REVERSIÓN A V.{{ rollbackVersion }}</span>
          <span v-else>PROCESANDO...</span>
        </button>
      </div>
    </div>
  </div>
</template>
