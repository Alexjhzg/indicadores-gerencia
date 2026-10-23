<script setup lang="ts">
import { ref } from 'vue';
import { UserCheck, CheckCircle2, HelpCircle } from 'lucide-vue-next';

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

const boletasTotal = ref(25410);
const nacimientos = ref(15230);
const defunciones = ref(4120);
const nupcialidad = ref(3050);
const tasaDigitalizacion = ref(100.0);

const motivoCambio = ref('Carga mensual regular de Hechos Vitales y Boletas EV');

if (props.initialData && props.initialData.length > 0) {
  for (const item of props.initialData) {
    if (item.codigo === 'DEM-VIT-01' && item.valor > 0) boletasTotal.value = item.valor;
    if (item.codigo === 'DEM-VIT-02' && item.valor > 0) nacimientos.value = item.valor;
    if (item.codigo === 'DEM-VIT-03' && item.valor > 0) defunciones.value = item.valor;
    if (item.codigo === 'DEM-VIT-04' && item.valor > 0) nupcialidad.value = item.valor;
    if (item.codigo === 'DEM-VIT-05' && item.valor > 0) tasaDigitalizacion.value = item.valor;
  }
}

const handleSubmit = () => {
  const mediciones = [
    { indicador_codigo: 'DEM-VIT-01', valor_registrado: Number(boletasTotal.value), meta_periodo: 25000 },
    { indicador_codigo: 'DEM-VIT-02', valor_registrado: Number(nacimientos.value), meta_periodo: 15000 },
    { indicador_codigo: 'DEM-VIT-03', valor_registrado: Number(defunciones.value), meta_periodo: 4000 },
    { indicador_codigo: 'DEM-VIT-04', valor_registrado: Number(nupcialidad.value), meta_periodo: 3000 },
    { indicador_codigo: 'DEM-VIT-05', valor_registrado: Number(tasaDigitalizacion.value), meta_periodo: 100 },
  ];

  emit('submit', {
    mediciones,
    motivo: motivoCambio.value || `Carga de estadísticas vitales ${props.selectedMesNombre} ${props.anio}`,
  });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
    <div class="flex items-center justify-between pb-4 border-b border-mist">
      <div>
        <h3 class="text-base font-semibold text-ink-black flex items-center gap-2">
          <UserCheck :size="18" :stroke-width="1.5" class="text-dept-dem" />
          <span>Formulario Oficial: Unidad de Demografía y Población</span>
        </h3>
        <p class="text-xs text-steel mt-0.5">
          Registro continuo de hechos vitales (Nacimientos, Defunciones, Nupcialidad) y flujo de boletas EV en los 13 municipios
        </p>
      </div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-1 bg-dept-dem-light text-dept-dem border border-dept-dem-border rounded-[3px] text-xs font-semibold">
        <span>5 Indicadores Vinculados</span>
      </div>
    </div>

    <!-- Hechos Vitales -->
    <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-4">
      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Total Boletas Vitales Recolectadas (DEM-VIT-01)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="boletasTotal"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">boletas (Meta: 25,000)</span>
        </div>
      </div>

      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Nacimientos Registrados (DEM-VIT-02)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="nacimientos"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">actas (Meta: 15,000)</span>
        </div>
      </div>

      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Defunciones Registradas (DEM-VIT-03)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="defunciones"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">actas (Meta: 4,000)</span>
        </div>
      </div>

      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Nupcialidad y Uniones Estables (DEM-VIT-04)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="nupcialidad"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">actas (Meta: 3,000)</span>
        </div>
      </div>
    </div>

    <!-- Tasa de Digitalización -->
    <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
      <label class="text-xs font-semibold text-ink-black">
        Tasa de Transcripción y Digitalización Vital (DEM-VIT-05)
      </label>
      <div class="flex items-center gap-2 mt-1">
        <input
          v-model.number="tasaDigitalizacion"
          type="number"
          step="0.1"
          min="0"
          max="100"
          required
          class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
        />
        <span class="text-xs text-steel shrink-0">% (Meta: 100.0%)</span>
      </div>
    </div>

    <!-- Justificación -->
    <div class="flex flex-col gap-1.5 pt-2">
      <label class="text-xs font-semibold text-ink-black flex items-center gap-1.5">
        <span>Justificación Técnica / Observaciones del Mes:</span>
        <HelpCircle :size="13" :stroke-width="1.5" class="text-steel" />
      </label>
      <input
        v-model="motivoCambio"
        type="text"
        placeholder="Ej: Remisión completa de boletas de hospitales y registros civiles sin rezago"
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
        <span>{{ isSubmitting ? 'Guardando en BD...' : 'Guardar Cifras de Demografía' }}</span>
      </button>
    </div>
  </form>
</template>
