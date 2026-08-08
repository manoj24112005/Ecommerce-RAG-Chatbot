from src.rag.assistant import ECommerceRAG
from src.config import Settings

def test_rag_assistant():
    settings = Settings()
    rag = ECommerceRAG(
        product_dataset_path=settings.PRODUCT_DATA_PATH,
        order_dataset_path=settings.ORDER_DATA_PATH
    )
    
    # Test catalog product query retrieval & generation
    res = rag.process_query("best camera phone")
    assert "response" in res
    assert len(res["response"]) > 0
    assert len(res["products"]) > 0
    
    # Test high priority order query
    res_priority = rag.process_query("high priority orders")
    assert "response" in res_priority
    assert "priority" in res_priority["response"].lower() or "order" in res_priority["response"].lower()

    # Test customer order query
    res_customer = rag.process_query("show my orders", customer_id=37077)
    assert "response" in res_customer
    assert "order" in res_customer["response"].lower()

def test_anti_hallucination_refusal():
    settings = Settings()
    rag = ECommerceRAG(
        product_dataset_path=settings.PRODUCT_DATA_PATH,
        order_dataset_path=settings.ORDER_DATA_PATH
    )
    
    # Test off-topic query refusal (unlisted brand / general knowledge)
    off_topic_res = rag.process_query("tell me about Toyota electric cars")
    assert "response" in off_topic_res
    assert "restricted" in off_topic_res["response"].lower() or "catalog" in off_topic_res["response"].lower()
    assert len(off_topic_res["products"]) == 0

def test_camera_under_50k_no_phones():
    settings = Settings()
    rag = ECommerceRAG(
        product_dataset_path=settings.PRODUCT_DATA_PATH,
        order_dataset_path=settings.ORDER_DATA_PATH
    )
    
    # Test camera under 50k query returns real cameras and 0 phones
    res = rag.process_query("camera under 50 k")
    assert "response" in res
    assert len(res["products"]) > 0
    for p in res["products"]:
        cat = str(p.get("Category", "")).lower()
        assert "camera" in cat
        assert float(p["Price"]) <= 50000

def test_gaming_setup_multi_product_bundle():
    settings = Settings()
    rag = ECommerceRAG(
        product_dataset_path=settings.PRODUCT_DATA_PATH,
        order_dataset_path=settings.ORDER_DATA_PATH
    )
    
    # Test setup phrasing returns full 5-item bundle
    res = rag.process_query("set of products for gaming set up")
    assert "response" in res
    assert len(res["products"]) == 5
