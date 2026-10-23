<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue';
import type { DepartamentoId } from '@/types';
import { useAuthStore } from '@/stores/auth';
import api from '@/api/client';
import {
  Layers,
  Calendar,
  CheckCircle2,
  FileSpreadsheet,
  Edit3,
  Award,
  AlertTriangle,
  Clock,
} from 'lucide-vue-next';

import EcoUploadForm from './forms/EcoUploadForm.vue';
import SocUploadForm from './forms/SocUploadForm.vue';
import DemUploadForm from './forms/DemUploadForm.vue';
import CartUploadForm from './forms/CartUploadForm.vue';
import SegUploadForm from './forms/SegUploadForm.vue';
import SeemUploadForm from './forms/SeemUploadForm.vue';
import ExcelUploadZone from './ExcelUploadZone.vue';

const authStore = useAuthStore();

const emit = defineEmits<{
  (e: 'dataUpdated'): void;
}>();

const deptConfig: Record<DepartamentoId, {
  name: string;
  shortName: string;
  chief: string;
  colorClass: string;
  badgeClass: string;
}> = {
  ECO: {
    name: 'Unidad de Estadísticas Económicas',
    shortName: 'Estadísticas Económicas',
    chief: 'Wilfredo Rojas (Jefe de Unidad)',
    colorClass: 'text-dept-eco',
    badgeClass: 'bg-dept-eco text-white',
  },
  SOC: {
    name: 'Unidad de Estadísticas Sociales',
    shortName: 'Estadísticas Sociales',
    chief: 'Rubén Alejandro (Jefe de Unidad)',
    colorClass: 'text-dept-soc',
    badgeClass: 'bg-dept-soc text-white',
  },
  DEM: {
    name: 'Unidad de Demografía y Población',
    shortName: 'Demografía y Población',
    chief: 'Cledys Bastardo (Jefa de Unidad)',
    colorClass: 'text-dept-dem',
    badgeClass: 'bg-dept-dem text-white',
  },
  CART: {
    name: 'Unidad de Cartografía',
    shortName: 'Cartografía',
    chief: 'Henri Guevara (Jefe de Unidad)',
    colorClass: 'text-dept-cart',
    badgeClass: 'bg-dept-cart text-white',
  },
  SEG: {
    name: 'Unidad de SEGEN',
    shortName: 'SEGEN',
    chief: 'Johana Larez (Jefa de Unidad)',
    colorClass: 'text-dept-seg',
    badgeClass: 'bg-dept-seg text-white',
  },
  SEEM: {
    name: 'Coordinación de SEEM',
    shortName: 'Coordinación SEEM',
    chief: 'Luis Velásquez (Coordinador)',
    colorClass: 'text-teal-700',
    badgeClass: 'bg-teal-700 text-white',
  },
};

interface PeriodoDisponible {
  anio: number;
  mes: number;
  mes_nombre: string;
  total_mediciones: number;
}

// Unidades permitidas para el usuario actual
const availableDepts = computed<DepartamentoId[]>(() => {
  return authStore.allowedDepts.length > 0
    ? authStore.allowedDepts
    : (['ECO', 'SOC', 'DEM', 'CART', 'SEG', 'SEEM'] as DepartamentoId[]);
});

// Bloqueado a una única unidad si es Encargado individual
const isSingleUnitLocked = computed(() => {
  return authStore.isEncargado && availableDepts.value.length === 1;
});

const selectedDept = ref<DepartamentoId>('CART');

// Períodos cargados dinámicamente desde la BD
const availablePeriods = ref<PeriodoDisponible[]>([]);
const availableYears = ref<number[]>([2026]);

// Meses que efectivamente tienen datos en la BD para el año seleccionado
const availableMonths = computed(() => {
  const filtered = availablePeriods.value
    .filter((p) => p.anio === selectedAnio.value)
    .map((p) => ({ num: p.mes, nombre: p.mes_nombre }));

  if (filtered.length === 0 && availablePeriods.value.length > 0) {
    return availablePeriods.value.map((p) => ({ num: p.mes, nombre: p.mes_nombre }));
  }
  return filtered.length > 0 ? filtered : [{ num: 8, nombre: 'Agosto' }];
});

// Período activo
const selectedMesNum = ref(8);
const selectedAnio = ref(2026);

const selectedMesNombre = computed(() => {
  const m = availableMonths.value.find((item) => item.num === selectedMesNum.value);
  return m ? m.nombre : 'Agosto';
});

// Modalidad de carga: 'EXCEL' o 'FORM' (Por defecto Excel para facilitar la carga al usuario)
const uploadMode = ref<'EXCEL' | 'FORM'>('EXCEL');

// Estado de la carga y datos remotos
const isSubmitting = ref(false);
const isLoadingUnitData = ref(false);
const currentUnitData = ref<any>(null);
const feedbackMessage = ref<{ type: 'success' | 'error'; text: string } | null>(null);

// Obtener períodos disponibles con datos reales en la BD para la unidad
const fetchAvailablePeriods = async () => {
  try {
    const res = await api.get('/mediciones/periodos-disponibles', {
      params: { departamento_codigo: selectedDept.value }
    });
    const data = res.data;
    availablePeriods.value = data.periodos || [];
    availableYears.value = (data.anios && data.anios.length > 0) ? data.anios : [2026];

    // Ajustar año si el actual no existe en los datos
    if (!availableYears.value.includes(selectedAnio.value)) {
      selectedAnio.value = availableYears.value[0];
    }

    // Ajustar mes si el actual no existe para este año
    const validMonths = availablePeriods.value
      .filter((p) => p.anio === selectedAnio.value)
      .map((p) => p.mes);

    if (validMonths.length > 0 && !validMonths.includes(selectedMesNum.value)) {
      selectedMesNum.value = validMonths[0];
    }
  } catch (err) {
    console.error('Error al cargar períodos disponibles:', err);
  }
};

const fetchCurrentUnitData = async () => {
  isLoadingUnitData.value = true;
  try {
    const res = await api.get(`/mediciones/unidad/${selectedDept.value}`, {
      params: {
        periodo_anio: selectedAnio.value,
        periodo_mes: selectedMesNum.value,
      },
    });
    currentUnitData.value = res.data;
  } catch (err) {
    console.error('Error al obtener datos de la unidad:', err);
  } finally {
    isLoadingUnitData.value = false;
  }
};

onMounted(async () => {
  if (availableDepts.value.length > 0) {
    selectedDept.value = availableDepts.value[0];
  }
  await fetchAvailablePeriods();
  await fetchCurrentUnitData();
});

watch(selectedDept, async () => {
  feedbackMessage.value = null;
  await fetchAvailablePeriods();
  await fetchCurrentUnitData();
});

watch(selectedAnio, (newYear) => {
  const validMonths = availablePeriods.value
    .filter((p) => p.anio === newYear)
    .map((p) => p.mes);
  if (validMonths.length > 0 && !validMonths.includes(selectedMesNum.value)) {
    selectedMesNum.value = validMonths[0];
  }
});

watch([selectedMesNum, selectedAnio], async () => {
  feedbackMessage.value = null;
  await fetchCurrentUnitData();
});

// Extraer mediciones iniciales existentes para rellenar el formulario
const initialFormData = computed(() => {
  if (!currentUnitData.value || !currentUnitData.value.items) return [];
  return currentUnitData.value.items.map((row: any) => ({
    codigo: row.indicador.codigo,
    valor: row.medicion ? row.medicion.valor_registrado : 0,
    meta: row.indicador.meta_referencial || 0,
  }));
});

// Guardar mediciones por Lote (usado tanto por Formulario como por Excel)
const handleBatchSubmit = async (payload: {
  mediciones: Array<{ indicador_codigo: string; valor_registrado: number; meta_periodo: number; observaciones?: string }>;
  motivo: string;
}) => {
  isSubmitting.value = true;
  feedbackMessage.value = null;

  try {
    const res = await api.post('/mediciones/lote', {
      departamento_codigo: selectedDept.value,
      periodo_anio: selectedAnio.value,
      periodo_mes: selectedMesNum.value,
      motivo_general: payload.motivo,
      mediciones: payload.mediciones,
    });

    feedbackMessage.value = {
      type: 'success',
      text: res.data.mensaje || `Se registraron exitosamente las cifras para ${deptConfig[selectedDept.value]?.name}.`,
    };

    await fetchAvailablePeriods();
    await fetchCurrentUnitData();
    emit('dataUpdated');
  } catch (err: any) {
    feedbackMessage.value = {
      type: 'error',
      text: err.response?.data?.detail || 'Error al guardar las mediciones en el servidor.',
    };
  } finally {
    isSubmitting.value = false;
  }
};

// Certificar el mes completo de la unidad
const handleCertifyUnit = async () => {
  if (!confirm(`¿Confirma la certificación oficial de todas las cifras de la ${deptConfig[selectedDept.value]?.name} para ${selectedMesNombre.value} ${selectedAnio.value}?`)) {
    return;
  }

  isSubmitting.value = true;
  feedbackMessage.value = null;

  try {
    const res = await api.post(`/mediciones/unidad/${selectedDept.value}/certificar`, null, {
      params: {
        periodo_anio: selectedAnio.value,
        periodo_mes: selectedMesNum.value,
      },
    });

    feedbackMessage.value = {
      type: 'success',
      text: res.data.mensaje || 'Cifras certificadas exitosamente como oficiales.',
    };

    await fetchCurrentUnitData();
    emit('dataUpdated');
  } catch (err: any) {
    feedbackMessage.value = {
      type: 'error',
      text: err.response?.data?.detail || 'No se pudo certificar las mediciones.',
    };
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <div class="flex flex-col gap-6">
    <!-- Barra de Configuración y Filtros: Unidad + Período -->
    <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <!-- Selector de Unidades Técnicas y Coordinación -->
      <div class="flex flex-col gap-2">
        <label class="text-xs font-semibold text-steel uppercase tracking-wider flex items-center gap-1.5">
          <Layers :size="14" :stroke-width="1.5" />
          <span>Unidad Técnica / Coordinación Asignada</span>
        </label>

        <!-- Selector interactivo para Gerente (todas) o Jefe de Área (sus 4 unidades) -->
        <div v-if="!isSingleUnitLocked" class="flex items-center gap-1.5 overflow-x-auto pb-1 max-w-full">
          <button
            v-for="code in availableDepts"
            :key="code"
            type="button"
            class="px-3 py-1.5 rounded-[3px] text-xs font-semibold transition-all cursor-pointer border-none shrink-0"
            :class="selectedDept === code ? (deptConfig[code]?.badgeClass) : 'bg-mist text-steel hover:text-ink-black'"
            @click="selectedDept = code"
          >
            {{ code }} · {{ deptConfig[code]?.shortName || deptConfig[code]?.name }}
          </button>
        </div>

        <!-- Indicador fijo para Jefe de Unidad (bloqueado a su unidad) -->
        <div v-else class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-[3px] text-xs font-semibold" :class="deptConfig[selectedDept]?.badgeClass">
            {{ selectedDept }}
          </span>
          <span class="text-sm font-semibold text-ink-black">
            {{ deptConfig[selectedDept]?.name }}
          </span>
          <span class="text-xs text-steel font-normal">
            (Acceso exclusivo autorizado: {{ authStore.userCedula }})
          </span>
        </div>
      </div>

      <!-- Selector de Período (Mes y Año) -->
      <div class="flex items-center gap-3 shrink-0">
        <div class="flex flex-col gap-1">
          <label class="text-xs font-semibold text-steel flex items-center gap-1">
            <Calendar :size="13" :stroke-width="1.5" />
            <span>Mes a Cargar</span>
          </label>
          <select
            v-model.number="selectedMesNum"
            class="px-3 py-1.5 text-xs font-semibold bg-white border border-ash rounded-[3px] text-ink-black focus:outline-none focus:border-signal-blue cursor-pointer"
          >
            <option v-for="m in availableMonths" :key="m.num" :value="m.num">
              {{ m.nombre }}
            </option>
          </select>
        </div>

        <div class="flex flex-col gap-1">
          <label class="text-xs font-semibold text-steel">Año</label>
          <select
            v-model.number="selectedAnio"
            class="px-3 py-1.5 text-xs font-semibold bg-white border border-ash rounded-[3px] text-ink-black focus:outline-none focus:border-signal-blue cursor-pointer"
          >
            <option v-for="y in availableYears" :key="y" :value="y">
              {{ y }}
            </option>
          </select>
        </div>
      </div>
    </div>

    <!-- Ficha de Estado de la Unidad en el Mes Seleccionado -->
    <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-[3px] bg-mist flex items-center justify-center shrink-0">
          <Award :size="24" :stroke-width="1.5" :class="deptConfig[selectedDept]?.colorClass" />
        </div>
        <div>
          <div class="flex items-center gap-2 mb-0.5">
            <h2 class="text-lg font-semibold text-ink-black">
              {{ deptConfig[selectedDept]?.name }}
            </h2>
            <!-- Badge de Estado General -->
            <span
              v-if="currentUnitData"
              class="inline-flex items-center gap-1 px-2 py-0.5 rounded-[3px] text-xs font-semibold border"
              :class="
                currentUnitData.estado_general === 'CERTIFICADO'
                  ? 'bg-emerald-50 text-emerald-700 border-emerald-200'
                  : currentUnitData.estado_general === 'BORRADOR'
                  ? 'bg-amber-50 text-amber-800 border-amber-200'
                  : 'bg-mist text-steel border-ash'
              "
            >
              <CheckCircle2 v-if="currentUnitData.estado_general === 'CERTIFICADO'" :size="12" :stroke-width="1.5" />
              <Clock v-else :size="12" :stroke-width="1.5" />
              <span>{{ currentUnitData.estado_general || 'SIN DATOS' }}</span>
            </span>
          </div>
          <p class="text-xs text-steel">
            Responsable: <strong class="text-ink-black">{{ deptConfig[selectedDept]?.chief }}</strong> · Período activo: <strong class="text-ink-black">{{ selectedMesNombre }} {{ selectedAnio }}</strong>
          </p>
        </div>
      </div>

      <!-- Botón de Certificación Oficial de la Unidad -->
      <div class="flex items-center gap-3">
        <button
          v-if="currentUnitData && currentUnitData.total_medidos > 0 && currentUnitData.estado_general !== 'CERTIFICADO'"
          type="button"
          :disabled="isSubmitting"
          class="inline-flex items-center justify-center gap-2 px-4 py-2 bg-emerald-600 text-white rounded-[3px] text-xs font-semibold hover:bg-emerald-700 transition-colors cursor-pointer border-none disabled:opacity-50"
          title="Certificar oficialmente todas las cifras de este mes"
          @click="handleCertifyUnit"
        >
          <Award :size="15" :stroke-width="1.5" />
          <span>Certificar Cifras del Mes</span>
        </button>
      </div>
    </div>

    <!-- Banner de Notificación -->
    <div
      v-if="feedbackMessage"
      class="flex items-center gap-2 p-3.5 rounded-[3px] text-sm font-medium"
      :class="
        feedbackMessage.type === 'success'
          ? 'bg-signal-blue/10 text-signal-blue border border-signal-blue/20'
          : 'bg-red-50 text-red-700 border border-red-200'
      "
    >
      <CheckCircle2 v-if="feedbackMessage.type === 'success'" :size="16" :stroke-width="1.5" class="shrink-0" />
      <AlertTriangle v-else :size="16" :stroke-width="1.5" class="shrink-0" />
      <span>{{ feedbackMessage.text }}</span>
    </div>

    <!-- Pestañas de Modalidad de Carga: Excel vs Formulario -->
    <div class="bg-white border border-ash rounded-[3px]">
      <div class="flex border-b border-ash bg-mist/30">
        <button
          type="button"
          class="inline-flex items-center gap-2 px-5 py-3 text-xs font-semibold border-b-2 transition-all cursor-pointer bg-transparent border-t-0 border-l-0 border-r-0"
          :class="
            uploadMode === 'EXCEL'
              ? 'border-signal-blue text-signal-blue bg-white'
              : 'border-transparent text-steel hover:text-ink-black'
          "
          @click="uploadMode = 'EXCEL'"
        >
          <FileSpreadsheet :size="15" :stroke-width="1.5" />
          <span>Carga Masiva con Archivo Excel (.xlsx)</span>
          <span class="ml-1 px-1.5 py-0.2 bg-signal-blue/10 text-signal-blue text-[10px] rounded-[2px] font-bold uppercase">Recomendado</span>
        </button>

        <button
          type="button"
          class="inline-flex items-center gap-2 px-5 py-3 text-xs font-semibold border-b-2 transition-all cursor-pointer bg-transparent border-t-0 border-l-0 border-r-0"
          :class="
            uploadMode === 'FORM'
              ? 'border-signal-blue text-signal-blue bg-white'
              : 'border-transparent text-steel hover:text-ink-black'
          "
          @click="uploadMode = 'FORM'"
        >
          <Edit3 :size="15" :stroke-width="1.5" />
          <span>Formulario Interactivo por Unidad</span>
        </button>
      </div>

      <!-- Contenedor del Formulario o del Importador Excel -->
      <div class="p-6">
        <!-- MODALIDAD 1: FORMULARIOS WEB ESPECIALIZADOS -->
        <div v-if="uploadMode === 'FORM'">
          <EcoUploadForm
            v-if="selectedDept === 'ECO'"
            :initial-data="initialFormData"
            :is-submitting="isSubmitting"
            :selected-mes-nombre="selectedMesNombre"
            :anio="selectedAnio"
            @submit="handleBatchSubmit"
          />

          <SocUploadForm
            v-else-if="selectedDept === 'SOC'"
            :initial-data="initialFormData"
            :is-submitting="isSubmitting"
            :selected-mes-nombre="selectedMesNombre"
            :anio="selectedAnio"
            @submit="handleBatchSubmit"
          />

          <DemUploadForm
            v-else-if="selectedDept === 'DEM'"
            :initial-data="initialFormData"
            :is-submitting="isSubmitting"
            :selected-mes-nombre="selectedMesNombre"
            :anio="selectedAnio"
            @submit="handleBatchSubmit"
          />

          <CartUploadForm
            v-else-if="selectedDept === 'CART'"
            :initial-data="initialFormData"
            :is-submitting="isSubmitting"
            :selected-mes-nombre="selectedMesNombre"
            :anio="selectedAnio"
            @submit="handleBatchSubmit"
          />

          <SegUploadForm
            v-else-if="selectedDept === 'SEG'"
            :initial-data="initialFormData"
            :is-submitting="isSubmitting"
            :selected-mes-nombre="selectedMesNombre"
            :anio="selectedAnio"
            @submit="handleBatchSubmit"
          />

          <SeemUploadForm
            v-else-if="selectedDept === 'SEEM'"
            :initial-data="initialFormData"
            :is-submitting="isSubmitting"
            :selected-mes-nombre="selectedMesNombre"
            :anio="selectedAnio"
            @submit="handleBatchSubmit"
          />
        </div>

        <!-- MODALIDAD 2: CARGA MASIVA EXCEL (.XLSX) -->
        <div v-else>
          <ExcelUploadZone
            :dept-code="selectedDept"
            :dept-name="deptConfig[selectedDept]?.name || ''"
            :selected-mes-nombre="selectedMesNombre"
            :anio="selectedAnio"
            :is-submitting="isSubmitting"
            @submit-batch="handleBatchSubmit"
          />
        </div>
      </div>
    </div>
  </div>
</template>
