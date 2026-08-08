from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any, Optional
import pandas as pd
from ...config import Settings

router = APIRouter()
settings = Settings()

def get_product_df():
    df = pd.read_csv(settings.PRODUCT_DATA_PATH)
    df.fillna('', inplace=True)
    return df

@router.get("/all", response_model=List[Dict[str, Any]])
async def get_all_products(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    max_price: Optional[float] = None,
    sort_by: Optional[str] = Query(default="rating_desc")
):
    """Retrieve all products with optional filters"""
    df = get_product_df()
    
    if category and category.lower() != "all":
        df = df[df['Category'].str.contains(category, case=False, na=False)]
        
    if brand:
        df = df[df['Brand'].str.contains(brand, case=False, na=False)]
        
    if max_price:
        df = df[df['Price'] <= max_price]
        
    if sort_by == "price_asc":
        df = df.sort_values('Price', ascending=True)
    elif sort_by == "price_desc":
        df = df.sort_values('Price', ascending=False)
    else:
        df = df.sort_values('Rating', ascending=False)
        
    return df.to_dict('records')

@router.get("/search", response_model=List[Dict[str, Any]])
async def search_products(
    query: str = Query(..., min_length=1),
    category: Optional[str] = None,
    min_rating: Optional[float] = None,
    max_price: Optional[float] = None,
    limit: int = Query(default=20, ge=1, le=50)
):
    """Search products with various filters"""
    df = get_product_df()
    
    if query:
        search_mask = (
            df['Product_Title'].str.contains(query, case=False, na=False) |
            df['Description'].str.contains(query, case=False, na=False) |
            df['Category'].str.contains(query, case=False, na=False) |
            df['Brand'].str.contains(query, case=False, na=False)
        )
        df = df[search_mask]
    
    if category and category.lower() != "all":
        df = df[df['Category'].str.contains(category, case=False, na=False)]
    
    if min_rating is not None:
        df = df[df['Rating'] >= min_rating]
    
    if max_price is not None:
        df = df[df['Price'] <= max_price]
    
    df = df.sort_values('Rating', ascending=False).head(limit)
    return df.to_dict('records')

@router.get("/detail/{product_id}", response_model=Dict[str, Any])
async def get_product_by_id(product_id: int):
    """Retrieve single product details by ID"""
    df = get_product_df()
    match = df[df['Product_ID'] == product_id]
    if match.empty:
        raise HTTPException(status_code=404, detail="Product not found")
    return match.iloc[0].to_dict()

@router.get("/category/{category}", response_model=List[Dict[str, Any]])
async def get_products_by_category(
    category: str,
    limit: int = Query(default=20, ge=1, le=50),
    min_rating: Optional[float] = None
):
    """Retrieve products in a specific category"""
    df = get_product_df()
    category_products = df[df['Category'].str.contains(category, case=False, na=False)].copy()
    
    if min_rating is not None:
        category_products = category_products[category_products['Rating'] >= min_rating]
    
    category_products = category_products.sort_values('Rating', ascending=False).head(limit)
    return category_products.to_dict('records')

@router.get("/top-rated", response_model=List[Dict[str, Any]])
async def get_top_rated_products(
    min_rating: float = Query(4.0, ge=0, le=5),
    category: Optional[str] = None,
    limit: int = Query(default=10, ge=1, le=50)
):
    """Get top-rated products"""
    df = get_product_df()
    top_products = df[df['Rating'] >= min_rating].copy()
    if category and category.lower() != "all":
        top_products = top_products[top_products['Category'].str.contains(category, case=False, na=False)]
    
    top_products = top_products.sort_values('Rating', ascending=False).head(limit)
    return top_products.to_dict('records')