from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_calculate_add():
    response = client.get("/calculate/add?x=2&y=3")
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "x": 2.0, "y": 3.0, "result": 5.0}

def test_calculate_divide():
    response = client.get("/calculate/divide?x=6&y=2")
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "x": 6.0, "y": 2.0, "result": 3.0}

def test_calculate_divide_by_zero():
    response = client.get("/calculate/divide?x=6&y=0")
    assert response.status_code == 400
    assert "Division by zero" in response.json()["detail"]

def test_invalid_operation():
    response = client.get("/calculate/power?x=2&y=3")
    assert response.status_code == 400
    assert "not supported" in response.json()["detail"]