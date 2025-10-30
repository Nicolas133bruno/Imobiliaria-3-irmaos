import os
import sqlite3
from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import sessionmaker

# Importar os modelos para criar as tabelas
from src.database.database import Base, engine
from src.models.models import Perfil, StatusImovel, Usuario

# Criar todas as tabelas definidas nos modelos
print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")

# Inserir alguns dados de exemplo
print("Inserindo dados de exemplo...")
conn = engine.connect()

# Inserir perfis
conn.execute(text("""
INSERT OR IGNORE INTO Perfil (id_Perf, tipo_perf) VALUES 
(1, 'Administrador'),
(2, 'Corretor'),
(3, 'Cliente')
"""))

# Inserir status de imóvel
conn.execute(text("""
INSERT OR IGNORE INTO Status_Imovel (id_status, descricao_status) VALUES 
(1, 'Disponível'),
(2, 'Vendido'),
(3, 'Alugado'),
(4, 'Em manutenção')
"""))

# Inserir um usuário administrador
conn.execute(text("""
INSERT OR IGNORE INTO Usuario (nome, cpf, telefone, email, data_nascimento, sexo, login_usu, senha_usu, fk_Perfil_id) VALUES 
('Administrador', '12345678900', '(11) 99999-9999', 'admin@imobiliaria.com', '1990-01-01', 'M', 'admin', 'admin123', 1)
"""))

conn.close()
print("Dados de exemplo inseridos com sucesso!")
print("Banco de dados inicializado com sucesso!")