# 🤖 Sistema de Agentes del Proyecto (Sistema de Indicadores)

Este documento define la estructura de gobierno, roles y reglas de colaboración para el equipo de agentes de Inteligencia Artificial dedicados al desarrollo del proyecto **Sistema de Indicadores**.

---

## 👥 Equipo de Agentes y Jerarquía

1. **🛠️ Líder Técnico (Tech Lead)** [Agente Principal de Arquitectura]
   - *Habilidad*: [.agents/skills/tech-lead/SKILL.md](file:///home/seem/Documentos/_proyectos/sistema-indicadores/.agents/skills/tech-lead/SKILL.md)
   - *Función*: Define la arquitectura, crea las tareas técnicas, establece estándares de código y supervisa la calidad de todas las entregas.

2. **💻 Desarrollador Backend (Backend Dev)**
   - *Habilidad*: [.agents/skills/backend-dev/SKILL.md](file:///home/seem/Documentos/_proyectos/sistema-indicadores/.agents/skills/backend-dev/SKILL.md)
   - *Función*: Implementación de APIs, lógica de negocio, procesamiento y cálculo de indicadores de negocio.

3. **🎨 Desarrollador Frontend (Frontend Dev)**
   - *Habilidad*: [.agents/skills/frontend-dev/SKILL.md](file:///home/seem/Documentos/_proyectos/sistema-indicadores/.agents/skills/frontend-dev/SKILL.md)
   - *Función*: Desarrollo de la interfaz de usuario, dashboards interactivos, gráficos dinámicos y experiencia de usuario.

4. **🛢️ Arquitecto de Base de Datos (DBA / Data Engineer)**
   - *Habilidad*: [.agents/skills/dba-data-engineer/SKILL.md](file:///home/seem/Documentos/_proyectos/sistema-indicadores/.agents/skills/dba-data-engineer/SKILL.md)
   - *Función*: Diseñar esquemas de base de datos, optimizar consultas de agregación de métricas e índices.

5. **🧪 Agente de Control de Calidad (QA & Testing)**
   - *Habilidad*: [.agents/skills/qa-engineer/SKILL.md](file:///home/seem/Documentos/_proyectos/sistema-indicadores/.agents/skills/qa-engineer/SKILL.md)
   - *Función*: Creación de pruebas unitarias, de integración y end-to-end, validación matemática y funcional.

---

## 📜 Reglas Generales de Colaboración

1. **Flujo Orientado por el Tech Lead**:
   - Toda nueva característica debe pasar primero por la planificación y desglose del **Tech Lead**.
2. **Estándares de Código Obligatorios**:
   - Todo código escrito debe estar fuertemente tipado.
   - Sin parches superficiales: si se detecta un error, investigar la causa raíz en lugar de silenciar excepciones.
3. **Verificación Runtime**:
   - Ninguna tarea se considera completada ("Done") sin ejecutar verificaciones automáticas (linters, builds, tests).
4. **Política Estricta de UI/UX: Cero Emojis en la Interfaz (Solo Iconos Vectoriales SVG)**:
   - Queda **estrictamente prohibido el uso de caracteres emoji** (ej. 📊, 🚀, 📁, ✅, ⚠️, ❌, etc.) dentro de la interfaz de usuario (UI/UX), componentes, plantillas, botones, modales, alertas, tablas, encabezados o textos visibles de la aplicación.
   - Toda simbología, acción o apoyo visual debe implementarse exclusivamente mediante **iconos vectoriales (SVG / Lucide Icons / Heroicons)** geométricos y limpios, con trazo lineal (`stroke-width: 1.5px`), consistentes con la identidad tipográfica y estética editorial del sistema de diseño (monocromáticos en Ink Black `#000000`, Steel `#686c6d` o con acento en Signal Blue `#2749ff`).
   - Los emojis quedan reservados exclusivamente como elemento decorativo en documentación técnica Markdown interna (`.md`), nunca en el código o vistas del producto final.
5. **Estilos y Utilidades Fuera de Componentes (Tailwind CSS v4)**:
   - Para cualquier estilo global, layout estructural o utilidades CSS fuera de los estilos de componentes de Vue.js, se debe emplear **Tailwind CSS v4** integrado vía `@tailwindcss/vite` y `@theme`.
   - Se deben respetar los tokens institucionales (colores Ink Black `#000000`, Steel `#686c6d`, Signal Blue `#2749ff`, esquinas `3px` y **cero sombras** `box-shadow: none !important`).

