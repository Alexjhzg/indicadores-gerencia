<script setup lang="ts">
import {
  FileSpreadsheet,
  Download,
} from 'lucide-vue-next';

import EcoCuadroTable from '@/components/departments/cuadros/EcoCuadroTable.vue';
import SocCuadroTable from '@/components/departments/cuadros/SocCuadroTable.vue';
import DemCuadroTable from '@/components/departments/cuadros/DemCuadroTable.vue';
import CartCuadroTable from '@/components/departments/cuadros/CartCuadroTable.vue';
import SegCuadroTable from '@/components/departments/cuadros/SegCuadroTable.vue';
import SeemCuadroTable from '@/components/departments/cuadros/SeemCuadroTable.vue';
import { exportCuadroXLSX } from '@/utils/exportCuadrosXLSX';

const props = defineProps<{
  deptCode: string;
}>();

const handleExport = () => {
  exportCuadroXLSX(props.deptCode);
};
</script>

<template>
  <div class="flex flex-col gap-6">

    <!-- Barra de Control del Cuadro: Título Oficial y Botón de Descarga -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white border border-ash rounded-[3px] p-4.5">
      <div class="flex items-center gap-2.5">
        <FileSpreadsheet :size="20" :stroke-width="1.5" class="text-signal-blue shrink-0" />
        <div>
          <h3 class="text-base font-semibold text-ink-black leading-snug">
            Matriz Estadística Oficial · Informe Mensual de Gestión
          </h3>
          <span class="text-xs font-normal text-steel">
            Fuente oficial: Gerencia Estadal Monagas (Entidad 16) · Agosto 2026
          </span>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <button
          type="button"
          class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-[3px] text-xs font-semibold bg-white border border-ash text-ink-black hover:border-signal-blue hover:text-signal-blue transition-colors cursor-pointer"
          @click="handleExport"
          title="Descargar este cuadro en formato Excel (.xlsx)"
        >
          <Download :size="14" :stroke-width="1.5" class="shrink-0" />
          <span>Exportar Cuadro Excel (.xlsx)</span>
        </button>
      </div>
    </div>

    <!-- Renderizado modularizado de Cuadros Oficiales por Departamento -->
    <EcoCuadroTable v-if="deptCode === 'ECO'" />
    <SocCuadroTable v-else-if="deptCode === 'SOC'" />
    <DemCuadroTable v-else-if="deptCode === 'DEM'" />
    <CartCuadroTable v-else-if="deptCode === 'CART'" />
    <SegCuadroTable v-else-if="deptCode === 'SEG'" />
    <SeemCuadroTable v-else-if="deptCode === 'SEEM'" />

  </div>
</template>
