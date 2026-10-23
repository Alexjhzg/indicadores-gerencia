<script setup lang="ts">
import { ref } from 'vue';
import { MapPin, CheckCircle2, HelpCircle } from 'lucide-vue-next';

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

const tasaVectorizacion = ref(100.0);
const consejosGeorref = ref(1361);
const circuitosCompletos = ref(199);
const coberturaMunicipios = ref(13);
const comunasVectorizadas = ref(199);

const motivoCambio = ref('Carga mensual regular del Proyecto Circuitos Comunales y Cartografía');

if (props.initialData && props.initialData.length > 0) {
  for (const item of props.initialData) {
    if (item.codigo === 'CART-CIR-01' && item.valor > 0) tasaVectorizacion.value = item.valor;
    if (item.codigo === 'CART-CIR-02' && item.valor > 0) consejosGeorref.value = item.valor;
    if (item.codigo === 'CART-CIR-03' && item.valor > 0) circuitosCompletos.value = item.valor;
    if (item.codigo === 'CART-MUN-01' && item.valor > 0) coberturaMunicipios.value = item.valor;
    if (item.codigo === 'CART-VEC-01' && item.valor > 0) comunasVectorizadas.value = item.valor;
  }
}

const handleSubmit = () => {
  const mediciones = [
    { indicador_codigo: 'CART-CIR-01', valor_registrado: Number(tasaVectorizacion.value), meta_periodo: 100 },
    { indicador_codigo: 'CART-CIR-02', valor_registrado: Number(consejosGeorref.value), meta_periodo: 1361 },
    { indicador_codigo: 'CART-CIR-03', valor_registrado: Number(circuitosCompletos.value), meta_periodo: 199 },
    { indicador_codigo: 'CART-MUN-01', valor_registrado: Number(coberturaMunicipios.value), meta_periodo: 13 },
    { indicador_codigo: 'CART-VEC-01', valor_registrado: Number(comunasVectorizadas.value), meta_periodo: 199 },
  ];

  emit('submit', {
    mediciones,
    motivo: motivoCambio.value || `Carga de avances cartográficos ${props.selectedMesNombre} ${props.anio}`,
  });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
    <div class="flex items-center justify-between pb-4 border-b border-mist">
      <div>
        <h3 class="text-base font-semibold text-ink-black flex items-center gap-2">
          <MapPin :size="18" :stroke-width="1.5" class="text-dept-cart" />
          <span>Formulario Oficial: Unidad de Cartografía</span>
        </h3>
        <p class="text-xs text-steel mt-0.5">
          Proyecto Circuitos Comunales, consejos comunales delimitados y vectorización con IGVSB en los 13 municipios
        </p>
      </div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-1 bg-dept-cart-light text-dept-cart border border-dept-cart-border rounded-[3px] text-xs font-semibold">
        <span>5 Indicadores Vinculados</span>
      </div>
    </div>

    <!-- Indicadores Cartográficos -->
    <div class="grid grid-cols-2 max-sm:grid-cols-1 gap-4">
      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Tasa Vectorización Circuitos (CART-CIR-01)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="tasaVectorizacion"
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

      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Consejos Comunales Georreferenciados (CART-CIR-02)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="consejosGeorref"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">consejos (Meta: 1,361)</span>
        </div>
      </div>

      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Completitud Vectorial Plena (CART-CIR-03)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="circuitosCompletos"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">circuitos (Meta: 199)</span>
        </div>
      </div>

      <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
        <label class="text-xs font-semibold text-ink-black">
          Comunas y Circuitos Vectorizados (CART-VEC-01)
        </label>
        <div class="flex items-center gap-2 mt-1">
          <input
            v-model.number="comunasVectorizadas"
            type="number"
            min="0"
            required
            class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
          />
          <span class="text-xs text-steel shrink-0">comunas (Meta: 199)</span>
        </div>
      </div>
    </div>

    <!-- Cobertura Municipal -->
    <div class="flex flex-col gap-1 p-3.5 bg-mist/30 border border-ash rounded-[3px]">
      <label class="text-xs font-semibold text-ink-black">
        Cobertura Territorial de Municipios Actualizados (CART-MUN-01)
      </label>
      <div class="flex items-center gap-2 mt-1">
        <input
          v-model.number="coberturaMunicipios"
          type="number"
          min="1"
          max="13"
          required
          class="w-full px-3 py-2 text-sm font-semibold text-ink-black bg-white border border-ash rounded-[3px] focus:outline-none focus:border-signal-blue"
        />
        <span class="text-xs text-steel shrink-0">/ 13 Municipios del estado Monagas</span>
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
        placeholder="Ej: Delimitación de poligonales comunales y consolidación geoespacial IGVSB"
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
        <span>{{ isSubmitting ? 'Guardando en BD...' : 'Guardar Cifras de Cartografía' }}</span>
      </button>
    </div>
  </form>
</template>
