import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="taquilla",
)
conexion.autocommit = True
cursor = conexion.cursor()


def ver_estado():
    cursor.execute("SELECT * FROM clientes ORDER BY id")
    print("CLIENTES:", cursor.fetchall())
    cursor.execute("SELECT * FROM entradas ORDER BY id")
    print("ENTRADAS:", cursor.fetchall())
    print()


def comprar(cliente_id, evento, precio):
    try:
        conexion.start_transaction()

        cursor.execute(
            "UPDATE clientes SET saldo = saldo - %s WHERE id = %s",
            (precio, cliente_id),
        )

        cursor.execute("SELECT saldo FROM clientes WHERE id = %s", (cliente_id,))
        fila = cursor.fetchone()
        if fila is None:
            raise ValueError("cliente inexistente")
        saldo = fila[0]
        if saldo < 0:
            raise ValueError("saldo insuficiente")

        cursor.execute(
            "INSERT INTO entradas (cliente_id, evento) VALUES (%s, %s)",
            (cliente_id, evento),
        )

        conexion.commit()
        print("Compra realizada")

    except Exception as error:
        conexion.rollback()
        print("Compra cancelada:", error)


try:
    print("Estado inicial:")
    ver_estado()

    # Demostración del fallo sin transacción: la primera orden se confirma
    # automáticamente y la segunda usa a propósito el nombre de tabla erróneo.
    try:
        cursor.execute("UPDATE clientes SET saldo = saldo - 20 WHERE id = 1")
        cursor.execute(
            "INSERT INTO entrada (cliente_id, evento) VALUES (1, 'Concierto')"
        )
    except mysql.connector.Error as error:
        print("Error:", error)
    print("Después del intento sin transacción:")
    ver_estado()

    # Devolvemos el importe para iniciar la prueba de transacciones desde 50 €.
    cursor.execute("UPDATE clientes SET saldo = saldo + 20 WHERE id = 1")

    comprar(1, "Concierto", 20)
    ver_estado()

    comprar(2, "Festival", 40)
    ver_estado()
finally:
    cursor.close()
    conexion.close()
