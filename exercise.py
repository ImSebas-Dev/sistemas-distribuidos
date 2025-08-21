from dataclasses import dataclass
import os
from urllib.parse import urlparse, unquote
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import sqlite3


load_dotenv()

# Object Class
class Heroe:
    def _init_(
        self, nombre: str, codigo: str, fuerza: int, destreza: int
    ):  # atributos parametros de entrada
        self.nombre = nombre
        self.codigo = codigo
        self.fuerza = fuerza
        self.destreza = destreza

    def _str_(self):
        return f"mi es Heroe({self.nombre}, {self.codigo}, F:{self.fuerza}, D:{self.destreza})"  # concatenar


def crear_tabla():
    conexion = sqlite3.connect("db_heroes.sqlite")
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS heroes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            codigo TEXT UNIQUE NOT NULL,
            fuerza INTEGER NOT NULL,
            destreza INTEGER NOT NULL
        );
    """
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def guardar_heroe(heroe):
    """
    Función para guardar un héroe en la base de datos SQLite.
    """
    try:
        conexion = sqlite3.connect("db_heroes.sqlite")
        cursor = conexion.cursor()
        ## Insertar datos en la tabla
        cursor.execute(
            """
            INSERT INTO heroes (nombre, codigo, fuerza, destreza)
            VALUES (?, ?, ?, ?);
        """,
            (heroe.nombre, heroe.codigo, heroe.fuerza, heroe.destreza),
        )

        conexion.commit()
        print(f"Héroe '{heroe.nombre}' guardado con éxito.")

    except sqlite3.IntegrityError:
        print("Error: El código del héroe ya existe en la base de datos.")
    except Exception as e:
        print("Error al guardar el héroe:", e)
    finally:
        cursor.close()
        conexion.close()

def guardar_info(heroe):
    # Función para guardar información de un héroe en la base de datos en Railway.
    try:
        conexion = mysql.connector.connect(
            host="nozomi.proxy.rlwy.net",
            user="root",
            password="cvsUxhyaigqsIIDoJYXFJZIHXhaiNgPp",
            database="railway",
        )
        cursor = conexion.cursor()
        ## Insertar datos en la tabla
        cursor.execute(
            """
            INSERT INTO estudiosos_distribuidos (nombre, codigo, fuerza, destreza)
            VALUES (?, ?, ?, ?);
        """,
            (heroe.nombre, heroe.codigo, heroe.fuerza, heroe.destreza),

        )
    except Exception as e:
        print("Error al guardar la información:", e)
    finally:
        cursor.close()
        conexion.close()

# main code
if _name_ == "_main_":
    hero1 = Heroe("Sebastian Lopez", "1000591423", 100, 100)
    print(hero1)
    guardar_heroe(hero1)
    guardar_info(hero1)
