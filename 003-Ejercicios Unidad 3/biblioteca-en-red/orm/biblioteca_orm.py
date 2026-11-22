import os

from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from modelos import Base, Libro, Socio


IP_VM = os.getenv("IP_VM", "192.168.1.50")
DATABASE_URL = (
    f"mysql+pymysql://alumno:alumno123@{IP_VM}:3306/biblioteca"
)
engine = create_engine(DATABASE_URL)

# Reinicia las tablas para que el ejemplo pueda ejecutarse repetidamente.
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print(f"Tablas creadas en MySQL ({IP_VM})")

with Session(engine) as session:
    ana = Socio(nombre="Ana Pons")
    luis = Socio(nombre="Luis Mir")
    session.add_all(
        [
            ana,
            luis,
            Libro(titulo="El Quijote", autor="Cervantes", anio=1605),
            Libro(titulo="La Regenta", autor="Clarín", anio=1884),
            Libro(titulo="Nada", autor="Carmen Laforet", anio=1945),
        ]
    )
    session.commit()
    print("Socios y libros guardados")

    quijote = session.scalars(
        select(Libro).where(Libro.titulo == "El Quijote")
    ).one()
    quijote.socio = ana
    session.commit()
    print("Préstamo registrado: El Quijote -> Ana Pons")

    print("Libros de la biblioteca:")
    for libro in session.scalars(select(Libro).order_by(Libro.anio)):
        estado = f"prestado a {libro.socio.nombre}" if libro.socio else "disponible"
        print(f"- {libro.titulo} ({libro.anio}): {estado}")

    regenta = session.scalars(
        select(Libro).where(Libro.titulo == "La Regenta")
    ).one()
    regenta.autor = "Leopoldo Alas (Clarín)"
    session.commit()
    print("Actualizado el autor de La Regenta")

    nada = session.scalars(select(Libro).where(Libro.titulo == "Nada")).one()
    session.delete(nada)
    session.commit()
    total = session.scalar(select(func.count()).select_from(Libro))
    print(f"Borrado el libro Nada. Quedan {total} libros en la tabla")
