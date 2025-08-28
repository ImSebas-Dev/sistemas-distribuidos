from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import JSONResponse
import mysql.connector
import os
import requests

app = FastAPI(title="[SISDIS] FastAPI Project")

# Primer Endpoint
@app.get("/")
def inicio():
    return {"mensaje": "Primer endpoint"}

# Conversión de pesos a dólares
@app.get("/mi-trm")
async def obtener_trm(pesos: str = Form(...)):
        trm = 4500
        try:
            pesos = float(pesos)
            dolares = pesos / trm
        except ValueError:
            raise HTTPException(status_code=400, detail="El valor de pesos debe ser un número válido")
        return {"mensaje": f"El valor de {pesos} pesos es equivalente a {dolares} dólares"}

## Actividad MySQL ##

# Conexión a MySQL
def conexion_mysql():
    try:
        conexion = mysql.connector.connect(
            host="maglev.proxy.rlwy.net",
            user="root",
            password="tHjaliBkKdJUIBMqEkleuBKEJLvDIKDJ",
            port=20228,
            database="railway",
        )
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# POST: Insertar Libro
@app.post("/libros")
async def insertar_libro(titulo: str = Form(...), autor: str = Form(...), anio: int = Form(...), genero: str = Form(...), estado: str = Form(...)):
    try:
        conn = conexion_mysql()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO libros (titulo, autor, anio, genero, estado)
            VALUES (%s, %s, %s, %s, %s);
        """,
            (titulo, autor, anio, genero, estado),
        )
        conn.commit()
        conn.close()
        return {"mensaje": "Libro insertado con éxito"}
    except Exception as e:
        print("Error al insertar el libro:", e)
        raise HTTPException(status_code=400, detail="Error al insertar el libro")


# GET: Listar todos los libros
@app.get("/libros")
async def listar_libros():
    try:
        conn = conexion_mysql()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()
        conn.close()
        return {"libros": libros}
    except Exception as e:
        print("Error al listar los libros:", e)
        raise HTTPException(status_code=500, detail="Error al listar los libros")

# GET: Consultar libro por ID
@app.get("/libros/{libro_id}")
async def consultar_libro(libro_id: int):
    try:
        conn = conexion_mysql()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM libros WHERE id = %s", (libro_id,))
        libro = cursor.fetchone()
        conn.close()
        if libro:
            return {"libro": libro}
        else:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
    except Exception as e:
        print("Error al consultar el libro:", e)
        raise HTTPException(status_code=500, detail="Error al consultar el libro")

# PUT: Actualizar libro por ID
@app.put("/libros/{libro_id}")
async def actualizar_libro(libro_id: int, titulo: str = Form(...), autor: str = Form(...), anio: int = Form(...), genero: str = Form(...), estado: str = Form(...)):
    try:
        conn = conexion_mysql()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE libros
            SET titulo = %s, autor = %s, anio = %s, genero = %s, estado = %s
            WHERE id = %s;
        """,
            (titulo, autor, anio, genero, estado, libro_id),
        )
        conn.commit()
        conn.close()
        return {"mensaje": "Libro actualizado con éxito"}
    except Exception as e:
        print("Error al actualizar el libro:", e)
        raise HTTPException(status_code=500, detail="Error al actualizar el libro")

# DELETE: Eliminar libro por ID
@app.delete("/libros/{libro_id}")
async def eliminar_libro(libro_id: int):
    try:
        conn = conexion_mysql()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
        conn.commit()
        conn.close()
        return {"mensaje": "Libro eliminado con éxito"}
    except Exception as e:
        print("Error al eliminar el libro:", e)
        raise HTTPException(status_code=500, detail="Error al eliminar el libro")