from fastapi import FastAPI, HTTPException, status
from models.producto import Producto

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "Hi Class!"}

@app.post("/productos/")
def crear_producto(producto: Producto):
    return {
        "message": "Producto creado correctamente",
        "data": producto.dict()
    }