import os
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Configuração do banco de dados - Usando diretamente SQLite para garantir integração
SQLALCHEMY_DATABASE_URL = "sqlite:///./imobiliaria.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Habilitar suporte a chaves estrangeiras no SQLite
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

print("Usando SQLite para o banco de dados (imobiliaria.db)")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass

# Dependencia para o FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
