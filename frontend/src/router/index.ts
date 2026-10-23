import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router';
import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';
import DepartmentDetailView from '@/views/DepartmentDetailView.vue';
import OperationsView from '@/views/OperationsView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { public: true },
  },
  {
    path: '/',
    redirect: '/dashboard',
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/departamentos/:id',
    name: 'department-detail',
    component: DepartmentDetailView,
    meta: { requiresAuth: true },
  },
  {
    path: '/operaciones',
    name: 'operations',
    component: OperationsView,
    meta: { requiresAuth: true },
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/dashboard',
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});

router.beforeEach((to, _from, next) => {
  const token = localStorage.getItem('ine_auth_token');
  const userInfoStr = localStorage.getItem('ine_user_info');
  const user = userInfoStr ? JSON.parse(userInfoStr) : null;
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);

  if (requiresAuth && !token) {
    next('/login');
    return;
  }

  // Redirección si ya está autenticado e intenta ir a login
  if (to.path === '/login' && token) {
    if (user && user.rol_id === 'ENCARGADO' && user.departamento_id) {
      next(`/departamentos/${user.departamento_id}`);
    } else if (user && user.rol_id === 'JEFE_AREA') {
      next('/departamentos/CART');
    } else {
      next('/dashboard');
    }
    return;
  }

  // Aislamiento estricto de roles:
  // 1. Jefe de Área (JEFE_AREA - Jesús Ramón Pérez):
  // Acceso exclusivo a sus 4 unidades asignadas (CART, ECO, SOC, SEG) y Panel Operativo (sin acceso al Dashboard ejecutivo de Gerencia)
  if (token && user && user.rol_id === 'JEFE_AREA') {
    const allowed = (user.departamentos_codigos && user.departamentos_codigos.length > 0)
      ? user.departamentos_codigos.map((c: string) => c.toUpperCase())
      : ['CART', 'ECO', 'SOC', 'SEG'];

    // Redirección fuera del Dashboard Ejecutivo consolidado de Gerencia
    if (to.path === '/dashboard' || to.path === '/') {
      next('/departamentos/CART');
      return;
    }

    // Restricción a departamentos fuera de su supervisión (ej. DEM o SEEM)
    if (to.path.startsWith('/departamentos/')) {
      const targetDept = (to.params.id as string || '').toUpperCase();
      if (targetDept && !allowed.includes(targetDept)) {
        next('/departamentos/CART');
        return;
      }
    }
  }

  // 2. Jefe de Unidad (ENCARGADO): Solo puede ver su unidad asignada
  if (token && user && user.rol_id === 'ENCARGADO' && user.departamento_id) {
    const userDept = user.departamento_id.toUpperCase();

    // No tiene acceso al Resumen Ejecutivo consolidado
    if (to.path === '/dashboard' || to.path === '/') {
      next(`/departamentos/${userDept}`);
      return;
    }

    // Solo puede ver el detalle de su propia unidad técnica
    if (to.path.startsWith('/departamentos/')) {
      const targetDept = (to.params.id as string || '').toUpperCase();
      if (targetDept && targetDept !== userDept) {
        next(`/departamentos/${userDept}`);
        return;
      }
    }
  }

  next();
});

export default router;
