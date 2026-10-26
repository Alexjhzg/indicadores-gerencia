# 📊 Sistema de Indicadores de Gestión — INE Estado Monagas

Sistema integral para la centralización, procesamiento, auditoría y visualización de indicadores operativos y estadísticos del **Instituto Nacional de Estadística (INE)** en la **Gerencia Estadal del Estado Monagas (Entidad Federal 16)**.

Digitaliza y automatiza los flujos de gestión que históricamente se gestionaban en el informe mensual oficial en hojas de cálculo (`Cuadros Informe Mensual de Gestion Gerencias Estadales MONAGAS AGOSTO 2026.xlsx`), incorporando integridad transaccional, control de acceso por roles (RBAC), control de versiones con auditoría inmutable y cuadros de mando interactivos en tiempo real.

---

## 📚 Documentación del Proyecto

| Documento | Descripción |
|---|---|
| 📖 [**`LOGICA_DE_NEGOCIO.md`**](./LOGICA_DE_NEGOCIO.md) | **Especificación completa de la lógica de negocio**: Unidades técnicas, catálogo oficial de 29 indicadores, fórmulas matemáticas, umbrales de calidad, flujo de certificación, triggers de versionado y glosario. |
| 🛢️ [**`docs/database_model.md`**](./docs/database_model.md) | Modelo relacional de base de datos en PostgreSQL, diagrama entidad-relación (ERD), diseño de tablas, índices y vistas analíticas. |
| 📋 [**`docs/catalogo_indicadores_reales.md`**](./docs/catalogo_indicadores_reales.md) | Catálogo normativo con las cifras reales y series históricas del informe oficial de agosto 2026. |
| 🚀 [**`DEPLOY_RENDER.md`**](./DEPLOY_RENDER.md) | Guía paso a paso para el despliegue en producción en Render.com mediante Infrastructure-as-Code (`render.yaml`). |

---

## 🏛️ Unidades Técnicas Operativas

El sistema estructura la gestión estadística del estado Monagas en **5 unidades técnicas** y **1 unidad de coordinación**:

1. **`SOC` — Estadísticas Sociales:** Encuesta de Hogares por Muestreo (EHM) y Encuesta de Seguimiento al Consumo de Alimentos (ESCA). Tasas de levantamiento, viviendas efectivas y tasas de no respuesta.
2. **`DEM` — Estadísticas Demográficas y Hechos Vitales:** Captura y flujo continuo de boletas vitales (Nacimientos, Defunciones, Nupcialidad, Divorcios) en registros civiles y hospitales, con control de transcripción y cero rezago.
3. **`ECO` — Estadísticas Económicas y Precios:** Monitoreo del Directorio de Establecimientos comerciales y relevamiento de precios para la Canasta Alimentaria Normativa (CAN).
4. **`CART` — Cartografía Estadística:** Georreferenciación y vectorización poligonal de los Circuitos Comunales y Consejos Comunales en los 13 municipios en alianza con el IGVSB.
5. **`SEG` — Estructura y Encuestas SEGEN:** Monitoreo de la red territorial de Nodos, operatividad del parque tecnológico móvil (DMC) y procesamiento de encuestas digitales ODK (Conteo Rápido Intercensal v2, Coyuntura, Laboral).
6. **`SEEM / GER` — Coordinación Estadal:** Seguimiento, evaluación, comités de coordinación estadística estadal (CCEE) y talento humano institucional.

---

## 🛠️ Stack Tecnológico

### Backend
- **Framework:** FastAPI (Python 3.11+)
- **ORM & BD:** SQLAlchemy 2.0 + PostgreSQL con extensiones `uuid-ossp`
- **Seguridad:** JWT (JSON Web Tokens) + Hashing seguro con Passlib (Argon2 / Bcrypt)
- **Validación de Datos:** Pydantic v2
- **Auditoría & Integridad:** Triggers PL/pgSQL nativos y vistas analíticas (`v_dashboard_central_resumen`)

### Frontend
- **Framework:** Vue.js 3 (Composition API, `<script setup>`)
- **Lenguaje:** TypeScript estricto
- **Estilos:** Tailwind CSS v4 integrado con `@tailwindcss/vite`
- **Iconografía:** Lucide Icons (diseño editorial sobrio, cero emojis en interfaz)
- **Gestión de Estado:** Pinia
- **Interoperabilidad:** XLSX (SheetJS) para lectura y generación de cuadros oficiales

---

## 🚀 Inicio Rápido en Desarrollo Local

### Requisitos Previos
- Node.js (v18+)
- Python (v3.11+)
- PostgreSQL (v14+) o Docker

### Opción A: Con Docker Compose

```bash
# Iniciar base de datos PostgreSQL local
docker-compose up -d
```

### Opción B: Ejecución Manual

#### 1. Configurar Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Inicializar esquema de base de datos y cargar semillas oficiales
python -m app.db.init_db

# Ejecutar servidor de desarrollo
uvicorn app.main:app --reload --port 8000
```
La documentación interactiva OpenAPI/Swagger estará disponible en `http://localhost:8000/docs`.

#### 2. Configurar Frontend
```bash
cd frontend
npm install
npm run dev
```
La aplicación web estará disponible en `http://localhost:5173`.

---

## 👥 Usuarios y Credenciales por Defecto (Entorno de Pruebas)

| Cédula | Contraseña | Rol | Acceso y Permisos |
|---|---|---|---|
| `V-10000000` | `10000000` | `ADMIN` | Administrador general del sistema. |
| `V-20000000` | `20000000` | `GERENTE` | Gerente Estadal (Supervisión ejecutiva, tableros consolidados, solo lectura). |
| `V-11111111` | `11111111` | `ENCARGADO` | Encargado Unidad Sociales (`SOC`). |
| `V-22222222` | `22222222` | `ENCARGADO` | Encargado Unidad Demografía (`DEM`). |
| `V-33333333` | `33333333` | `ENCARGADO` | Encargado Unidad Económica (`ECO`). |
| `V-44444444` | `44444444` | `ENCARGADO` | Encargado Unidad Cartografía (`CART`). |
| `V-55555555` | `55555555` | `ENCARGADO` | Encargado Unidad SEGEN (`SEG`). |

---

## 📄 Licencia

Desarrollado para el **Instituto Nacional de Estadística (INE)**, Gerencia Estadal del Estado Monagas, República Bolivariana de Venezuela. Todos los derechos reservados.
