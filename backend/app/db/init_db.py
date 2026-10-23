"""
Script de Inicialización y Migración Automática para Despliegues Cloud (Render / Producción).
Ejecuta el script SQL maestro (init.sql) para crear tipos ENUM, tablas, vistas,
funciones de auditoría y triggers, y posteriormente sincroniza las semillas maestras.
"""

import os
import sys
from sqlalchemy import text
from app.core.database import engine
from app.db.seed_indicators import seed_database

def init_schema():
    print("🔍 Comprobando estado del esquema de base de datos...")
    
    # Ruta al archivo init.sql
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sql_path = os.path.join(base_dir, "sql", "init.sql")
    
    if not os.path.exists(sql_path):
        print(f"⚠️ Advertencia: No se encontró init.sql en {sql_path}")
        return

    # Verificar si la tabla 'roles' ya existe
    tables_exist = False
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT to_regclass('public.roles');"))
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
            raw_conn = connection.connection
            old_autocommit = getattr(raw_conn, "autocommit", False)
            raw_conn.autocommit = True
            try:
                with raw_conn.cursor() as cursor:
                    cursor.execute(sql_content)
                print("✅ Esquema, tablas, tipos ENUM, vistas y triggers creados exitosamente.")
            finally:
                raw_conn.autocommit = old_autocommit
    else:
        print("ℹ️ El esquema de tablas base ya existe.")

def run_all():
    try:
        init_schema()
        print("🌱 Sincronizando catálogo de indicadores y usuarios...")
        seed_database()
        print("🎉 Inicialización completada con éxito.")
    except Exception as e:
        print(f"❌ Error durante la inicialización: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_all()
