from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_root_web_ui():
    response = client.get("/")
    assert response.status_code == 200
    assert "E-Cart" in response.text or "Flipkart" in response.text or "SmartPhone" in response.text

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_product_search():
    response = client.get("/products/search?query=iphone")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_all_products():
    response = client.get("/products/all")
    assert response.status_code == 200
    assert len(response.json()) >= 10

def test_orders_priority():
    response = client.get("/orders/priority/high")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_chat_query_endpoint():
    response = client.post("/chat/query", json={"query": "Show me iPhones", "customer_id": 37077})
    assert response.status_code == 200
    data = response.json()
    assert "iphone" in data["response"].lower() or "apple" in data["response"].lower() or len(data.get("products", [])) > 0
