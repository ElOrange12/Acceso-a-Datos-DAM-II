import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="app_biblioteca",
    password="Biblio_2026",
    database="biblioteca",
)
conexion.autocommit = True
cursor = conexion.cursor()

try:
    print("=== Listado de libros ===")
    cursor.callproc("listar_libros", ())
    for resultado in cursor.stored_results():
        for id_libro, titulo, autor, ejemplares in resultado.fetchall():
            print(
                f"{id_libro} - {titulo} ({autor}) - "
                f"{ejemplares} ejemplares"
            )

    print("\n=== Libros de Federico García Lorca ===")
    cursor.callproc("buscar_por_autor", ("Federico García Lorca",))
    for resultado in cursor.stored_results():
        for titulo, ejemplares in resultado.fetchall():
            print(f"{titulo} - {ejemplares} ejemplares")

    print("\n=== Total de libros ===")
    resultado = cursor.callproc("contar_libros", (0,))
    print(f"Hay {resultado[0]} libros en la biblioteca")

    print("\n=== Préstamo del libro 1 ===")
    try:
        cursor.callproc("prestar_libro", (1,))
        conexion.commit()
        print("Préstamo registrado")
    except mysql.connector.Error as error:
        conexion.rollback()
        print("Error:", error.msg)

    print("\n=== Préstamo del libro 4 ===")
    try:
        cursor.callproc("prestar_libro", (4,))
        conexion.commit()
        print("Préstamo registrado")
    except mysql.connector.Error as error:
        conexion.rollback()
        print("Error:", error.msg)

    print("\n=== Prueba de permisos ===")
    try:
        cursor.execute("SELECT * FROM libros")
        print("ERROR: el usuario pudo leer la tabla directamente")
    except mysql.connector.Error as error:
        conexion.rollback()
        print("Acceso denegado:", error.msg)
finally:
    cursor.close()
    conexion.close()
