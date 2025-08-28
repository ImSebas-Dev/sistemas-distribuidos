# 📘 [SISDIS] FastAPI Project  

Este proyecto implementa una **API REST con FastAPI** que permite:
1. Gestionar un CRUD de **portátiles** (insertar, consultar, listar, actualizar y eliminar) conectado a **MongoDB**.  

---

## ⚙️ Tecnologías usadas  
- [Python 3.10+](https://www.python.org/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Uvicorn](https://www.uvicorn.org/)  
- [Motor](https://pypi.org/project/motor/) (para interactuar con MongoDB)
- [Pymongo](https://pypi.org/project/pymongo/) (para interactuar con MongoDB)
- [Pydantic](https://pypi.org/project/pydantic/) (para validación de datos)
- [Typing](https://pypi.org/project/typing/) (para anotaciones de tipos)

---

## 📂 Estructura del proyecto  
```bash
.
├── models
  └── portatiles.py # Modelo de portátiles
├── main.py   # Código principal de la API
├── requirements.txt # Librerías utilizadas
└── README.md
```