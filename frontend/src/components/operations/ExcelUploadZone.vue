<script setup lang="ts">
import { ref } from 'vue';
import type { DepartamentoId } from '@/types';
import { downloadUnitExcelTemplate } from '@/utils/excelTemplates';
import { parseUnitExcelFile, type ExcelParseResult, type ParsedBatchItem } from '@/utils/excelParser';
import {
  FileSpreadsheet,
  Download,
  UploadCloud,
  CheckCircle2,
  AlertTriangle,
  XCircle,
  FileCheck,
  RefreshCw,
} from 'lucide-vue-next';

const props = defineProps<{
  deptCode: DepartamentoId;
  deptName: string;
  selectedMesNombre: string;
  anio: number;
  isSubmitting: boolean;
}>();

const emit = defineEmits<{
  (e: 'submitBatch', payload: {
    mediciones: Array<{ indicador_codigo: string; valor_registrado: number; meta_periodo: number; observaciones: string }>;
    motivo: string;
  }): void;
}>();

const isDragging = ref(false);
const isParsing = ref(false);
const selectedFile = ref<File | null>(null);
const parseResult = ref<ExcelParseResult | null>(null);
const motivoUpload = ref('');

const handleDownloadTemplate = () => {
  downloadUnitExcelTemplate(props.deptCode, props.selectedMesNombre, props.anio);
};

const processFile = async (file: File) => {
  if (!file.name.endsWith('.xlsx') && !file.name.endsWith('.xls')) {
    alert('Por favor selecciona un archivo con formato Excel (.xlsx o .xls).');
    return;
  }

  selectedFile.value = file;
  isParsing.value = true;
  motivoUpload.value = `Carga masiva vía Excel (${file.name}) · ${props.selectedMesNombre} ${props.anio}`;

  try {
    const res = await parseUnitExcelFile(file, props.deptCode);
    parseResult.value = res;
  } catch (err) {
    console.error('Error al parsear Excel:', err);
  } finally {
    isParsing.value = false;
  }
};

const onFileInputChange = (e: Event) => {
  const target = e.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    processFile(target.files[0]);
  }
};

const onDrop = (e: DragEvent) => {
  isDragging.value = false;
  if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files.length > 0) {
    processFile(e.dataTransfer.files[0]);
  }
};

const resetFile = () => {
  selectedFile.value = null;
  parseResult.value = null;
  motivoUpload.value = '';
};

const onValueChange = (item: ParsedBatchItem) => {
  if (isNaN(item.valor_registrado) || item.valor_registrado === null) {
    item.isValid = false;
    item.error = 'El valor numérico no es válido.';
  } else if (item.valor_registrado < 0) {
    item.isValid = false;
    item.error = 'El valor no puede ser negativo.';
  } else {
    item.isValid = true;
    item.error = undefined;
  }

  // Recalcular contador de válidos
  if (parseResult.value) {
    parseResult.value.validRows = parseResult.value.items.filter((i) => i.isValid).length;
    parseResult.value.success = parseResult.value.validRows > 0;
  }
};

const getCumplimientoPct = (item: ParsedBatchItem): number => {
  if (!item.meta_periodo || item.meta_periodo <= 0) return 100;
  return Math.round((Number(item.valor_registrado || 0) / item.meta_periodo) * 100);
};

const handleConfirmBatch = () => {
  if (!parseResult.value || !parseResult.value.success) return;

  const validItems = parseResult.value.items
    .filter((item) => item.isValid)
    .map((item) => ({
      indicador_codigo: item.indicador_codigo,
      valor_registrado: Number(item.valor_registrado),
      meta_periodo: Number(item.meta_periodo),
      observaciones: item.observaciones,
    }));

  emit('submitBatch', {
    mediciones: validItems,
    motivo: motivoUpload.value || `Importación masiva Excel ${props.deptCode}`,
  });
};
</script>

<template>
  <div class="flex flex-col gap-6">
    <!-- Barra superior de descarga de plantilla -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between p-4 bg-mist/40 border border-ash rounded-[3px] gap-3">
      <div class="flex items-center gap-3">
        <FileSpreadsheet :size="24" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <div>
          <h4 class="text-sm font-semibold text-ink-black">
            Plantilla Oficial de Carga Excel: {{ deptName }}
          </h4>
          <p class="text-xs text-steel">
            Descarga el formato estandarizado con los indicadores y metas oficiales de {{ selectedMesNombre }} {{ anio }}
          </p>
        </div>
      </div>

      <button
        type="button"
        class="inline-flex items-center justify-center gap-2 px-3.5 py-2 bg-white text-ink-black border border-ash rounded-[3px] text-xs font-semibold hover:border-ink-black transition-colors cursor-pointer shrink-0"
        @click="handleDownloadTemplate"
      >
        <Download :size="14" :stroke-width="1.5" />
        <span>Descargar Plantilla (.xlsx)</span>
      </button>
    </div>

    <!-- Zona Drag & Drop cuando no hay archivo seleccionado -->
    <div
      v-if="!selectedFile"
      class="border-2 border-dashed rounded-[3px] p-8 text-center flex flex-col items-center justify-center gap-3 transition-colors cursor-pointer"
      :class="isDragging ? 'border-signal-blue bg-signal-blue/5' : 'border-ash hover:border-steel bg-white'"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="onDrop"
      @click="($refs.fileInput as HTMLInputElement)?.click()"
    >
      <input
        ref="fileInput"
        type="file"
        accept=".xlsx, .xls"
        class="hidden"
        @change="onFileInputChange"
      />

      <div class="w-12 h-12 rounded-[3px] bg-mist flex items-center justify-center text-steel">
        <UploadCloud :size="24" :stroke-width="1.5" />
      </div>

      <div>
        <p class="text-sm font-semibold text-ink-black">
          Arrastra y suelta tu archivo Excel (.xlsx) aquí, o haz clic para examinar
        </p>
        <p class="text-xs text-steel mt-1">
          El sistema validará automáticamente la correspondencia de códigos y consistencia de cifras
        </p>
      </div>

      <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-mist text-steel text-xs font-medium rounded-[3px]">
        Soporta archivos generados con la plantilla oficial (.xlsx)
      </span>
    </div>

    <!-- Panel de Previsualización cuando ya hay archivo cargado -->
    <div v-else class="flex flex-col gap-5">
      <!-- Ficha del archivo cargado -->
      <div class="flex items-center justify-between p-3.5 bg-white border border-ash rounded-[3px]">
        <div class="flex items-center gap-2.5">
          <FileCheck :size="20" :stroke-width="1.5" class="text-signal-blue shrink-0" />
          <div>
            <span class="text-xs font-semibold text-ink-black">{{ selectedFile.name }}</span>
            <span class="text-[11px] text-steel ml-2">({{ Math.round(selectedFile.size / 1024) }} KB)</span>
          </div>
        </div>

        <button
          type="button"
          class="inline-flex items-center gap-1.5 text-xs text-steel hover:text-ink-black transition-colors bg-transparent border-none cursor-pointer"
          @click="resetFile"
        >
          <RefreshCw :size="13" :stroke-width="1.5" />
          <span>Cambiar archivo</span>
        </button>
      </div>

      <!-- Alertas de Validación -->
      <div v-if="parseResult">
        <!-- Errores críticos -->
        <div
          v-if="parseResult.errors.length > 0"
          class="p-3.5 rounded-[3px] bg-red-50 text-red-700 border border-red-200 text-xs font-medium flex flex-col gap-1 mb-3"
        >
          <div class="flex items-center gap-1.5 font-semibold">
            <XCircle :size="15" :stroke-width="1.5" />
            <span>Se encontraron errores que impiden la carga:</span>
          </div>
          <ul class="list-disc pl-5 space-y-0.5">
            <li v-for="(err, idx) in parseResult.errors" :key="idx">{{ err }}</li>
          </ul>
        </div>

        <!-- Advertencias -->
        <div
          v-if="parseResult.warnings.length > 0"
          class="p-3.5 rounded-[3px] bg-amber-50 text-amber-800 border border-amber-200 text-xs font-medium flex flex-col gap-1 mb-3"
        >
          <div class="flex items-center gap-1.5 font-semibold">
            <AlertTriangle :size="15" :stroke-width="1.5" />
            <span>Advertencias de consistencia:</span>
          </div>
          <ul class="list-disc pl-5 space-y-0.5">
            <li v-for="(warn, idx) in parseResult.warnings" :key="idx">{{ warn }}</li>
          </ul>
        </div>
      </div>

      <!-- Tabla de Previsualización y Edición de Filas -->
      <div v-if="parseResult && parseResult.items.length > 0" class="overflow-x-auto border border-ash rounded-[3px]">
        <table class="w-full border-collapse text-left text-xs">
          <thead>
            <tr class="bg-mist/50 border-b border-ash font-semibold text-steel">
              <th class="py-2.5 px-3">CÓDIGO</th>
              <th class="py-2.5 px-3">INDICADOR</th>
              <th class="py-2.5 px-3">UNIDAD</th>
              <th class="py-2.5 px-3">META</th>
              <th class="py-2.5 px-3 w-[160px]">VALOR REPORTADO</th>
              <th class="py-2.5 px-3">CUMPLIMIENTO</th>
              <th class="py-2.5 px-3">ESTATUS</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-mist">
            <tr
              v-for="item in parseResult.items"
              :key="item.indicador_codigo"
              class="hover:bg-black/[0.01]"
              :class="!item.isValid ? 'bg-red-50/50' : ''"
            >
              <td class="py-2 px-3 font-mono font-semibold text-ink-black">{{ item.indicador_codigo }}</td>
              <td class="py-2 px-3 font-medium text-ink-black max-w-[260px] truncate" :title="item.indicador_nombre">
                {{ item.indicador_nombre }}
              </td>
              <td class="py-2 px-3 text-steel">{{ item.unidad_medida }}</td>
              <td class="py-2 px-3 font-medium text-steel">{{ item.meta_periodo.toLocaleString() }}</td>
              
              <!-- Input editable para verificar o ajustar el número -->
              <td class="py-1 px-3">
                <input
                  v-model.number="item.valor_registrado"
                  type="number"
                  step="any"
                  min="0"
                  class="w-full px-2 py-1 text-xs font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
                  @input="onValueChange(item)"
                />
              </td>

              <!-- Porcentaje de Cumplimiento Calculado -->
              <td class="py-2 px-3">
                <span
                  class="inline-flex items-center px-1.5 py-0.5 rounded-[3px] text-[11px] font-semibold"
                  :class="
                    getCumplimientoPct(item) >= 100
                      ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                      : getCumplimientoPct(item) >= 80
                      ? 'bg-amber-50 text-amber-800 border border-amber-200'
                      : 'bg-signal-blue/10 text-signal-blue border border-signal-blue/20'
                  "
                >
                  {{ getCumplimientoPct(item) }}%
                </span>
              </td>

              <td class="py-2 px-3">
                <span
                  v-if="item.isValid"
                  class="inline-flex items-center gap-1 px-1.5 py-0.5 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-[3px] text-[11px] font-semibold"
                >
                  <CheckCircle2 :size="12" :stroke-width="1.5" />
                  <span>Válido</span>
                </span>
                <span
                  v-else
                  class="inline-flex items-center gap-1 px-1.5 py-0.5 bg-red-100 text-red-800 border border-red-300 rounded-[3px] text-[11px] font-semibold"
                  :title="item.error"
                >
                  <XCircle :size="12" :stroke-width="1.5" />
                  <span>{{ item.error || 'Inválido' }}</span>
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Justificación de la importación -->
      <div class="flex flex-col gap-1.5">
        <label class="text-xs font-semibold text-ink-black">
          Justificación Técnica de la Carga Masiva:
        </label>
        <input
          v-model="motivoUpload"
          type="text"
          class="w-full px-3 py-2 text-sm text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
        />
      </div>

      <!-- Acciones de confirmación -->
      <div class="flex items-center justify-end gap-3 pt-2">
        <button
          type="button"
          class="px-4 py-2 text-xs font-semibold text-steel hover:text-ink-black bg-transparent border-none cursor-pointer"
          @click="resetFile"
        >
          Cancelar
        </button>

        <button
          type="button"
          :disabled="!parseResult || !parseResult.success || isSubmitting"
          class="inline-flex items-center gap-2 px-5 py-2.5 bg-signal-blue text-white rounded-[3px] text-sm font-semibold hover:opacity-90 transition-opacity cursor-pointer border-none disabled:opacity-50"
          @click="handleConfirmBatch"
        >
          <CheckCircle2 :size="16" :stroke-width="1.5" />
          <span>{{ isSubmitting ? 'Registrando en BD...' : `Confirmar y Cargar ${parseResult?.validRows || 0} Cifras en la BD` }}</span>
        </button>
      </div>
    </div>
  </div>
</template>
