import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database"] == "connected"
    assert data["municipios"] == 13

def test_login_gerente():
    response = client.post("/api/v1/auth/login", json={
        "cedula": "V-12345678",
        "password": "gerente2026"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    token = data["access_token"]

    # Verificar perfil
    me_resp = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me_resp.status_code == 200
    me_data = me_resp.json()
    assert me_data["cedula"] == "V-12345678"
    assert me_data["rol_nombre"] == "GERENTE"

def test_dashboard_gerente():
    # Login Gerente
    login_resp = client.post("/api/v1/auth/login", json={
        "cedula": "V-12345678",
        "password": "gerente2026"
    })
    token = login_resp.json()["access_token"]

    response = client.get("/api/v1/dashboard/resumen", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["total_departamentos"] == 6
    dept_codes = [d["departamento_codigo"] for d in data["departamentos"]]
    assert set(dept_codes) == {"ECO", "SOC", "DEM", "CART", "SEG", "SEEM"}

def test_login_jefe_seem():
    # Login Coordinador SEEM
    login_resp = client.post("/api/v1/auth/login", json={
        "cedula": "V-19876543",
        "password": "gerente2026"
    })
    assert login_resp.status_code == 200
    data = login_resp.json()
    assert "access_token" in data
    token = data["access_token"]

    me_resp = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me_resp.status_code == 200
    me_data = me_resp.json()
    assert me_data["cedula"] == "V-19876543"
    assert me_data["rol_nombre"] == "ENCARGADO"
    assert me_data["departamento_codigo"] == "SEEM"

def test_municipalities_ine():
    login_resp = client.post("/api/v1/auth/login", json={
        "cedula": "V-12345678",
        "password": "gerente2026"
    })
    token = login_resp.json()["access_token"]

    response = client.get("/api/v1/municipios/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    muns = response.json()
    assert len(muns) == 13
    
    # Validar códigos DPT oficiales 1601 a 1613
    codigos = [m["codigo_ine"] for m in muns]
    for i in range(1, 14):
        expected_code = f"16{i:02d}"
        assert expected_code in codigos, f"Falta código {expected_code}"

def test_measurement_flow_versioning_and_rollback():
    # 1. Login como Encargado de Estadísticas Económicas (Dept ECO)
    login_resp = client.post("/api/v1/auth/login", json={
        "cedula": "V-14892103",
        "password": "gerente2026"
    })
    assert login_resp.status_code == 200
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Obtener un indicador de Dept ECO
    me_resp = client.get("/api/v1/auth/me", headers=headers)
    dept_id = me_resp.json()["departamento_id"]
    ind_resp = client.get(f"/api/v1/indicadores/?departamento_id={dept_id}", headers=headers)
    assert ind_resp.status_code == 200
    indicators = ind_resp.json()
    assert len(indicators) > 0
    indicator = indicators[0]
    ind_id = indicator["id"]

    # 3. Limpiar previamente la medición de prueba del mes 10 para garantizar idempotencia
    from app.core.database import SessionLocal
    from app.models.measurement import IndicatorMeasurement
    from app.models.version import MeasurementVersion
    from app.models.audit import MeasurementAudit

    db = SessionLocal()
    prev_m = db.query(IndicatorMeasurement).filter(
        IndicatorMeasurement.indicador_id == ind_id,
        IndicatorMeasurement.periodo_anio == 2026,
        IndicatorMeasurement.periodo_mes == 10
    ).first()
    if prev_m:
        db.query(MeasurementVersion).filter(MeasurementVersion.medicion_id == prev_m.id).delete()
        db.query(MeasurementAudit).filter(MeasurementAudit.medicion_id == prev_m.id).delete()
        db.delete(prev_m)
        db.commit()
    db.close()

    create_payload = {
        "indicador_id": ind_id,
        "municipio_id": None, # Consolidado Estadal
        "periodo_anio": 2026,
        "periodo_tipo": "MENSUAL",
        "periodo_mes": 10,
        "valor_registrado": 500.0,
        "meta_periodo": 500.0,
        "observaciones": "Prueba de ciclo de vida de medición e inmunidad de versiones"
    }

    create_resp = client.post("/api/v1/mediciones/", json=create_payload, headers=headers)
    assert create_resp.status_code == 201
    medicion = create_resp.json()

    medicion_id = medicion["id"]
    assert medicion["valor_registrado"] == 500.0

    # 4. Aprobar la medición por parte del Encargado de unidad
    aprob_resp = client.post(f"/api/v1/mediciones/{medicion_id}/aprobar", headers=headers)
    assert aprob_resp.status_code == 200
    assert aprob_resp.json()["estado"] == "APROBADO"

    # 5. Modificar la medición con un error simulado (ej. valor_registrado = 99999.0) y motivo obligatorio
    update_resp = client.put(f"/api/v1/mediciones/{medicion_id}", json={
        "valor_registrado": 99999.0,
        "motivo_cambio": "Digitación errónea accidental de captura"
    }, headers=headers)
    assert update_resp.status_code == 200
    assert update_resp.json()["valor_registrado"] == 99999.0

    # 6. Consultar el historial de versiones inmutables
    versiones_resp = client.get(f"/api/v1/mediciones/{medicion_id}/versiones", headers=headers)
    assert versiones_resp.status_code == 200
    versiones = versiones_resp.json()
    assert len(versiones) >= 2

    # 7. Consultar el Diff entre versiones
    v_nums = [v["numero_version"] for v in versiones]
    v_min = min(v_nums)
    v_max = max(v_nums)
    diff_resp = client.get(f"/api/v1/mediciones/{medicion_id}/diff?version_from={v_min}&version_to={v_max}", headers=headers)
    assert diff_resp.status_code == 200
    diff_data = diff_resp.json()
    assert "valor_registrado" in diff_data["diferencias"]
    assert diff_data["diferencias"]["valor_registrado"]["nuevo"] == 99999.0

    # 8. Revertir a la versión sana previa
    rollback_resp = client.post(f"/api/v1/mediciones/{medicion_id}/revertir", json={
        "version_destino": v_min,
        "motivo": "Reversión técnica de emergencia por error de digitación"
    }, headers=headers)
    assert rollback_resp.status_code == 200
    rollback_result = rollback_resp.json()
    assert rollback_result["status"].upper() == "SUCCESS"

    # 9. Verificar que el valor en la medición activa regresó al valor sano
    check_resp = client.get(f"/api/v1/mediciones/?indicador_id={ind_id}&periodo_anio=2026&periodo_mes=10", headers=headers)
    assert check_resp.status_code == 200
    medicion_restaurada = check_resp.json()[0]
    assert medicion_restaurada["valor_registrado"] == 500.0
