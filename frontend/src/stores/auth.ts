import { defineStore } from 'pinia';
import api from '@/api/client';
import type { Usuario, RolUsuario, DepartamentoId } from '@/types';

interface AuthState {
  token: string | null;
  user: Usuario | null;
  loading: boolean;
  error: string | null;
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    token: localStorage.getItem('ine_auth_token'),
    user: localStorage.getItem('ine_user_info')
      ? JSON.parse(localStorage.getItem('ine_user_info') as string)
      : null,
    loading: false,
    error: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
    userCedula: (state) => state.user?.cedula || '',
    userRol: (state): RolUsuario => state.user?.rol_id || 'ENCARGADO',
    userDept: (state) => state.user?.departamento_id,
    isGerente: (state) => state.user?.rol_id === 'GERENTE' || state.user?.rol_id === 'ADMIN',
    isJefeArea: (state) => state.user?.rol_id === 'JEFE_AREA',
    isEncargado: (state) => state.user?.rol_id === 'ENCARGADO',
    allowedDepts: (state): DepartamentoId[] => {
      if (state.user?.rol_id === 'GERENTE' || state.user?.rol_id === 'ADMIN') {
        return ['ECO', 'SOC', 'DEM', 'CART', 'SEG', 'SEEM'];
      }
      if (state.user?.rol_id === 'JEFE_AREA') {
        if (state.user?.departamentos_codigos && state.user.departamentos_codigos.length > 0) {
          return state.user.departamentos_codigos;
        }
        return ['CART', 'ECO', 'SOC', 'SEG'];
      }
      if (state.user?.departamento_id) {
        return [state.user.departamento_id];
      }
      return [];
    },
  },

  actions: {
    async login(cedula: string, password: string): Promise<boolean> {
      this.loading = true;
      this.error = null;
      try {
        const response = await api.post('/auth/login', {
          cedula: cedula.trim().toUpperCase(),
          password,
        });

        const { access_token } = response.data;
        this.token = access_token;
        localStorage.setItem('ine_auth_token', access_token);

        // Obtener datos del perfil
        await this.fetchCurrentUser();
        return true;
      } catch (err: any) {
        this.error =
          err.response?.data?.detail || 'Error al autenticar con el servidor';
        return false;
      } finally {
        this.loading = false;
      }
    },

    async fetchCurrentUser(): Promise<void> {
      try {
        const response = await api.get('/auth/me');
        const data = response.data;
        const mappedUser: Usuario = {
          cedula: data.cedula,
          nombres: data.nombre_completo || data.cedula,
          apellidos: '',
          rol_id: (data.rol_nombre || 'ENCARGADO') as RolUsuario,
          departamento_id: data.departamento_codigo || null,
          departamentos_codigos: data.departamentos_codigos || [],
          activo: data.activo,
        };
        this.user = mappedUser;
        localStorage.setItem('ine_user_info', JSON.stringify(mappedUser));
      } catch (err) {
        console.error('Error fetching user profile', err);
      }
    },

    logout(): void {
      this.token = null;
      this.user = null;
      localStorage.removeItem('ine_auth_token');
      localStorage.removeItem('ine_user_info');
    },
  },
});
