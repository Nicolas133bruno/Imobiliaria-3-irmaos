#!/usr/bin/env python3
"""
Script para criar o banco de dados SQLite da Imobiliária 3 Irmãos
"""
import sqlite3
import os

def create_sqlite_database():
    """Cria o banco de dados SQLite com todas as tabelas e dados"""
    try:
        # Remover arquivo de banco de dados existente se estiver corrompido
        db_path = "imobiliaria.db"
        if os.path.exists(db_path):
            os.remove(db_path)
            print("🗑️  Arquivo de banco de dados corrompido removido")
        
        # Conectar ao SQLite (cria o arquivo se não existir)
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        print("✅ Conexão com SQLite estabelecida com sucesso!")
        
        # Criar tabelas
        cursor.execute("""
        CREATE TABLE Perfil (
            id_Perf INTEGER PRIMARY KEY,
            tipo_perf TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Usuario (
            id_usuario INTEGER PRIMARY KEY,
            nome TEXT,
            cpf TEXT,
            telefone TEXT,
            email TEXT,
            data_nascimento TEXT,
            sexo TEXT,
            login_usu TEXT,
            senha_usu TEXT,
            fk_Perfil_id INTEGER,
            FOREIGN KEY (fk_Perfil_id) REFERENCES Perfil(id_Perf)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Corretor (
            id_corretor INTEGER PRIMARY KEY,
            creci TEXT,
            fk_usuario_id INTEGER,
            FOREIGN KEY (fk_usuario_id) REFERENCES Usuario(id_usuario)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Status_Imovel (
            id_status INTEGER PRIMARY KEY,
            descricao_status TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Endereco(
            id_endereco INTEGER PRIMARY KEY,
            logradouro TEXT,
            numero TEXT,
            bairro TEXT,
            complemento TEXT,
            cidade TEXT,
            estado TEXT,
            cep TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Imovel (
            id_imovel INTEGER PRIMARY KEY,
            area_total REAL,
            quarto INTEGER,
            banheiro INTEGER,
            vaga_garagem INTEGER,
            valor REAL,
            tipo TEXT,
            desc_tipo_imovel TEXT,
            fk_id_status INTEGER,
            fk_id_endereco INTEGER,
            fk_id_corretor INTEGER,
            FOREIGN KEY(fk_id_endereco) REFERENCES Endereco(id_endereco),
            FOREIGN KEY (fk_id_status) REFERENCES Status_Imovel(id_status),
            FOREIGN KEY (fk_id_corretor) REFERENCES Corretor(id_corretor)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Visita (
            id_visita INTEGER PRIMARY KEY,
            data_visita TEXT,
            hora_visita TEXT,
            status_visita TEXT,
            fk_id_usuario INTEGER,
            fk_id_corretor INTEGER,
            fk_id_imovel INTEGER,
            FOREIGN KEY (fk_id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (fk_id_corretor) REFERENCES Corretor(id_corretor),
            FOREIGN KEY (fk_id_imovel) REFERENCES Imovel(id_imovel)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Contrato_Aluguel (
            id_contrato_alug INTEGER PRIMARY KEY,
            tipo TEXT,
            data_inicio TEXT,
            data_fim TEXT,
            valor_mensalidade REAL,
            fk_id_usuario INTEGER,
            fk_id_imovel INTEGER,
            FOREIGN KEY (fk_id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (fk_id_imovel) REFERENCES Imovel(id_imovel)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Contrato_Venda (
            id_contrato_venda INTEGER PRIMARY KEY,
            tipo_venda TEXT,
            data_inicio TEXT,
            data_fim TEXT,
            valor_negociado REAL,
            fk_id_usuario INTEGER,
            fk_id_imovel INTEGER,
            FOREIGN KEY (fk_id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (fk_id_imovel) REFERENCES Imovel(id_imovel)
        )
        """)
        
        print("✅ Tabelas criadas com sucesso!")
        
        # Inserir dados
        # Perfil
        cursor.executemany("INSERT INTO Perfil (id_Perf, tipo_perf) VALUES (?, ?)", [
            (1, 'Administrador'),
            (2, 'Corretor'),
            (3, 'Cliente')
        ])
        
        # Usuario
        cursor.executemany("""
        INSERT INTO Usuario (id_usuario, nome, cpf, telefone, email, data_nascimento, sexo, login_usu, senha_usu, fk_Perfil_id) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 'Carlos Silva', '123.456.789-01', '(34) 9999-8888', 'carlos@imobiliaria.com', '1980-05-15', 'M', 'carlos.silva', 'senha123', 1),
            (2, 'Ana Paula Oliveira', '987.654.321-09', '(34) 9888-7777', 'ana@imobiliaria.com', '1985-08-20', 'F', 'ana.oliveira', 'senha456', 1),
            (3, 'Marcos Antônio', '111.222.333-44', '(34) 9777-6666', 'marcos@imobiliaria.com', '1990-03-10', 'M', 'marcos.antonio', 'senha789', 2),
            (4, 'Juliana Costa', '555.666.777-88', '(34) 9666-5555', 'juliana@imobiliaria.com', '1988-11-25', 'F', 'juliana.costa', 'senha101', 2),
            (5, 'Roberto Almeida', '999.888.777-66', '(34) 9555-4444', 'roberto@imobiliaria.com', '1982-07-30', 'M', 'roberto.almeida', 'senha202', 2),
            (6, 'Fernando Gomes', '222.333.444-55', '(34) 9444-3333', 'fernando@gmail.com', '1995-02-18', 'M', 'fernando.gomes', 'senha303', 3),
            (7, 'Patrícia Souza', '333.444.555-66', '(34) 9333-2222', 'patricia@gmail.com', '1992-09-12', 'F', 'patricia.souza', 'senha404', 3),
            (8, 'Ricardo Pereira', '444.555.666-77', '(34) 9222-1111', 'ricardo@gmail.com', '1987-04-05', 'M', 'ricardo.pereira', 'senha505', 3),
            (9, 'Amanda Nunes', '555.666.777-88', '(34) 9111-0000', 'amanda@gmail.com', '1993-12-22', 'F', 'amanda.nunes', 'senha606', 3),
            (10, 'Lucas Martins', '666.777.888-99', '(34) 9000-9999', 'lucas@gmail.com', '1991-06-15', 'M', 'lucas.martins', 'senha707', 3)
        ])
        
        # Corretor
        cursor.executemany("INSERT INTO Corretor (id_corretor, creci, fk_usuario_id) VALUES (?, ?, ?)", [
            (1, 'MG-12345', 3),
            (2, 'MG-54321', 4),
            (3, 'MG-98765', 5)
        ])
        
        # Status_Imovel
        cursor.executemany("INSERT INTO Status_Imovel (id_status, descricao_status) VALUES (?, ?)", [
            (1, 'Disponível para venda'),
            (2, 'Disponível para aluguel'),
            (3, 'Vendido'),
            (4, 'Alugado'),
            (5, 'Indisponível')
        ])
        
        # Endereco
        cursor.executemany("""
        INSERT INTO Endereco (id_endereco, logradouro, numero, bairro, complemento, cidade, estado, cep) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 'Rua Professor José Ignácio de Souza', '1450', 'Martins', 'Apto 302', 'Uberlândia', 'MG', '38400-128'),
            (2, 'Avenida João Naves de Ávila', '2500', 'Santa Mônica', 'Casa 2', 'Uberlândia', 'MG', '38408-100'),
            (3, 'Rua Tiradentes', '789', 'Centro', 'Sala 501', 'Uberlândia', 'MG', '38400-186'),
            (4, 'Rua das Acácias', '45', 'Jardim Patrícia', '', 'Uberlândia', 'MG', '38411-108'),
            (5, 'Avenida Rondon Pacheco', '3700', 'Tibery', 'Bloco B', 'Uberlândia', 'MG', '38405-000'),
            (6, 'Rua dos Ipês', '120', 'Planalto', '', 'Uberlândia', 'MG', '38410-558'),
            (7, 'Rua das Hortênsias', '85', 'Mansour', 'Fundos', 'Uberlândia', 'MG', '38400-456'),
            (8, 'Avenida Antônio Thomaz Ferreira de Rezende', '2001', 'Laranjeiras', 'Apto 1204', 'Uberlândia', 'MG', '38411-006'),
            (9, 'Rua Goiás', '500', 'Fundinho', 'Sobrado', 'Uberlândia', 'MG', '38400-012'),
            (10, 'Rua das Rosas', '33', 'Jardim Karaíba', '', 'Uberlândia', 'MG', '38412-345')
        ])
        
        # Imovel
        cursor.executemany("""
        INSERT INTO Imovel (id_imovel, area_total, quarto, banheiro, vaga_garagem, valor, tipo, desc_tipo_imovel, fk_id_status, fk_id_endereco, fk_id_corretor) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 85.50, 2, 1, 1, 250000.00, 'Apartamento', 'Apartamento padrão, 2 quartos', 1, 1, 1),
            (2, 120.00, 3, 2, 2, 450000.00, 'Apartamento', 'Apartamento luxo, 3 quartos', 1, 8, 2),
            (3, 180.00, 4, 3, 2, 650000.00, 'Casa', 'Casa padrão, 4 quartos', 1, 2, 3),
            (4, 220.00, 5, 4, 3, 850000.00, 'Casa', 'Casa luxo, 5 quartos', 1, 4, 1),
            (5, 65.00, 1, 1, 1, 1200.00, 'Apartamento', 'Kitnet para aluguel', 2, 3, 2),
            (6, 90.00, 2, 1, 1, 1800.00, 'Apartamento', 'Apartamento para aluguel', 2, 5, 3),
            (7, 150.00, 3, 2, 2, 2500.00, 'Casa', 'Casa para aluguel', 2, 6, 1),
            (8, 200.00, 4, 3, 2, 750000.00, 'Casa', 'Casa vendida', 3, 7, 2),
            (9, 75.00, 2, 1, 1, 1500.00, 'Apartamento', 'Apartamento alugado', 4, 9, 3),
            (10, 300.00, 0, 2, 5, 1200000.00, 'Comercial', 'Sala comercial', 1, 10, 1)
        ])
        
        # Visita
        cursor.executemany("""
        INSERT INTO Visita (id_visita, data_visita, hora_visita, status_visita, fk_id_usuario, fk_id_corretor, fk_id_imovel) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, '2023-05-10', '14:00:00', 'Realizada', 6, 1, 1),
            (2, '2023-05-12', '10:30:00', 'Realizada', 7, 2, 3),
            (3, '2023-05-15', '16:00:00', 'Realizada', 8, 3, 5),
            (4, '2023-05-18', '09:00:00', 'Cancelada', 9, 1, 2),
            (5, '2023-05-20', '15:30:00', 'Realizada', 10, 2, 4),
            (6, '2023-05-22', '11:00:00', 'Agendada', 6, 3, 6),
            (7, '2023-05-25', '17:00:00', 'Agendada', 7, 1, 7),
            (8, '2023-05-28', '14:30:00', 'Realizada', 8, 2, 8),
            (9, '2023-06-01', '10:00:00', 'Realizada', 9, 3, 9),
            (10, '2023-06-05', '16:30:00', 'Realizada', 10, 1, 10)
        ])
        
        # Contrato_Aluguel
        cursor.executemany("""
        INSERT INTO Contrato_Aluguel (id_contrato_alug, tipo, data_inicio, data_fim, valor_mensalidade, fk_id_usuario, fk_id_imovel) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 'Residencial', '2023-01-15', '2024-01-14', 1500.00, 6, 9),
            (2, 'Residencial', '2023-03-01', '2024-02-28', 1800.00, 7, 6),
            (3, 'Residencial', '2023-04-10', '2024-04-09', 1200.00, 8, 5)
        ])
        
        # Contrato_Venda
        cursor.executemany("""
        INSERT INTO Contrato_Venda (id_contrato_venda, tipo_venda, data_inicio, data_fim, valor_negociado, fk_id_usuario, fk_id_imovel) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 'À vista', '2023-02-20', '2023-02-20', 730000.00, 9, 8),
            (2, 'Financiado', '2023-04-05', '2023-06-05', 240000.00, 10, 1),
            (3, 'À vista', '2023-05-15', '2023-05-15', 820000.00, 6, 3)
        ])
        
        # Commit das alterações
        connection.commit()
        print("✅ Dados inseridos com sucesso!")
        
        # Verificar dados inseridos
        cursor.execute("SELECT COUNT(*) FROM Usuario")
        user_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM Imovel")
        property_count = cursor.fetchone()[0]
        
        print(f"📊 {user_count} usuários inseridos")
        print(f"🏠 {property_count} imóveis inseridos")
        print(f"💾 Banco de dados SQLite criado em: {os.path.abspath(db_path)}")
        
        cursor.close()
        connection.close()
        print("✅ Banco de dados SQLite criado e populado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao criar banco de dados SQLite: {e}")
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    create_sqlite_database()