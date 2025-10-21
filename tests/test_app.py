import json
from app.main import create_app

def test_healthz():
    app = create_app()
    client = app.test_client()
    r = client.get("/healthz")
    assert r.status_code == 200
    data = r.get_json()
    assert data["status"] == "ok"

def test_info():
    app = create_app()
    client = app.test_client()
    r = client.get("/api/info")
    assert r.status_code == 200
    data = r.get_json()
    assert "build" in data

def test_error_endpoint():
    app = create_app()
    client = app.test_client()
    r = client.get("/api/error")
    assert r.status_code == 500
