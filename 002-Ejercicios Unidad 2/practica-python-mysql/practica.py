import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
)
cursor = conexion.cursor()

print("Conexión correcta con MySQL")

# Crear y seleccionar la base de datos.
cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")
cursor.execute("SHOW DATABASES")
for base in cursor.fetchall():
    print(base[0])
cursor.execute("USE tienda")

# Crear una tabla vacía para que las inserciones no se acumulen al repetir.
cursor.execute("DROP TABLE IF EXISTS productos")
cursor.execute(
    """CREATE TABLE productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50),
        precio DECIMAL(6, 2)
    )"""
)
cursor.execute("SHOW TABLES")
for tabla in cursor.fetchall():
    print("Tabla creada:", tabla[0])

# Insertar los cuatro productos en una única operación parametrizada.
sql = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
datos = [
    ("Teclado", 25),
    ("Raton", 12.5),
    ("Monitor", 140),
    ("Altavoces", 30),
]
cursor.executemany(sql, datos)
conexion.commit()
print(cursor.rowcount, "filas insertadas")

# Consultar toda la tabla.
print("--- Todos los productos ---")
cursor.execute("SELECT * FROM productos")
for fila in cursor.fetchall():
    print(f"{fila[0]} | {fila[1]} | {fila[2]:.2f}")

# Filtrar por precio.
print("--- Productos de menos de 30 euros ---")
sql = "SELECT nombre, precio FROM productos WHERE precio < %s"
cursor.execute(sql, (30,))
for fila in cursor.fetchall():
    print(f"{fila[0]} | {fila[1]:.2f}")

# Actualizar el precio del Monitor y borrar el Raton.
sql = "UPDATE productos SET precio = %s WHERE nombre = %s"
cursor.execute(sql, (120, "Monitor"))
print("Filas modificadas:", cursor.rowcount)

cursor.execute("DELETE FROM productos WHERE nombre = %s", ("Raton",))
print("Filas borradas:", cursor.rowcount)
conexion.commit()

# Mostrar el estado final.
print("--- Productos después de los cambios ---")
cursor.execute("SELECT * FROM productos")
for fila in cursor.fetchall():
    print(f"{fila[0]} | {fila[1]} | {fila[2]:.2f}")

cursor.close()
conexion.close()
print("Conexión cerrada")
