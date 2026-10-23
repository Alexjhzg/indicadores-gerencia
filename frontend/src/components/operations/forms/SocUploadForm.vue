<script setup lang="ts">
import { ref } from 'vue';
import { Users, CheckCircle2, HelpCircle } from 'lucide-vue-next';

interface InitialMeasurement {
  codigo: string;
  valor: number;
  meta: number;
}

const props = defineProps<{
  initialData?: InitialMeasurement[];
  isSubmitting: boolean;
  selectedMesNombre: string;
  anio: number;
}>();

const emit = defineEmits<{
  (e: 'submit', payload: { mediciones: Array<{ indicador_codigo: string; valor_registrado: number; meta_periodo: number }>; motivo: string }): void;
}>();

// Valores interactivos EHM
const ehmEfectivas = ref(172);
const ehmTasa = ref(100.0);
const ehmNoResp = ref(12.5);

// Valores interactivos ESCA
const escaEfectivas = ref(287);
const escaTasa = ref(100.0);
const escaNoResp = ref(14.8);

// Valores interactivos EAM
const eamSectores = ref(13);
const eamViviendas = ref(172);

const motivoCambio = ref('Carga mensual regular de Estadísticas Sociales (EHM y ESCA)');

if (props.initialData && props.initialData.length > 0) {
  for (const item of props.initialData) {
    if (item.codigo === 'SOC-EHM-02' && item.valor > 0) ehmEfectivas.value = item.valor;
    if (item.codigo === 'SOC-EHM-01' && item.valor > 0) ehmTasa.value = item.valor;
    if (item.codigo === 'SOC-EHM-03' && item.valor > 0) ehmNoResp.value = item.valor;

    if (item.codigo === 'SOC-ESCA-02' && item.valor > 0) escaEfectivas.value = item.valor;
    if (item.codigo === 'SOC-ESCA-01' && item.valor > 0) escaTasa.value = item.valor;
    if (item.codigo === 'SOC-ESCA-03' && item.valor > 0) escaNoResp.value = item.valor;

    if (item.codigo === 'SOC-EAM-01' && item.valor > 0) eamSectores.value = item.valor;
    if (item.codigo === 'SOC-EAM-02' && item.valor > 0) eamViviendas.value = item.valor;
  }
}

const handleSubmit = () => {
  const mediciones = [
    { indicador_codigo: 'SOC-EAM-01', valor_registrado: Number(eamSectores.value), meta_periodo: 13 },
    { indicador_codigo: 'SOC-EAM-02', valor_registrado: Number(eamViviendas.value), meta_periodo: 172 },
    { indicador_codigo: 'SOC-EHM-01', valor_registrado: Number(ehmTasa.value), meta_periodo: 100 },
    { indicador_codigo: 'SOC-EHM-02', valor_registrado: Number(ehmEfectivas.value), meta_periodo: 172 },
    { indicador_codigo: 'SOC-EHM-03', valor_registrado: Number(ehmNoResp.value), meta_periodo: 15 },
    { indicador_codigo: 'SOC-ESCA-01', valor_registrado: Number(escaTasa.value), meta_periodo: 100 },
    { indicador_codigo: 'SOC-ESCA-02', valor_registrado: Number(escaEfectivas.value), meta_periodo: 287 },
    { indicador_codigo: 'SOC-ESCA-03', valor_registrado: Number(escaNoResp.value), meta_periodo: 20 },
  ];

  emit('submit', {
    mediciones,
    motivo: motivoCambio.value || `Carga de cifras sociales ${props.selectedMesNombre} ${props.anio}`,
  });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
    <div class="flex items-center justify-between pb-4 border-b border-mist">
      <div>
        <h3 class="text-base font-semibold text-ink-black flex items-center gap-2">
          <Users :size="18" :stroke-width="1.5" class="text-dept-soc" />
          <span>Formulario Oficial: Unidad de Estadísticas Sociales</span>
        </h3>
        <p class="text-xs text-steel mt-0.5">
          Encuesta de Hogares por Muestreo (EHM) y Encuesta de Seguimiento al Consumo de Alimentos (ESCA) · {{ selectedMesNombre }} {{ anio }}
        </p>
      </div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-1 bg-dept-soc-light text-dept-soc border border-dept-soc-border rounded-[3px] text-xs font-semibold">
        <span>8 Indicadores Vinculados</span>
      </div>
    </div>

    <!-- Módulo 1: Encuesta de Hogares (EHM) -->
    <div class="flex flex-col gap-3">
      <span class="text-xs font-semibold text-ink-black tracking-wide uppercase">
        1. Encuesta de Hogares por Muestreo (EHM)
      </span>
      <div class="grid grid-cols-3 max-sm:grid-cols-1 gap-3">
        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Viviendas Efectivas (SOC-EHM-02)</span>
          <input
            v-model.number="ehmEfectivas"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 172 viviendas</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Tasa Levantamiento (SOC-EHM-01)</span>
          <input
            v-model.number="ehmTasa"
            type="number"
            step="0.1"
            min="0"
            max="100"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 100.0%</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Tasa No Respuesta (SOC-EHM-03)</span>
          <input
            v-model.number="ehmNoResp"
            type="number"
            step="0.1"
            min="0"
            max="100"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Tolerancia máx: ≤15.0%</span>
        </div>
      </div>
    </div>

    <!-- Módulo 2: Encuesta de Consumo de Alimentos (ESCA) -->
    <div class="flex flex-col gap-3">
      <span class="text-xs font-semibold text-ink-black tracking-wide uppercase">
        2. Encuesta de Seguimiento al Consumo de Alimentos (ESCA)
      </span>
      <div class="grid grid-cols-3 max-sm:grid-cols-1 gap-3">
        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Viviendas Efectivas (SOC-ESCA-02)</span>
          <input
            v-model.number="escaEfectivas"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 287 viviendas</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Tasa Levantamiento (SOC-ESCA-01)</span>
          <input
            v-model.number="escaTasa"
            type="number"
            step="0.1"
            min="0"
            max="100"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 100.0%</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Tasa No Respuesta (SOC-ESCA-03)</span>
          <input
            v-model.number="escaNoResp"
            type="number"
            step="0.1"
            min="0"
            max="100"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Tolerancia máx: ≤20.0%</span>
        </div>
      </div>
    </div>

    <!-- Módulo 3: Encuesta Ampliada (EAM) -->
    <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-4 pt-1">
      <div class="flex flex-col gap-1">
        <label class="text-xs font-semibold text-ink-black">
          Sectores Operativos EAM (SOC-EAM-01)
        </label>
        <div class="flex items-center gap-2">
          <input
            v-model.number="eamSectores"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-medium text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">sectores (Meta: 13)</span>
        </div>
      </div>

      <div class="flex flex-col gap-1">
        <label class="text-xs font-semibold text-ink-black">
          Viviendas Efectivas EAM (SOC-EAM-02)
        </label>
        <div class="flex items-center gap-2">
          <input
            v-model.number="eamViviendas"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-medium text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">viviendas (Meta: 172)</span>
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-1.5 pt-2">
      <label class="text-xs font-semibold text-ink-black flex items-center gap-1.5">
        <span>Justificación Técnica / Observaciones del Mes:</span>
        <HelpCircle :size="13" :stroke-width="1.5" class="text-steel" />
      </label>
      <input
        v-model="motivoCambio"
        type="text"
        placeholder="Ej: Levantamiento EHM y ESCA culminado según cronograma muestral"
        class="w-full px-3 py-2 text-sm text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
      />
    </div>

    <div class="flex items-center justify-end gap-3 pt-4 border-t border-mist">
      <button
        type="submit"
        :disabled="isSubmitting"
        class="inline-flex items-center gap-2 px-5 py-2.5 bg-signal-blue text-white rounded-[3px] text-sm font-semibold hover:opacity-90 transition-opacity cursor-pointer border-none disabled:opacity-50"
      >
        <CheckCircle2 :size="16" :stroke-width="1.5" />
        <span>{{ isSubmitting ? 'Guardando en BD...' : 'Guardar Cifras de Sociales' }}</span>
      </button>
    </div>
  </form>
</template>
