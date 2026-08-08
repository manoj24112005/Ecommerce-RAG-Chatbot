import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional, Tuple
import logging
import os
from pathlib import Path
import pickle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

try:
    from sentence_transformers import SentenceTransformer
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

class ECommerceRAG:
    """
    Strict 3-Stage Grounded RAG Pipeline:
    1. Retrieval: Vector similarity search against local catalog embeddings.
    2. Augmentation: Ground-truth context construction from retrieved product metadata.
    3. Generation: Constrained LLM response generation with anti-hallucination guardrails.
    """
    
    def __init__(self, 
                 product_dataset_path: str, 
                 order_dataset_path: str,
                 model_name: str = "all-MiniLM-L6-v2"):
        """Initialize RAG pipeline datasets and embedding model"""
        self.product_dataset_path = product_dataset_path
        self.order_dataset_path = order_dataset_path
        self.product_df = pd.read_csv(product_dataset_path)
        self.order_df = pd.read_csv(order_dataset_path)
        
        self.model = None
        if SENTENCE_TRANSFORMERS_AVAILABLE:
            try:
                self.model = SentenceTransformer(model_name)
            except Exception as e:
                logger.warning(f"Could not load SentenceTransformer: {e}")
        else:
            logger.info("sentence-transformers not installed; using TF-IDF fallback for serverless environment.")
            
        self._preprocess_data()
        self._create_product_embeddings()
        
        self.gemini_model = None
        api_key = os.environ.get("GEMINI_API_KEY")
        if GEMINI_AVAILABLE and api_key:
            try:
                genai.configure(api_key=api_key)
                for m_name in ["gemini-2.0-flash", "gemini-flash-latest", "gemini-3.6-flash"]:
                    try:
                        self.gemini_model = genai.GenerativeModel(m_name)
                        logger.info(f"Initialized Gemini LLM ({m_name}) for strictly grounded RAG generation.")
                        break
                    except Exception:
                        continue
            except Exception as e:
                logger.warning(f"Could not initialize Gemini LLM: {e}")

    def _preprocess_data(self):
        """Preprocess catalog and order datasets"""
        for col in self.product_df.columns:
            if self.product_df[col].dtype == 'object':
                self.product_df[col] = self.product_df[col].fillna('')

        for col in self.order_df.columns:
            if self.order_df[col].dtype == 'object':
                self.order_df[col] = self.order_df[col].fillna('')

        if 'Product_Title' not in self.product_df.columns:
            column_mapping = {
                'title': 'Product_Title',
                'average_rating': 'Rating',
                'description': 'Description',
                'price': 'Price',
                'parent_asin': 'Product_ID'
            }
            for old_col, new_col in column_mapping.items():
                if old_col in self.product_df.columns:
                    self.product_df[new_col] = self.product_df[old_col]

        if 'Order_DateTime' not in self.order_df.columns:
            if 'Order_Date' in self.order_df.columns and 'Time' in self.order_df.columns:
                self.order_df['Order_DateTime'] = pd.to_datetime(
                    self.order_df['Order_Date'].astype(str) + ' ' +
                    self.order_df['Time'].astype(str)
                )
            else:
                logger.warning("Order data missing datetime information")
                return
        else:
            self.order_df['Order_DateTime'] = pd.to_datetime(self.order_df['Order_DateTime'])

        self.order_df = self.order_df.sort_values('Order_DateTime', ascending=False)
    
    def _create_product_embeddings(self):
        """Create or load cached dense vector embeddings for products, plus TF-IDF fallback"""
        self.texts = self.product_df.apply(
            lambda x: f"{x.get('Product_Title', '')} {x.get('Brand', '')} {x.get('Category', '')} {x.get('Description', '')} {x.get('Ram_Storage', '')} {x.get('Processor', '')} {x.get('Camera_Specs', '')}", 
            axis=1
        ).tolist()

        if SKLEARN_AVAILABLE:
            try:
                self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
                self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.texts)
            except Exception as e:
                logger.warning(f"Could not initialize TF-IDF vectorizer: {e}")

        embeddings_path = Path(self.product_dataset_path).parent / "product_embeddings.pkl"
        if embeddings_path.exists():
            try:
                with open(embeddings_path, 'rb') as f:
                    self.product_embeddings = pickle.load(f)
                if len(self.product_embeddings) == len(self.product_df):
                    logger.info("Loaded pre-computed embeddings successfully.")
                    return
            except Exception as e:
                logger.warning(f"Could not load pre-computed embeddings: {e}")

        if self.model is not None:
            logger.info("Generating product embeddings...")
            self.product_embeddings = self.model.encode(self.texts)

    def extract_category_intent(self, query: str) -> Optional[str]:
        """Extract explicit category intent from query to prevent cross-category matches (e.g. phones returned for camera queries)"""
        q = query.lower()
        if any(w in q for w in ['camera', 'cameras', 'dslr', 'mirrorless', 'vlog', 'vlogging', 'action cam']):
            return 'Cameras'
        if any(w in q for w in ['laptop', 'laptops', 'computer', 'desktop', 'macbook', 'workstation', 'notebook', 'ultrabook', 'pc']):
            return 'Laptops'
        if any(w in q for w in ['phone', 'phones', 'smartphone', 'smartphones', 'mobile', 'iphone']):
            return 'Smartphones'
        if any(w in q for w in ['watch', 'watches', 'smartwatch', 'smartwatches']):
            return 'Smartwatches'
        if any(w in q for w in ['headphone', 'headphones', 'earbud', 'earbuds', 'audio', 'anc', 'earphone']):
            return 'Audio'
        if any(w in q for w in ['charger', 'chargers', 'power bank', 'cable', 'cables', 'adapter']):
            return 'Chargers'
        return None

    # -------------------------------------------------------------
    # STAGE 1: RETRIEVAL
    # -------------------------------------------------------------
    def retrieve(self, query: str, top_k: int = 2, min_rating: Optional[float] = None, max_price: Optional[float] = None, category_filter: Optional[str] = None) -> Tuple[List[Dict[str, Any]], float]:
        """
        Stage 1 Retrieval: Compute dense vector or TF-IDF similarity against store catalog.
        Filter out low-similarity, non-matching, or category-mismatched items.
        """
        if self.model is not None and hasattr(self, 'product_embeddings'):
            query_embedding = self.model.encode(query)
            similarities = np.dot(self.product_embeddings, query_embedding)
        elif SKLEARN_AVAILABLE and hasattr(self, 'tfidf_matrix'):
            query_vec = self.tfidf_vectorizer.transform([query])
            similarities = cosine_similarity(self.tfidf_matrix, query_vec).flatten()
        else:
            similarities = np.zeros(len(self.product_df))
        
        results_df = self.product_df.copy()
        results_df['similarity'] = similarities
        
        has_category_match = False
        # Apply strict category intent filter if present
        if category_filter is not None:
            cat_col = 'Category' if 'Category' in results_df.columns else ('main_category' if 'main_category' in results_df.columns else '')
            if cat_col:
                cat_matches = results_df[results_df[cat_col].astype(str).str.lower().str.contains(category_filter.lower())]
                if not cat_matches.empty:
                    results_df = cat_matches
                    has_category_match = True
        
        if min_rating is not None:
            results_df = results_df[results_df['Rating'] >= min_rating]
        
        if max_price is not None:
            results_df = results_df[results_df['Price'] <= max_price]
        
        # Deduplicate matches by Product_ID / parent_asin
        if 'Product_ID' in results_df.columns:
            results_df = results_df.drop_duplicates(subset=['Product_ID'])
        elif 'parent_asin' in results_df.columns:
            results_df = results_df.drop_duplicates(subset=['parent_asin'])
            
        results_df = results_df.sort_values('similarity', ascending=False)
        top_similarity = results_df.iloc[0]['similarity'] if not results_df.empty else 0.0
        
        # Lower threshold when category match is explicitly found (0.05 vs 0.20)
        min_threshold = 0.05 if has_category_match else 0.20
        if top_similarity < min_threshold and not has_category_match:
            return [], top_similarity
            
        top_matches = results_df.head(top_k).to_dict('records')
        return top_matches, top_similarity
        return top_matches, top_similarity

    # -------------------------------------------------------------
    # STAGE 2: AUGMENTATION
    # -------------------------------------------------------------
    def augment(self, retrieved_products: List[Dict[str, Any]]) -> str:
        """
        Stage 2 Augmentation: Format retrieved store items into structured ground-truth context.
        """
        if not retrieved_products:
            return "NO RELEVANT PRODUCTS FOUND IN STORE CATALOG."

        context_blocks = []
        for i, p in enumerate(retrieved_products, 1):
            context_blocks.append(
                f"--- PRODUCT MATCH #{i} ---\n"
                f"Product ID: {p.get('Product_ID', p.get('parent_asin'))}\n"
                f"Title: {p.get('Product_Title')}\n"
                f"Brand: {p.get('Brand')}\n"
                f"Category: {p.get('Category')}\n"
                f"Price: ₹{float(p.get('Price', 0)):,.0f}\n"
                f"Rating: {p.get('Rating')} Stars ({p.get('Rating_Count', 400)} ratings)\n"
                f"RAM/Storage: {p.get('Ram_Storage', 'N/A')}\n"
                f"Processor: {p.get('Processor', 'N/A')}\n"
                f"Camera Specs: {p.get('Camera_Specs', 'N/A')}\n"
                f"Battery Specs: {p.get('Battery', 'N/A')}\n"
                f"Description: {p.get('Description', '')}\n"
            )
        return "\n".join(context_blocks)

    # -------------------------------------------------------------
    # STAGE 3: GENERATION (CONSTRAINED & ANTI-HALLUCINATION)
    # -------------------------------------------------------------
    def generate(self, query: str, augmented_context: str, retrieved_products: List[Dict[str, Any]], similarity: float) -> str:
        """
        Stage 3 Generation: Synthesize response using LLM with zero-hallucination guardrails.
        Rejects off-topic / ungrounded queries immediately.
        """
        # Refusal guardrail for empty context
        if not retrieved_products or "NO RELEVANT PRODUCTS FOUND" in augmented_context:
            return (
                "I am restricted to answering questions about products and orders available in our E-Cart catalog.\n\n"
                "I cannot provide information on unlisted items or off-topic subjects. "
                "Please ask about available Laptops, Desktops, Monitors, Gaming Mice, Keyboards, Cameras, Smartwatches, or Phones!"
            )

        if self.gemini_model:
            try:
                system_prompt = (
                    f"You are the official E-Cart AI Tech Shopping Assistant.\n"
                    f"User Query: {query}\n\n"
                    f"GROUND-TRUTH STORE CONTEXT:\n{augmented_context}\n\n"
                    f"STRICT UNCOMPROMISING RULES:\n"
                    f"1. You MUST ONLY use the ground-truth store context above to answer the user query.\n"
                    f"2. Do NOT use any external pre-trained knowledge or guess facts.\n"
                    f"3. Do NOT mention any external brand or product not listed in the ground-truth context.\n"
                    f"4. Quote exact prices in Indian Rupees (₹).\n"
                    f"5. If the query asks for anything outside this store context, respond ONLY with:\n"
                    f"   'I am restricted to answering questions about products and orders available in our E-Cart catalog.'"
                )
                response = self.gemini_model.generate_content(system_prompt)
                if response and response.text:
                    return response.text.strip()
            except Exception as e:
                logger.warning(f"Gemini generation error: {e}")

        # Deterministic grounded template fallback (when Gemini API is unconfigured/unavailable)
        count = len(retrieved_products)
        item_word = "top recommendation" if count == 1 else "top 2 recommendations"
        intro = f"Here is my {item_word} from our E-Cart store catalog for **\"{query}\"**:\n\n"
        
        details = []
        for i, p in enumerate(retrieved_products, 1):
            specs_summary = []
            if p.get('Ram_Storage'): specs_summary.append(f"💾 {p['Ram_Storage']}")
            if p.get('Processor'): specs_summary.append(f"⚡ {p['Processor']}")
            if p.get('Camera_Specs') and p['Camera_Specs'] != 'N/A': specs_summary.append(f"📸 {p['Camera_Specs']}")
            if p.get('Battery') and p['Battery'] != 'N/A': specs_summary.append(f"🔋 {p['Battery']}")
            
            specs_line = " | ".join(specs_summary)
            orig_price = f" *(MRP: ₹{float(p['Original_Price']):,.0f})*" if p.get('Original_Price') else ""
            
            details.append(
                f"**Option {i}: {p['Product_Title']}**\n"
                f"🏷️ **₹{float(p['Price']):,.0f}**{orig_price} | ⭐ **{float(p['Rating']):.1f} Stars**\n"
                f"{specs_line}\n"
                f"*{p.get('Description', '')[:130]}...*\n"
            )
        
        outro = "👇 *Click the product card below to view details or add to cart!*"
        return intro + "\n".join(details) + outro

    def get_customer_orders(self, customer_id: int) -> List[Dict[str, Any]]:
        """Get orders for a specific customer"""
        customer_orders = self.order_df[self.order_df['Customer_Id'] == customer_id]
        return customer_orders.sort_values('Order_DateTime', ascending=False).to_dict('records')
    
    def get_high_priority_orders(self) -> List[Dict[str, Any]]:
        """Get high priority orders"""
        high_priority = self.order_df[
            self.order_df['Order_Priority'].str.lower() == 'high'
        ]
        return high_priority.sort_values('Order_DateTime', ascending=False).head(5).to_dict('records')
    
    def format_single_order(self, order: Dict[str, Any]) -> str:
        """Format single order details in INR (₹)"""
        dt_str = pd.Timestamp(order['Order_DateTime']).strftime('%Y-%m-%d %H:%M:%S')
        sales_val = float(order['Sales'])
        shipping_val = float(order['Shipping_Cost'])
        return (f"📦 **Order #{order['Order_ID']} Details**\n"
                f"- **Item**: {order['Product']}\n"
                f"- **Category**: {order.get('Product_Category', 'Tech')}\n"
                f"- **Date**: {dt_str}\n"
                f"- **Total Amount**: ₹{sales_val:,.2f}\n"
                f"- **Shipping Cost**: ₹{shipping_val:,.2f}\n"
                f"- **Order Priority**: {order['Order_Priority']}\n"
                f"- **Payment Method**: {order.get('Payment_method', 'Online')}")
    
    def format_high_priority_orders(self, orders: List[Dict[str, Any]]) -> str:
        """Format high priority orders list in INR (₹)"""
        if not orders:
            return "No high priority orders found in store."
        
        response = "🔥 **Top High-Priority Orders:**\n\n"
        for i, order in enumerate(orders, 1):
            dt_str = pd.Timestamp(order['Order_DateTime']).strftime('%b %d, %Y %I:%M %p')
            response += (
                f"{i}. **{order['Product']}**\n"
                f"   - Customer ID: `{order['Customer_Id']}` | Date: {dt_str}\n"
                f"   - Amount: ₹{float(order['Sales']):,.2f} | Priority: **{order['Order_Priority']}**\n\n"
            )
        return response.strip()

    def get_gaming_setup_bundle(self) -> Tuple[str, List[Dict[str, Any]]]:
        """Assemble a complete high-end Gaming Setup bundle from store inventory with 5 unique components"""
        setup_specs = [
            ("Gaming Tower PC", ["strix", "omen"]),
            ("Gaming Display", ["odyssey", "ultragear"]),
            ("Pro Gaming Mouse", ["superlight"]),
            ("Mechanical Keyboard", ["blackwidow"]),
            ("Spatial Audio Headset", ["cloud iii"])
        ]
        setup_items = []
        seen_ids = set()

        for category_label, keywords in setup_specs:
            found = False
            for kw in keywords:
                matches = self.product_df[self.product_df['Product_Title'].str.lower().str.contains(kw)]
                for _, row in matches.iterrows():
                    p_dict = row.to_dict()
                    p_id = p_dict.get('Product_ID', p_dict.get('parent_asin'))
                    if p_id not in seen_ids:
                        seen_ids.add(p_id)
                        p_dict['setup_label'] = category_label
                        setup_items.append(p_dict)
                        found = True
                        break
                if found:
                    break

        total_price = sum([float(p['Price']) for p in setup_items])
        
        item_lines = []
        for i, item in enumerate(setup_items, 1):
            label = item.get('setup_label', 'Component')
            item_lines.append(f"{i}. **{label}**: {item['Product_Title']}")

        items_text = "\n".join(item_lines)

        text = (
            f"🎮 **Ultimate E-Cart Pro Gaming Setup Bundle**\n\n"
            f"Here is the complete high-performance gaming setup curated directly from our store catalog:\n\n"
            f"{items_text}\n\n"
            f"💰 **Total Setup Value**: **₹{total_price:,.0f}**\n"
            f"👇 *Click any component below to view full specs or add it to your cart!*"
        )
        return text, setup_items

    # -------------------------------------------------------------
    # MAIN QUERY PROCESSING ENTRY POINT
    # -------------------------------------------------------------
    def process_query(self, query: str, customer_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Main RAG Pipeline entry point executing Retrieval ➔ Augmentation ➔ Generation.
        """
        query_lower = query.lower()
        
        # Handle Gaming Setup / Multi-product bundle intent
        setup_triggers = [
            'gaming setup', 'build a gaming setup', 'setup', 'gaming set up', 
            'gaming bundle', 'pc setup', 'set of products for gaming', 
            'gaming set', 'setup for gaming', 'build a pc', 'gaming desktop setup'
        ]
        if any(term in query_lower for term in setup_triggers):
            text_res, setup_products = self.get_gaming_setup_bundle()
            return {
                "response": text_res,
                "products": setup_products
            }
        
        # Extract price constraints if present
        max_price = None
        if 'under' in query_lower:
            import re
            numbers = re.findall(r'\d+', query_lower.replace(',', ''))
            if numbers:
                val = float(numbers[0])
                if val < 500:
                    val = val * 1000
                max_price = val

        # Handle order relational queries
        if 'high priority' in query_lower or ('recent' in query_lower and 'priority' in query_lower):
            orders = self.get_high_priority_orders()
            return {"response": self.format_high_priority_orders(orders), "products": []}
        
        if any(keyword in query_lower for keyword in ['order', 'orders', 'purchase', 'bought', 'my order']):
            if not customer_id:
                return {"response": "Please specify your Customer ID (e.g. 37077) to retrieve your order details.", "products": []}
            
            orders = self.get_customer_orders(customer_id)
            if not orders:
                return {"response": f"No orders found for Customer ID `{customer_id}`.", "products": []}
            return {"response": self.format_single_order(orders[0]), "products": []}
        
        # Extract category intent (e.g. "camera" -> "Cameras")
        cat_intent = self.extract_category_intent(query)
        
        # 1. RETRIEVAL STAGE
        retrieved_products, similarity = self.retrieve(query, top_k=2, max_price=max_price, category_filter=cat_intent)
        
        # 2. AUGMENTATION STAGE
        augmented_context = self.augment(retrieved_products)
        
        # 3. GENERATION STAGE (Anti-Hallucination Guardrails)
        text_response = self.generate(query, augmented_context, retrieved_products, similarity)
        
        attached_products = retrieved_products if retrieved_products else []
        
        return {
            "response": text_response,
            "products": attached_products
        }
