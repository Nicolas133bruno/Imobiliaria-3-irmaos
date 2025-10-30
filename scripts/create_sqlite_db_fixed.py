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

# Script SQL adaptado para SQLite
sql_script = """
-- Tabela Perfil
CREATE TABLE IF NOT EXISTS Perfil (
    id_perfil INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_perfil VARCHAR(50) NOT NULL,
    descricao_perfil TEXT
);

-- Tabela Usuario
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(100) UNIQUE NOT NULL,
    data_nascimento DATE,
    sexo CHAR(1),
    login_usu VARCHAR(50) UNIQUE NOT NULL,
    senha_usu VARCHAR(255) NOT NULL,
    fk_Perfil_id INTEGER,
    FOREIGN KEY (fk_Perfil_id) REFERENCES Perfil(id_perfil)
);

-- Tabela Corretor
CREATE TABLE IF NOT EXISTS Corretor (
    id_corretor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(100) UNIQUE NOT NULL,
    data_nascimento DATE,
    sexo CHAR(1),
    creci VARCHAR(20) UNIQUE NOT NULL,
    salario DECIMAL(10,2),
    data_admissao DATE,
    fk_Usuario_id INTEGER,
    FOREIGN KEY (fk_Usuario_id) REFERENCES Usuario(id_usuario)
);

-- Tabela Status_Imovel
CREATE TABLE IF NOT EXISTS Status_Imovel (
    id_status INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_status VARCHAR(50) NOT NULL,
    descricao_status TEXT
);

-- Tabela Endereco
CREATE TABLE IF NOT EXISTS Endereco (
    id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
    logradouro VARCHAR(100) NOT NULL,
    numero VARCHAR(10),
    complemento VARCHAR(50),
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL
);

-- Tabela Imovel
CREATE TABLE IF NOT EXISTS Imovel (
    id_imovel INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_imovel VARCHAR(50) NOT NULL,
    descricao TEXT,
    area DECIMAL(10,2),
    quartos INTEGER,
    banheiros INTEGER,
    vagas_garagem INTEGER,
    valor_venda DECIMAL(15,2),
    valor_aluguel DECIMAL(15,2),
    data_cadastro DATE DEFAULT CURRENT_DATE,
    fk_Status_Imovel_id INTEGER,
    fk_Endereco_id INTEGER,
    fk_Corretor_id INTEGER,
    FOREIGN KEY (fk_Status_Imovel_id) REFERENCES Status_Imovel(id_status),
    FOREIGN KEY (fk_Endereco_id) REFERENCES Endereco(id_endereco),
    FOREIGN KEY (fk_Corretor_id) REFERENCES Corretor(id_corretor)
);

-- Tabela Visita
CREATE TABLE IF NOT EXISTS Visita (
    id_visita INTEGER PRIMARY KEY AUTOINCREMENT,
    data_visita DATE NOT NULL,
    hora_visita TIME NOT NULL,
    observacoes TEXT,
    fk_Imovel_id INTEGER,
    fk_Corretor_id INTEGER,
    fk_Usuario_id INTEGER,
    FOREIGN KEY (fk_Imovel_id) REFERENCES Imovel(id_imovel),
    FOREIGN KEY (fk_Corretor_id) REFERENCES Corretor(id_corretor),
    FOREIGN KEY (fk_Usuario_id) REFERENCES Usuario(id_usuario)
);

-- Tabela Contrato_Aluguel
CREATE TABLE IF NOT EXISTS Contrato_Aluguel (
    id_contrato_aluguel INTEGER PRIMARY KEY AUTOINCREMENT,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_mensal DECIMAL(15,2) NOT NULL,
    observacoes TEXT,
    fk_Imovel_id INTEGER,
    fk_Usuario_id INTEGER,
    fk_Corretor_id INTEGER,
    FOREIGN KEY (fk_Imovel_id) REFERENCES Imovel(id_imovel),
    FOREIGN KEY (fk_Usuario_id) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (fk_Corretor_id) REFERENCES Corretor(id_corretor)
);

-- Tabela Contrato_Venda
CREATE TABLE IF NOT EXISTS Contrato_Venda (
    id_contrato_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_contrato DATE NOT NULL,
    valor_venda DECIMAL(15,2) NOT NULL,
    observacoes TEXT,
    fk_Imovel_id INTEGER,
    fk_Usuario_id INTEGER,
    fk_Corretor_id INTEGER,
    FOREIGN KEY (fk_Imovel_id) REFERENCES Imovel(id_imovel),
    FOREIGN KEY (fk_Usuario_id) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (fk_Corretor_id) REFERENCES Corretor(id_corretor)
);

-- Inserir dados iniciais
INSERT INTO Perfil (nome_perfil, descricao_perfil) VALUES 
('Administrador', 'Acesso total ao sistema'),
('Corretor', 'Acesso às funcionalidades de corretor'),
('Cliente', 'Acesso às funcionalidades de cliente');

INSERT INTO Status_Imovel (nome_status, descricao_status) VALUES 
('Disponível', 'Imóvel disponível para venda ou aluguel'),
('Vendido', 'Imóvel vendido'),
('Alugado', 'Imóvel alugado'),
('Indisponível', 'Imóvel temporariamente indisponível');

INSERT INTO Usuario (nome, cpf, telefone, email, data_nascimento, sexo, login_usu, senha_usu, fk_Perfil_id) VALUES 
('Admin', '123.456.789-00', '(11) 9999-9999', 'admin@imobiliaria.com', '1990-01-01', 'M', 'admin', '$2b$12$r3zq7X8V2s5w6y7z8c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y', 1);

INSERT INTO Corretor (nome, cpf, telefone, email, data_nascimento, sexo, creci, salario, data_admissao, fk_Usuario_id) VALUES 
('João Silva', '111.222.333-44', '(11) 8888-8888', 'joao@imobiliaria.com', '1985-05-15', 'M', '12345', 3000.00, '2020-01-15', 1);
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