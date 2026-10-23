<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { ShieldCheck, User, Lock, AlertCircle, ArrowRight } from 'lucide-vue-next';
import LoginBackgroundAnimation from '@/components/auth/LoginBackgroundAnimation.vue';

const router = useRouter();
const authStore = useAuthStore();

const cedula = ref('V-12345678');
const password = ref('gerente2026');
const errorMsg = ref('');
const isSubmitting = ref(false);

const handleLogin = async () => {
  if (!cedula.value || !password.value) {
    errorMsg.value = 'Por favor ingrese su Cédula y contraseña.';
    return;
  }
  isSubmitting.value = true;
  errorMsg.value = '';

  const success = await authStore.login(cedula.value, password.value);
  isSubmitting.value = false;

  if (success) {
    if (authStore.isEncargado && authStore.userDept) {
      router.push(`/departamentos/${authStore.userDept}`);
    } else if (authStore.isJefeArea) {
      router.push('/departamentos/CART');
    } else {
      router.push('/dashboard');
    }
  } else {
    errorMsg.value = authStore.error || 'Credenciales inválidas en el sistema INE.';
  }
};
</script>

<template>
  <div class="relative min-h-screen flex items-center justify-center bg-white p-5 overflow-hidden">
    <!-- Fondo Dinámico con Red de Nodos Estadísticos y Cuadrícula Cartográfica -->
    <LoginBackgroundAnimation />

    <div class="relative z-10 w-full max-w-[440px] flex flex-col gap-6">
      
      <!-- Encabezado Institucional -->
      <div class="text-center flex flex-col items-center gap-1.5">
        <p class="text-[11px] font-semibold tracking-widest text-steel uppercase">
          REPÚBLICA BOLIVARIANA DE VENEZUELA
        </p>
        <p class="text-xs font-semibold tracking-wider text-ink-black uppercase">
          INSTITUTO NACIONAL DE ESTADÍSTICA · GERENCIA ESTADAL MONAGAS
        </p>
        <div class="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold bg-white/90 border border-ash text-ink-black rounded-[3px] mt-1 backdrop-blur-sm">
          <ShieldCheck :size="14" :stroke-width="1.5" class="shrink-0 text-signal-blue" />
          <span>ENTIDAD FEDERAL 16 · SISTEMA DE GESTIÓN</span>
        </div>
      </div>

      <!-- Tarjeta de Acceso Domaine en Tailwind -->
      <div class="bg-white/95 backdrop-blur-md border border-ash rounded-[3px] p-8 relative flex flex-col gap-5">
        <!-- Acento Signal Blue superior -->
        <div class="absolute top-0 left-0 right-0 h-[2px] bg-signal-blue rounded-t-[3px]"></div>

        <div>
          <h1 class="text-xl font-semibold text-ink-black tracking-tight mb-1">
            SISTEMA DE INDICADORES
          </h1>
          <p class="text-sm font-medium text-steel leading-relaxed">
            Control de gestión, seguimiento territorial y auditoría de cifras
          </p>
        </div>

        <div v-if="errorMsg" class="flex items-center gap-2 p-3 bg-red-50 border border-red-200 text-red-700 rounded-[3px] text-xs font-medium">
          <AlertCircle :size="16" :stroke-width="1.5" class="shrink-0" />
          <span>{{ errorMsg }}</span>
        </div>

        <form class="flex flex-col gap-4" @submit.prevent="handleLogin">
          <div class="flex flex-col gap-1.5">
            <label for="cedula" class="flex items-center gap-1.5 text-xs font-semibold text-steel tracking-wider">
              <User :size="14" :stroke-width="1.5" class="shrink-0" />
              <span>CÉDULA DE IDENTIDAD</span>
            </label>
            <input
              id="cedula"
              v-model="cedula"
              type="text"
              placeholder="Ej. 11206771 o V-11206771"
              class="w-full bg-white border-[1.5px] border-ash rounded-[3px] px-3.5 py-2.5 text-[15px] font-medium text-ink-black outline-none focus:border-signal-blue transition-colors"
              required
              autocomplete="username"
            />
          </div>

          <div class="flex flex-col gap-1.5">
            <div class="flex items-center justify-between">
              <label for="password" class="flex items-center gap-1.5 text-xs font-semibold text-steel tracking-wider">
                <Lock :size="14" :stroke-width="1.5" class="shrink-0" />
                <span>CONTRASEÑA</span>
              </label>
              <span class="text-[11px] font-medium text-steel">Tu número de cédula</span>
            </div>
            <input
              id="password"
              v-model="password"
              type="password"
              placeholder="Ingresa tu misma cédula"
              class="w-full bg-white border-[1.5px] border-ash rounded-[3px] px-3.5 py-2.5 text-[15px] font-medium text-ink-black outline-none focus:border-signal-blue transition-colors"
              required
              autocomplete="current-password"
            />
          </div>

          <button
            type="submit"
            class="w-full h-11 mt-2 inline-flex items-center justify-center gap-2 bg-carbon text-white rounded-[3px] text-[15px] font-semibold hover:opacity-90 transition-opacity cursor-pointer border-none disabled:opacity-60 disabled:cursor-not-allowed"
            :disabled="isSubmitting"
          >
            <span v-if="!isSubmitting">INGRESAR AL SISTEMA</span>
            <span v-else>VERIFICANDO...</span>
            <ArrowRight v-if="!isSubmitting" :size="16" :stroke-width="1.5" class="shrink-0" />
          </button>
        </form>

        <div class="pt-4 border-t border-ash text-center">
          <span class="text-xs font-normal text-steel">
            Acceso restringido a funcionarios certificados del INE Monagas
          </span>
        </div>
      </div>

    </div>
  </div>
</template>
