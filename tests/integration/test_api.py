from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page_renders():
    r = client.get("/")
    assert r.status_code == 200
    assert "Calculator" in r.text  # covers the HTML response

def test_add_endpoint():
    r = client.get("/add", params={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5

def test_sub_endpoint():
    r = client.get("/sub", params={"a": 2, "b": 5})
    assert r.status_code == 200
    assert r.json()["result"] == -3

def test_mul_endpoint():
    r = client.get("/mul", params={"a": 2.5, "b": 4})
    assert r.status_code == 200
    assert abs(r.json()["result"] - 10.0) < 1e-9

def test_div_endpoint():
    r = client.get("/div", params={"a": 9, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 3

def test_div_by_zero_endpoint():
    r = client.get("/div", params={"a": 1, "b": 0})
    assert r.status_code == 400
    assert r.json()["detail"] == "division by zero"
