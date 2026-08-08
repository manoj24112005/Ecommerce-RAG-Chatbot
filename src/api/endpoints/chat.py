from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from ...rag.assistant import ECommerceRAG
from ...config import Settings
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
settings = Settings()

# Lazy initialize or initialize RAG assistant
try:
    ASSISTANT = ECommerceRAG(
        product_dataset_path=settings.PRODUCT_DATA_PATH,
        order_dataset_path=settings.ORDER_DATA_PATH
    )
except Exception as e:
    logger.error(f"Failed to load RAG assistant: {e}")
    ASSISTANT = None

class ChatRequest(BaseModel):
    query: str
    customer_id: Optional[int] = None

class ChatResponse(BaseModel):
    query: str
    response: str
    customer_id: Optional[int] = None
    products: Optional[List[Dict[str, Any]]] = None

@router.post("/query", response_model=ChatResponse)
async def process_chat_query(request: ChatRequest):
    """Process a chat query using RAG system"""
    global ASSISTANT
    if ASSISTANT is None:
        # Re-try initialization if failed previously
        try:
            ASSISTANT = ECommerceRAG(
                product_dataset_path=settings.PRODUCT_DATA_PATH,
                order_dataset_path=settings.ORDER_DATA_PATH
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"RAG assistant not initialized: {e}")
    
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    res = ASSISTANT.process_query(request.query, request.customer_id)
    return ChatResponse(
        query=request.query,
        response=res.get("response", ""),
        customer_id=request.customer_id,
        products=res.get("products", [])
    )
