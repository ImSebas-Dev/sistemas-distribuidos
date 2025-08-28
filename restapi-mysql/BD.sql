CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio_publicacion INT NOT NULL,
    genero VARCHAR(50),
    estado ENUM('disponible', 'prestado') DEFAULT 'disponible'
);