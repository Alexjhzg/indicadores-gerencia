# Guía de Despliegue en Render.com 🚀
## Sistema de Indicadores de Gestión - INE Monagas

Esta guía detalla los pasos para poner en producción el sistema completo en **Render.com** utilizando el plan gratuito (Free Tier).

El proyecto consta de 3 componentes integrados:
1. **Base de Datos PostgreSQL**: Motor relacional gestionado por Render con extensiones UUID.
2. **Backend Web Service**: API REST en FastAPI (Python 3.11 + Uvicorn) con auto-migración y carga de semillas maestras.
3. **Frontend Static Site**: Interfaz gráfica SPA en Vue 3 + Vite + Tailwind CSS.

---

## 📌 Paso 1: Subir el proyecto a GitHub o GitLab

Render se conecta directamente a un repositorio de Git para desplegar y actualizar automáticamente el proyecto ante cada cambio (`git push`).

Abre una terminal en la raíz del proyecto (`sistema-indicadores`) y ejecuta:

```bash
# 1. Inicializar git
git init

# 2. Agregar todos los archivos (el archivo .gitignore ya excluye .venv y node_modules)
git add .

# 3. Crear el primer commit
git commit -m "feat: preparar proyecto para despliegue en Render"

# 4. Enlazar con tu repositorio remoto de GitHub (sustituye por tu URL)
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git

# 5. Subir los archivos
git push -u origin main
```

---

## 🚀 Paso 2: Despliegue en Render

Tienes **dos opciones** para desplegar. La **Opción A (Blueprint)** es la más rápida y recomendada porque configura todo en 1 solo clic.

---

### 🔹 Opción A: Despliegue Automático con Blueprint (Recomendado - 1 Clic)

El repositorio incluye el archivo [`render.yaml`](./render.yaml) listo para usar.

1. Inicia sesión en [https://dashboard.render.com/](https://dashboard.render.com/).
2. Haz clic en el botón azul superior **"New +"** y selecciona **"Blueprint"**.
3. Conecta tu cuenta de GitHub/GitLab y selecciona el repositorio del proyecto.
4. Render leerá automáticamente el archivo `render.yaml` y te mostrará el plan con los 3 recursos:
   - Base de Datos: `ine-indicadores-db`
   - Servicio Web: `ine-indicadores-backend`
   - Sitio Estático: `ine-indicadores-frontend`
5. Haz clic en **"Apply"** (Aplicar).
6. ¡Listo! Render creará la base de datos, compilará el backend, ejecutará la inicialización de tablas con las semillas oficiales y compilará el frontend enlazado a la API.

---

### 🔹 Opción B: Despliegue Manual Paso a Paso desde la Interfaz de Render

Si prefieres crear los recursos manualmente desde la interfaz web de Render, sigue estos pasos en orden:

#### 1. Crear la Base de Datos PostgreSQL
1. En Render Dashboard, haz clic en **New +** > **PostgreSQL**.
2. Configura los siguientes campos:
   - **Name**: `ine-indicadores-db`
   - **Database**: `ine_indicadores_monagas`
   - **User**: `ine_admin`
   - **Region**: Oregon (EE.UU.) u Ohio (recomendado mantener la misma región en los 3 servicios)
   - **Instance Type**: `Free`
3. Haz clic en **Create Database**.
4. Una vez creada, copia el valor de **Internal Database URL** (empieza con `postgres://...`).

---

#### 2. Crear el Servicio Web del Backend (API REST)
1. En Render Dashboard, haz clic en **New +** > **Web Service**.
2. Conecta tu repositorio de GitHub.
3. Configura los siguientes campos:
   - **Name**: `ine-indicadores-backend`
   - **Root Directory**: `backend`
   - **Runtime**: `Python`
   - **Region**: La misma de la base de datos
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python -m app.db.init_db && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: `Free`
4. En la sección **Environment Variables**, añade:
   - `DATABASE_URL`: Pega la *Internal Database URL* de tu base de datos creada en el paso 1.
   - `PYTHON_VERSION`: `3.11.9`
   - `SECRET_KEY`: Una cadena segura aleatoria (ej. `ine-monagas-secret-prod-2026-auth-token`)
   - `CORS_ORIGINS`: `http://localhost:5173` *(El backend ya autoriza automáticamente todos los dominios `*.onrender.com`)*
5. Haz clic en **Create Web Service**.
6. Render iniciará la construcción y verás en los logs:
   - Creación de esquema y tablas.
   - Carga de los 30 indicadores oficiales y mediciones de agosto 2026.
   - Servidor Uvicorn escuchando en puerto `$PORT`.
7. Copia la URL pública generada para tu backend (ejemplo: `https://ine-indicadores-backend.onrender.com`).

---

#### 3. Crear el Sitio Estático del Frontend (Vue 3 + Vite)
1. En Render Dashboard, haz clic en **New +** > **Static Site**.
2. Conecta tu repositorio de GitHub.
3. Configura los siguientes campos:
   - **Name**: `ine-indicadores-frontend`
   - **Root Directory**: `frontend`
   - **Branch**: `main`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist`
4. En **Redirects / Rewrites** (Enrutamiento SPA):
   - Haz clic en **Add Rule**:
     - **Type**: `Rewrite`
     - **Source**: `/*`
     - **Destination**: `/index.html`
5. En **Environment Variables**, añade:
   - `NODE_VERSION`: `22`
   - `VITE_API_BASE_URL`: La URL pública de tu backend (ejemplo: `https://ine-indicadores-backend.onrender.com`).
6. Haz clic en **Create Static Site**.
7. Render compilará los módulos de Vue y publicará el sitio web en una URL pública (ejemplo: `https://ine-indicadores-frontend.onrender.com`).

---

## 🔑 Credenciales de Acceso Inicial

Una vez completado el despliegue, podrás ingresar a la aplicación con los usuarios oficiales precargados en el sistema:

| Rol | Cédula | Contraseña | Funcionario Responsable | Unidad Técnica |
| :--- | :--- | :--- | :--- | :--- |
| **Gerente Estadal** | `V-11206771` | `gerente2026` | **Luis Alberto** | Gerencia Estadal Monagas (Acceso Total) |
| **Jefe de Área** | `V-8979338` | `gerente2026` | **Jesús Ramón Pérez** | Supervisión (CART, ECO, SOC, SEG) |
| **Jefe de Unidad** | `V-13814617` | `gerente2026` | **Wilfredo Rojas** | Estadísticas Económicas (ECO) |
| **Jefe de Unidad** | `V-17934142` | `gerente2026` | **Rubén Alejandro** | Estadísticas Sociales (SOC) |
| **Jefa de Unidad** | `V-11337533` | `gerente2026` | **Cledys Bastardo** | Demografía y Población (DEM) |
| **Jefe de Unidad** | `V-10198032` | `gerente2026` | **Henri Guevara** | Cartografía Estadística (CART) |
| **Jefa de Unidad** | `V-17723864` | `gerente2026` | **Johana Larez** | Estructura y Encuestas SEGEN (SEG) |
| **Coordinador** | `V-20916675` | `gerente2026` | **Luis Velásquez** | Coordinación de SEEM (Seguimiento y Eval.) |
| **Administrador** | `V-10000000` | `gerente2026` | **Administrador General** | Configuración Técnica y Auditoría |

---

## 💡 Notas Importantes sobre el Plan Gratuito de Render

- **Suspensión por inactividad (Spin down)**: Los servicios web en el plan gratuito de Render se suspenden tras 15 minutos de inactividad para ahorrar recursos. Al recibir la primera petición después de estar suspendido, puede tardar entre 30 y 50 segundos en despertar.
- **Base de Datos Gratuita**: Las instancias de PostgreSQL gratuitas en Render son ideales para demostraciones, pruebas y uso inicial (vigencia de 30 días renovable o migrable a plan básico de $7/mes para persistencia indefinida).
