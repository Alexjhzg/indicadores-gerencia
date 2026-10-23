import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_variants():
    # Login con y sin prefijo V-
    res_with_v = client.post("/api/v1/auth/login", json={"cedula": "V-8979338", "password": "gerente2026"})
    assert res_with_v.status_code == 200
    token1 = res_with_v.json()["access_token"]
    assert token1 is not None

    res_without_v = client.post("/api/v1/auth/login", json={"cedula": "8979338", "password": "gerente2026"})
    assert res_without_v.status_code == 200
    token2 = res_without_v.json()["access_token"]
    assert token2 is not None

def test_jesus_perez_profile_and_departments():
    res = client.post("/api/v1/auth/login", json={"cedula": "8979338", "password": "gerente2026"})
    token = res.json()["access_token"]

    res_me = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert res_me.status_code == 200
    data = res_me.json()

    assert data["cedula"] == "V-8979338"
    assert data["nombre_completo"] == "Jesús Ramón Pérez"
    assert data["rol_nombre"] == "JEFE_AREA"
    for dept in ["CART", "ECO", "SOC", "SEG"]:
        assert dept in data["departamentos_codigos"]
    assert "DEM" not in data["departamentos_codigos"]
    assert "SEEM" not in data["departamentos_codigos"]

def test_jesus_perez_permissions_allowed():
    res = client.post("/api/v1/auth/login", json={"cedula": "8979338", "password": "gerente2026"})
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Jesús Pérez puede acceder a sus 4 unidades
    for dept in ["CART", "ECO", "SOC", "SEG"]:
        res_dept = client.get(f"/api/v1/mediciones/unidad/{dept}", headers=headers)
        assert res_dept.status_code == 200, f"Error accediendo a {dept}: {res_dept.text}"

def test_jesus_perez_forbidden_departments():
    res = client.post("/api/v1/auth/login", json={"cedula": "8979338", "password": "gerente2026"})
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Jesús Pérez no tiene acceso a DEM ni SEEM
    res_dem = client.get("/api/v1/mediciones/unidad/DEM", headers=headers)
    assert res_dem.status_code == 403

    res_seem = client.get("/api/v1/mediciones/unidad/SEEM", headers=headers)
    assert res_seem.status_code == 403

def test_gerente_luis_alberto_access_all():
    res = client.post("/api/v1/auth/login", json={"cedula": "11206771", "password": "gerente2026"})
    assert res.status_code == 200
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    res_me = client.get("/api/v1/auth/me", headers=headers)
    assert res_me.status_code == 200
    assert res_me.json()["nombre_completo"] == "Luis Alberto"
    assert res_me.json()["rol_nombre"] == "GERENTE"

    # Acceso a todas las unidades
    for dept in ["ECO", "SOC", "DEM", "CART", "SEG", "SEEM"]:
        res_dept = client.get(f"/api/v1/mediciones/unidad/{dept}", headers=headers)
        assert res_dept.status_code == 200

def test_encargado_single_unit_isolation():
    # Wilfredo Rojas (ECO: 13814617)
    res = client.post("/api/v1/auth/login", json={"cedula": "13814617", "password": "gerente2026"})
    assert res.status_code == 200
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Puede acceder a ECO
    res_eco = client.get("/api/v1/mediciones/unidad/ECO", headers=headers)
    assert res_eco.status_code == 200

    # Rechazado en SOC y CART
    res_soc = client.get("/api/v1/mediciones/unidad/SOC", headers=headers)
    assert res_soc.status_code == 403

    res_cart = client.get("/api/v1/mediciones/unidad/CART", headers=headers)
    assert res_cart.status_code == 403
