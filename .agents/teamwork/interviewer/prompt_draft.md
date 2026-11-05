Perform a formal requirements analysis and recommendations report for operational production planning of the Sistema de Indicadores de Gestión for the Instituto Nacional de Estadística (INE) Gerencia Estadal Monagas (Entidad Federal 16), identifying gaps, new requirements, and the technical and business justifications for why each should be implemented.

Working directory: /home/seem/Documentos/_proyectos/sistema-indicadores
Integrity mode: development

## Verification Resources
- Qualitative official source: `FORMATO INFORME DE GESTION GERENCIAS ESTADALES JULIO 2026.docx` (12 official Líneas de Acción from INE Central Caracas).
- Quantitative official source: `Cuadros Informe Mensual de Gestion Gerencias Estadales MONAGAS AGOSTO 2026.xlsx` (29 management indicators across 5 departments: Sociales, Demográficas, Económicas, Cartografía, SEGEN, plus Coordinación/Gerencia).
- Existing formal SRS: `docs/SRS_SISTEMA_INDICADORES.md` (ISO/IEC/IEEE 29148 and IEEE 830).
- Indicator catalog: `docs/catalogo_indicadores_reales.md`.
- Database schema: `docs/database_model.md`.

## Requirements

### R1. Formal Requirements Analysis and Gap Assessment Document
Deliver a formal engineering report in `docs/` (e.g., `docs/ANALISIS_REQUERIMIENTOS_Y_MEJORAS.md`) containing:
1. A gap analysis comparing the existing implementation and SRS (`docs/SRS_SISTEMA_INDICADORES.md`) against the 12 official Líneas de Acción (`FORMATO INFORME DE GESTION...`) and the 29 operational indicators across all 5 departments plus Coordinación/Gerencia (`Cuadros Informe Mensual...`).
2. Proposed new functional and non-functional requirements to bridge identified gaps and improve operational performance.
3. A prioritized implementation roadmap (categorized using MoSCoW: Must have, Should have, Could have, Won't have) leaving code implementation for subsequent tasks.

### R2. Detailed Technical and Business Justifications
For every proposed requirement or improvement, provide:
1. A clear operational/business rationale explaining why it should be implemented for INE Gerencia Estadal Monagas.
2. An architectural and technical impact assessment across the project stack: FastAPI backend (Python 3.11), PostgreSQL database schema (SQLAlchemy 2.0), and Vue 3 frontend (TypeScript, Vite, Tailwind CSS v4).
3. A traceability matrix mapping each proposed requirement to its corresponding Línea de Acción, operational department, and management indicator.

### R3. Institutional UI/UX Design Compliance
Ensure all proposed interface or frontend-impacting requirements strictly comply with the institutional UI/UX design rules: zero emojis in the user interface (vector SVG icons only, such as Lucide or Heroicons) and the institutional editorial tokens (monochrome Ink Black `#000000`, Steel `#686c6d`, Signal Blue `#2749ff`, 3px border radius, and zero diffuse shadows `box-shadow: none`).

## Acceptance Criteria

### Gap Analysis & Requirements Completeness
- [ ] The analysis document exists in `docs/` and comprehensively covers all 12 Líneas de Acción and all 29 indicators across the 5 departments (Sociales, Demográficas, Económicas, Cartografía, SEGEN) and Coordinación/Gerencia.
- [ ] Discrepancies and missing features between the existing `docs/SRS_SISTEMA_INDICADORES.md` and the official Excel and Word sources are systematically cataloged.

### Rationale and Technical Impact
- [ ] Each new or improved requirement is specified with a unique identifier, description, priority (MoSCoW), business justification ("why it should be implemented"), and technical impact on backend, database, and frontend.
- [ ] A traceability matrix explicitly connects each requirement to its source Línea de Acción and quantitative indicator.
- [ ] No code modifications are applied to source code files (`src/`, `backend/`, `frontend/`, etc.); deliverables are strictly analytical documentation.

### UI/UX Standards Alignment
- [ ] All proposed UI components or dashboard views in the document explicitly specify the use of vector SVG icons and forbid emojis in user-facing elements.
- [ ] Proposed UI specifications adhere to institutional design tokens (colors `#000000`, `#686c6d`, `#2749ff`, `border-radius: 3px`, and `box-shadow: none`).
