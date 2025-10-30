import sqlite3
from sqlalchemy import create_engine, text
from src.database.database import engine

print("Iniciando importação de dados para o banco SQLite...")

# Conectar ao banco de dados SQLite
conn = engine.connect()

# Limpar tabelas existentes para evitar conflitos
try:
    conn.execute(text("DELETE FROM Visita"))
    conn.execute(text("DELETE FROM Contrato_Aluguel"))
    conn.execute(text("DELETE FROM Contrato_Venda"))
    conn.execute(text("DELETE FROM Imovel"))
    conn.execute(text("DELETE FROM Endereco"))
    conn.execute(text("DELETE FROM Corretor"))
    conn.execute(text("DELETE FROM Usuario"))
    conn.execute(text("DELETE FROM Status_Imovel"))
    conn.execute(text("DELETE FROM Perfil"))
    print("Tabelas limpas com sucesso!")
except Exception as e:
    print(f"Aviso ao limpar tabelas: {e}")

# Inserir dados nas tabelas
try:
    # Inserir perfis
    conn.execute(text("""
    INSERT OR IGNORE INTO Perfil (id_Perf, tipo_perf) VALUES
    (1, 'Administrador'),
    (2, 'Corretor'),
    (3, 'Cliente');
    """))
    print("Perfis importados com sucesso!")

    # Inserir status de imóveis
    conn.execute(text("""
    INSERT OR IGNORE INTO Status_Imovel (id_status, descricao_status) VALUES
    (1, 'Disponível'),
    (2, 'Vendido'),
    (3, 'Alugado'),
    (4, 'Em manutenção'),
    (5, 'Reservado');
    """))
    print("Status de imóveis importados com sucesso!")

    # Inserir usuários
    conn.execute(text("""
    INSERT OR IGNORE INTO Usuario (id_usuario, nome, cpf, telefone, email, data_nascimento, sexo, login_usu, senha_usu, fk_Perfil_id) VALUES
    (1, 'Carlos Silva', '123.456.789-01', '(34) 9999-8888', 'carlos@imobiliaria.com', '1980-05-15', 'M', 'carlos.silva', 'senha123', 1),
    (2, 'Ana Paula Oliveira', '987.654.321-09', '(34) 9888-7777', 'ana@imobiliaria.com', '1985-08-20', 'F', 'ana.oliveira', 'senha456', 1),
    (3, 'Marcos Antônio', '111.222.333-44', '(34) 9777-6666', 'marcos@imobiliaria.com', '1990-03-10', 'M', 'marcos.antonio', 'senha789', 2),
    (4, 'Juliana Costa', '555.666.777-88', '(34) 9666-5555', 'juliana@imobiliaria.com', '1988-11-25', 'F', 'juliana.costa', 'senha101', 2),
    (5, 'Roberto Almeida', '999.888.777-66', '(34) 9555-4444', 'roberto@imobiliaria.com', '1982-07-30', 'M', 'roberto.almeida', 'senha202', 2),
    (6, 'Fernando Gomes', '222.333.444-55', '(34) 9444-3333', 'fernando@gmail.com', '1995-02-18', 'M', 'fernando.gomes', 'senha303', 3),
    (7, 'Patrícia Souza', '333.444.555-66', '(34) 9333-2222', 'patricia@gmail.com', '1992-09-12', 'F', 'patricia.souza', 'senha404', 3),
    (8, 'Ricardo Pereira', '444.555.666-77', '(34) 9222-1111', 'ricardo@gmail.com', '1987-04-05', 'M', 'ricardo.pereira', 'senha505', 3),
    (9, 'Amanda Nunes', '555.666.777-89', '(34) 9111-0000', 'amanda@gmail.com', '1993-12-22', 'F', 'amanda.nunes', 'senha606', 3),
    (10, 'Lucas Martins', '666.777.888-99', '(34) 9000-9999', 'lucas@gmail.com', '1991-06-15', 'M', 'lucas.martins', 'senha707', 3);
    """))
    print("Usuários importados com sucesso!")
    
    # Inserir corretores
    conn.execute(text("""
    INSERT OR IGNORE INTO Corretor (id_corretor, creci, fk_usuario_id) VALUES
    (1, 'CRECI-123456', 3),
    (2, 'CRECI-789012', 4),
    (3, 'CRECI-345678', 5);
    """))
    print("Corretores importados com sucesso!")
    
    # Inserir endereços
    conn.execute(text("""
    INSERT OR IGNORE INTO Endereco (id_endereco, logradouro, numero, complemento, bairro, cidade, estado, cep) VALUES
    (1, 'Rua das Flores', '123', 'Apto 101', 'Centro', 'Uberlândia', 'MG', '38400-000'),
    (2, 'Avenida João Naves', '1000', 'Casa', 'Santa Mônica', 'Uberlândia', 'MG', '38408-100'),
    (3, 'Rua Quinze de Novembro', '500', 'Sala 3', 'Centro', 'Uberlândia', 'MG', '38400-200'),
    (4, 'Avenida Rondon Pacheco', '2000', 'Casa', 'Tibery', 'Uberlândia', 'MG', '38405-090'),
    (5, 'Rua Segismundo Pereira', '700', 'Apto 303', 'Santa Mônica', 'Uberlândia', 'MG', '38408-170');
    """))
    print("Endereços importados com sucesso!")
    
    # Inserir imóveis
    conn.execute(text("""
    INSERT OR IGNORE INTO Imovel (id_imovel, area_total, quarto, banheiro, vaga_garagem, valor, tipo, desc_tipo_imovel, fk_id_status, fk_id_endereco, fk_id_corretor) VALUES
    (1, 80.5, 2, 1, 1, 250000.00, 'Apartamento', 'Lindo apartamento com vista panorâmica', 1, 1, 1),
    (2, 150.0, 3, 2, 2, 350000.00, 'Casa', 'Casa espaçosa com quintal', 1, 2, 2),
    (3, 45.0, 0, 1, 1, 180000.00, 'Comercial', 'Ótima localização para seu negócio', 1, 3, 3),
    (4, 200.0, 4, 3, 3, 450000.00, 'Casa', 'Casa com piscina e área gourmet', 1, 4, 1),
    (5, 70.0, 2, 1, 1, 220000.00, 'Apartamento', 'Apartamento novo, pronto para morar', 1, 5, 2);
    """))
    print("Imóveis importados com sucesso!")
    
    conn.commit()
    print("Todos os dados foram importados com sucesso!")
    
except Exception as e:
    conn.rollback()
    print(f"Erro ao importar dados: {e}")
finally:
    conn.close()