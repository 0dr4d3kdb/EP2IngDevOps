from unittest.mock import patch, Mock
from fastapi.testclient import TestClient
from orders.main import app

client = TestClient(app)

def test_crear_orden():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": "p1",
        "name": "Teclado",
        "price": 24990
    }

    with patch(
        "orders.main.httpx.get",
        return_value=mock_response
    ):
        response = client.post(
            "/orders?product_id=p1&quantity=2"
        )

    assert response.status_code == 200
    assert response.json()["total"] == 49980

def test_cantidad_invalida():
    response = client.post(
        "/orders?product_id=p1&quantity=-1"
    )
    assert response.status_code == 422