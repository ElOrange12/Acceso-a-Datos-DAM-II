from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///tienda.db")
Base = declarative_base()


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)


Base.metadata.create_all(engine)
