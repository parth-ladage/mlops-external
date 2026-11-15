from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_addition():
    response = client.post("/add", params={"a": 10, "b": 20})
    assert response.status_code == 200
    assert response.json() == {"result": 30}

def test_zero():
    response = client.post("/add", params={"a": 10, "b": 0})
    assert response.json() == {"result": 10}

def test_negative():
    response = client.post("/add", params={"a": -5, "b": 10})
    assert response.json() == {"result": 5}
