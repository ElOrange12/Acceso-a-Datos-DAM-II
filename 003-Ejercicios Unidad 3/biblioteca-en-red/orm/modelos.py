from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Socio(Base):
    __tablename__ = "socios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    libros: Mapped[List["Libro"]] = relationship(back_populates="socio")


class Libro(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150))
    autor: Mapped[str] = mapped_column(String(100))
    anio: Mapped[int]
    socio_id: Mapped[Optional[int]] = mapped_column(ForeignKey("socios.id"))
    socio: Mapped[Optional["Socio"]] = relationship(back_populates="libros")
