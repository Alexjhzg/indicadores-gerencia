# 📊 Catálogo Maestro de Indicadores de Gestión — INE Monagas (Entidad 16)
## Basado en el Informe Mensual Oficial de Gestión (Agosto 2026)

> **Documento Fuente:** `Cuadros Informe Mensual de Gestion Gerencias Estadales MONAGAS AGOSTO 2026.xlsx`  
> **Ámbito:** Instituto Nacional de Estadística (INE) — Gerencia Estadal Monagas (Entidad Federal 16)  
> **Aprobado por:** Líder Técnico & Dirección de Gestión Estadística  
> **Propósito:** Catálogo oficial y normativo de indicadores, variables, fórmulas de cálculo y metas operativas para alimentar la base de datos, las APIs y los tableros del Sistema de Indicadores.

---

## 🏛️ Estructura Orgánica de Unidades Técnicas

El Sistema de Indicadores estructura la gestión estadística del Estado Monagas en **5 Unidades Técnicas Operativas** y **1 Unidad de Coordinación General**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   GERENCIA ESTADAL MONAGAS · INE (ENTIDAD 16)                          │
├────────────────────┬────────────────────┬────────────────────┬─────────────────────────┤
│ 1. SOC             │ 2. DEM             │ 3. ECO             │ 4. CART                 │
│ Estadísticas       │ Estadísticas       │ Estadísticas       │ Cartografía Estadística │
│ Sociales           │ Demográficas       │ Económicas         │ y Circuitos Comunales   │
├────────────────────┴────────────────────┴────────────────────┴─────────────────────────┤
│ 5. SEG (SEGEN)                                                                         │
│ Estructura, Nodos Territoriales y Encuestas Digitales del SEGEN                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 6. GER / ADM                                                                           │
│ Gestión Institucional, Talento Humano y Comités Estadales (CCEE)                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 1. UNIDAD DE ESTADÍSTICAS SOCIALES (`SOC`)
* **Responsable:** Jefe de Unidad de Estadísticas Sociales  
* **Fuente Operativa:** Hoja `LA 1.Estadísticas Sociales`

### 1.1 Encuesta de Hogares por Muestreo (EHM)

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`SOC-EHM-01`** | **Tasa de Levantamiento de Controles EHM** | Mide el porcentaje de sectores/controles de muestra levantados efectivamente respecto a los planificados en el mes. | `(Controles Levantados / Controles Planificados) * 100` | `%` | Mensual | `100.0%` | **84.62%** *(11 de 13 controles)* |
| **`SOC-EHM-02`** | **Viviendas Efectivas Entrevistadas EHM** | Cuantifica el volumen de hogares con entrevistas efectivas completadas. | `Σ Viviendas Efectivas investigadas` | `Viviendas` | Mensual | `172` | **97 viviendas** *(Acum. 2026: 699)* |
| **`SOC-EHM-03`** | **Tasa de No Respuesta EHM** | Evalúa el porcentaje de viviendas que no pudieron investigarse por rechazo o ausencia prolongada (Tipo A). | `(Viviendas Tipo A / (Viviendas Efectivas + Tipo A)) * 100` | `%` | Mensual | `≤ 15.0%` | **20.49%** *(25 viviendas Tipo A)* |

### 1.2 Encuesta de Seguimiento al Consumo de Alimentos (ESCA)

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`SOC-ESCA-01`** | **Tasa de Levantamiento de Controles ESCA** | Mide la cobertura operativa de los controles programados para la muestra de consumo de alimentos. | `(Controles Levantados / Controles Planificados) * 100` | `%` | Mensual | `100.0%` | **82.61%** *(19 de 23 controles)* |
| **`SOC-ESCA-02`** | **Viviendas Efectivas Entrevistadas ESCA** | Volumen de viviendas con registro efectivo de consumo y adquisición de alimentos. | `Σ Viviendas Efectivas ESCA` | `Viviendas` | Mensual | `287` | **139 viviendas** *(Acum. 2026: 1,109)* |
| **`SOC-ESCA-03`** | **Tasa de No Respuesta ESCA** | Porcentaje de no respuesta por rechazo o ausencia temporal de hogares en el estudio de consumo alimentario. | `(Viviendas Tipo A / (Viviendas Efectivas + Tipo A)) * 100` | `%` | Mensual | `≤ 20.0%` | **28.35%** *(55 viviendas Tipo A)* |

---

## 📋 2. UNIDAD DE DEMOGRAFÍA Y ESTADÍSTICAS VITALES (`DEM`)
* **Responsable:** Jefe de Unidad de Demografía y Estadísticas Vitales  
* **Fuente Operativa:** Hoja `LA 2.Estadísticas Demográficas` y `LA 9. Comites Estadales`

### 2.1 Flujo y Procesamiento de Boletas Vitales

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`DEM-VIT-01`** | **Volumen Total de Boletas Vitales Recolectadas** | Captura continua de hechos vitales (Nacimientos, Defunciones, Matrimonios, Unión Estable, Divorcios, Suicidios) en registros civiles y hospitales. | `Nacimientos + Defunciones + Matrimonios + Unión + Divorcios + Suicidios` | `Boletas` | Mensual / Anual | `25,000` | **11,615 boletas** *(Año 2026 a Ago)* |
| **`DEM-VIT-02`** | **Cantidad de Nacimientos Registrados** | Monitoreo del volumen de recién nacidos capturados mediante boleta oficial. | `Σ Boletas de Nacimiento` | `Actas` | Mensual / Anual | Continua | **6,972 nacimientos** |
| **`DEM-VIT-03`** | **Cantidad de Defunciones Registradas** | Registro de hechos de mortalidad recolectados en centros de salud y registros civiles. | `Σ Boletas de Defunción` | `Actas` | Mensual / Anual | Continua | **1,987 defunciones** |
| **`DEM-VIT-04`** | **Registro de Nupcialidad y Uniones Estables** | Conteo de matrimonios civiles y declaraciones de uniones estables de hecho. | `Σ Matrimonios + Σ Uniones Estables` | `Actas` | Mensual / Anual | Continua | **1,339 actos** *(790 matr. / 549 uniones)* |
| **`DEM-VIT-05`** | **Tasa de Transcripción y Digitalización Vital** | Porcentaje de boletas físicas ingresadas y codificadas en el sistema informático estadístico. | `(Boletas Transcritas / Boletas Recolectadas) * 100` | `%` | Mensual | `100.0%` | **94.90%** *(11,023 transcritas / 0 rezago)* |

---

## 📋 3. UNIDAD DE ESTADÍSTICAS ECONÓMICAS Y PRECIOS (`ECO`)
* **Responsable:** Jefe de Unidad de Estadísticas Económicas (Gerencia de Precios)  
* **Fuente Operativa:** Hoja `LA 3.Estadísticas Económicas`

### 3.1 Directorio de Tipologías y Canasta Alimentaria Normativa (CAN)

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`ECO-PRE-01`** | **Total Personal Levantamiento Encuesta** | Personal planificado y operativo desplegado en campo para encuestas de precios CAN. | `(Personal Levantamiento / Personal Planificado) * 100` | `Personas` | Mensual | `5` | **5 de 5 personas (100.0%)** *(Acum. 100 de 115)* |
| **`ECO-DIR-01`** | **Total Establecimientos Implantados Directorio de Tipologías de Precios** | Incorporación de nuevas unidades comerciales y tipologías de venta al marco muestral de precios. | `Σ Nuevos establecimientos implantados` | `Locales` | Mensual | `50` | **44 locales** *(Acum. 2026: 1,078)* |
| **`ECO-CAN-04`** | **Total Comunas con Levantamiento CAN (Incluye Complementaria)** | Alcance territorial del levantamiento de precios a nivel de comunas y nodos activos. | `Σ Comunas con levantamiento de precios CAN` | `Comunas` | Mensual | `25` | **25 comunas** *(16 nodos vinculados)* |
| **`ECO-PRE-02`** | **Total Establecimientos Planificados para Levantamiento CAN por Tipologías** | Meta mensual de establecimientos comerciales programados para investigación por canal de venta. | `Σ Establecimientos comerciales planificados` | `Establec.` | Mensual | `34` | **34 establecimientos planificados** |
| **`ECO-CAN-01`** | **Total Establecimientos con Encuesta Efectiva en el Levantamiento de Precios CAN** | Locales comerciales con encuesta efectiva de precios CAN y porcentaje de efectividad sobre la muestra planificada. | `(Establecimientos Efectivos / Establecimientos Planificados) * 100` | `%` | Mensual | `100.0%` | **100.0%** *(34 de 34 planificados)* |
| **`ECO-CAN-02`** | **Total Precios Levantados Reales Efectivos** | Cantidad total de cotizaciones de precios capturadas para los productos de la Canasta Alimentaria. | `Σ Precios / Cotizaciones recolectadas` | `Precios` | Mensual | `2,200` | **2,145 precios** *(Acum. 2026: 18,976)* |
| **`ECO-CAN-03`** | **Total Precios Levantados Reales (Sin Errores)** | Proporción de precios que superaron los controles de rango y consistencia técnica sin incidencias. | `(Precios Sin Errores / Precios Totales) * 100` | `%` | Mensual | `≥ 99.0%` | **99.35%** *(2,131 precios limpios)* |

---

## 📋 4. UNIDAD DE CARTOGRAFÍA ESTADÍSTICA Y CIRCUITOS COMUNALES (`CART`)
* **Responsable:** Jefe de Unidad de Cartografía  
* **Fuente Operativa:** Hoja `LA 6.Circuitos Comunales`

### 4.1 Georreferenciación y Vectorización Territorial

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`CART-CIR-01`** | **Tasa de Vectorización de Circuitos Comunales** | Porcentaje de poligonales de circuitos comunales digitalizadas y cartografiadas en Monagas. | `(Comunas Vectorizadas / Total Circuitos) * 100` | `%` | Mensual | `100.0%` | **97.99%** *(195 de 199 circuitos)* |
| **`CART-CIR-02`** | **Consejos Comunales Georreferenciados** | Total de organizaciones de base comunitaria delimitadas territorialmente dentro de los circuitos. | `Σ Consejos Comunales integrados` | `Consejos` | Mensual | `1,361` | **1,361 consejos comunales** |
| **`CART-CIR-03`** | **Completitud Vectorial Plena (100%)** | Cantidad de comunas y circuitos cuya poligonal está 100% cerrada y validada con sus organizaciones de base. | `Σ Circuitos con 100% de vectorización` | `Circuitos` | Mensual | `199` | **177 circuitos al 100%** *(18 parciales, 4 pendientes)* |
| **`CART-MUN-01`** | **Cobertura Cartográfica por Municipio** | Distribución y seguimiento de poligonales en los 13 municipios de la entidad federal. | `Desglose territorial municipal (Maturín 90, Caripe 15, etc.)` | `Municipios` | Mensual | `13` | **13 municipios cubiertos** |

---

## 📋 5. UNIDAD DE SEGUIMIENTO, ESTRUCTURA SEGEN Y OPERACIONES DIGITALES (`SEG`)
* **Responsable:** Jefe de Unidad de SEGEN  
* **Fuente Operativa:** Hojas `LA 4.Estructura SEGEN`, `LA 5.Encuestas en el SEGEN` y `LA 8.Capacitacion`

### 5.1 Red de Nodos y Parque Tecnológico SEGEN

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`SEG-NOD-01`** | **Tasa de Operatividad de Nodos SEGEN** | Porcentaje de nodos instalados que transmiten y operan activamente en el territorio monaguense. | `(Nodos Activos / Nodos Instalados) * 100` | `%` | Mensual | `≥ 80.0%` | **47.17%** *(50 activos de 106 instalados)* |
| **`SEG-NOD-02`** | **Cumplimiento de Despliegue de Nodos** | Proporción de nodos instalados en campo respecto al plan maestro institucional. | `(Nodos Instalados / Nodos Planificados) * 100` | `%` | Mensual | `100.0%` | **108.16%** *(106 instalados / 98 planif.)* |
| **`SEG-PAR-01`** | **Disponibilidad de Dispositivos Móviles de Captura (DMC)** | Equipos digitales de captura activos en despliegue operativo en campo. | `Σ DMCs operativos en campo` | `Equipos` | Mensual | `350` | **315 DMCs en campo** *(48 Laptops/MiniPC)* |
| **`SEG-PER-01`** | **Despliegue de Fuerza Territorial SEGEN** | Dotación operativa de personal desplegado en la red territorial de los 13 municipios. | `Σ Coord. Municipales + Coord. Nodos + Supervisores + Encuestadores` | `Personas` | Mensual | `210` | **208 funcionarios en campo** |

### 5.2 Levantamiento Digital de Encuestas en Plataforma SEGEN (ODK)

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`SEG-ENC-01`** | **Volumen Mensual de Encuestas Digitales SEGEN** | Captura consolidada de cuestionarios electrónicos a través de la infraestructura ODK y SEGEN. | `Σ Formularios capturados en todas las investigaciones del mes` | `Encuestas` | Mensual | `25,000` | **28,147 encuestas en Agosto** *(Total 2026: 257,255)* |
| **`SEG-ENC-02`** | **Captura Formulario Intercensal (Conteo Rápido v2)** | Cuestionarios del conteo rápido de estructuras y población procesados en el mes. | `Σ Formularios Conteo Rápido v2` | `Encuestas` | Mensual | `15,000` | **14,281 encuestas** *(Acum: 59,710)* |
| **`SEG-ENC-03`** | **Captura Encuesta de Coyuntura Económica y Laboral** | Volumen de cuestionarios de coyuntura social, laboral y productiva recolectados en nodos. | `Σ Encuesta Coyuntura + Consulta Laboral + ODK Económica` | `Encuestas` | Mensual | `8,000` | **8,376 encuestas** *(Coyuntura 3,227, Laboral 2,591, Económica 2,558)* |
| **`SEG-CAP-01`** | **Personal Capacitado en Metodologías Estadísticas** | Funcionarios y líderes de nodo formados en protocolos de levantamiento y verificación. | `Σ Personas capacitadas en planes de formación del mes` | `Personas` | Mensual | `100` | **145 personas capacitadas** *(129 personal INE + 16 campo)* |

---

## 📋 6. GERENCIA ESTADAL Y COORDINACIÓN INSTITUCIONAL (`GER`)
* **Responsable:** Gerente Estadal de Monagas  
* **Fuente Operativa:** Hojas `LA 9. Comites Estadales` y `LA 10.Gerencia Estadal`

| Código | Indicador | Descripción y Objetivo | Fórmula de Cálculo | Unidad | Frecuencia | Meta Base | Cifra Real Ago 2026 |
|---|---|---|---|---|---|---|---|
| **`GER-CCEE-01`** | **Sesiones de Comité de Coordinación Estadística (CCEE)** | Mesas técnicas interinstitucionales realizadas con entes del Estado (Salud, CNE, Gobernación). | `Σ Reuniones técnicas celebradas en el mes` | `Sesiones` | Mensual | `1` | **1 sesión** *(Mesa Registros Vitales Salud-CNE-INE)* |
| **`GER-TAL-01`** | **Planta de Personal Activo de la Gerencia Estadal** | Dotación de funcionarios adscritos a la sede regional del INE Monagas. | `Σ Personal Fijo + Personal Contratado activo` | `Trabajadores`| Mensual | `44` | **44 trabajadores** *(39 contratados + 5 fijos + 10 jubilados)* |

---

## 📊 Matriz de Resumen Cuantitativo por Unidad Técnica

| Unidad / Departamento | Código Depto | N° Indicadores Clave | Tipo Principal de Métrica | Fuente Oficial |
|---|---|---|---|---|
| **Estadísticas Sociales** | `SOC` | **6** | Tasas de levantamiento, viviendas efectivas y tasas de no respuesta (EHM y ESCA). | `LA 1.Estadísticas Sociales` |
| **Estadísticas Demográficas** | `DEM` | **5** | Volumen de boletas vitales, nacimientos, defunciones, nupcialidad y tasa de transcripción. | `LA 2.Estadísticas Demográficas` |
| **Estadísticas Económicas** | `ECO` | **5** | Directorio de establecimientos, efectividad CAN, volumen de precios y calidad sin errores. | `LA 3.Estadísticas Económicas` |
| **Cartografía Estadística** | `CART` | **4** | Tasa de circuitos vectorizados, consejos comunales integrados y completitud de poligonales. | `LA 6.Circuitos Comunales` |
| **Seguimiento y SEGEN** | `SEG` | **7** | Nodos activos, parque tecnológico, fuerza territorial, encuestas ODK y capacitación. | `LA 4`, `LA 5` y `LA 8` |
| **Gerencia Estadal** | `GER` | **2** | Comités CCEE interinstitucionales y talento humano activo. | `LA 9` y `LA 10` |
| **TOTAL SISTEMA INE MONAGAS** | — | **29 Indicadores** | **100% de cobertura operacional del informe de gestión real.** | **Informe Agosto 2026** |
