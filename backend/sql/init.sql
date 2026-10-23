-- =============================================================================
-- SISTEMA DE INDICADORES - INE ESTADO MONAGAS
-- SCRIPT COMPLETO DE BASE DE DATOS (PostgreSQL)
-- =============================================================================

-- Habilitar extensión UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- -----------------------------------------------------------------------------
-- TIPOS ENUMERADOS (ENUMS)
-- -----------------------------------------------------------------------------
DO $$ BEGIN
    CREATE TYPE tipo_frecuencia AS ENUM ('MENSUAL', 'TRIMESTRAL', 'SEMESTRAL', 'ANUAL');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE tipo_orientacion_meta AS ENUM ('ASCENDENTE', 'DESCENDENTE', 'RANGO');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE estado_medicion AS ENUM ('BORRADOR', 'ENVIADO', 'APROBADO', 'RECHAZADO');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- -----------------------------------------------------------------------------
-- TABLA: ROLES
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- TABLA: DEPARTAMENTOS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS departamentos (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(20) NOT NULL UNIQUE, -- ECO, SOC, DEM, CART, SEG
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- TABLA: USUARIOS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    cedula VARCHAR(20) NOT NULL UNIQUE,
    nombre_completo VARCHAR(150) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL REFERENCES roles(id) ON DELETE RESTRICT,
    departamento_id INT REFERENCES departamentos(id) ON DELETE SET NULL, -- NULL para Gerentes y Admins
    activo BOOLEAN DEFAULT TRUE,
    ultimo_ingreso TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- TABLA: USUARIO_DEPARTAMENTOS (Asignaciones Multi-Unidad para Supervisores)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuario_departamentos (
    id SERIAL PRIMARY KEY,
    usuario_id UUID NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    departamento_id INT NOT NULL REFERENCES departamentos(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_usuario_departamento UNIQUE (usuario_id, departamento_id)
);

-- -----------------------------------------------------------------------------
-- TABLA: MUNICIPIOS (ESTADO MONAGAS)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS municipios (
    id SERIAL PRIMARY KEY,
    codigo_ine VARCHAR(10) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- TABLA: CATEGORIAS DE INDICADORES
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    departamento_id INT NOT NULL REFERENCES departamentos(id) ON DELETE CASCADE,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_categoria_departamento UNIQUE (departamento_id, nombre)
);

-- -----------------------------------------------------------------------------
-- TABLA: INDICADORES
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS indicadores (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    codigo VARCHAR(30) NOT NULL UNIQUE, -- Ej: ECO-PRE-01, DEM-VIT-01
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    departamento_id INT NOT NULL REFERENCES departamentos(id) ON DELETE RESTRICT,
    categoria_id INT REFERENCES categorias(id) ON DELETE SET NULL,
    unidad_medida VARCHAR(50) NOT NULL, -- Porcentaje, Cantidad, Bs., M², Encuestas, etc.
    frecuencia tipo_frecuencia NOT NULL DEFAULT 'MENSUAL',
    tipo_meta tipo_orientacion_meta NOT NULL DEFAULT 'ASCENDENTE',
    meta_referencial NUMERIC(14, 4),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- TABLA: MEDICIONES DE INDICADORES (DATOS CARGADOS)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mediciones_indicador (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    indicador_id UUID NOT NULL REFERENCES indicadores(id) ON DELETE CASCADE,
    municipio_id INT REFERENCES municipios(id) ON DELETE SET NULL, -- NULL indica nivel estadal consolidado
    periodo_anio INT NOT NULL CHECK (periodo_anio BETWEEN 2000 AND 2100),
    periodo_tipo tipo_frecuencia NOT NULL,
    periodo_mes INT NOT NULL CHECK (periodo_mes BETWEEN 1 AND 12),
    valor_registrado NUMERIC(16, 4) NOT NULL,
    meta_periodo NUMERIC(16, 4),
    estado estado_medicion NOT NULL DEFAULT 'BORRADOR',
    observaciones TEXT,
    registrado_por UUID NOT NULL REFERENCES usuarios(id) ON DELETE RESTRICT,
    aprobado_por UUID REFERENCES usuarios(id) ON DELETE SET NULL,
    version INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_medicion_periodo UNIQUE (indicador_id, municipio_id, periodo_anio, periodo_tipo, periodo_mes)
);

-- -----------------------------------------------------------------------------
-- TABLA: VERSIONES DE MEDICIONES (SNAPSHOTS INMUTABLES Y ROLLBACK)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS versiones_medicion (
    id BIGSERIAL PRIMARY KEY,
    medicion_id UUID NOT NULL REFERENCES mediciones_indicador(id) ON DELETE CASCADE,
    numero_version INT NOT NULL,
    valor_registrado NUMERIC(16, 4) NOT NULL,
    meta_periodo NUMERIC(16, 4),
    estado estado_medicion NOT NULL,
    observaciones TEXT,
    tipo_accion VARCHAR(20) NOT NULL DEFAULT 'MODIFICACION', -- CREACION, MODIFICACION, REVERSION, APROBACION
    motivo_cambio TEXT,
    modificado_por UUID REFERENCES usuarios(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_medicion_version UNIQUE (medicion_id, numero_version)
);

CREATE INDEX IF NOT EXISTS idx_versiones_medicion_id ON versiones_medicion(medicion_id);
CREATE INDEX IF NOT EXISTS idx_versiones_fecha ON versiones_medicion(created_at);

-- -----------------------------------------------------------------------------
-- TABLA: AUDITORIA DE MEDICIONES
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS auditoria_mediciones (
    id BIGSERIAL PRIMARY KEY,
    medicion_id UUID NOT NULL REFERENCES mediciones_indicador(id) ON DELETE CASCADE,
    valor_anterior NUMERIC(16, 4),
    valor_nuevo NUMERIC(16, 4),
    estado_anterior VARCHAR(30),
    estado_nuevo VARCHAR(30),
    usuario_id UUID NOT NULL REFERENCES usuarios(id) ON DELETE RESTRICT,
    justificacion TEXT NOT NULL,
    fecha_cambio TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- ÍNDICES DE ALTO RENDIMIENTO
-- -----------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_indicadores_dept ON indicadores(departamento_id);
CREATE INDEX IF NOT EXISTS idx_mediciones_indicador ON mediciones_indicador(indicador_id);
CREATE INDEX IF NOT EXISTS idx_mediciones_periodo ON mediciones_indicador(periodo_anio, periodo_tipo, periodo_mes);
CREATE INDEX IF NOT EXISTS idx_mediciones_estado ON mediciones_indicador(estado);
CREATE INDEX IF NOT EXISTS idx_mediciones_municipio ON mediciones_indicador(municipio_id);

-- -----------------------------------------------------------------------------
-- VISTAS PARA DASHBOARDS
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_dashboard_central_resumen AS
SELECT 
    d.id AS departamento_id,
    d.codigo AS departamento_codigo,
    d.nombre AS departamento_nombre,
    COUNT(DISTINCT i.id) AS total_indicadores,
    COUNT(m.id) AS total_mediciones_registradas,
    COUNT(CASE WHEN m.estado = 'APROBADO' THEN 1 END) AS mediciones_aprobadas,
    COUNT(CASE WHEN m.estado = 'ENVIADO' THEN 1 END) AS mediciones_pendientes_aprobacion,
    ROUND(
        AVG(
            CASE 
                WHEN m.meta_periodo IS NOT NULL AND m.meta_periodo > 0 
                THEN (m.valor_registrado / m.meta_periodo) * 100 
                ELSE NULL 
            END
        ), 2
    ) AS porcentaje_cumplimiento_promedio
FROM departamentos d
LEFT JOIN indicadores i ON i.departamento_id = d.id AND i.activo = TRUE
LEFT JOIN mediciones_indicador m ON m.indicador_id = i.id
WHERE d.activo = TRUE
GROUP BY d.id, d.codigo, d.nombre;

-- -----------------------------------------------------------------------------
-- VISTA DE AUDITORÍA Y CONTROL DE VERSIONES
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_historial_versiones_indicador AS
SELECT 
    v.id AS version_id,
    v.medicion_id,
    i.codigo AS indicador_codigo,
    i.nombre AS indicador_nombre,
    d.codigo AS departamento_codigo,
    d.nombre AS departamento_nombre,
    m.periodo_anio,
    m.periodo_tipo,
    m.periodo_mes,
    mun.nombre AS municipio_nombre,
    v.numero_version,
    v.valor_registrado,
    v.meta_periodo,
    ROUND(
        CASE 
            WHEN v.meta_periodo IS NOT NULL AND v.meta_periodo > 0 
            THEN (v.valor_registrado / v.meta_periodo) * 100 
            ELSE 0 
        END, 2
    ) AS porcentaje_cumplimiento,
    v.estado,
    v.tipo_accion,
    v.motivo_cambio,
    u.nombre_completo AS modificado_por_nombre,
    u.cedula AS modificado_por_cedula,
    v.created_at AS fecha_version
FROM versiones_medicion v
JOIN mediciones_indicador m ON v.medicion_id = m.id
JOIN indicadores i ON m.indicador_id = i.id
JOIN departamentos d ON i.departamento_id = d.id
LEFT JOIN municipios mun ON m.municipio_id = mun.id
LEFT JOIN usuarios u ON v.modificado_por = u.id
ORDER BY v.medicion_id, v.numero_version DESC;

-- -----------------------------------------------------------------------------
-- FUNCIONES Y TRIGGERS DE CONTROL DE VERSIONES Y ROLLBACK
-- -----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION trg_fn_incrementar_version_medicion()
RETURNS TRIGGER AS $$
BEGIN
    IF (OLD.valor_registrado IS DISTINCT FROM NEW.valor_registrado) OR 
       (OLD.meta_periodo IS DISTINCT FROM NEW.meta_periodo) OR 
       (OLD.estado IS DISTINCT FROM NEW.estado) THEN
        IF NEW.version <= OLD.version THEN
            NEW.version := OLD.version + 1;
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_incrementar_version_medicion ON mediciones_indicador;
CREATE TRIGGER trg_incrementar_version_medicion
BEFORE UPDATE ON mediciones_indicador
FOR EACH ROW
EXECUTE FUNCTION trg_fn_incrementar_version_medicion();

CREATE OR REPLACE FUNCTION trg_fn_guardar_version_medicion()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO versiones_medicion (
            medicion_id,
            numero_version,
            valor_registrado,
            meta_periodo,
            estado,
            observaciones,
            tipo_accion,
            motivo_cambio,
            modificado_por,
            created_at
        ) VALUES (
            NEW.id,
            NEW.version,
            NEW.valor_registrado,
            NEW.meta_periodo,
            NEW.estado,
            NEW.observaciones,
            'CREACION',
            'Carga inicial de la medición',
            NEW.registrado_por,
            NEW.created_at
        ) ON CONFLICT (medicion_id, numero_version) DO NOTHING;
        RETURN NEW;
    ELSIF (TG_OP = 'UPDATE') THEN
        IF (OLD.valor_registrado IS DISTINCT FROM NEW.valor_registrado) OR 
           (OLD.meta_periodo IS DISTINCT FROM NEW.meta_periodo) OR 
           (OLD.estado IS DISTINCT FROM NEW.estado) THEN

            INSERT INTO versiones_medicion (
                medicion_id,
                numero_version,
                valor_registrado,
                meta_periodo,
                estado,
                observaciones,
                tipo_accion,
                motivo_cambio,
                modificado_por,
                created_at
            ) VALUES (
                NEW.id,
                NEW.version,
                NEW.valor_registrado,
                NEW.meta_periodo,
                NEW.estado,
                NEW.observaciones,
                CASE 
                    WHEN NEW.observaciones LIKE 'Revertido a versión%' THEN 'REVERSION'
                    WHEN NEW.estado = 'APROBADO' AND OLD.estado != 'APROBADO' THEN 'APROBACION'
                    ELSE 'MODIFICACION'
                END,
                COALESCE(NEW.observaciones, 'Actualización de valor'),
                COALESCE(NEW.aprobado_por, NEW.registrado_por),
                CURRENT_TIMESTAMP
            );

            INSERT INTO auditoria_mediciones (
                medicion_id,
                valor_anterior,
                valor_nuevo,
                estado_anterior,
                estado_nuevo,
                usuario_id,
                justificacion
            ) VALUES (
                NEW.id,
                OLD.valor_registrado,
                NEW.valor_registrado,
                OLD.estado::text,
                NEW.estado::text,
                COALESCE(NEW.aprobado_por, NEW.registrado_por),
                COALESCE(NEW.observaciones, 'Modificación registrada')
            );
        END IF;
        RETURN NEW;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_guardar_version_medicion ON mediciones_indicador;
CREATE TRIGGER trg_guardar_version_medicion
AFTER INSERT OR UPDATE ON mediciones_indicador
FOR EACH ROW
EXECUTE FUNCTION trg_fn_guardar_version_medicion();

-- Función de Reversión (Rollback)
CREATE OR REPLACE FUNCTION fn_revertir_medicion(
    p_medicion_id UUID,
    p_version_destino INT,
    p_usuario_id UUID,
    p_motivo TEXT
) RETURNS JSONB AS $$
DECLARE
    v_version_historica RECORD;
    v_resultado JSONB;
BEGIN
    SELECT * INTO v_version_historica
    FROM versiones_medicion
    WHERE medicion_id = p_medicion_id AND numero_version = p_version_destino;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontró la versión % para la medición con ID %', p_version_destino, p_medicion_id;
    END IF;

    UPDATE mediciones_indicador
    SET valor_registrado = v_version_historica.valor_registrado,
        meta_periodo = v_version_historica.meta_periodo,
        estado = v_version_historica.estado,
        observaciones = 'Revertido a versión ' || p_version_destino || ': ' || p_motivo,
        aprobado_por = p_usuario_id,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = p_medicion_id;

    v_resultado := jsonb_build_object(
        'status', 'SUCCESS',
        'medicion_id', p_medicion_id,
        'version_restaurada', p_version_destino,
        'valor_restaurado', v_version_historica.valor_registrado,
        'motivo', p_motivo,
        'fecha_reversion', CURRENT_TIMESTAMP
    );

    RETURN v_resultado;
END;
$$ LANGUAGE plpgsql;

-- -----------------------------------------------------------------------------
-- DATOS SEMILLA (SEEDS INICIALES - INE MONAGAS)
-- -----------------------------------------------------------------------------

-- Roles
INSERT INTO roles (id, nombre, descripcion) VALUES
(1, 'ADMIN', 'Administrador total del sistema y gestión técnica'),
(2, 'GERENTE', 'Gerente Estadal con acceso de supervisión y solo lectura a estadísticas y dashboards ejecutivos generales'),
(3, 'ENCARGADO', 'Encargado de unidad responsable de cargar, validar y aprobar las mediciones de su departamento'),
(4, 'JEFE_AREA', 'Jefe de Área con control y supervisión sobre múltiples unidades técnicas asignadas')
ON CONFLICT (id) DO NOTHING;

-- Departamentos INE Monagas
INSERT INTO departamentos (id, codigo, nombre, descripcion) VALUES
(1, 'ECO', 'Económica', 'Gerencia de Precios, Cesta Alimentaria Nacional e índices económicos'),
(2, 'SOC', 'Sociales', 'Investigaciones estadales y Encuesta Social de Hogares (EAM)'),
(3, 'DEM', 'Demográficas', 'Estadísticas Vitales, registros de población y flujo de boletas'),
(4, 'CART', 'Cartografía', 'Georreferenciación, poligonales y vectorización de circuitos comunales'),
(5, 'SEG', 'SEGEN', 'Sistema Estadístico y Geográfico Nacional, nodos ODK y tecnología')
ON CONFLICT (id) DO NOTHING;

-- Municipios del Estado Monagas (Entidad 16 - Codificación Oficial INE DPT)
INSERT INTO municipios (id, codigo_ine, nombre) VALUES
(1, '1601', 'Acosta'),
(2, '1602', 'Aguasay'),
(3, '1603', 'Bolívar'),
(4, '1604', 'Caripe'),
(5, '1605', 'Cedeño'),
(6, '1606', 'Ezequiel Zamora'),
(7, '1607', 'Libertador'),
(8, '1608', 'Maturín'),
(9, '1609', 'Piar'),
(10, '1610', 'Punceres'),
(11, '1611', 'Santa Bárbara'),
(12, '1612', 'Sotillo'),
(13, '1613', 'Uracoa')
ON CONFLICT (id) DO UPDATE SET codigo_ine = EXCLUDED.codigo_ine, nombre = EXCLUDED.nombre;

-- Resetear secuencias SERIAL
SELECT setval('roles_id_seq', (SELECT MAX(id) FROM roles));
SELECT setval('departamentos_id_seq', (SELECT MAX(id) FROM departamentos));
SELECT setval('municipios_id_seq', (SELECT MAX(id) FROM municipios));
