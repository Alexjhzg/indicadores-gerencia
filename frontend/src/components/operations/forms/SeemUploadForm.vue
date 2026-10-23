<script setup lang="ts">
import { ref } from 'vue';
import { GraduationCap, CheckCircle2, HelpCircle } from 'lucide-vue-next';

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

const personalCapacitado = ref(145);
const talleresRealizados = ref(7);
const mesasTecnicas = ref(1);
const participantesCCEE = ref(6);

const motivoCambio = ref('Carga mensual de capacitación metodológica y comités CCEE');

if (props.initialData && props.initialData.length > 0) {
  for (const item of props.initialData) {
    if (item.codigo === 'SEEM-CAP-01' && item.valor > 0) personalCapacitado.value = item.valor;
    if (item.codigo === 'SEEM-CAP-02' && item.valor > 0) talleresRealizados.value = item.valor;
    if (item.codigo === 'SEEM-COM-01' && item.valor > 0) mesasTecnicas.value = item.valor;
    if (item.codigo === 'SEEM-COM-02' && item.valor > 0) participantesCCEE.value = item.valor;
  }
}

const handleSubmit = () => {
  const mediciones = [
    { indicador_codigo: 'SEEM-CAP-01', valor_registrado: Number(personalCapacitado.value), meta_periodo: 150 },
    { indicador_codigo: 'SEEM-CAP-02', valor_registrado: Number(talleresRealizados.value), meta_periodo: 10 },
    { indicador_codigo: 'SEEM-COM-01', valor_registrado: Number(mesasTecnicas.value), meta_periodo: 2 },
    { indicador_codigo: 'SEEM-COM-02', valor_registrado: Number(participantesCCEE.value), meta_periodo: 10 },
  ];

  emit('submit', {
    mediciones,
    motivo: motivoCambio.value || `Carga de cifras SEEM ${props.selectedMesNombre} ${props.anio}`,
  });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
    <div class="flex items-center justify-between pb-4 border-b border-mist">
      <div>
        <h3 class="text-base font-semibold text-ink-black flex items-center gap-2">
          <GraduationCap :size="18" :stroke-width="1.5" class="text-teal-700" />
          <span>Formulario Oficial: Coordinación de SEEM</span>
        </h3>
        <p class="text-xs text-steel mt-0.5">
          Capacitación y educación metodológica (LA 8) y Comités Estadales de Coordinación Estadística CCEE (LA 9)
        </p>
      </div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-1 bg-teal-50 text-teal-800 border border-teal-200 rounded-[3px] text-xs font-semibold">
        <span>4 Indicadores Vinculados</span>
      </div>
    </div>

    <!-- Módulo 1: Capacitación y Planes de Formación Metodológica (LA 8) -->
    <div class="flex flex-col gap-3">
      <span class="text-xs font-semibold text-ink-black tracking-wide uppercase">
        1. Formación y Capacitación Metodológica (LA 8)
      </span>
      <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-3">
        <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Personal Capacitado (SEEM-CAP-01)</span>
          <input
            v-model.number="personalCapacitado"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 150 personas (Sede regional + Campo)</span>
        </div>

        <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Talleres y Jornadas Realizadas (SEEM-CAP-02)</span>
          <input
            v-model.number="talleresRealizados"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 10 talleres mensuales</span>
        </div>
      </div>
    </div>

    <!-- Módulo 2: Comités de Coordinación Estadística (CCEE · LA 9) -->
    <div class="flex flex-col gap-3">
      <span class="text-xs font-semibold text-ink-black tracking-wide uppercase">
        2. Comités de Coordinación Estadística CCEE (LA 9)
      </span>
      <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-3">
        <div class="flex flex-col gap-1 p-3.5 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Mesas Técnicas Realizadas (SEEM-COM-01)</span>
          <input
            v-model.number="mesasTecnicas"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 2 mesas técnicas</span>
        </div>

        <div class="flex flex-col gap-1 p-3.5 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Delegados Participantes (SEEM-COM-02)</span>
          <input
            v-model.number="participantesCCEE"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 10 participantes interinstitucionales</span>
        </div>
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
        placeholder="Ej: Ejecución de 7 talleres metodológicos y mesa técnica de registros vitales con Salud y CNE"
        class="w-full px-3 py-2 text-sm text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
      />
    </div>

    <div class="flex items-center justify-end gap-3 pt-4 border-t border-mist">
      <button
        type="submit"
        :disabled="isSubmitting"
        class="inline-flex items-center gap-2 px-5 py-2.5 bg-teal-700 text-white rounded-[3px] text-sm font-semibold hover:opacity-90 transition-opacity cursor-pointer border-none disabled:opacity-50"
      >
        <CheckCircle2 :size="16" :stroke-width="1.5" />
        <span>{{ isSubmitting ? 'Guardando en BD...' : 'Guardar Cifras de Coordinación SEEM' }}</span>
      </button>
    </div>
  </form>
</template>
