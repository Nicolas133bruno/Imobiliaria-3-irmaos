from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import OperationalError
import os
from dotenv import load_dotenv

# Carregar variaveis de ambiente
load_dotenv("config.env")

# Configuracoes do banco de dados
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root123")
DB_NAME = os.getenv("DB_NAME", "imobiliaria_3_irmaos")

# URL de conexao MySQL
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Forçar uso do SQLite primeiro devido a problemas de conexão MySQL
print("🔧 Usando SQLite para desenvolvimento local...")
SQLALCHEMY_DATABASE_URL = "sqlite:///./imobiliaria.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Fallback original comentado - descomente quando MySQL estiver disponível
'''
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
    # Teste de conexao
    with engine.connect() as conn:
        conn.execute("SELECT 1")
    print("OK: Conectado ao MySQL")
except OperationalError as e:
    print(f"AVISO: MySQL nao disponivel, usando SQLite: {e}")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./imobiliaria.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
'''

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
