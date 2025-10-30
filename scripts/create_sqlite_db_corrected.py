import os
import sqlite3

# Remover arquivo corrompido se existir
if os.path.exists('imobiliaria.db'):
    try:
        os.remove('imobiliaria.db')
        print("Arquivo corrompido removido")
    except:
        print("Não foi possível remover o arquivo, continuando...")

# Criar novo banco de dados SQLite
conn = sqlite3.connect('imobiliaria.db')
print("Novo banco de dados SQLite criado com sucesso!")

# Script SQL adaptado para corresponder aos modelos
sql_script = """
-- Tabela Perfil (corrigida para corresponder ao modelo)
CREATE TABLE IF NOT EXISTS Perfil (
    id_Perf INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_perf VARCHAR(50) NOT NULL
);

-- Tabela Usuario
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_nascimento DATE,
    sexo VARCHAR(1),
    login_usu VARCHAR(50) UNIQUE NOT NULL,
    senha_usu VARCHAR(100) NOT NULL,
    fk_Perfil_id INTEGER,
    FOREIGN KEY (fk_Perfil_id) REFERENCES Perfil(id_Perf)
);

-- Tabela Corretor
CREATE TABLE IF NOT EXISTS Corretor (
    id_corretor INTEGER PRIMARY KEY AUTOINCREMENT,
    creci VARCHAR(20) UNIQUE NOT NULL,
    fk_usuario_id INTEGER,
    FOREIGN KEY (fk_usuario_id) REFERENCES Usuario(id_usuario)
);

-- Tabela Status_Imovel
CREATE TABLE IF NOT EXISTS Status_Imovel (
    id_status INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao_status VARCHAR(100) NOT NULL UNIQUE
);

-- Tabela Endereco
CREATE TABLE IF NOT EXISTS Endereco (
    id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
    logradouro VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    complemento VARCHAR(50),
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(10) NOT NULL
);

-- Tabela Imovel
CREATE TABLE IF NOT EXISTS Imovel (
    id_imovel INTEGER PRIMARY KEY AUTOINCREMENT,
    area_total DECIMAL(10,2) NOT NULL,
    quarto INTEGER,
    banheiro INTEGER,
    vaga_garagem INTEGER,
    valor DECIMAL(12,2) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    desc_tipo_imovel VARCHAR(100),
    fk_id_status INTEGER,
    fk_id_endereco INTEGER,
    fk_id_corretor INTEGER,
    FOREIGN KEY (fk_id_status) REFERENCES Status_Imovel(id_status),
    FOREIGN KEY (fk_id_endereco) REFERENCES Endereco(id_endereco),
    FOREIGN KEY (fk_id_corretor) REFERENCES Corretor(id_corretor)
);

-- Tabela Visita
CREATE TABLE IF NOT EXISTS Visita (
    id_visita INTEGER PRIMARY KEY AUTOINCREMENT,
    data_visita DATE NOT NULL,
    hora_visita TIME NOT NULL,
    status_visita VARCHAR(50) NOT NULL,
    fk_id_usuario INTEGER,
    fk_id_corretor INTEGER,
    fk_id_imovel INTEGER,
    FOREIGN KEY (fk_id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (fk_id_corretor) REFERENCES Corretor(id_corretor),
    FOREIGN KEY (fk_id_imovel) REFERENCES Imovel(id_imovel)
);

-- Tabela Contrato_Aluguel
CREATE TABLE IF NOT EXISTS Contrato_Aluguel (
    id_contrato_alug INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo VARCHAR(50) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_mensalidade DECIMAL(12,2) NOT NULL,
    fk_id_usuario INTEGER,
    fk_id_imovel INTEGER,
    FOREIGN KEY (fk_id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (fk_id_imovel) REFERENCES Imovel(id_imovel)
);

-- Tabela Contrato_Venda
CREATE TABLE IF NOT EXISTS Contrato_Venda (
    id_contrato_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_venda VARCHAR(50) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_negociado DECIMAL(12,2) NOT NULL,
    fk_id_usuario INTEGER,
    fk_id_imovel INTEGER,
    FOREIGN KEY (fk_id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (fk_id_imovel) REFERENCES Imovel(id_imovel)
);

-- Inserir dados iniciais
INSERT INTO Perfil (tipo_perf) VALUES 
('Administrador'),
('Corretor'),
('Cliente');

INSERT INTO Status_Imovel (descricao_status) VALUES 
('Disponível'),
('Vendido'),
('Alugado'),
('Indisponível');

INSERT INTO Usuario (nome, cpf, telefone, email, data_nascimento, sexo, login_usu, senha_usu, fk_Perfil_id) VALUES 
('Admin', '123.456.789-00', '(11) 9999-9999', 'admin@imobiliaria.com', '1990-01-01', 'M', 'admin', '$2b$12$r3zq7X8V2s5w6y7z8c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y', 1);

INSERT INTO Corretor (creci, fk_usuario_id) VALUES 
('12345', 1);
"""

# Executar o script SQL
cursor = conn.cursor()
try:
    cursor.executescript(sql_script)
    conn.commit()
    print("Estrutura do banco de dados criada com sucesso!")
    
    # Verificar tabelas criadas
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print("Tabelas criadas:", [table[0] for table in tables])
    
    # Verificar dados inseridos
    usuarios = cursor.execute("SELECT COUNT(*) FROM Usuario").fetchone()[0]
    perfis = cursor.execute("SELECT COUNT(*) FROM Perfil").fetchone()[0]
    corretores = cursor.execute("SELECT COUNT(*) FROM Corretor").fetchone()[0]
    
    print(f"Usuários inseridos: {usuarios}")
    print(f"Perfis inseridos: {perfis}")
    print(f"Corretores inseridos: {corretores}")
    
except Exception as e:
    print(f"Erro ao executar script SQL: {e}")

conn.close()