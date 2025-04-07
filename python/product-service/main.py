from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Product Catalog Service")

# In-memory database
products_db = []

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
    category: str

@app.get("/")
async def root():
    return {"message": "Product Catalog Service is running"}

@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    product.id = len(products_db) + 1
    products_db.append(product)
    return product

@app.get("/products/", response_model=List[Product])
async def get_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/products/category/{category}", response_model=List[Product])
async def get_products_by_category(category: str):
    return [product for product in products_db if product.category.lower() == category.lower()]

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product):
    for i, product in enumerate(products_db):
        if product.id == product_id:
            updated_product.id = product_id
            products_db[i] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for i, product in enumerate(products_db):
        if product.id == product_id:
            products_db.pop(i)
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True) 