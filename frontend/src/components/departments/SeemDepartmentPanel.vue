<script setup lang="ts">
import { computed } from 'vue';
import { datosSeemPorMes, mesesDisponibles } from '@/data/departmentMonthlyData';
import { GraduationCap, Users2, Building2, CheckCircle2, Layers } from 'lucide-vue-next';

interface IndicatorItem {
  id: string;
  codigo: string;
  nombre: string;
  descripcion: string;
  meta_referencial: number | null;
  unidad_medida: string;
}

defineProps<{
  indicators: IndicatorItem[];
}>();

const selectedMes = defineModel<string>('selectedMes', { default: 'Ago' });

const currentSeemData = computed(() => {
  const key = selectedMes.value in datosSeemPorMes ? selectedMes.value : 'Ago';
  return datosSeemPorMes[key];
});
</script>

<template>
  <div class="flex flex-col gap-6 w-full min-w-0 max-w-full overflow-hidden">
    <!-- Barra de Filtro de Mes -->
    <div class="bg-white border border-ash rounded-[3px] p-4 flex items-center justify-between flex-wrap gap-3">
      <div class="flex items-center gap-2">
        <GraduationCap :size="18" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <div>
          <h3 class="text-sm font-semibold text-ink-black">
            Período de Capacitación y Comités CCEE: {{ currentSeemData.mesNombre }} 2026
          </h3>
          <p class="text-xs text-steel">
            Planes de formación metodológica y mesas técnicas interinstitucionales
          </p>
        </div>
      </div>

      <!-- Selector de Meses -->
      <div class="flex items-center gap-1 overflow-x-auto pb-0.5">
        <button
          v-for="mes in mesesDisponibles"
          :key="mes.id"
          type="button"
          class="px-2.5 py-1 text-xs font-semibold rounded-[3px] transition-colors cursor-pointer border-none"
          :class="selectedMes === mes.id ? 'bg-ink-black text-white' : 'bg-mist text-steel hover:text-ink-black'"
          @click="selectedMes = mes.id"
        >
          {{ mes.nombreCorto }}
        </button>
      </div>
    </div>

    <!-- 1. Tarjetas Resumen de KPIs SEEM -->
    <div class="grid grid-cols-4 max-lg:grid-cols-2 max-sm:grid-cols-1 gap-3.5">
      <!-- Total Capacitados -->
      <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold tracking-wider text-steel uppercase">Personal Capacitado</span>
          <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-signal-blue/10 text-signal-blue border border-signal-blue/20">
            {{ Math.round((currentSeemData.totalCapacitados / currentSeemData.metaCapacitados) * 100) }}% Meta
          </span>
        </div>
        <div class="flex items-baseline gap-2">
          <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentSeemData.totalCapacitados }}
          </span>
          <span class="text-xs font-semibold text-steel">personas</span>
        </div>
        <span class="text-xs font-normal text-steel">
          {{ currentSeemData.capacitadosSede }} sede regional + {{ currentSeemData.capacitadosCampo }} campo territorial
        </span>
      </div>

      <!-- Talleres Ejecutados -->
      <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold tracking-wider text-steel uppercase">Talleres Realizados</span>
          <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
            {{ currentSeemData.totalTalleres }} / {{ currentSeemData.metaTalleres }}
          </span>
        </div>
        <div class="flex items-baseline gap-2">
          <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentSeemData.totalTalleres }}
          </span>
          <span class="text-xs font-semibold text-steel">talleres</span>
        </div>
        <span class="text-xs font-normal text-steel">
          Jornadas metodológicas y talleres de actualización técnica
        </span>
      </div>

      <!-- Mesas Técnicas CCEE -->
      <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold tracking-wider text-steel uppercase">Mesas Técnicas CCEE</span>
          <span
            class="text-xs font-semibold px-2 py-0.5 rounded-[3px]"
            :class="currentSeemData.totalMesasCCEE > 0 ? 'bg-signal-blue/10 text-signal-blue border border-signal-blue/20' : 'bg-mist text-steel'"
          >
            {{ currentSeemData.totalMesasCCEE > 0 ? 'Activa' : 'Sin Sesión' }}
          </span>
        </div>
        <div class="flex items-baseline gap-2">
          <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentSeemData.totalMesasCCEE }}
          </span>
          <span class="text-xs font-semibold text-steel">sesiones</span>
        </div>
        <span class="text-xs font-normal text-steel">
          Comité de Coordinación Estadística del estado Monagas
        </span>
      </div>

      <!-- Participantes CCEE -->
      <div class="bg-white border border-ash rounded-[3px] p-4.5 flex flex-col gap-2 hover:border-ink-black transition-colors">
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold tracking-wider text-steel uppercase">Delegados en CCEE</span>
          <span class="text-xs font-semibold px-2 py-0.5 rounded-[3px] bg-mist text-ink-black">
            Articulación
          </span>
        </div>
        <div class="flex items-baseline gap-2">
          <span class="text-[30px] max-md:text-[24px] font-semibold text-ink-black tracking-tight">
            {{ currentSeemData.participantesCCEE }}
          </span>
          <span class="text-xs font-semibold text-steel">delegados</span>
        </div>
        <span class="text-xs font-normal text-steel">
          Representantes de entes del Estado (Salud, CNE, INE)
        </span>
      </div>
    </div>

    <!-- 2. Gráficas y Tablas Especializadas: Talleres Realizados y Mesa Técnica CCEE -->
    <div class="grid grid-cols-1 lg:grid-cols-[1.6fr_1.4fr] gap-4">
      <!-- Tarjeta 1: Detalle de Talleres de Capacitación (LA 8) -->
      <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
        <div>
          <div class="flex items-start justify-between mb-3">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <GraduationCap :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
                <h3 class="text-base font-semibold text-ink-black">
                  Actividades Formativas Ejecutadas (LA 8. Capacitación)
                </h3>
              </div>
              <p class="text-xs text-steel">
                Registro de talleres, jornadas y distribución de funcionarios capacitados en {{ currentSeemData.mesNombre }}
              </p>
            </div>
            <span class="text-xs font-semibold px-2 py-0.5 bg-mist text-ink-black rounded-[3px]">
              {{ currentSeemData.talleres.length }} Talleres
            </span>
          </div>

          <!-- Tabla de Talleres -->
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs border-collapse">
              <thead>
                <tr class="border-b border-mist bg-canvas">
                  <th class="py-2 px-3 font-semibold text-ink-black">Taller / Actividad Formativa</th>
                  <th class="py-2 px-3 font-semibold text-ink-black">Tipo</th>
                  <th class="py-2 px-3 font-semibold text-ink-black text-center">Fecha</th>
                  <th class="py-2 px-3 font-semibold text-ink-black text-right">Participantes</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-mist">
                <tr
                  v-for="(taller, idx) in currentSeemData.talleres"
                  :key="idx"
                  class="hover:bg-mist/30 transition-colors"
                >
                  <td class="py-2.5 px-3 font-medium text-ink-black">
                    {{ taller.nombre }}
                  </td>
                  <td class="py-2.5 px-3">
                    <span
                      class="px-2 py-0.5 rounded-[3px] text-[11px] font-semibold"
                      :class="taller.tipo === 'Sede Regional' ? 'bg-signal-blue/10 text-signal-blue border border-signal-blue/20' : 'bg-emerald-50 text-emerald-800 border border-emerald-200'"
                    >
                      {{ taller.tipo }}
                    </span>
                  </td>
                  <td class="py-2.5 px-3 text-steel text-center font-mono text-[11px]">
                    {{ taller.fecha }}
                  </td>
                  <td class="py-2.5 px-3 text-right font-semibold text-ink-black font-mono">
                    {{ taller.participantes }}
                  </td>
                </tr>
                <tr v-if="currentSeemData.talleres.length === 0">
                  <td colspan="4" class="py-6 text-center text-steel italic">
                    No se registraron talleres en este período
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="flex items-center justify-between pt-3 border-t border-mist text-xs text-steel mt-4">
          <span>Distribución: {{ currentSeemData.capacitadosSede }} sede regional / {{ currentSeemData.capacitadosCampo }} campo</span>
          <span class="text-ink-black font-semibold">Total: {{ currentSeemData.totalCapacitados }} personas</span>
        </div>
      </div>

      <!-- Tarjeta 2: Mesas Técnicas de Coordinación Estadística (LA 9) -->
      <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
        <div>
          <div class="flex items-start justify-between mb-3">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <Building2 :size="16" :stroke-width="1.5" class="text-signal-blue shrink-0" />
                <h3 class="text-base font-semibold text-ink-black">
                  Comités Estadales (LA 9. Comités CCEE)
                </h3>
              </div>
              <p class="text-xs text-steel">
                Articulación interinstitucional con organismos del Estado en Monagas
              </p>
            </div>
            <span class="text-xs font-semibold px-2 py-0.5 bg-signal-blue/10 text-signal-blue border border-signal-blue/20 rounded-[3px]">
              CCEE Monagas
            </span>
          </div>

          <div v-if="currentSeemData.mesas.length > 0" class="flex flex-col gap-3">
            <div
              v-for="(mesa, idx) in currentSeemData.mesas"
              :key="idx"
              class="border border-ash rounded-[3px] p-3.5 bg-canvas flex flex-col gap-2.5"
            >
              <div class="flex items-start justify-between gap-2">
                <div>
                  <h4 class="text-xs font-semibold text-ink-black">{{ mesa.nombre }}</h4>
                  <span class="text-[11px] text-steel">{{ mesa.ente }}</span>
                </div>
                <span class="text-[11px] font-mono font-semibold px-1.5 py-0.5 bg-mist text-ink-black rounded-[3px] shrink-0">
                  {{ mesa.fecha }}
                </span>
              </div>

              <div class="p-2 bg-white border border-mist rounded-[3px]">
                <span class="text-[11px] font-semibold text-steel block mb-0.5">Acuerdos y Compromisos Técnicos:</span>
                <p class="text-xs text-ink-black leading-relaxed">
                  {{ mesa.acuerdos }}
                </p>
              </div>

              <div class="flex items-center justify-between text-[11px] text-steel">
                <span class="flex items-center gap-1">
                  <Users2 :size="12" :stroke-width="1.5" class="text-signal-blue" />
                  <span>Participación: {{ mesa.participantes }} delegados</span>
                </span>
                <span class="flex items-center gap-1 text-dept-eco font-medium">
                  <CheckCircle2 :size="12" :stroke-width="1.5" />
                  <span>Acta firmada</span>
                </span>
              </div>
            </div>
          </div>

          <div v-else class="py-12 flex flex-col items-center justify-center text-center gap-2">
            <Layers :size="32" :stroke-width="1.5" class="text-steel/40" />
            <p class="text-xs text-steel">
              No hubo sesiones de comités convocadas en el mes de {{ currentSeemData.mesNombre }}.
            </p>
            <span class="text-[11px] text-steel/70">
              Las mesas técnicas se celebran con periodicidad bimestral o según requerimiento del SEN.
            </span>
          </div>
        </div>

        <div class="flex items-center justify-between pt-3 border-t border-mist text-xs text-steel mt-4">
          <span>Responsable: Coordinador de SEEM</span>
          <span class="text-ink-black font-semibold">{{ currentSeemData.participantesCCEE }} Delegados Activos</span>
        </div>
      </div>
    </div>
  </div>
</template>
