<script setup lang="ts">
import { computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import {
  LayoutDashboard,
  Layers,
  FileSpreadsheet,
  LogOut,
} from 'lucide-vue-next';

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const currentPath = computed(() => route.path);

const handleLogout = () => {
  authStore.logout();
  router.push('/login');
};
</script>

<template>
  <nav class="flex md:hidden fixed bottom-0 left-0 right-0 h-[62px] bg-white border-t border-ash z-50 items-center justify-around px-2">
    <!-- Resumen Ejecutivo: Solo para Gerente -->
    <router-link
      v-if="authStore.isGerente"
      to="/dashboard"
      class="flex flex-col items-center justify-center gap-0.5 flex-1 h-full py-1.5 transition-colors no-underline"
      :class="currentPath === '/dashboard' || currentPath === '/' ? 'text-signal-blue font-semibold' : 'text-steel font-medium'"
    >
      <LayoutDashboard :size="20" :stroke-width="1.5" class="shrink-0" />
      <span class="text-xs tracking-tight">Resumen</span>
    </router-link>

    <!-- Mi Unidad para Encargado -->
    <router-link
      v-if="authStore.isEncargado && authStore.userDept"
      :to="`/departamentos/${authStore.userDept}`"
      class="flex flex-col items-center justify-center gap-0.5 flex-1 h-full py-1.5 transition-colors no-underline"
      :class="currentPath.startsWith('/departamentos') ? 'text-signal-blue font-semibold' : 'text-steel font-medium'"
    >
      <Layers :size="20" :stroke-width="1.5" class="shrink-0" />
      <span class="text-xs tracking-tight">Mi Unidad</span>
    </router-link>

    <!-- Mis Unidades para Jefe de Área (Jesús Pérez) -->
    <router-link
      v-else-if="authStore.isJefeArea"
      to="/departamentos/CART"
      class="flex flex-col items-center justify-center gap-0.5 flex-1 h-full py-1.5 transition-colors no-underline"
      :class="currentPath.startsWith('/departamentos') ? 'text-signal-blue font-semibold' : 'text-steel font-medium'"
    >
      <Layers :size="20" :stroke-width="1.5" class="shrink-0" />
      <span class="text-xs tracking-tight">Unidades</span>
    </router-link>

    <!-- Unidades para Gerente -->
    <router-link
      v-else-if="authStore.isGerente"
      to="/departamentos/ECO"
      class="flex flex-col items-center justify-center gap-0.5 flex-1 h-full py-1.5 transition-colors no-underline"
      :class="currentPath.startsWith('/departamentos') ? 'text-signal-blue font-semibold' : 'text-steel font-medium'"
    >
      <Layers :size="20" :stroke-width="1.5" class="shrink-0" />
      <span class="text-xs tracking-tight">Unidades</span>
    </router-link>

    <!-- Panel Operativo -->
    <router-link
      to="/operaciones"
      class="flex flex-col items-center justify-center gap-0.5 flex-1 h-full py-1.5 transition-colors no-underline"
      :class="currentPath === '/operaciones' ? 'text-signal-blue font-semibold' : 'text-steel font-medium'"
    >
      <FileSpreadsheet :size="20" :stroke-width="1.5" class="shrink-0" />
      <span class="text-xs tracking-tight">Operaciones</span>
    </router-link>

    <button
      type="button"
      class="flex flex-col items-center justify-center gap-0.5 flex-1 h-full py-1.5 text-steel hover:text-ink-black transition-colors bg-transparent border-none cursor-pointer"
      @click="handleLogout"
    >
      <LogOut :size="20" :stroke-width="1.5" class="shrink-0" />
      <span class="text-xs font-medium tracking-tight">Salir</span>
    </button>
  </nav>
</template>
