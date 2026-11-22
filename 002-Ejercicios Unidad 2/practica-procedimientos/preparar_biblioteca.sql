-- Ejecutar en MySQL Workbench como administrador.
-- Reinicia la base de datos y el usuario de aplicación para esta práctica.
DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    ejemplares INT
);

INSERT INTO libros (titulo, autor, ejemplares) VALUES
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 3),
    ('Novelas ejemplares', 'Miguel de Cervantes', 1),
    ('La casa de Bernarda Alba', 'Federico García Lorca', 2),
    ('Romancero gitano', 'Federico García Lorca', 0);

DROP USER IF EXISTS 'app_biblioteca'@'localhost';
CREATE USER 'app_biblioteca'@'localhost' IDENTIFIED BY 'Biblio_2026';

DELIMITER //

CREATE PROCEDURE listar_libros()
BEGIN
    SELECT id, titulo, autor, ejemplares
    FROM libros
    ORDER BY id;
END //

CREATE PROCEDURE buscar_por_autor(IN p_autor VARCHAR(100))
BEGIN
    SELECT titulo, ejemplares
    FROM libros
    WHERE autor = p_autor
    ORDER BY id;
END //

CREATE PROCEDURE contar_libros(OUT p_total INT)
BEGIN
    SELECT COUNT(*) INTO p_total FROM libros;
END //

CREATE PROCEDURE prestar_libro(IN p_id INT)
BEGIN
    DECLARE v_ejemplares INT DEFAULT NULL;

    SELECT ejemplares INTO v_ejemplares
    FROM libros
    WHERE id = p_id;

    IF v_ejemplares IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Libro no encontrado';
    END IF;

    IF v_ejemplares = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No quedan ejemplares';
    END IF;

    UPDATE libros
    SET ejemplares = ejemplares - 1
    WHERE id = p_id;
END //

DELIMITER ;

-- El usuario puede ejecutar procedimientos, pero no consultar la tabla.
GRANT EXECUTE ON biblioteca.* TO 'app_biblioteca'@'localhost';

-- Deja el ejemplar del Quijote como en el resultado inicial esperado.
UPDATE biblioteca.libros SET ejemplares = 3 WHERE id = 1;
