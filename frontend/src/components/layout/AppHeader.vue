<script setup lang="ts">
import { computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import {
  LayoutDashboard,
  Layers,
  FileSpreadsheet,
  LogOut,
  Building,
} from 'lucide-vue-next';

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const currentPath = computed(() => route.path);
const userCedula = computed(() => authStore.userCedula || 'V-12345678');
const userRol = computed(() => authStore.userRol || 'GERENTE');

const handleLogout = () => {
  authStore.logout();
  router.push('/login');
};
</script>

<template>
  <header class="sticky top-0 z-50 h-[60px] max-md:h-[52px] bg-white border-b border-ash">
    <div class="max-w-[1440px] mx-auto h-full flex items-center justify-between px-10 max-md:px-4">
      <!-- Identidad Institucional -->
      <div class="flex items-center gap-2 sm:gap-2.5 shrink-0">
        <router-link
          :to="authStore.isEncargado && authStore.userDept ? `/departamentos/${authStore.userDept}` : (authStore.isJefeArea ? '/departamentos/CART' : '/dashboard')"
          class="flex items-center gap-1.5 sm:gap-2 text-[14px] sm:text-[15px] font-semibold text-ink-black tracking-tight"
        >
          <Building :size="18" :stroke-width="1.5" class="shrink-0" />
          <span>INE MONAGAS</span>
        </router-link>
        <span class="hidden sm:inline-flex items-center px-2 py-0.5 text-xs font-semibold bg-mist text-ink-black rounded-[3px]">
          ENTIDAD 16
        </span>
      </div>

      <!-- Navegación Principal en Desktop -->
      <nav class="hidden md:flex items-center gap-6">
        <!-- Resumen Ejecutivo: Solo visible para Gerente y Administrador -->
        <router-link
          v-if="authStore.isGerente"
          to="/dashboard"
          class="inline-flex items-center gap-1.5 py-1 text-[15px] transition-colors"
          :class="
            currentPath === '/dashboard' || currentPath === '/'
              ? 'text-ink-black font-semibold border-b-[1.5px] border-ink-black'
              : 'text-steel font-medium hover:text-ink-black'
          "
        >
          <LayoutDashboard :size="16" :stroke-width="1.5" />
          <span>Resumen Ejecutivo</span>
        </router-link>

        <!-- Jefe de Unidad: Enlace exclusivo a su Unidad Técnica Asignada -->
        <router-link
          v-if="authStore.isEncargado && authStore.userDept"
          :to="`/departamentos/${authStore.userDept}`"
          class="inline-flex items-center gap-1.5 py-1 text-[15px] transition-colors"
          :class="
            currentPath.startsWith('/departamentos')
              ? 'text-ink-black font-semibold border-b-[1.5px] border-ink-black'
              : 'text-steel font-medium hover:text-ink-black'
          "
        >
          <Layers :size="16" :stroke-width="1.5" />
          <span>Mi Unidad ({{ authStore.userDept }})</span>
        </router-link>

        <!-- Jefe de Área (Jesús Pérez): Enlace a sus Unidades Técnicas Asignadas -->
        <router-link
          v-else-if="authStore.isJefeArea"
          to="/departamentos/CART"
          class="inline-flex items-center gap-1.5 py-1 text-[15px] transition-colors"
          :class="
            currentPath.startsWith('/departamentos')
              ? 'text-ink-black font-semibold border-b-[1.5px] border-ink-black'
              : 'text-steel font-medium hover:text-ink-black'
          "
        >
          <Layers :size="16" :stroke-width="1.5" />
          <span>Mis Unidades (Estadísticas)</span>
        </router-link>

        <!-- Gerente y Admin: Enlace a todas las Unidades -->
        <router-link
          v-else
          to="/departamentos/ECO"
          class="inline-flex items-center gap-1.5 py-1 text-[15px] transition-colors"
          :class="
            currentPath.startsWith('/departamentos')
              ? 'text-ink-black font-semibold border-b-[1.5px] border-ink-black'
              : 'text-steel font-medium hover:text-ink-black'
          "
        >
          <Layers :size="16" :stroke-width="1.5" />
          <span>Unidades</span>
        </router-link>

        <!-- Panel de Carga Operativa -->
        <router-link
          to="/operaciones"
          class="inline-flex items-center gap-1.5 py-1 text-[15px] transition-colors"
          :class="
            currentPath === '/operaciones'
              ? 'text-ink-black font-semibold border-b-[1.5px] border-ink-black'
              : 'text-steel font-medium hover:text-ink-black'
          "
        >
          <FileSpreadsheet :size="16" :stroke-width="1.5" />
          <span>Panel Operativo</span>
        </router-link>
      </nav>

      <!-- Perfil de Usuario y Logout -->
      <div class="flex items-center gap-2 sm:gap-4 shrink-0">
        <div class="inline-flex items-center px-2 sm:px-2.5 py-0.5 sm:py-1 text-[11px] sm:text-xs font-semibold bg-mist text-ink-black rounded-[3px] truncate max-w-[150px] sm:max-w-none">
          <span class="truncate">{{ userCedula }} · {{ userRol }}</span>
        </div>
        <button
          type="button"
          class="hidden md:inline-flex items-center gap-1 text-[14px] font-semibold text-ink-black hover:opacity-75 transition-opacity cursor-pointer bg-transparent border-none p-0"
          title="Cerrar sesión institucional"
          @click="handleLogout"
        >
          <LogOut :size="15" :stroke-width="1.5" />
          <span class="border-b-[1.5px] border-ink-black pb-[1px]">Salir</span>
        </button>
      </div>
    </div>
  </header>
</template>
