from fastapi.testclient import TestClient
from catalog.main import app

client = TestClient(app)

def test_listar_productos():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_producto_existente():
    response = client.get("/products/p1")
    assert response.status_code == 200
    assert response.json()["price"] == 24990

def test_producto_inexistente():
    response = client.get("/products/no-existe")
    assert response.status_code == 404