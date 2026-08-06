from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_root_web_ui():
    response = client.get("/")
    assert response.status_code == 200
    assert "E-Commerce AI Assistant" in response.text

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_product_search():
    response = client.get("/products/search?query=guitar")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_orders_priority():
    response = client.get("/orders/priority/high")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_chat_query_endpoint():
    response = client.post("/chat/query", json={"query": "Show me guitars", "customer_id": 37077})
    assert response.status_code == 200
    data = response.json()
    assert "guitars" in data["response"].lower() or "guitar" in data["response"].lower() or "product" in data["response"].lower()
