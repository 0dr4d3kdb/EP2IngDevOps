from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="catalog")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PRODUCTS = {
    "p1": {"name": "Teclado", "price": 24990},
    "p2": {"name": "Mouse", "price": 12990},
    "p3": {"name": "Monitor", "price": 189990},
}


@app.get("/products")
def list_products():
    return [{"id": pid, **product} for pid, product in PRODUCTS.items()]


@app.get("/products/{product_id}")
def get_product(product_id: str):
    product = PRODUCTS.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"id": product_id, **product}

@app.get("/health")
def health():
    return {"status": "ok"}