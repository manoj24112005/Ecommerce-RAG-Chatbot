from src.rag.assistant import ECommerceRAG
from src.config import Settings

def test_rag_assistant():
    settings = Settings()
    rag = ECommerceRAG(
        product_dataset_path=settings.PRODUCT_DATA_PATH,
        order_dataset_path=settings.ORDER_DATA_PATH
    )
    
    # Test product query
    res = rag.process_query("acoustic guitar")
    assert "guitars" in res.lower() or "guitar" in res.lower() or "product" in res.lower()
    
    # Test high priority order query
    res_priority = rag.process_query("high priority orders")
    assert "high-priority" in res_priority.lower() or "order" in res_priority.lower()

    # Test customer order query
    res_customer = rag.process_query("show my orders", customer_id=37077)
    assert "order" in res_customer.lower()
