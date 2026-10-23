import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token(cedula: str, password: str = "pbkdf2_sha256$hashedpasswordeco") -> str:
    response = client.post("/api/v1/auth/login", json={
        "cedula": cedula,
        "password": password
    })
    if response.status_code != 200:
        # Fallback para contraseñas de prueba
        response = client.post("/api/v1/auth/login", json={
            "cedula": cedula,
            "password": "gerente2026"
        })
    return response.json()["access_token"]

def test_get_unit_measurements():
    token = get_token("V-12345678", "gerente2026")
    response = client.get(
        "/api/v1/mediciones/unidad/ECO?periodo_anio=2026&periodo_mes=8",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["departamento_codigo"] == "ECO"
    assert data["total_indicadores"] >= 5
    assert len(data["items"]) >= 5

def test_batch_upload_authorized_unit_chief():
    # Login como Jefe de Unidad de Estadísticas Económicas (V-14892103)
    token = get_token("V-14892103")
    
    payload = {
        "departamento_codigo": "ECO",
        "periodo_anio": 2026,
        "periodo_mes": 10,
        "motivo_general": "Carga de prueba automatizada para Octubre 2026",
        "mediciones": [
            {
                "indicador_codigo": "ECO-CAN-02",
                "valor_registrado": 2200,
                "meta_periodo": 2200,
                "observaciones": "2200 precios efectivos"
            },
            {
                "indicador_codigo": "ECO-CAN-04",
                "valor_registrado": 25,
                "meta_periodo": 25,
                "observaciones": "25 comunas cubiertas"
            }
        ]
    }

    response = client.post(
        "/api/v1/mediciones/lote",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["departamento_codigo"] == "ECO"
    assert data["total_procesados"] == 2
    assert len(data["mediciones"]) == 2

def test_batch_upload_forbidden_different_unit():
    # Jefe de Unidad de Estadísticas Económicas intentando cargar en CART (Cartografía)
    token = get_token("V-14892103")

    payload = {
        "departamento_codigo": "CART",
        "periodo_anio": 2026,
        "periodo_mes": 10,
        "motivo_general": "Intento de carga no autorizada",
        "mediciones": [
            {
                "indicador_codigo": "CART-CIR-01",
                "valor_registrado": 100
            }
        ]
    }

    response = client.post(
        "/api/v1/mediciones/lote",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )
    # Debe ser rechazado con 403 Forbidden por RBAC
    assert response.status_code == 403
    assert "No tiene permiso" in response.json()["detail"]

def test_certify_unit_measurements():
    # El Gerente Estadal o Jefe de la unidad certifica las cifras
    token = get_token("V-12345678", "gerente2026")

    response = client.post(
        "/api/v1/mediciones/unidad/ECO/certificar?periodo_anio=2026&periodo_mes=10",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["departamento_codigo"] == "ECO"
    assert data["total_certificados"] >= 1
    assert "certificado" in data["mensaje"].lower()

def test_unit_chief_isolation_and_rbac():
    # Login como Jefe de Unidad de Estadísticas Económicas (ECO)
    token = get_token("V-14892103", "gerente2026")
    headers = {"Authorization": f"Bearer {token}"}

    # 1. No debe poder acceder al Resumen Ejecutivo consolidado (403 Forbidden)
    res_dash = client.get("/api/v1/dashboard/resumen", headers=headers)
    assert res_dash.status_code == 403
    assert "restringido" in res_dash.json()["detail"].lower()

    # 2. En /indicadores/ solo debe recibir indicadores de ECO
    res_ind = client.get("/api/v1/indicadores/", headers=headers)
    assert res_ind.status_code == 200
    ind_items = res_ind.json()
    assert len(ind_items) > 0
    for item in ind_items:
        assert item["departamento_codigo"] == "ECO"

    # 3. En /departamentos/ solo debe recibir su departamento ECO
    res_dept = client.get("/api/v1/departamentos/", headers=headers)
    assert res_dept.status_code == 200
    dept_items = res_dept.json()
    assert len(dept_items) == 1
    assert dept_items[0]["codigo"] == "ECO"

