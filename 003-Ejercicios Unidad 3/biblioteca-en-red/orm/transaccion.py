import os

from sqlalchemy import create_engine, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from modelos import Libro


IP_VM = os.getenv("IP_VM", "192.168.1.50")
engine = create_engine(
    f"mysql+pymysql://alumno:alumno123@{IP_VM}:3306/biblioteca"
)


def contar(session: Session) -> int:
    return session.scalar(select(func.count()).select_from(Libro)) or 0


with Session(engine) as session:
    print("Libros antes de la transacción:", contar(session))
    try:
        session.add(Libro(titulo="Fortunata y Jacinta", autor="Galdós", anio=1887))
        # titulo es obligatorio; este registro provoca IntegrityError.
        session.add(Libro(titulo=None, autor="Anónimo", anio=1554))  # type: ignore[arg-type]
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Error: un libro no tiene título.")
        print("Se deshace toda la transacción (rollback).")
    print("Libros después de la transacción:", contar(session))
