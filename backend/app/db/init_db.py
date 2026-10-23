"""
Script de Inicialización y Migración Automática para Despliegues Cloud (Render / Producción).
Ejecuta el script SQL maestro (init.sql) para crear tipos ENUM, tablas, vistas,
funciones de auditoría y triggers, y posteriormente sincroniza las semillas maestras.
"""

import os
import sys
import time
from sqlalchemy import text
from app.core.database import engine
from app.db.seed_indicators import seed_database

def wait_for_database(max_retries=20, delay=3):
    """
    Espera de forma resiliente a que el motor PostgreSQL de Render acepte conexiones.
    """
    print("⏳ Conectando con el motor de base de datos PostgreSQL...")
    for attempt in range(1, max_retries + 1):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print(f"✅ Conexión con PostgreSQL establecida exitosamente (intento {attempt}).")
            return True
        except Exception as e:
            print(f"⚠️ Intento {attempt}/{max_retries}: Base de datos en preparación ({e}). Esperando {delay}s...")
            time.sleep(delay)
    print("❌ Error: No se pudo conectar a PostgreSQL tras los intentos programados.", file=sys.stderr)
    return False

def init_schema():
    print("🔍 Comprobando estado del esquema de base de datos...")
    
    # Ruta al archivo init.sql
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sql_path = os.path.join(base_dir, "sql", "init.sql")
    
    if not os.path.exists(sql_path):
        print(f"⚠️ Advertencia: No se encontró init.sql en {sql_path}")
        return

    # Verificar si la tabla 'departamentos' ya existe
    tables_exist = False
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT to_regclass('public.departamentos');"))
            val = result.scalar()
            if val is not None:
                tables_exist = True
    except Exception as e:
        print(f"Nota en verificación de tablas: {e}")

    if not tables_exist:
        print(f"📦 Base de datos limpia detectada. Ejecutando esquema inicial desde {sql_path}...")
        with open(sql_path, "r", encoding="utf-8") as f:
            sql_content = f.read()

        with engine.connect() as connection:
            dbapi_conn = connection.connection.dbapi_connection
            with dbapi_conn.cursor() as cursor:
                cursor.execute(sql_content)
            dbapi_conn.commit()
            print("✅ Esquema maestro, tablas, tipos ENUM, vistas y triggers creados y confirmados (commit).")
    else:
        print("ℹ️ El esquema de tablas base ya existe y está activo.")

def run_all():
    try:
        if not wait_for_database():
            sys.exit(1)
        init_schema()
        print("🌱 Sincronizando catálogo de indicadores y nómina oficial...")
        seed_database()
        print("🎉 Inicialización completada con éxito.")
    except Exception as e:
        print(f"❌ Error durante la inicialización: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_all()
