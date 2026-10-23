"""
Script para poblar el Catálogo Maestro de Indicadores Oficiales del INE Monagas (Entidad 16)
y sus Mediciones Reales correspondientes al Informe Mensual de Gestión de Agosto 2026.
Fuente: Cuadros Informe Mensual de Gestion Gerencias Estadales MONAGAS AGOSTO 2026.xlsx
"""

import uuid
from decimal import Decimal
from app.core.database import SessionLocal
from app.core.security import get_password_hash
from app.models import (
    Role, Department, Municipality, Category, User,
    Indicator, FrequencyType, TargetOrientationType,
    IndicatorMeasurement, MeasurementStatus, MeasurementVersion
)

def seed_database():
    db = SessionLocal()
    try:
        print("🌱 Iniciando carga y sincronización de Indicadores Oficiales INE Monagas...")
        
        # 1. Departamentos Reales (5 Unidades Técnicas Oficiales)
        depts_data = [
            ("ECO", "Estadísticas Económicas", "Gerencia de Precios, Directorio de Tipologías y Canasta Alimentaria Normativa (CAN)"),
            ("SOC", "Estadísticas Sociales", "Encuesta de Hogares por Muestreo (EHM) y Encuesta de Seguimiento al Consumo de Alimentos (ESCA)"),
            ("DEM", "Estadísticas Demográficas", "Registro continuo de hechos vitales (Nacimientos, Defunciones, Nupcialidad) y flujo de boletas"),
            ("CART", "Cartografía Estadística", "Proyecto Circuitos Comunales, consejos comunales y vectorización territorial con IGVSB"),
            ("SEG", "Estructura y Encuestas SEGEN", "Red de Nodos territoriales, parque tecnológico DMC y encuestas ODK"),
            ("SEEM", "Coordinación de SEEM", "Seguimiento, Evaluación, Educación Metodológica y Comités Estadales (Capacitación LA 8 y Comités CCEE LA 9)")
        ]
        
        depts = {}
        for codigo, nombre, desc in depts_data:
            dept = db.query(Department).filter(Department.codigo == codigo).first()
            if not dept:
                dept = Department(codigo=codigo, nombre=nombre, descripcion=desc, activo=True)
                db.add(dept)
                db.flush()
            depts[codigo] = dept

        # Limpiar departamento GER si existía para mantener exactamente los 5 departamentos técnicos del sistema
        dept_ger_antiguo = db.query(Department).filter(Department.codigo == "GER").first()
        if dept_ger_antiguo:
            # Reasignar cualquier indicador o categoría hacia SEG
            for ind_old in db.query(Indicator).filter(Indicator.departamento_id == dept_ger_antiguo.id).all():
                ind_old.departamento_id = depts["SEG"].id
            for cat_old in db.query(Category).filter(Category.departamento_id == dept_ger_antiguo.id).all():
                cat_old.departamento_id = depts["SEG"].id
            db.flush()
            db.delete(dept_ger_antiguo)
            db.flush()
        
        # 2. Roles y Usuarios
        # Asegurar existencia del rol JEFE_AREA
        rol_jefe_area = db.query(Role).filter(Role.nombre == "JEFE_AREA").first()
        if not rol_jefe_area:
            rol_jefe_area = Role(
                nombre="JEFE_AREA",
                descripcion="Jefe de Área con control y supervisión sobre múltiples unidades técnicas asignadas"
            )
            db.add(rol_jefe_area)
            db.flush()

        roles = {r.nombre: r for r in db.query(Role).all()}
        
        # Administrador Técnico General
        admin_user = db.query(User).filter(User.cedula == "V-10000000").first()
        if not admin_user:
            admin_user = User(
                cedula="V-10000000",
                nombre_completo="Administrador General INE",
                password_hash=get_password_hash("gerente2026"),
                rol_id=roles["ADMIN"].id,
                departamento_id=None
            )
            db.add(admin_user)
            db.flush()

        # 1. Gerente Estadal: Luis Alberto (V-11206771)
        gerente_user = db.query(User).filter(User.cedula == "V-11206771").first()
        if not gerente_user:
            gerente_user = User(
                cedula="V-11206771",
                nombre_completo="Luis Alberto",
                password_hash=get_password_hash("gerente2026"),
                rol_id=roles["GERENTE"].id,
                departamento_id=None
            )
            db.add(gerente_user)
            db.flush()
        else:
            gerente_user.nombre_completo = "Luis Alberto"
            gerente_user.rol_id = roles["GERENTE"].id
            gerente_user.departamento_id = None
            gerente_user.password_hash = get_password_hash("gerente2026")
            db.flush()

        # 2. Jefe de Área de Programas Estadísticos: Jesús Ramón Pérez (V-8979338)
        # Supervisión y control total sobre: Cartografía, Económica, Sociales y SEGEN
        jefe_area_user = db.query(User).filter(User.cedula == "V-8979338").first()
        if not jefe_area_user:
            jefe_area_user = User(
                cedula="V-8979338",
                nombre_completo="Jesús Ramón Pérez",
                password_hash=get_password_hash("gerente2026"),
                rol_id=roles["JEFE_AREA"].id,
                departamento_id=depts["CART"].id
            )
            db.add(jefe_area_user)
            db.flush()
        else:
            jefe_area_user.nombre_completo = "Jesús Ramón Pérez"
            jefe_area_user.rol_id = roles["JEFE_AREA"].id
            jefe_area_user.departamento_id = depts["CART"].id
            jefe_area_user.password_hash = get_password_hash("gerente2026")
            db.flush()

        # Asignar explícitamente sus 4 departamentos supervisados: CART, ECO, SOC, SEG
        jefe_depts = [depts["CART"], depts["ECO"], depts["SOC"], depts["SEG"]]
        jefe_area_user.departamentos_asignados = jefe_depts
        db.flush()

        # Encargados Oficiales por Unidad Técnica (Primer Nombre y Primer Apellido según nómina)
        encargados_info = {
            "DEM": ("V-11337533", "Cledys Bastardo", "Técnico INPC / Encargada de Estadísticas Demográficas"),
            "ECO": ("V-13814617", "Wilfredo Rojas", "Dir. de Proyectos / Encargado de Estadísticas Económicas"),
            "SOC": ("V-17934142", "Rubén Alejandro", "Profesional / Encargado de Estadísticas Sociales"),
            "CART": ("V-10198032", "Henri Guevara", "Planificador II / Encargado de Cartografía"),
            "SEG": ("V-17723864", "Johana Larez", "Profesional / Encargada de SEGEN"),
            "SEEM": ("V-20916675", "Luis Velásquez", "Coordinador de SEEM")
        }
        
        encargados = {}
        for code, (cedula, nombre, cargo) in encargados_info.items():
            u = db.query(User).filter(User.cedula == cedula).first()
            if not u:
                u = User(
                    cedula=cedula,
                    nombre_completo=nombre,
                    password_hash=get_password_hash("gerente2026"),
                    rol_id=roles["ENCARGADO"].id,
                    departamento_id=depts[code].id
                )
                db.add(u)
                db.flush()
            else:
                u.nombre_completo = nombre
                u.password_hash = get_password_hash("gerente2026")
                u.rol_id = roles["ENCARGADO"].id
                u.departamento_id = depts[code].id
                db.flush()
            encargados[code] = u
        
        # 3. Categorías Especializadas
        categories_data = [
            ("SOC", "Encuesta de Hogares por Muestreo (EHM)", "Investigaciones socioeconómicas continuas en sectores y viviendas"),
            ("SOC", "Encuesta de Seguimiento al Consumo de Alimentos (ESCA)", "Monitoreo del consumo alimentario y adquisición de canastas"),
            ("DEM", "Estadísticas Vitales y Registros Continuos", "Hechos vitales: Nacimientos, Defunciones, Nupcialidad y flujo de boletas"),
            ("ECO", "Directorio de Tipologías de Precios", "Actualización e implantación de tipologías comerciales en Monagas"),
            ("ECO", "Canasta Alimentaria Normativa (CAN)", "Levantamiento de precios mensual por tipologías comerciales"),
            ("CART", "Circuitos Comunales y Territorio", "Poligonales de comunas y consejos comunales vectorizados"),
            ("SEG", "Red Territorial de Nodos SEGEN", "Operatividad de nodos, equipamiento tecnológico DMC y laptops"),
            ("SEG", "Levantamiento de Encuestas Digitales ODK", "Captura electrónica de cuestionarios en la plataforma SEGEN"),
            ("SEEM", "Capacitación y Formación Metodológica", "Planes de formación, talleres y personas capacitadas en Monagas (LA 8)"),
            ("SEEM", "Comités de Coordinación Estadística (CCEE)", "Mesas técnicas interinstitucionales con salud, CNE y organismos (LA 9)")
        ]
        
        categories = {}
        for dept_code, cat_nombre, cat_desc in categories_data:
            cat = db.query(Category).filter(
                Category.departamento_id == depts[dept_code].id,
                Category.nombre == cat_nombre
            ).first()
            if not cat:
                cat = Category(
                    departamento_id=depts[dept_code].id,
                    nombre=cat_nombre,
                    descripcion=cat_desc
                )
                db.add(cat)
                db.flush()
            categories[(dept_code, cat_nombre)] = cat
            
        db.commit()
        print("✅ Departamentos, Usuarios y Categorías sincronizados.")

        # 4. Municipios (Mapeo por nombre en mayúsculas / estándar)
        municipios = {m.nombre.upper(): m for m in db.query(Municipality).all()}
        # Mapeo flexible
        def get_mun(nombre):
            clean = nombre.strip().upper()
            if "MATUR" in clean: return municipios.get("MATURÍN") or municipios.get("MATURIN")
            if "BOL" in clean: return municipios.get("BOLÍVAR") or municipios.get("BOLIVAR")
            if "CEDE" in clean: return municipios.get("CEDEÑO") or municipios.get("CEDENO")
            if "PUNCE" in clean: return municipios.get("PUNCERES") or municipios.get("PÚNCERES")
            if "BARBARA" in clean: return municipios.get("SANTA BÁRBARA") or municipios.get("SANTA BARBARA")
            for k in municipios:
                if clean in k or k in clean:
                    return municipios[k]
            return None

        # 5. Catálogo Maestro de los 29 Indicadores Oficiales
        indicadores_def = [
            # ----------------------------------------------------
            # 1. SOCIALES (SOC)
            # ----------------------------------------------------
            {
                "codigo": "SOC-EHM-01",
                "nombre": "Tasa de Levantamiento de Controles EHM",
                "descripcion": "Porcentaje de controles de muestra levantados efectivamente respecto a los planificados en la Encuesta de Hogares por Muestreo",
                "dept": "SOC",
                "cat": "Encuesta de Hogares por Muestreo (EHM)",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("100.00"),
                "valor_ago": Decimal("84.62"),
                "obs": "11 de 13 controles levantados en agosto 2026 (Acumulado 85 de 106 controles, 80.19%)"
            },
            {
                "codigo": "SOC-EHM-02",
                "nombre": "Viviendas Efectivas Entrevistadas EHM",
                "descripcion": "Total de viviendas con entrevistas completas y efectivas en la muestra EHM",
                "dept": "SOC",
                "cat": "Encuesta de Hogares por Muestreo (EHM)",
                "unidad": "Viviendas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("172.00"),
                "valor_ago": Decimal("97.00"),
                "obs": "97 viviendas efectivas en agosto 2026 frente a 172 planificadas (Acumulado anual: 699)"
            },
            {
                "codigo": "SOC-EHM-03",
                "nombre": "Tasa de No Respuesta EHM",
                "descripcion": "Porcentaje de viviendas que no pudieron investigarse por rechazo o ausencia prolongada (Tipo A)",
                "dept": "SOC",
                "cat": "Encuesta de Hogares por Muestreo (EHM)",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.DESCENDENTE,
                "meta": Decimal("15.00"),
                "valor_ago": Decimal("20.49"),
                "obs": "25 viviendas Tipo A frente a 97 efectivas en agosto (20.49% de no respuesta)"
            },
            {
                "codigo": "SOC-ESCA-01",
                "nombre": "Tasa de Levantamiento de Controles ESCA",
                "descripcion": "Efectividad operativa en la ejecución de controles de la Encuesta de Consumo de Alimentos",
                "dept": "SOC",
                "cat": "Encuesta de Seguimiento al Consumo de Alimentos (ESCA)",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("100.00"),
                "valor_ago": Decimal("82.61"),
                "obs": "19 de 23 controles ejecutados en agosto (Acumulado: 146 de 180, 81.11%)"
            },
            {
                "codigo": "SOC-ESCA-02",
                "nombre": "Viviendas Efectivas Entrevistadas ESCA",
                "descripcion": "Total de viviendas con registro efectivo de adquisición y consumo alimentario",
                "dept": "SOC",
                "cat": "Encuesta de Seguimiento al Consumo de Alimentos (ESCA)",
                "unidad": "Viviendas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("287.00"),
                "valor_ago": Decimal("139.00"),
                "obs": "139 viviendas efectivas en agosto 2026 (Acumulado anual: 1,109 viviendas)"
            },
            {
                "codigo": "SOC-ESCA-03",
                "nombre": "Tasa de No Respuesta ESCA",
                "descripcion": "Porcentaje de no respuesta en la investigación de consumo alimentario (Tipo A)",
                "dept": "SOC",
                "cat": "Encuesta de Seguimiento al Consumo de Alimentos (ESCA)",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.DESCENDENTE,
                "meta": Decimal("20.00"),
                "valor_ago": Decimal("28.35"),
                "obs": "55 viviendas Tipo A en agosto (28.35% no respuesta frente a 139 efectivas)"
            },

            # ----------------------------------------------------
            # 2. DEMOGRÁFICAS (DEM)
            # ----------------------------------------------------
            {
                "codigo": "DEM-VIT-01",
                "nombre": "Volumen Total de Boletas Vitales Recolectadas",
                "descripcion": "Captura continua de hechos vitales (Nacimientos, Defunciones, Nupcialidad, Divorcios, Suicidios)",
                "dept": "DEM",
                "cat": "Estadísticas Vitales y Registros Continuos",
                "unidad": "Boletas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("25000.00"),
                "valor_ago": Decimal("11615.00"),
                "obs": "Total boletas vitales recolectadas en Monagas al 31/08/2026"
            },
            {
                "codigo": "DEM-VIT-02",
                "nombre": "Cantidad de Nacimientos Registrados",
                "descripcion": "Total de hechos de natalidad capturados mediante boleta oficial en centros de salud y registros",
                "dept": "DEM",
                "cat": "Estadísticas Vitales y Registros Continuos",
                "unidad": "Actas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("15000.00"),
                "valor_ago": Decimal("6972.00"),
                "obs": "6,972 nacimientos registrados en el estado Monagas al 31/08/2026"
            },
            {
                "codigo": "DEM-VIT-03",
                "nombre": "Cantidad de Defunciones Registradas",
                "descripcion": "Hechos de mortalidad recolectados de fuentes oficiales de salud y registros civiles",
                "dept": "DEM",
                "cat": "Estadísticas Vitales y Registros Continuos",
                "unidad": "Actas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("4000.00"),
                "valor_ago": Decimal("1987.00"),
                "obs": "1,987 defunciones registradas en Monagas al mes de agosto 2026"
            },
            {
                "codigo": "DEM-VIT-04",
                "nombre": "Registro de Nupcialidad y Uniones Estables",
                "descripcion": "Total de matrimonios civiles y declaraciones de unión estable de hecho capturadas",
                "dept": "DEM",
                "cat": "Estadísticas Vitales y Registros Continuos",
                "unidad": "Actas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("3000.00"),
                "valor_ago": Decimal("1339.00"),
                "obs": "790 matrimonios y 549 uniones estables de hecho al mes de agosto 2026"
            },
            {
                "codigo": "DEM-VIT-05",
                "nombre": "Tasa de Transcripción y Digitalización Vital",
                "descripcion": "Porcentaje de boletas físicas recolectadas que fueron transcritas y codificadas sin rezago",
                "dept": "DEM",
                "cat": "Estadísticas Vitales y Registros Continuos",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("100.00"),
                "valor_ago": Decimal("94.90"),
                "obs": "11,023 boletas transcritas de 11,615 recolectadas (94.90% efectividad sin rezago acumulado)"
            },

            # ----------------------------------------------------
            # 3. ECONÓMICAS (ECO)
            # ----------------------------------------------------
            {
                "codigo": "ECO-DIR-01",
                "nombre": "Total Establecimientos Implantados Directorio de Tipologías de Precios",
                "descripcion": "Nuevos locales comerciales y tipologías de precios georreferenciados e implantados en el marco muestral (Columna E)",
                "dept": "ECO",
                "cat": "Directorio de Tipologías de Precios",
                "unidad": "Locales",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("50.00"),
                "valor_ago": Decimal("44.00"),
                "obs": "44 establecimientos implantados en agosto 2026 (Acumulado anual: 1,078 establecimientos)"
            },
            {
                "codigo": "ECO-CAN-01",
                "nombre": "Total Establecimientos con Encuesta Efectiva en el Levantamiento de Precios CAN",
                "descripcion": "Locales comerciales con encuesta efectiva de precios CAN y porcentaje de efectividad sobre la muestra planificada (Columna J y K)",
                "dept": "ECO",
                "cat": "Canasta Alimentaria Normativa (CAN)",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("100.00"),
                "valor_ago": Decimal("100.00"),
                "obs": "34 de 34 establecimientos comerciales planificados investigados al 100% en agosto"
            },
            {
                "codigo": "ECO-CAN-02",
                "nombre": "Total Precios Levantados Reales Efectivos",
                "descripcion": "Total de cotizaciones de precios recolectadas efectivamente para los rubros de la Canasta Alimentaria (Columna L)",
                "dept": "ECO",
                "cat": "Canasta Alimentaria Normativa (CAN)",
                "unidad": "Precios",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("2200.00"),
                "valor_ago": Decimal("2145.00"),
                "obs": "2,145 precios recolectados en agosto 2026 (Acumulado anual: 18,976 precios)"
            },
            {
                "codigo": "ECO-CAN-03",
                "nombre": "Total Precios Levantados Reales (Sin Errores)",
                "descripcion": "Cotizaciones validadas que superaron los controles de consistencia estadística sin errores de captura (Columna M y N)",
                "dept": "ECO",
                "cat": "Canasta Alimentaria Normativa (CAN)",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("99.00"),
                "valor_ago": Decimal("99.35"),
                "obs": "2,131 precios limpios de 2,145 recolectados (99.35% de consistencia técnica)"
            },
            {
                "codigo": "ECO-CAN-04",
                "nombre": "Total Comunas con Levantamiento CAN (Incluye Complementaria)",
                "descripcion": "Cantidad de comunas con levantamiento activo de precios de la Canasta Alimentaria y articulación SEGEN (Columna F)",
                "dept": "ECO",
                "cat": "Canasta Alimentaria Normativa (CAN)",
                "unidad": "Comunas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("25.00"),
                "valor_ago": Decimal("25.00"),
                "obs": "25 comunas activas en levantamiento CAN articuladas con 16 nodos territoriales"
            },

            # ----------------------------------------------------
            # 4. CARTOGRAFÍA (CART)
            # ----------------------------------------------------
            {
                "codigo": "CART-CIR-01",
                "nombre": "Tasa de Vectorización de Circuitos Comunales",
                "descripcion": "Porcentaje de circuitos comunales delimitados y vectorizados cartográficamente en Monagas",
                "dept": "CART",
                "cat": "Circuitos Comunales y Territorio",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("100.00"),
                "valor_ago": Decimal("97.99"),
                "obs": "195 de 199 circuitos comunales vectorizados en el estado Monagas al mes de agosto"
            },
            {
                "codigo": "CART-CIR-02",
                "nombre": "Consejos Comunales Georreferenciados",
                "descripcion": "Organizaciones comunitarias georreferenciadas e incorporadas a las poligonales de circuitos",
                "dept": "CART",
                "cat": "Circuitos Comunales y Territorio",
                "unidad": "Consejos",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("1361.00"),
                "valor_ago": Decimal("1361.00"),
                "obs": "1,361 consejos comunales estructurados territorialmente en Monagas"
            },
            {
                "codigo": "CART-CIR-03",
                "nombre": "Completitud Vectorial Plena (100%)",
                "descripcion": "Total de circuitos comunales con poligonales cartográficas cerradas al 100%",
                "dept": "CART",
                "cat": "Circuitos Comunales y Territorio",
                "unidad": "Circuitos",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("199.00"),
                "valor_ago": Decimal("177.00"),
                "obs": "177 circuitos 100% completados, 18 en avance (33-93%) y 4 pendientes por vectorizar"
            },
            {
                "codigo": "CART-MUN-01",
                "nombre": "Cobertura Cartográfica por Municipio",
                "descripcion": "Cantidad de municipios del estado con circuitos comunales delimitados",
                "dept": "CART",
                "cat": "Circuitos Comunales y Territorio",
                "unidad": "Municipios",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("13.00"),
                "valor_ago": Decimal("13.00"),
                "obs": "13 municipios de Monagas con cobertura cartográfica y circuitos asignados"
            },

            # ----------------------------------------------------
            # 5. SEGEN (SEG)
            # ----------------------------------------------------
            {
                "codigo": "SEG-NOD-01",
                "nombre": "Tasa de Operatividad de Nodos SEGEN",
                "descripcion": "Porcentaje de nodos del Sistema Estadístico Geográfico instalados que transmiten activamente",
                "dept": "SEG",
                "cat": "Red Territorial de Nodos SEGEN",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("80.00"),
                "valor_ago": Decimal("47.17"),
                "obs": "50 nodos activos de 106 instalados en los 13 municipios del estado Monagas"
            },
            {
                "codigo": "SEG-NOD-02",
                "nombre": "Cumplimiento de Despliegue de Nodos",
                "descripcion": "Porcentaje de nodos territoriales instalados en campo respecto a la meta planificada",
                "dept": "SEG",
                "cat": "Red Territorial de Nodos SEGEN",
                "unidad": "%",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("100.00"),
                "valor_ago": Decimal("108.16"),
                "obs": "106 nodos instalados frente a 98 planificados (108.16% de meta física)"
            },
            {
                "codigo": "SEG-PAR-01",
                "nombre": "Disponibilidad de Dispositivos Móviles (DMC)",
                "descripcion": "Total de Dispositivos Móviles de Captura (DMC) asignados y operativos en campo",
                "dept": "SEG",
                "cat": "Red Territorial de Nodos SEGEN",
                "unidad": "Equipos",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("350.00"),
                "valor_ago": Decimal("315.00"),
                "obs": "315 DMCs y 48 Laptops/MiniPC activos en campo al mes de agosto 2026"
            },
            {
                "codigo": "SEG-PER-01",
                "nombre": "Despliegue de Fuerza Territorial SEGEN",
                "descripcion": "Personal activo en campo: Coordinadores Municipales, de Nodos, Supervisores y Encuestadores",
                "dept": "SEG",
                "cat": "Red Territorial de Nodos SEGEN",
                "unidad": "Personas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("210.00"),
                "valor_ago": Decimal("208.00"),
                "obs": "17 Coord. Municipales, 50 Coord. Nodos, 50 Supervisores y 91 Encuestadores Integrales"
            },
            {
                "codigo": "SEG-ENC-01",
                "nombre": "Volumen Mensual de Encuestas Digitales SEGEN",
                "descripcion": "Total de cuestionarios capturados electrónicamente en la plataforma ODK y SEGEN",
                "dept": "SEG",
                "cat": "Levantamiento de Encuestas Digitales ODK",
                "unidad": "Encuestas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("25000.00"),
                "valor_ago": Decimal("28147.00"),
                "obs": "28,147 cuestionarios procesados en agosto 2026 (Acumulado anual: 257,255 formularios)"
            },
            {
                "codigo": "SEG-ENC-02",
                "nombre": "Captura Formulario Intercensal Conteo Rápido",
                "descripcion": "Cuestionarios de estructuras y población procesados mediante el Conteo Rápido v2",
                "dept": "SEG",
                "cat": "Levantamiento de Encuestas Digitales ODK",
                "unidad": "Encuestas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("15000.00"),
                "valor_ago": Decimal("14281.00"),
                "obs": "14,281 encuestas de Conteo Rápido en agosto (Acumulado anual: 59,710)"
            },
            # ----------------------------------------------------
            # 6. SEEM (SEGUIMIENTO, EVALUACIÓN, EDUCACIÓN Y COMITÉS)
            # ----------------------------------------------------
            {
                "codigo": "SEEM-CAP-01",
                "nombre": "Personal Capacitado en Actividades Formativas",
                "descripcion": "Total de funcionarios y personal de campo capacitados en planes formativos y metodológicos (LA 8)",
                "dept": "SEEM",
                "cat": "Capacitación y Formación Metodológica",
                "unidad": "Personas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("150.00"),
                "valor_ago": Decimal("145.00"),
                "obs": "145 personas capacitadas en agosto (129 sede + 16 campo) en 7 talleres ejecutados"
            },
            {
                "codigo": "SEEM-CAP-02",
                "nombre": "Talleres y Actividades de Formación Ejecutadas",
                "descripcion": "Cantidad de talleres y jornadas metodológicas ejecutadas durante el mes (LA 8)",
                "dept": "SEEM",
                "cat": "Capacitación y Formación Metodológica",
                "unidad": "Talleres",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("10.00"),
                "valor_ago": Decimal("7.00"),
                "obs": "7 talleres formativos realizados en el mes de agosto 2026"
            },
            {
                "codigo": "SEEM-COM-01",
                "nombre": "Mesas Técnicas y Sesiones de Comités Estadales (CCEE)",
                "descripcion": "Sesiones técnicas del Comité de Coordinación Estadística celebradas con entes del Estado (LA 9)",
                "dept": "SEEM",
                "cat": "Comités de Coordinación Estadística (CCEE)",
                "unidad": "Mesas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("2.00"),
                "valor_ago": Decimal("1.00"),
                "obs": "Mesa Técnica de Registros Vitales celebrada con Dirección de Salud y CNE"
            },
            {
                "codigo": "SEEM-COM-02",
                "nombre": "Participantes en Mesas Técnicas CCEE",
                "descripcion": "Total de funcionarios y delegados participantes en las mesas técnicas del CCEE (LA 9)",
                "dept": "SEEM",
                "cat": "Comités de Coordinación Estadística (CCEE)",
                "unidad": "Personas",
                "frecuencia": FrequencyType.MENSUAL,
                "orientacion": TargetOrientationType.ASCENDENTE,
                "meta": Decimal("10.00"),
                "valor_ago": Decimal("6.00"),
                "obs": "6 delegados técnicos participantes en la Mesa de Registros Vitales"
            }
        ]

        # Desactivar indicadores anteriores obsoletos
        db.query(Indicator).filter(
            Indicator.codigo.in_(["SEG-CAP-01", "GER-CCEE-01", "GER-TAL-01"])
        ).update({"activo": False}, synchronize_session=False)
        db.flush()

        # 6. Sincronización de Indicadores y Mediciones Consolidadas
        print(f"📊 Sincronizando {len(indicadores_def)} indicadores y sus mediciones...")
        
        indicadores_map = {}
        for item in indicadores_def:
            code = item["codigo"]
            cat_obj = categories[(item["dept"], item["cat"])]
            
            ind = db.query(Indicator).filter(Indicator.codigo == code).first()
            if not ind:
                ind = Indicator(
                    codigo=code,
                    nombre=item["nombre"],
                    descripcion=item["descripcion"],
                    departamento_id=depts[item["dept"]].id,
                    categoria_id=cat_obj.id,
                    unidad_medida=item["unidad"],
                    frecuencia=item["frecuencia"],
                    tipo_meta=item["orientacion"],
                    meta_referencial=item["meta"],
                    activo=True
                )
                db.add(ind)
                db.flush()
            else:
                # Actualizar datos si cambiaron
                ind.nombre = item["nombre"]
                ind.descripcion = item["descripcion"]
                ind.categoria_id = cat_obj.id
                ind.unidad_medida = item["unidad"]
                ind.meta_referencial = item["meta"]
                ind.tipo_meta = item["orientacion"]
                ind.activo = True
            
            indicadores_map[code] = ind

            # Medición Consolidada Estadal (Agosto 2026)
            med = db.query(IndicatorMeasurement).filter(
                IndicatorMeasurement.indicador_id == ind.id,
                IndicatorMeasurement.municipio_id.is_(None),
                IndicatorMeasurement.periodo_anio == 2026,
                IndicatorMeasurement.periodo_tipo == FrequencyType.MENSUAL,
                IndicatorMeasurement.periodo_mes == 8
            ).first()

            encargado = encargados[item["dept"]]
            
            if not med:
                med = IndicatorMeasurement(
                    indicador_id=ind.id,
                    municipio_id=None,
                    periodo_anio=2026,
                    periodo_tipo=FrequencyType.MENSUAL,
                    periodo_mes=8,
                    valor_registrado=item["valor_ago"],
                    meta_periodo=item["meta"],
                    estado=MeasurementStatus.APROBADO,
                    observaciones=item["obs"],
                    registrado_por=encargado.id,
                    aprobado_por=encargado.id,
                    version=1
                )
                db.add(med)
                db.flush()
            else:
                med.valor_registrado = item["valor_ago"]
                med.meta_periodo = item["meta"]
                med.observaciones = item["obs"]
                med.estado = MeasurementStatus.APROBADO

        db.commit()
        print("✅ Indicadores y mediciones consolidadas estadales guardadas.")

        # 7. Carga de Mediciones Municipales Desglosadas (13 Municipios)
        # -----------------------------------------------------------
        # Caso A: CART-CIR-01 (Circuitos Comunales por Municipio)
        cart_mun_data = [
            ("Acosta", 9, 9),
            ("Aguasay", 8, 8),
            ("Bolívar", 10, 8),
            ("Caripe", 15, 14),
            ("Cedeño", 7, 7),
            ("Ezequiel Zamora", 9, 9),
            ("Libertador", 12, 12),
            ("Maturín", 90, 90),
            ("Piar", 12, 12),
            ("Punceres", 6, 6),
            ("Santa Bárbara", 4, 3),
            ("Sotillo", 10, 10),
            ("Uracoa", 7, 7)
        ]
        
        ind_cart = indicadores_map["CART-CIR-01"]
        encargado_cart = encargados["CART"]
        
        for mun_name, planif, vectorizados in cart_mun_data:
            mun = get_mun(mun_name)
            if mun:
                porcentaje = Decimal(str(round((vectorizados / planif) * 100, 2)))
                m_cart = db.query(IndicatorMeasurement).filter(
                    IndicatorMeasurement.indicador_id == ind_cart.id,
                    IndicatorMeasurement.municipio_id == mun.id,
                    IndicatorMeasurement.periodo_anio == 2026,
                    IndicatorMeasurement.periodo_tipo == FrequencyType.MENSUAL,
                    IndicatorMeasurement.periodo_mes == 8
                ).first()
                if not m_cart:
                    m_cart = IndicatorMeasurement(
                        indicador_id=ind_cart.id,
                        municipio_id=mun.id,
                        periodo_anio=2026,
                        periodo_tipo=FrequencyType.MENSUAL,
                        periodo_mes=8,
                        valor_registrado=porcentaje,
                        meta_periodo=Decimal("100.00"),
                        estado=MeasurementStatus.APROBADO,
                        observaciones=f"{vectorizados} de {planif} circuitos vectorizados en {mun.nombre}",
                        registrado_por=encargado_cart.id,
                        aprobado_por=encargado_cart.id,
                        version=1
                    )
                    db.add(m_cart)
                else:
                    m_cart.valor_registrado = porcentaje

        # Caso B: SEG-NOD-01 (Nodos Activos por Municipio)
        seg_mun_data = [
            ("Acosta", 9, 2),
            ("Aguasay", 2, 1),
            ("Bolívar", 5, 2),
            ("Caripe", 6, 2),
            ("Cedeño", 8, 3),
            ("Ezequiel Zamora", 3, 2),
            ("Libertador", 7, 2),
            ("Maturín", 49, 23),
            ("Piar", 9, 5),
            ("Punceres", 3, 3),
            ("Santa Bárbara", 2, 2),
            ("Sotillo", 2, 2),
            ("Uracoa", 1, 1)
        ]
        
        ind_seg = indicadores_map["SEG-NOD-01"]
        encargado_seg = encargados["SEG"]
        
        for mun_name, instalados, activos in seg_mun_data:
            mun = get_mun(mun_name)
            if mun:
                pct = Decimal(str(round((activos / instalados) * 100, 2))) if instalados > 0 else Decimal("0.00")
                m_seg = db.query(IndicatorMeasurement).filter(
                    IndicatorMeasurement.indicador_id == ind_seg.id,
                    IndicatorMeasurement.municipio_id == mun.id,
                    IndicatorMeasurement.periodo_anio == 2026,
                    IndicatorMeasurement.periodo_tipo == FrequencyType.MENSUAL,
                    IndicatorMeasurement.periodo_mes == 8
                ).first()
                if not m_seg:
                    m_seg = IndicatorMeasurement(
                        indicador_id=ind_seg.id,
                        municipio_id=mun.id,
                        periodo_anio=2026,
                        periodo_tipo=FrequencyType.MENSUAL,
                        periodo_mes=8,
                        valor_registrado=pct,
                        meta_periodo=Decimal("80.00"),
                        estado=MeasurementStatus.APROBADO,
                        observaciones=f"{activos} de {instalados} nodos activos en {mun.nombre}",
                        registrado_por=encargado_seg.id,
                        aprobado_por=encargado_seg.id,
                        version=1
                    )
                    db.add(m_seg)
                else:
                    m_seg.valor_registrado = pct

        db.commit()
        print("✅ Mediciones municipales en los 13 municipios sincronizadas.")
        print("🎉 ¡Carga completa del Catálogo Maestro y Mediciones de Agosto 2026 finalizada con éxito!")

    except Exception as e:
        db.rollback()
        print("❌ Error en la carga de semillas:", str(e))
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
