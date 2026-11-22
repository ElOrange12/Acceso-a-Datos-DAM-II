import pickle

from sqlalchemy.orm import Session

from modelos import Cliente, engine


with Session(engine) as session:
    clientes = session.query(Cliente).all()
    datos = [
        {"nombre": cliente.nombre, "ciudad": cliente.ciudad}
        for cliente in clientes
    ]

with open("copia.bin", "wb") as archivo:
    pickle.dump(datos, archivo)

print("Copia guardada con", len(datos), "clientes")
