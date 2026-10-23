<script setup lang="ts">
import { ref, computed } from 'vue';
import { DollarSign, CheckCircle2, HelpCircle } from 'lucide-vue-next';

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

// Valores interactivos
const s1 = ref(585);
const s2 = ref(585);
const s3 = ref(585);
const s4 = ref(585);

const totalPreciosCalculados = computed(() => Number(s1.value || 0) + Number(s2.value || 0) + Number(s3.value || 0) + Number(s4.value || 0));

const canComunas = ref(25);
const canLocales = ref(49);
const canLocalesMeta = ref(49);
const canSinErrorPct = ref(99.49);
const personal = ref(5);
const directorioLocales = ref(50);
const motivoCambio = ref('Carga mensual regular de Estadísticas Económicas');

// Si vienen datos iniciales del backend, sincronizarlos
if (props.initialData && props.initialData.length > 0) {
  for (const item of props.initialData) {
    if (item.codigo === 'ECO-CAN-02' && item.valor > 0) {
      const perWeek = Math.floor(item.valor / 4);
      s1.value = perWeek;
      s2.value = perWeek;
      s3.value = perWeek;
      s4.value = item.valor - (perWeek * 3);
    }
    if (item.codigo === 'ECO-CAN-04' && item.valor > 0) canComunas.value = item.valor;
    if (item.codigo === 'ECO-PRE-02' && item.valor > 0) canLocales.value = item.valor;
    if (item.codigo === 'ECO-CAN-03' && item.valor > 0) canSinErrorPct.value = item.valor;
    if (item.codigo === 'ECO-PRE-01' && item.valor > 0) personal.value = item.valor;
    if (item.codigo === 'ECO-DIR-01' && item.valor > 0) directorioLocales.value = item.valor;
  }
}

const handleSubmit = () => {
  const mediciones = [
    { indicador_codigo: 'ECO-PRE-01', valor_registrado: Number(personal.value), meta_periodo: 5 },
    { indicador_codigo: 'ECO-PRE-02', valor_registrado: Number(canLocales.value), meta_periodo: Number(canLocalesMeta.value) },
    { indicador_codigo: 'ECO-CAN-01', valor_registrado: 100, meta_periodo: 100 },
    { indicador_codigo: 'ECO-CAN-02', valor_registrado: totalPreciosCalculados.value, meta_periodo: 2200 },
    { indicador_codigo: 'ECO-CAN-03', valor_registrado: Number(canSinErrorPct.value), meta_periodo: 99 },
    { indicador_codigo: 'ECO-CAN-04', valor_registrado: Number(canComunas.value), meta_periodo: 25 },
    { indicador_codigo: 'ECO-DIR-01', valor_registrado: Number(directorioLocales.value), meta_periodo: 50 },
  ];

  emit('submit', {
    mediciones,
    motivo: motivoCambio.value || `Carga de cifras ${props.selectedMesNombre} ${props.anio}`,
  });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
    <!-- Encabezado de la Unidad -->
    <div class="flex items-center justify-between pb-4 border-b border-mist">
      <div>
        <h3 class="text-base font-semibold text-ink-black flex items-center gap-2">
          <DollarSign :size="18" :stroke-width="1.5" class="text-dept-eco" />
          <span>Formulario Oficial: Unidad de Estadísticas Económicas</span>
        </h3>
        <p class="text-xs text-steel mt-0.5">
          Levantamiento de Precios CAN, Directorio de Tipologías y cobertura de 25 comunas en {{ selectedMesNombre }} {{ anio }}
        </p>
      </div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-1 bg-dept-eco-light text-dept-eco border border-dept-eco-border rounded-[3px] text-xs font-semibold">
        <span>7 Indicadores Vinculados</span>
      </div>
    </div>

    <!-- Sección 1: Cotizaciones Semanales de Precios -->
    <div class="flex flex-col gap-3">
      <div class="flex items-center justify-between">
        <label class="text-xs font-semibold text-ink-black tracking-wide uppercase">
          1. Cotizaciones Semanales (ECO-CAN-02 · Meta Referencial: 2,200 precios)
        </label>
        <span class="text-xs font-semibold text-signal-blue">
          Total Acumulado: {{ totalPreciosCalculados.toLocaleString() }} precios
        </span>
      </div>

      <div class="grid grid-cols-4 max-sm:grid-cols-2 gap-3">
        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Semana 1</span>
          <input
            v-model.number="s1"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 585 precios</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Semana 2</span>
          <input
            v-model.number="s2"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 585 precios</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Semana 3</span>
          <input
            v-model.number="s3"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 585 precios</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Semana 4</span>
          <input
            v-model.number="s4"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 585 precios</span>
        </div>
      </div>
    </div>

    <!-- Sección 2: Parámetros de Cobertura y Calidad -->
    <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-4 pt-2">
      <!-- Comunas Cubiertas -->
      <div class="flex flex-col gap-1">
        <label class="text-xs font-semibold text-ink-black">
          Comunas con Levantamiento CAN (ECO-CAN-04)
        </label>
        <div class="flex items-center gap-2">
          <input
            v-model.number="canComunas"
            type="number"
            min="1"
            max="25"
            required
            class="w-full px-3 py-2 text-sm font-medium text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">/ 25 comunas</span>
        </div>
      </div>

      <!-- Calidad de Precios Sin Error -->
      <div class="flex flex-col gap-1">
        <label class="text-xs font-semibold text-ink-black">
          Porcentaje de Precios Sin Error (ECO-CAN-03)
        </label>
        <div class="flex items-center gap-2">
          <input
            v-model.number="canSinErrorPct"
            type="number"
            step="0.01"
            min="0"
            max="100"
            required
            class="w-full px-3 py-2 text-sm font-medium text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">% (Meta: ≥99.0%)</span>
        </div>
      </div>

      <!-- Locales Relevados Planificados -->
      <div class="flex flex-col gap-1">
        <label class="text-xs font-semibold text-ink-black">
          Establecimientos Relevados CAN (ECO-PRE-02)
        </label>
        <div class="flex items-center gap-2">
          <input
            v-model.number="canLocales"
            type="number"
            min="1"
            required
            class="w-full px-3 py-2 text-sm font-medium text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">locales</span>
        </div>
      </div>

      <!-- Directorio de Tipologías -->
      <div class="flex flex-col gap-1">
        <label class="text-xs font-semibold text-ink-black">
          Establecimientos Implantados Directorio (ECO-DIR-01)
        </label>
        <div class="flex items-center gap-2">
          <input
            v-model.number="directorioLocales"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-medium text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">locales (Meta: 50)</span>
        </div>
      </div>

      <!-- Personal de Levantamiento -->
      <div class="flex flex-col gap-1">
        <label class="text-xs font-semibold text-ink-black">
          Personal Activo en Campo (ECO-PRE-01)
        </label>
        <div class="flex items-center gap-2">
          <input
            v-model.number="personal"
            type="number"
            min="1"
            required
            class="w-full px-3 py-2 text-sm font-medium text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">personas (Meta: 5)</span>
        </div>
      </div>
    </div>

    <!-- Motivo de la Carga / Justificación -->
    <div class="flex flex-col gap-1.5 pt-2">
      <label class="text-xs font-semibold text-ink-black flex items-center gap-1.5">
        <span>Justificación Técnica / Observaciones del Mes:</span>
        <HelpCircle :size="13" :stroke-width="1.5" class="text-steel" />
      </label>
      <input
        v-model="motivoCambio"
        type="text"
        placeholder="Ej: Reporte oficial de precios completado al 100% de la muestra"
        class="w-full px-3 py-2 text-sm text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
      />
    </div>

    <!-- Botón de Envío -->
    <div class="flex items-center justify-end gap-3 pt-4 border-t border-mist">
      <button
        type="submit"
        :disabled="isSubmitting"
        class="inline-flex items-center gap-2 px-5 py-2.5 bg-signal-blue text-white rounded-[3px] text-sm font-semibold hover:opacity-90 transition-opacity cursor-pointer border-none disabled:opacity-50"
      >
        <CheckCircle2 :size="16" :stroke-width="1.5" />
        <span>{{ isSubmitting ? 'Guardando en BD...' : 'Guardar Cifras de Económicas' }}</span>
      </button>
    </div>
  </form>
</template>
