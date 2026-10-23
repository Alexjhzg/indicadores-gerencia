<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useIndicatorsStore } from '@/stores/indicators';
import api from '@/api/client';
import { CheckCircle2, AlertTriangle } from 'lucide-vue-next';
import OperationsHeader from '@/components/operations/OperationsHeader.vue';
import UnitUploadWorkspace from '@/components/operations/UnitUploadWorkspace.vue';
import MeasurementsAuditTable, { type MeasurementRow } from '@/components/operations/MeasurementsAuditTable.vue';
import RollbackModal from '@/components/operations/RollbackModal.vue';

const indicatorsStore = useIndicatorsStore();

const activeTab = ref<'UPLOAD' | 'AUDIT'>('UPLOAD');

const showRollbackModal = ref(false);
const selectedMeasurement = ref<MeasurementRow | null>(null);
const rollbackVersion = ref<number>(1);
const rollbackReason = ref('');
const isSubmitting = ref(false);
const message = ref<{ type: 'success' | 'error'; text: string } | null>(null);

onMounted(async () => {
  await Promise.all([
    indicatorsStore.fetchIndicators(),
    indicatorsStore.fetchMeasurements(),
    indicatorsStore.fetchMunicipalities(),
  ]);
});

const measurements = computed<MeasurementRow[]>(() => indicatorsStore.measurements);

const onDataUpdated = async () => {
  await indicatorsStore.fetchMeasurements();
};

const openRollbackDialog = (m: MeasurementRow) => {
  selectedMeasurement.value = m;
  rollbackVersion.value = Math.max(1, (m.version || 2) - 1);
  rollbackReason.value = 'Corrección técnica autorizada por la Gerencia Estadal.';
  showRollbackModal.value = true;
};

const executeRollback = async () => {
  if (!selectedMeasurement.value) return;
  isSubmitting.value = true;
  message.value = null;

  try {
    await api.post(`/mediciones/${selectedMeasurement.value.id}/rollback`, {
      version_destino: rollbackVersion.value,
      motivo_rollback: rollbackReason.value,
    });

    message.value = {
      type: 'success',
      text: `Reversión exitosa a la Versión ${rollbackVersion.value}. Auditoría inmutable registrada.`,
    };
    showRollbackModal.value = false;
    await indicatorsStore.fetchMeasurements();
  } catch (err: any) {
    message.value = {
      type: 'error',
      text: err.response?.data?.detail || 'Error al ejecutar la reversión.',
    };
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <div class="py-10 max-md:py-5 pb-20">
    <div class="max-w-[1440px] mx-auto px-10 max-md:px-4 flex flex-col gap-8 max-md:gap-5">
      
      <!-- Cabecera Operativa con Selector de Pestañas -->
      <OperationsHeader
        :active-tab="activeTab"
        @change-tab="activeTab = $event"
      />

      <!-- Banner de Notificación -->
      <div
        v-if="message"
        class="flex items-center gap-2 p-3.5 rounded-[3px] text-sm font-medium"
        :class="
          message.type === 'success'
            ? 'bg-signal-blue/10 text-signal-blue border border-signal-blue/20'
            : 'bg-red-50 text-red-700 border border-red-200'
        "
      >
        <CheckCircle2 v-if="message.type === 'success'" :size="16" :stroke-width="1.5" class="shrink-0" />
        <AlertTriangle v-else :size="16" :stroke-width="1.5" class="shrink-0" />
        <span>{{ message.text }}</span>
      </div>

      <!-- PESTAÑA 1: Espacio de Carga de Datos por Unidad (Formularios y Excel) -->
      <div v-show="activeTab === 'UPLOAD'">
        <UnitUploadWorkspace @data-updated="onDataUpdated" />
      </div>

      <!-- PESTAÑA 2: Tabla de Mediciones y Auditoría de Versiones Inmutables -->
      <div v-show="activeTab === 'AUDIT'">
        <MeasurementsAuditTable
          :measurements="measurements"
          @rollback="openRollbackDialog"
        />
      </div>

      <!-- Modal de Rollback Atómico -->
      <RollbackModal
        v-model:rollback-version="rollbackVersion"
        v-model:rollback-reason="rollbackReason"
        :show="showRollbackModal"
        :selected-measurement="selectedMeasurement"
        :is-submitting="isSubmitting"
        @close="showRollbackModal = false"
        @confirm="executeRollback"
      />

    </div>
  </div>
</template>
