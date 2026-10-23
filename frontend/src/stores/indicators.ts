import { defineStore } from 'pinia';
import api from '@/api/client';
import type { DepartamentoId } from '@/types';

interface IndicatorsState {
  dashboardSummary: any | null;
  indicators: any[];
  measurements: any[];
  departments: any[];
  municipalities: any[];
  selectedDepartment: DepartamentoId | 'TODOS';
  selectedYear: number;
  selectedMonth: number;
  loading: boolean;
  error: string | null;
}

export const useIndicatorsStore = defineStore('indicators', {
  state: (): IndicatorsState => ({
    dashboardSummary: null,
    indicators: [],
    measurements: [],
    departments: [],
    municipalities: [],
    selectedDepartment: 'TODOS',
    selectedYear: 2026,
    selectedMonth: 8, // Agosto 2026 (mes del informe oficial de gestión)
    loading: false,
    error: null,
  }),

  getters: {
    indicatorsByDepartment: (state) => (deptId: string) => {
      return state.indicators.filter((ind) => ind.departamento_codigo === deptId);
    },
    filteredIndicators: (state) => {
      if (state.selectedDepartment === 'TODOS') return state.indicators;
      return state.indicators.filter(
        (ind) => ind.departamento_codigo === state.selectedDepartment
      );
    },
    filteredMeasurements: (state) => {
      return state.measurements.filter((m) => {
        const matchYear = !state.selectedYear || m.periodo_anio === state.selectedYear;
        const matchMonth = !state.selectedMonth || m.periodo_mes === state.selectedMonth;
        const matchDept =
          state.selectedDepartment === 'TODOS' ||
          m.departamento_codigo === state.selectedDepartment;
        return matchYear && matchMonth && matchDept;
      });
    },
  },

  actions: {
    async fetchDashboardSummary() {
      this.loading = true;
      try {
        const response = await api.get('/dashboard/resumen');
        this.dashboardSummary = response.data;
      } catch (err: any) {
        console.error('Error fetching dashboard summary', err);
        this.error = 'No se pudo cargar el resumen ejecutivo.';
      } finally {
        this.loading = false;
      }
    },

    async fetchIndicators() {
      try {
        const response = await api.get('/indicadores/');
        this.indicators = response.data;
      } catch (err) {
        console.error('Error fetching indicators', err);
      }
    },

    async fetchMeasurements() {
      try {
        const response = await api.get('/mediciones/', {
          params: {
            periodo_anio: this.selectedYear,
            periodo_mes: this.selectedMonth,
          },
        });
        this.measurements = response.data;
      } catch (err) {
        console.error('Error fetching measurements', err);
      }
    },

    async fetchDepartments() {
      try {
        const response = await api.get('/departamentos/');
        this.departments = response.data;
      } catch (err) {
        console.error('Error fetching departments', err);
      }
    },

    async fetchMunicipalities() {
      try {
        const response = await api.get('/municipios/');
        this.municipalities = response.data;
      } catch (err) {
        console.error('Error fetching municipalities', err);
      }
    },

    setSelectedDepartment(dept: DepartamentoId | 'TODOS') {
      this.selectedDepartment = dept;
    },

    setSelectedPeriod(year: number, month: number) {
      this.selectedYear = year;
      this.selectedMonth = month;
      this.fetchMeasurements();
    },
  },
});
