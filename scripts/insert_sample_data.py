import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('imobiliaria.db')
cursor = conn.cursor()

print("Inserindo dados de exemplo no banco de dados...")

# Script SQL com os dados fornecidos
sql_script = """
-- Inserir perfis
INSERT INTO Perfil (id_Perf, tipo_perf) VALUES 
(1, 'Administrador'), 
(2, 'Corretor'), 
(3, 'Cliente');

-- Inserir usuários
INSERT INTO Usuario (id_usuario, nome, cpf, telefone, email, data_nascimento, sexo, login_usu, senha_usu, fk_Perfil_id) VALUES 
(1, 'Carlos Silva', '123.456.789-01', '(34) 9999-8888', 'carlos@imobiliaria.com', '1980-05-15', 'M', 'carlos.silva', 'senha123', 1), 
(2, 'Ana Paula Oliveira', '987.654.321-09', '(34) 9888-7777', 'ana@imobiliaria.com', '1985-08-20', 'F', 'ana.oliveira', 'senha456', 1), 
(3, 'Marcos Antônio', '111.222.333-44', '(34) 9777-6666', 'marcos@imobiliaria.com', '1990-03-10', 'M', 'marcos.antonio', 'senha789', 2), 
(4, 'Juliana Costa', '555.666.777-88', '(34) 9666-5555', 'juliana@imobiliaria.com', '1988-11-25', 'F', 'juliana.costa', 'senha101', 2), 
(5, 'Roberto Almeida', '999.888.777-66', '(34) 9555-4444', 'roberto@imobiliaria.com', '1982-07-30', 'M', 'roberto.almeida', 'senha202', 2), 
(6, 'Fernando Gomes', '222.333.444-55', '(34) 9444-3333', 'fernando@gmail.com', '1995-02-18', 'M', 'fernando.gomes', 'senha303', 3), 
(7, 'Patrícia Souza', '333.444.555-66', '(34) 9333-2222', 'patricia@gmail.com', '1992-09-12', 'F', 'patricia.souza', 'senha404', 3), 
(8, 'Ricardo Pereira', '444.555.666-77', '(34) 9222-1111', 'ricardo@gmail.com', '1987-04-05', 'M', 'ricardo.pereira', 'senha505', 3), 
(9, 'Amanda Nunes', '555.666.777-88', '(34) 9111-0000', 'amanda@gmail.com', '1993-12-22', 'F', 'amanda.nunes', 'senha606', 3), 
(10, 'Lucas Martins', '666.777.888-99', '(34) 9000-9999', 'lucas@gmail.com', '1991-06-15', 'M', 'lucas.martins', 'senha707', 3);

-- Inserir corretores
INSERT INTO Corretor (id_corretor, creci, fk_usuario_id) VALUES 
(1, 'MG-12345', 3), 
(2, 'MG-54321', 4), 
(3, 'MG-98765', 5);

-- Inserir status de imóveis
INSERT INTO Status_Imovel (id_status, descricao_status) VALUES 
(1, 'Disponível para venda'), 
(2, 'Disponível para aluguel'), 
(3, 'Vendido'), 
(4, 'Alugado'), 
(5, 'Indisponível');

-- Inserir endereços
INSERT INTO Endereco (id_endereco, logradouro, numero, bairro, complemento, cidade, estado, cep) VALUES 
(1, 'Rua Professor José Ignácio de Souza', '1450', 'Martins', 'Apto 302', 'Uberlândia', 'MG', '38400-128'), 
(2, 'Avenida João Naves de Ávila', '2500', 'Santa Mônica', 'Casa 2', 'Uberlândia', 'MG', '38408-100'), 
(3, 'Rua Tiradentes', '789', 'Centro', 'Sala 501', 'Uberlândia', 'MG', '38400-186'), 
(4, 'Rua das Acácias', '45', 'Jardim Patrícia', '', 'Uberlândia', 'MG', '38411-108'), 
(5, 'Avenida Rondon Pacheco', '3700', 'Tibery', 'Bloco B', 'Uberlândia', 'MG', '38405-000'), 
(6, 'Rua dos Ipês', '120', 'Planalto', '', 'Uberlândia', 'MG', '38410-558'), 
(7, 'Rua das Hortênsias', '85', 'Mansour', 'Fundos', 'Uberlândia', 'MG', '38400-456'), 
(8, 'Avenida Antônio Thomaz Ferreira de Rezende', '2001', 'Laranjeiras', 'Apto 1204', 'Uberlândia', 'MG', '38411-006'), 
(9, 'Rua Goiás', '500', 'Fundinho', 'Sobrado', 'Uberlândia', 'MG', '38400-012'), 
(10, 'Rua das Rosas', '33', 'Jardim Karaíba', '', 'Uberlândia', 'MG', '38412-345');

-- Inserir imóveis
INSERT INTO Imovel (id_imovel, area_total, quarto, banheiro, vaga_garagem, valor, tipo, desc_tipo_imovel, fk_id_status, fk_id_endereco, fk_id_corretor) VALUES 
(1, 85.50, 2, 1, 1, 250000.00, 'Apartamento', 'Apartamento padrão, 2 quartos', 1, 1, 1), 
(2, 120.00, 3, 2, 2, 450000.00, 'Apartamento', 'Apartamento luxo, 3 quartos', 1, 8, 2), 
(3, 180.00, 4, 3, 2, 650000.00, 'Casa', 'Casa padrão, 4 quartos', 1, 2, 3), 
(4, 220.00, 5, 4, 3, 850000.00, 'Casa', 'Casa luxo, 5 quartos', 1, 4, 1), 
(5, 65.00, 1, 1, 1, 1200.00, 'Apartamento', 'Kitnet para aluguel', 2, 3, 2), 
(6, 90.00, 2, 1, 1, 1800.00, 'Apartamento', 'Apartamento para aluguel', 2, 5, 3), 
(7, 150.00, 3, 2, 2, 2500.00, 'Casa', 'Casa para aluguel', 2, 6, 1), 
(8, 200.00, 4, 3, 2, 750000.00, 'Casa', 'Casa vendida', 3, 7, 2), 
(9, 75.00, 2, 1, 1, 1500.00, 'Apartamento', 'Apartamento alugado', 4, 9, 3), 
(10, 300.00, 0, 2, 5, 1200000.00, 'Comercial', 'Sala comercial', 1, 10, 1);

-- Inserir visitas
INSERT INTO Visita (id_visita, data_visita, hora_visita, status_visita, fk_id_usuario, fk_id_corretor, fk_id_imovel) VALUES 
(1, '2023-05-10', '14:00:00', 'Realizada', 6, 1, 1), 
(2, '2023-05-12', '10:30:00', 'Realizada', 7, 2, 3), 
(3, '2023-05-15', '16:00:00', 'Realizada', 8, 3, 5), 
(4, '2023-05-18', '09:00:00', 'Cancelada', 9, 1, 2), 
(5, '2023-05-20', '15:30:00', 'Realizada', 10, 2, 4), 
(6, '2023-05-22', '11:00:00', 'Agendada', 6, 3, 6), 
(7, '2023-05-25', '17:00:00', 'Agendada', 7, 1, 7), 
(8, '2023-05-28', '14:30:00', 'Realizada', 8, 2, 8), 
(9, '2023-06-01', '10:00:00', 'Realizada', 9, 3, 9), 
(10, '2023-06-05', '16:30:00', 'Realizada', 10, 1, 10);

-- Inserir contratos de aluguel
INSERT INTO Contrato_Aluguel (id_contrato_alug, tipo, data_inicio, data_fim, valor_mensalidade, fk_id_usuario, fk_id_imovel) VALUES 
(1, 'Residencial', '2023-01-15', '2024-01-14', 1500.00, 6, 9), 
(2, 'Residencial', '2023-03-01', '2024-02-28', 1800.00, 7, 6), 
(3, 'Residencial', '2023-04-10', '2024-04-09', 1200.00, 8, 5);

-- Inserir contratos de venda
INSERT INTO Contrato_Venda (id_contrato_venda, tipo_venda, data_inicio, data_fim, valor_negociado, fk_id_usuario, fk_id_imovel) VALUES 
(1, 'À vista', '2023-02-20', '2023-02-20', 730000.00, 9, 8), 
(2, 'Financiado', '2023-04-05', '2023-06-05', 240000.00, 10, 1), 
(3, 'À vista', '2023-05-15', '2023-05-15', 820000.00, 6, 3);
"""

try:
    # Executar o script SQL
    cursor.executescript(sql_script)
    conn.commit()
    print("✅ Dados inseridos com sucesso!")
    
    # Verificar contagem de registros
    tables = ['Perfil', 'Usuario', 'Corretor', 'Status_Imovel', 'Endereco', 'Imovel', 'Visita', 'Contrato_Aluguel', 'Contrato_Venda']
    for table in tables:
        count = cursor.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"📊 {table}: {count} registros")
    
except Exception as e:
    print(f"❌ Erro ao inserir dados: {e}")

conn.close()