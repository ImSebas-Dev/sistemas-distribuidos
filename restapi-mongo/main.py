from fastapi import FastAPI, HTTPException
from models.portatiles import Portatil
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI(title="Gestión de Portátiles")

# Conexión con MongoDB
client = AsyncIOMotorClient("mongodb+srv://imsebas:1203@sistemas-distribuidos.hilonhx.mongodb.net/")
db = client["tienda"]
collection = db["portatiles"]

# Helper para ObjectId
def portatil_helper(portatil) -> dict:
    return {
        "id": str(portatil["_id"]),
        "marca": portatil["marca"],
        "modelo": portatil["modelo"],
        "procesador": portatil["procesador"],
        "ram": portatil["ram"],
        "almacenamiento": portatil["almacenamiento"],
        "precio": portatil["precio"],
        "estado": portatil["estado"]
    }

# POST - Crear
@app.post("/portatiles/")
async def crear_portatil(portatil: Portatil):
    nuevo = await collection.insert_one(portatil.dict())
    creado = await collection.find_one({"_id": nuevo.inserted_id})
    return portatil_helper(creado)

# GET - Listar todos
@app.get("/portatiles/")
async def listar_portatiles():
    portatiles = []
    async for p in collection.find():
        portatiles.append(portatil_helper(p))
    return portatiles

# GET - Buscar por ID
@app.get("/portatiles/{id}")
async def buscar_portatil(id: str):
    portatil = await collection.find_one({"_id": ObjectId(id)})
    if not portatil:
        raise HTTPException(status_code=404, detail="Portátil no encontrado")
    return portatil_helper(portatil)

# PATCH - Actualizar
@app.patch("/portatiles/{id}")
async def actualizar_portatil(id: str, datos: dict):
    result = await collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": datos}
    )
    return {"mensaje": "Portátil actualizado correctamente"}

# DELETE - Eliminar
@app.delete("/portatiles/{id}")
async def eliminar_portatil(id: str):
    eliminado = await collection.find_one_and_delete({"_id": ObjectId(id)})
    if not eliminado:
        raise HTTPException(status_code=404, detail="Portátil no encontrado")
    return {"mensaje": "Portátil eliminado correctamente"}