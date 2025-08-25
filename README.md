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
![Verificar la Inserción de Datos](https://cdn.discordapp.com/attachments/1255608070357254274/1409276813271892150/image.png?ex=68ae1c4f&is=68accacf&hm=09ff419a06c83713e09b6c5ff987c441d621dc27bcc98f8131f03e684470d8fc&)

4. En el método GET para listar libros, insertamos el dominio de conexión (http://127.0.0.1:8000/libros) y clickamos en "Send".
![Listar Libro](https://media.discordapp.net/attachments/1255608070357254274/1409276704723042519/image.png?ex=68ae1c35&is=68accab5&hm=2c811e01da138818bc6a9b7ca4ac621982d9a31defcba41a4f7e8d5a85596ac2&=&format=webp&quality=lossless)

5. Para consultar el libro por ID creamos un método GET con el siguiente dominio: http://127.0.0.1:8000/libros/[id-libro], y clickamos en "Send".
![Listar Libro por ID](https://media.discordapp.net/attachments/1255608070357254274/1409278993533767680/image.png?ex=68ae1e57&is=68acccd7&hm=3258e01092680d5d366758c2d81da844ee055989f938556f47946a083f6ce498&=&format=webp&quality=lossless)

6. Para actualizar los datos del libro creamos un método UPDATE e insertamos el dominio del API con el ID del libro que queremos editar (http://127.0.0.1:8000/libros/[id-libro]) y clickamos en "Send". Para verificar los cambios podemos ir al método consultar libro por ID o directamente desde Railway.
![Actualizar Libro por ID](https://media.discordapp.net/attachments/1255608070357254274/1409279905669054615/Captura_de_pantalla_2025-08-24_155338.png?ex=68ae1f30&is=68accdb0&hm=40e70337ce0f7c11983453d89f13f5795d3579e534cb699831a299584602f204&=&format=webp&quality=lossless)
![Verificar Actualización de Datos](https://media.discordapp.net/attachments/1255608070357254274/1409279906080358500/Captura_de_pantalla_2025-08-24_155349.png?ex=68ae1f30&is=68accdb0&hm=2d4c569671f4ec9e3176383f170598e856e871b70dd089d02f9d3f07a3891dc3&=&format=webp&quality=lossless)

7. Por último, para eliminar un libro nuevamente insertamos el dominio junto con el ID del libro que deseamos eliminar () y clickamos en "Send". Para verificar los cambios podemos ir al método consultar libro por ID o directamente desde Railway.
![Eliminar Libro por ID](https://media.discordapp.net/attachments/1255608070357254274/1409279904658362398/Captura_de_pantalla_2025-08-24_155400.png?ex=68ae1f30&is=68accdb0&hm=5e4b5258a606f259255cf8208972d4efe2fc5bf16241e241fb8c478964779ae6&=&format=webp&quality=lossless)
![Verificar la Eliminación](https://media.discordapp.net/attachments/1255608070357254274/1409279905031651469/Captura_de_pantalla_2025-08-24_155408.png?ex=68ae1f30&is=68accdb0&hm=ed70a8db0fe3435815c40a9e408994d926914a71d7cf048e3654cd244b394462&=&format=webp&quality=lossless&width=1732&height=856)
