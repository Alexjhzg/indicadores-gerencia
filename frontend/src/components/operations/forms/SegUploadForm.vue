<script setup lang="ts">
import { ref } from 'vue';
import { Smartphone, CheckCircle2, HelpCircle } from 'lucide-vue-next';

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

const encuestasTotal = ref(26789);
const conteoRapido = ref(15420);
const operatividadNodos = ref(84.5);
const despliegueNodos = ref(100.0);
const dmcDisponibles = ref(350);
const personalTerritorial = ref(210);

const motivoCambio = ref('Carga mensual regular de Nodos SEGEN, parque DMC y formularios ODK');

if (props.initialData && props.initialData.length > 0) {
  for (const item of props.initialData) {
    if (item.codigo === 'SEG-ENC-01' && item.valor > 0) encuestasTotal.value = item.valor;
    if (item.codigo === 'SEG-ENC-02' && item.valor > 0) conteoRapido.value = item.valor;
    if (item.codigo === 'SEG-NOD-01' && item.valor > 0) operatividadNodos.value = item.valor;
    if (item.codigo === 'SEG-NOD-02' && item.valor > 0) despliegueNodos.value = item.valor;
    if (item.codigo === 'SEG-PAR-01' && item.valor > 0) dmcDisponibles.value = item.valor;
    if (item.codigo === 'SEG-PER-01' && item.valor > 0) personalTerritorial.value = item.valor;
  }
}

const handleSubmit = () => {
  const mediciones = [
    { indicador_codigo: 'SEG-ENC-01', valor_registrado: Number(encuestasTotal.value), meta_periodo: 25000 },
    { indicador_codigo: 'SEG-ENC-02', valor_registrado: Number(conteoRapido.value), meta_periodo: 15000 },
    { indicador_codigo: 'SEG-NOD-01', valor_registrado: Number(operatividadNodos.value), meta_periodo: 80 },
    { indicador_codigo: 'SEG-NOD-02', valor_registrado: Number(despliegueNodos.value), meta_periodo: 100 },
    { indicador_codigo: 'SEG-PAR-01', valor_registrado: Number(dmcDisponibles.value), meta_periodo: 350 },
    { indicador_codigo: 'SEG-PER-01', valor_registrado: Number(personalTerritorial.value), meta_periodo: 210 },
  ];

  emit('submit', {
    mediciones,
    motivo: motivoCambio.value || `Carga de cifras SEGEN ${props.selectedMesNombre} ${props.anio}`,
  });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
    <div class="flex items-center justify-between pb-4 border-b border-mist">
      <div>
        <h3 class="text-base font-semibold text-ink-black flex items-center gap-2">
          <Smartphone :size="18" :stroke-width="1.5" class="text-dept-seg" />
          <span>Formulario Oficial: Unidad de SEGEN</span>
        </h3>
        <p class="text-xs text-steel mt-0.5">
          Red territorial de 106 nodos, parque tecnológico DMC, cuestionarios electrónicos ODK y comités interinstitucionales
        </p>
      </div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-1 bg-dept-seg-light text-dept-seg border border-dept-seg-border rounded-[3px] text-xs font-semibold">
        <span>6 Indicadores Vinculados</span>
      </div>
    </div>

    <!-- Módulo 1: Encuestas Digitales y ODK -->
    <div class="flex flex-col gap-3">
      <span class="text-xs font-semibold text-ink-black tracking-wide uppercase">
        1. Encuestas Digitales y Cuestionarios ODK
      </span>
      <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-3">
        <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Volumen Mensual de Encuestas (SEG-ENC-01)</span>
          <input
            v-model.number="encuestasTotal"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 25,000 encuestas</span>
        </div>

        <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Captura Conteo Rápido / ODK (SEG-ENC-02)</span>
          <input
            v-model.number="conteoRapido"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 15,000 encuestas</span>
        </div>
      </div>
    </div>

    <!-- Módulo 2: Red Territorial de Nodos y Parque Tecnológico -->
    <div class="flex flex-col gap-3">
      <span class="text-xs font-semibold text-ink-black tracking-wide uppercase">
        2. Nodos Territoriales, Parque Tecnológico y Despliegue de Fuerza Humana
      </span>
      <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3">
        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Operatividad Nodos (SEG-NOD-01)</span>
          <input
            v-model.number="operatividadNodos"
            type="number"
            step="0.1"
            min="0"
            max="100"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: ≥80.0%</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Despliegue Nodos (SEG-NOD-02)</span>
          <input
            v-model.number="despliegueNodos"
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
          <span class="text-xs font-medium text-steel">Dispositivos DMC (SEG-PAR-01)</span>
          <input
            v-model.number="dmcDisponibles"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 350 equipos</span>
        </div>

        <div class="flex flex-col gap-1 p-3 bg-mist/40 border border-ash rounded-[3px]">
          <span class="text-xs font-medium text-steel">Fuerza Territorial (SEG-PER-01)</span>
          <input
            v-model.number="personalTerritorial"
            type="number"
            min="0"
            required
            class="w-full px-2.5 py-1.5 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-[11px] text-steel">Meta: 210 personas</span>
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
        placeholder="Ej: Reporte integral de operatividad de nodos SEGEN y cuestionarios ODK sincronizados"
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
        <span>{{ isSubmitting ? 'Guardando en BD...' : 'Guardar Cifras de SEGEN' }}</span>
      </button>
    </div>
  </form>
</template>
