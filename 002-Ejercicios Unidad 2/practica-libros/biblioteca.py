from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


# PASO 1: conexión a una base SQLite guardada en el archivo biblioteca.db.
engine = create_engine("sqlite:///biblioteca.db")


# PASO 2: clase base de las entidades ORM.
class Base(DeclarativeBase):
    pass


# PASO 3: entidad Libro y columnas de la tabla libros.
class Libro(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    autor: Mapped[str]
    paginas: Mapped[Optional[int]]


# PASO 4: crea la tabla si todavía no existe.
Base.metadata.create_all(engine)


# PASOS 5 a 9: todas las operaciones se realizan en una sola sesión.
with Session(engine) as session:
    # PASO 5: insertar los tres libros. El id se genera automáticamente.
    session.add_all(
        [
            Libro(
                titulo="Don Quijote de la Mancha",
                autor="Miguel de Cervantes",
                paginas=1250,
            ),
            Libro(
                titulo="La casa de los espíritus",
                autor="Isabel Allende",
                paginas=480,
            ),
            Libro(
                titulo="Platero y yo",
                autor="Juan Ramón Jiménez",
                paginas=None,
            ),
        ]
    )
    session.commit()

    # PASO 6: buscar por clave primaria y luego libros de más de 400 páginas.
    libro = session.get(Libro, 1)
    if libro is not None:
        print(f"{libro.titulo} - {libro.autor}")

    consulta_largos = select(Libro).where(Libro.paginas > 400)
    for libro in session.scalars(consulta_largos):
        print(f"{libro.titulo} {libro.paginas}")

    # PASO 7: asignar las páginas que faltaban.
    platero = session.get(Libro, 3)
    if platero is not None:
        platero.paginas = 150
        session.commit()

    # PASO 8: eliminar La casa de los espíritus.
    casa = session.get(Libro, 2)
    if casa is not None:
        session.delete(casa)
        session.commit()

    # PASO 9: mostrar el estado final.
    for libro in session.scalars(select(Libro).order_by(Libro.id)):
        print(f"{libro.id} {libro.titulo} {libro.paginas}")
