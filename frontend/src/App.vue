<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import AppHeader from '@/components/layout/AppHeader.vue';
import MobileBottomNav from '@/components/layout/MobileBottomNav.vue';

const route = useRoute();
const isLoginPage = computed(() => route.path === '/login');
</script>

<template>
  <div class="app-layout">
    <AppHeader v-if="!isLoginPage" />
    <main class="main-content">
      <router-view />
    </main>
    <MobileBottomNav v-if="!isLoginPage" />
  </div>
</template>

<style scoped>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--surface-canvas);
}

.main-content {
  flex: 1;
}

@media (max-width: 768px) {
  .main-content {
    padding-bottom: 68px; /* Espacio para no solapar la barra de navegación móvil */
  }
}
</style>
