import pickle

from sqlalchemy.orm import Session

from modelos import Cliente, engine


with open("copia.bin", "rb") as archivo:
    datos = pickle.load(archivo)

with Session(engine) as session:
    for dato in datos:
        session.add(Cliente(nombre=dato["nombre"], ciudad=dato["ciudad"]))
    session.commit()

print("Restaurados", len(datos), "clientes")
