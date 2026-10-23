-- =============================================================================
-- INE MONAGAS - DATOS SEMILLA E INDICADORES REALES (AGOSTO 2026)
-- =============================================================================

-- 1. Insertar Usuarios Base
INSERT INTO usuarios (id, cedula, nombre_completo, password_hash, rol_id, departamento_id) VALUES
('a0000000-0000-0000-0000-000000000001', 'V-10000000', 'Administrador General INE', 'pbkdf2_sha256$hashedpasswordadmin', 1, NULL),
('a0000000-0000-0000-0000-000000000002', 'V-12345678', 'Gerente Estadal Monagas', 'pbkdf2_sha256$hashedpasswordgerente', 2, NULL),
('a0000000-0000-0000-0000-000000000003', 'V-20000001', 'Encargado Económica', 'pbkdf2_sha256$hashedpassword', 3, 1),
('a0000000-0000-0000-0000-000000000004', 'V-20000002', 'Encargado Sociales', 'pbkdf2_sha256$hashedpassword', 3, 2),
('a0000000-0000-0000-0000-000000000005', 'V-20000003', 'Encargado Demográficas', 'pbkdf2_sha256$hashedpassword', 3, 3),
('a0000000-0000-0000-0000-000000000006', 'V-20000004', 'Encargado Cartografía', 'pbkdf2_sha256$hashedpassword', 3, 4),
('a0000000-0000-0000-0000-000000000007', 'V-20000005', 'Encargado SEGEN', 'pbkdf2_sha256$hashedpassword', 3, 5)
ON CONFLICT (cedula) DO NOTHING;

-- 2. Insertar Categorías Reales
INSERT INTO categorias (id, departamento_id, nombre, descripcion) VALUES
(1, 1, 'Gerencia de Precios y Cesta Alimentaria', 'Levantamiento de la CAN y directorio de tipologías de precios'),
(2, 2, 'Encuestas de Hogares (EAM)', 'Investigaciones estadales y seguimiento de viviendas'),
(3, 3, 'Estadísticas Vitales', 'Nacimientos, defunciones, matrimonios y flujo de boletas'),
(4, 4, 'Circuitos Comunales y Vectorización', 'Vectorización y poligonales de comunas y consejos comunales'),
(5, 5, 'Estructura Nodos y ODK', 'Despliegue de nodos y encuestas digitales ODK')
ON CONFLICT (departamento_id, nombre) DO NOTHING;

-- Resetear secuencia de categorías
SELECT setval('categorias_id_seq', (SELECT MAX(id) FROM categorias));

-- 3. Insertar Indicadores Reales (Extraídos del Informe Agosto 2026)
INSERT INTO indicadores (id, codigo, nombre, descripcion, departamento_id, categoria_id, unidad_medida, frecuencia, tipo_meta, meta_referencial) VALUES
('b0000000-0000-0000-0000-000000000001', 'ECO-PRE-01', 'Personal en Levantamiento CAN', 'Total personal en operaciones de campo para levantamiento de encuestas CAN', 1, 1, 'Personas', 'MENSUAL', 'ASCENDENTE', 5.0),
('b0000000-0000-0000-0000-000000000002', 'ECO-PRE-02', 'Establecimientos con Encuesta Efectiva CAN', 'Total establecimientos comerciales con encuesta efectiva de precios CAN', 1, 1, 'Establecimientos', 'MENSUAL', 'ASCENDENTE', 34.0),
('b0000000-0000-0000-0000-000000000003', 'SOC-EAM-01', 'Efectividad Operativa de Sectores EAM', 'Sectores levantados efectivamente vs planificados', 2, 2, 'Sectores', 'MENSUAL', 'ASCENDENTE', 13.0),
('b0000000-0000-0000-0000-000000000004', 'SOC-EAM-02', 'Viviendas Efectivas EAM', 'Viviendas encuestadas efectivamente en el mes', 2, 2, 'Viviendas', 'MENSUAL', 'ASCENDENTE', 172.0),
('b0000000-0000-0000-0000-000000000005', 'DEM-VIT-01', 'Nacimientos Registrados (Acumulado 2026)', 'Boletas de nacimientos recolectadas y transcritas', 3, 3, 'Personas', 'ANUAL', 'ASCENDENTE', 7000.0),
('b0000000-0000-0000-0000-000000000006', 'SEG-ODK-01', 'Formulario Intercensal Conteo Rápido ODK', 'Total encuestas digitales cargadas en el sistema ODK', 5, 5, 'Encuestas', 'MENSUAL', 'ASCENDENTE', 15000.0),
('b0000000-0000-0000-0000-000000000007', 'CART-VEC-01', 'Comunas y Circuitos Vectorizados', 'Comunas con poligonales cartográficas vectorizadas al 100%', 4, 4, 'Comunas', 'MENSUAL', 'ASCENDENTE', 199.0)
ON CONFLICT (codigo) DO NOTHING;

-- 4. Insertar Mediciones Reales para Agosto 2026
INSERT INTO mediciones_indicador (id, indicador_id, municipio_id, periodo_anio, periodo_tipo, periodo_mes, valor_registrado, meta_periodo, estado, observaciones, registrado_por, aprobado_por) VALUES
('c0000000-0000-0000-0000-000000000001', 'b0000000-0000-0000-0000-000000000001', NULL, 2026, 'MENSUAL', 8, 5.0, 5.0, 'APROBADO', 'Levantamiento completado al 100% en agosto 2026', 'a0000000-0000-0000-0000-000000000003', 'a0000000-0000-0000-0000-000000000003'),
('c0000000-0000-0000-0000-000000000002', 'b0000000-0000-0000-0000-000000000002', NULL, 2026, 'MENSUAL', 8, 34.0, 34.0, 'APROBADO', '34 de 34 establecimientos planificados completados', 'a0000000-0000-0000-0000-000000000003', 'a0000000-0000-0000-0000-000000000003'),
('c0000000-0000-0000-0000-000000000003', 'b0000000-0000-0000-0000-000000000003', NULL, 2026, 'MENSUAL', 8, 11.0, 13.0, 'APROBADO', '11 de 13 sectores efectivos en el mes de agosto', 'a0000000-0000-0000-0000-000000000004', 'a0000000-0000-0000-0000-000000000004'),
('c0000000-0000-0000-0000-000000000004', 'b0000000-0000-0000-0000-000000000004', NULL, 2026, 'MENSUAL', 8, 97.0, 172.0, 'APROBADO', '97 viviendas efectivas encuestadas', 'a0000000-0000-0000-0000-000000000004', 'a0000000-0000-0000-0000-000000000004'),
('c0000000-0000-0000-0000-000000000005', 'b0000000-0000-0000-0000-000000000005', NULL, 2026, 'ANUAL', 8, 6972.0, 7000.0, 'APROBADO', '6.972 nacimientos registrados en 2026', 'a0000000-0000-0000-0000-000000000005', 'a0000000-0000-0000-0000-000000000005'),
('c0000000-0000-0000-0000-000000000006', 'b0000000-0000-0000-0000-000000000006', NULL, 2026, 'MENSUAL', 8, 14281.0, 15000.0, 'APROBADO', '14.281 encuestas ODK procesadas en el mes de agosto', 'a0000000-0000-0000-0000-000000000007', 'a0000000-0000-0000-0000-000000000007'),
('c0000000-0000-0000-0000-000000000007', 'b0000000-0000-0000-0000-000000000007', NULL, 2026, 'MENSUAL', 8, 195.0, 199.0, 'APROBADO', '195 de 199 comunas vectorizadas en el estado Monagas', 'a0000000-0000-0000-0000-000000000006', 'a0000000-0000-0000-0000-000000000006')
ON CONFLICT (indicador_id, municipio_id, periodo_anio, periodo_tipo, periodo_mes) DO NOTHING;
