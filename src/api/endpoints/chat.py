from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
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

@router.post("/query", response_model=ChatResponse)
async def process_chat_query(request: ChatRequest):
    """Process a chat query using RAG system"""
    if ASSISTANT is None:
        raise HTTPException(status_code=500, detail="RAG assistant not initialized")
    
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    res_text = ASSISTANT.process_query(request.query, request.customer_id)
    return ChatResponse(
        query=request.query,
        response=res_text,
        customer_id=request.customer_id
    )
