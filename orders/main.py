import os
from itertools import count

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query

app = FastAPI(title="orders")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CATALOG_URL = os.getenv("CATALOG_URL", "http://localhost:8002")

ORDERS = {}
order_ids = count(1)


@app.post("/orders")
def create_order(product_id: str, quantity: int = Query(default=1, ge=1)):
    try:
        response = httpx.get(f"{CATALOG_URL}/products/{product_id}", timeout=3)
    except httpx.HTTPError:
        raise HTTPException(status_code=503, detail="Catalogo no disponible")

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    if response.status_code != 200:
        raise HTTPException(status_code=503, detail="Catalogo no disponible")

    product = response.json()
    order = {
        "id": next(order_ids),
        "product_id": product_id,
        "name": product["name"],
        "quantity": quantity,
        "total": product["price"] * quantity,
    }
    ORDERS[order["id"]] = order
    return order


@app.get("/orders")
def list_orders():
    return list(ORDERS.values())

@app.get("/health")
def health():
    return {"status": "ok"}