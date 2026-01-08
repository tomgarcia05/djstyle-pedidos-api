from fastapi import FastAPI
from app.routes.pedidos import router as pedidos_router

app = FastAPI(title="DJStyle Pedidos API")

app.include_router(pedidos_router, prefix="/pedidos")

@app.get("/")
def root():
    return {"status": "ok"}
