# 🎨 Catálogo de Pantallas Generadas en Stitch
## Sistema de Indicadores de Gestión — INE Monagas (Entidad 16)

> **Proyecto Stitch:** `projects/3839814326263931017`  
> **Nombre:** *Sistema de Indicadores INE Monagas - Halfhelix*  
> **Sistema de Diseño:** Domaine Editorial / Halfhelix (`assets/e28daad81c694892b52849c3abc05147`)  
> **Tokens & Reglas:** [desing-system/desing.md](file:///home/seem/Documentos/_proyectos/sistema-indicadores/desing-system/desing.md) (Canvas blanco marfil `#ffffff`, tipografía Suisse Int'l / Inter en peso regular 400 exclusivo, estética *shadowless*, esquinas de 3px y líneas hairline de 1px ash).

---

## 🖥️ Pantallas Diseñadas y Enlaces de Captura

### 1. Pantalla 01: Login Institucional (Acceso con Cédula)
* **ID en Stitch:** `cc4342a0045c43ebbb7787eac55633d4`
* **Dispositivo:** Desktop (1440px / 2560px)
* **Descripción:** Acceso formal con Cédula de Identidad (`V-12345678`) y contraseña. Sin sombras, marco centrado con borde de 1px ash, botón de entrada en bloque Carbon (`#262626`) con radio de 3px y tipografía en peso 400.
* **Captura Oficial:** [Ver Screenshot en Alta Resolución (Con Signal Blue)](https://lh3.googleusercontent.com/aida/AEtjO1XnYzgJS8XGRZSEZ_PvYvMktnFMSpjlD3KhcyWuYsUsjnWeyN4E3OHg4T5Y20MZaTdW_gs6HcSwL3PYxJkq_C7bKIG068riW0A5Izb0wwSJ_dtcQlD8F5gfq3ypQ55o-ITAjClEiwqhw-VpErlMAfrPwwDgK6AMcUK9Ndgwpqdy6dqSL3ZuKJKXIVQg68-1uifxVWTAXtCJL8vldJShBZW0c6ERhQ480F5NcCqHO3xQ)
* **Integración Signal Blue (`#2749ff`):** Borde superior decorativo de 2px en la tarjeta de autenticación, anillo de foco del input Cédula y contorno sutil en el distintivo territorial "Entidad Federal 16".

---

### 2. Pantalla 02: Dashboard Ejecutivo Central (Gerente Estadal)
* **ID en Stitch:** `63ff12e3acc74c35a768bff153730d97` *(Variante previa: `2ef97faa39c7420fbe31e1ea4cdc37a2`)*
* **Dispositivo:** Desktop (1440px / 2560px)
* **Descripción:** Cuadro de mando ejecutivo integral y analítico enriquecido con componentes visuales:
  * Minimal Top Navigation con credencial del Gerente (`V-12345678 · GERENTE ESTADAL`).
  * Display Headline regular: `MONAGAS / INFORME DE GESTIÓN` (Agosto 2026).
  * Stat Block Row: Cumplimiento global estadal (`94.2%`), 13 municipios, 5 departamentos y 28 indicadores certificados.
  * **Visualizaciones Gráficas (Charts):**
    * **Curva de Evolución Histórica (Time Series SVG):** Gráfica continua de cumplimiento mensual con trazo nítido en `#2749ff` (grosor 2.5), nodos circulares de datos en `#2749ff` y degradado suave traslúcido bajo la curva.
    * **Medidor Radial / Donut Gauge (94.2%):** Arco de avance activo en `#2749ff` sobre pista base en `#ededed`.
    * **Barras de Distribución y Progreso Técnico:** Barras de cumplimiento rellenas en sólido `#2749ff` para cada departamento y municipio.
  * **Botones Interactivos en Signal Blue:**
    * Botón primario `Exportar Informe Ejecutivo` y `Generar Certificación` con fondo sólido `#2749ff`, texto `#ffffff` y radio de 3px.
    * Pestaña activa de período (`Mensual Agosto 2026`) en fondo `#2749ff`.
    * Botones secundarios y filtros (`Descargar Consolidado CSV`, `Filtrar por Cumplimiento`) con borde de 1px en `#2749ff` y texto en `#2749ff`.
* **Captura Oficial:** [Ver Screenshot en Alta Resolución (Con Botones y Gráficas en Signal Blue)](https://lh3.googleusercontent.com/aida/AEtjO1UoDZwfqg0x5xXnxOQS6ZNPOU44iqpUrDE7ZIsQZkDASlIssuJyMyAynQt8muI-D-bWUnLFOD9WfpGGJfA2RXWwbsM74gxEy8t-OJLzKpjJ0U7zwNeSkAMzsLgZPI-BQ_n1VF_NYO8bAA00X2nxTGAG18T2Id3K5iH0AiaOZPFeJ5rYbqcbxOPRjAjUisgfMU2saaBNlYUllLzoYBxEjeZQ3qqLHTL9eZXyABHV3hBUqI3DBhUEglttaUs)

---

### 3. Pantalla 03: Panel Operativo & Rollback de Versiones (Encargado)
* **ID en Stitch:** `7dd42f77ad7147b1bcbb4279f9307fbe` *(Variante previa: `2d30f9628e6942e582271968f3d56548`)*
* **Dispositivo:** Desktop (1440px / 2560px)
* **Descripción:** Panel de trabajo técnico para el Encargado de Unidad (Estadísticas Económicas):
  * Matriz operativa de captura mensual por indicador (`ECO-IP-01`, `ECO-IPC-01`, `ECO-AGR-01`).
  * **Botones de Acción en Signal Blue:**
    * Botón de acción principal `+ Cargar Cifra` / `REGISTRAR MEDICIÓN` en fondo sólido `#2749ff` y texto blanco.
    * Botón de reversión segura `EJECUTAR REVERSIÓN A VERSIÓN 2 (ROLLBACK)` destacado con fondo sólido `#2749ff`, texto `#ffffff`, esquinas de 3px y cero sombras.
    * Botones de acción en tabla (`Certificar y Aprobar`, `Historial Versiones`) estilizados con borde de 1px en `#2749ff` y texto `#2749ff`.
    * Pestañas de estado operativo (`Todos`, `Aprobados`, `Borrador`) con botón activo en fondo `#2749ff`.
  * **Visualizaciones Gráficas (Charts):**
    * **Sparklines de Tendencia en Tabla:** Micro-gráficas vectoriales SVG de tendencia mensual por indicador con línea y nodos en `#2749ff`.
    * **Barra de Progreso Operativo:** Medidor de avance en cabecera (`24 / 28 Indicadores Certificados · 85.7%`) con barra de progreso rellena en `#2749ff`.
    * **Gráfica Comparativa Diff / Auditoría:** Barra de referencia válida (`Valor Base Sano V.2: 542.00`) rellena en `#2749ff` contrastando la anomalía (`99,999.00`).
    * **Timeline de Versiones:** Nodo de restauración objetivo (`Versión 2`) con conector e indicador nodal circular en `#2749ff`.
* **Captura Oficial:** [Ver Screenshot en Alta Resolución (Con Botones y Gráficas en Signal Blue)](https://lh3.googleusercontent.com/aida/AEtjO1WpSt3xOIrYliu32s_-USxrzeBubzBhTQD2U3NiAgP8m2NQ-XdNkSbS5FmwaIqzyL2lZa7_7Ao2qoVs0GC6tUixUVL5x0l87dd0n2Q6at9ztDelMXD1k13X5k45I2vx_upMRWumakiF5S7L4HnWQBoPsVmiJMLn7f1wNVafMg-e6jsbkW57PqnBbFDAfLTtYqYCaA2ppsi_oZM-KKlhs8fcYbO7v2DaWg7gaqECIkQPpNPrF7PdXLEQ4OU)

---

### 4. Pantalla 04: Dashboard Ejecutivo Móvil (Gerente en Smartphone)
* **ID en Stitch:** `9bb9b6a5c3ae489ca30a0d922e5711d2` *(Variante previa: `42e6ceadd4d14c4eaf2d0af595e4c1c2`)*
* **Dispositivo:** Mobile (375px / 780px)
* **Descripción:** Adaptación ergonómica y táctil enriquecida con gráficas móviles y botones activos:
  * Top bar compacta con identificador institucional `INE MONAGAS` y badge `E-16`.
  * **Botones y Controles Móviles en Signal Blue:**
    * Selector segmentado de período (`Mensual Ago 2026`) con fondo sólido `#2749ff` y texto `#ffffff`.
    * Botón de acción principal `Descargar PDF` con fondo sólido `#2749ff`, texto blanco y 3px de radio.
    * Botón secundario `Filtrar Municipios` con borde y texto en `#2749ff` y fondo traslúcido.
    * Barra inferior de navegación (`Bottom Bar`): Pestaña activa `Resumen` con indicador superior de 2px, icono y texto en `#2749ff`.
  * **Visualizaciones Gráficas Móviles (Charts):**
    * **Gráfica Histórica SVG Móvil:** Serie temporal mensual (Ene - Ago 2026) con trazo en `#2749ff`, puntos de muestreo en `#2749ff` y degradado suave inferior.
    * **Medidor Circular / Gauge (94.2%):** Anillo de progreso SVG con arco activo en `#2749ff`.
    * **Barras de Avance Territorial:** Barras horizontales de progreso en los municipios y unidades técnicas rellenas en `#2749ff`.
* **Captura Oficial:** [Ver Screenshot en Alta Resolución (Con Botones y Gráficas en Signal Blue)](https://lh3.googleusercontent.com/aida/AEtjO1VDamLWmkD-2ZC-YM0IzCQOH0yl_ardJuU5jLu4WUJpHDhQLpPx8oWjdyIvvjDzjvWrI89YxAvlPBKFV6G2rzzf_OPuRVIg8araooPuD7aKS6pLwc2kRIRPWQfpo0uSpP2RhYUQrDHnBxOW-giFbMDLgQL2yZng2S5ww2QDN5V3RoiIr03NciZELYBgcZPcOkLSTynktOI9gSu1mLAclDMsJA_d6CjT-ErU_bP4Oqw5amkk6k_cUr75Dms)

---

### 5. Pantalla 05: Dashboard Simplificado por Unidades (Desktop — Unit-First Hub)
* **ID en Stitch:** `3855e87a95e249feba1456497617fee1`
* **Dispositivo:** Desktop (1440px / 2560px)
* **Arquitectura Simplificada:**
  * **Top Hub de Unidades (Primera Sección):** Fila interactiva superior con acceso directo a las 5 unidades de estadística (`[ECO] ECONÓMICAS`, `[SOC] SOCIALES`, `[DEM] DEMOGRAFÍA`, `[CART] CARTOGRAFÍA`, `[SEG] CALIDAD`) más `[CONSOLIDADO] MONAGAS`.
  * **Pestaña Activa (`[ECO]`):** Resaltada en **Signal Blue (`#2749ff`)** con tipografía blanca, badge `VISTA ACTIVA` y métrica integrada (`98.4% · 6 Indicadores`).
  * **Vista Focalizada de la Unidad Seleccionada:**
    * Ficha de la unidad con Coordinación asignada (*Coordinación de Estadísticas Económicas*), período y badge `CERTIFICADO AL 98.4%`.
    * Botones primarios de exportación en `#2749ff` (`Exportar Informe ECO (PDF)` y `Descargar Matriz CSV`).
    * **Gráficas Específicas ECO:** Anillo gauge radial (98.4%), serie temporal histórica mensual SVG (Ene-Ago) en `#2749ff` y gráfica de barras metas vs captura.
    * **Tabla de Indicadores ECO:** Fichas exclusivas de economía (`ECO-IP-01`, `ECO-IPC-01`, `ECO-AGR-01`, `ECO-PET-01`, `ECO-COM-01`) con enlaces directos a ficha técnica e inspección Diff.
    * **Cobertura Territorial ECO:** Barras de cumplimiento por municipio en sólido `#2749ff`.
* **Captura Oficial:** [Ver Screenshot en Alta Resolución (Dashboard Simplificado Desktop)](https://lh3.googleusercontent.com/aida/AEtjO1X2l-kKYibe1uo832PGWshFcqUyJUlV_pBLh1FXN-urnxQCb8um6ZhcxnZ5qwYiRpoGgVpovZGe6Ykia_UJuKnludI8vgRJkpIZo2Eh5M8MKAsd8gFvDt_rtr3A8MghKOisPlur6uj9xVT93xWxhb0A0TCKF24jAfPipt29mX3Kg0-aI0dJBJK8n98P_8zjDQwUWGRp2-Iz38zjUvYWFMuFJm3IBYdcv8cpTHlhNdUa3VwaouzjWu3KiL8)

---

### 6. Pantalla 06: Dashboard Móvil Focalizado por Unidad (Mobile — Unit-First)
* **ID en Stitch:** `dbc051f6557441a4a1006601c255faf9`
* **Dispositivo:** Mobile (375px / 780px)
* **Arquitectura Simplificada:**
  * **Selector Horizontal de Unidades en Cabecera:** Carrusel superior táctil con botón activo `[ECO] ECONÓMICAS` en fondo sólido `#2749ff` con tipografía blanca y botones secundarios delimitados en líneas finas de 1px ash.
  * **Contenido Modular de la Unidad Activa:**
    * Ficha ejecutiva de la unidad con botón táctil `Descargar Reporte ECO (PDF)` en `#2749ff`.
    * Medidor radial gauge SVG para el 98.4% y gráfica de tendencia histórica móvil en `#2749ff`.
    * Tarjetas de los indicadores económicos individuales con barras de avance en `#2749ff`.
    * Desglose territorial de captura por municipio en Monagas.
    * Barra de navegación inferior con acceso a unidades activas.
* **Captura Oficial:** [Ver Screenshot en Alta Resolución (Dashboard Simplificado Móvil)](https://lh3.googleusercontent.com/aida/AEtjO1UWPlBAAwYfgL0C3mAPPUjRxEWuOQZINJ0owl7uTTj7AH_bV9IYpuJj7swXnSM_ZqOGM9CTV2QHc8mzt8PM_6_Gy6HuZdnvy_9phZMGQHQS_B-kWui806s-gRKTx1QkkdJthW3fQm4yXISc6z3JIQ5y8g4fjFhFXQikbLwMKXzQJ6hfjiKdLVr3vQfy6aEe0qhEPAbLQgFdrbQrpW565KRuXO6ebTn_JgwiF-BCFttpMNUE-BccQ39LzeU)
