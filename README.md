# 📘 [SISDIS] FastAPI Project  

Este proyecto implementa una **API REST con FastAPI** que permite:  
1. Probar un endpoint inicial.  
2. Realizar una conversión de **pesos colombianos a dólares**.  
3. Gestionar un CRUD de **libros** (insertar, consultar, listar, actualizar y eliminar) conectado a **MySQL (Railway)**.  

---

## ⚙️ Tecnologías usadas  
- [Python 3.10+](https://www.python.org/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Uvicorn](https://www.uvicorn.org/)  
- [MySQL Connector](https://pypi.org/project/mysql-connector-python/)  
- Railway (como hosting para la BD)  

---

## 📂 Estructura del proyecto  
```bash
.
├── main.py   # Código principal de la API
├── BD.sql # Código SQL utilizado
├── requirements.txt # Librerías utilizadas
└── README.md
```

# Paso a Paso - POSTMAN
1. Creación de los métodos GET, POST, PUT y DELETE.
2. En el método POST insertamos los valores de las llaves para insertar datos en la BD.
![Insertar Libro](https://media.discordapp.net/attachments/1255608070357254274/1409276559021309952/image.png?ex=68ae1c12&is=68acca92&hm=7322240b46f1d5bc5ce18664031651d50a3c57210572fddf6f86c4ee0a8808bb&=&format=webp&quality=lossless)
