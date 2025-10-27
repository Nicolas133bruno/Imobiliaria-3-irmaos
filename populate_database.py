#!/usr/bin/env python3

"""
Script para popular o banco de dados com dados de exemplo
baseados no schema SQL da Imobiliaria 3 Irmaos
"""

from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Perfil, Usuario, Corretor, StatusImovel, Endereco, Imovel, Visita, ContratoAluguel, ContratoVenda
from datetime import date, time

def create_tables():
    """Cria todas as tabelas no banco"""
    print("Criando tabelas...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

def populate_perfis(db: Session):
    """Popula a tabela de perfis"""
    print("Populando perfis...")
    
    perfis = [
        {"id_Perf": 1, "tipo_perf": "Administrador"},
        {"id_Perf": 2, "tipo_perf": "Corretor"},
        {"id_Perf": 3, "tipo_perf": "Cliente"}
    ]
    
    for perfil_data in perfis:
        perfil = Perfil(**perfil_data)
        db.add(perfil)
    
    db.commit()
    print("Perfis populados!")

def populate_usuarios(db: Session):
    """Popula a tabela de usuarios"""
    print("Populando usuarios...")
    
    usuarios = [
        {
            "id_usuario": 1,
            "nome": "Joao Silva",
            "cpf": "123.456.789-00",
            "telefone": "(11) 99999-1111",
            "email": "joao@email.com",
            "data_nascimento": date(1985, 5, 15),
            "sexo": "M",
            "login_usu": "joao.silva",
            "senha_usu": "senha123",
            "fk_Perfil_id": 1
        },
        {
            "id_usuario": 2,
            "nome": "Maria Santos",
            "cpf": "987.654.321-00",
            "telefone": "(11) 99999-2222",
            "email": "maria@email.com",
            "data_nascimento": date(1990, 8, 22),
            "sexo": "F",
            "login_usu": "maria.santos",
            "senha_usu": "senha456",
            "fk_Perfil_id": 2
        },
        {
            "id_usuario": 3,
            "nome": "Pedro Oliveira",
            "cpf": "456.789.123-00",
            "telefone": "(11) 99999-3333",
            "email": "pedro@email.com",
            "data_nascimento": date(1988, 12, 10),
            "sexo": "M",
            "login_usu": "pedro.oliveira",
            "senha_usu": "senha789",
            "fk_Perfil_id": 3
        }
    ]
    
    for usuario_data in usuarios:
        usuario = Usuario(**usuario_data)
        db.add(usuario)
    
    db.commit()
    print("Usuarios populados!")

def populate_corretores(db: Session):
    """Popula a tabela de corretores"""
    print("Populando corretores...")
    
    corretores = [
        {
            "id_corretor": 1,
            "creci": "12345-F",
            "fk_usuario_id": 2
        }
    ]
    
    for corretor_data in corretores:
        corretor = Corretor(**corretor_data)
        db.add(corretor)
    
    db.commit()
    print("Corretores populados!")

def populate_status_imovel(db: Session):
    """Popula a tabela de status de imovel"""
    print("Populando status de imovel...")
    
    status = [
        {"id_status": 1, "descricao_status": "Disponivel"},
        {"id_status": 2, "descricao_status": "Vendido"},
        {"id_status": 3, "descricao_status": "Alugado"},
        {"id_status": 4, "descricao_status": "Reservado"}
    ]
    
    for status_data in status:
        status_obj = StatusImovel(**status_data)
        db.add(status_obj)
    
    db.commit()
    print("Status de imovel populados!")

def populate_enderecos(db: Session):
    """Popula a tabela de enderecos"""
    print("Populando enderecos...")
    
    enderecos = [
        {
            "id_endereco": 1,
            "logradouro": "Rua das Flores",
            "numero": "123",
            "bairro": "Centro",
            "complemento": "Apto 101",
            "cidade": "Sao Paulo",
            "estado": "SP",
            "cep": "01234-567"
        },
        {
            "id_endereco": 2,
            "logradouro": "Avenida Paulista",
            "numero": "456",
            "bairro": "Bela Vista",
            "complemento": None,
            "cidade": "Sao Paulo",
            "estado": "SP",
            "cep": "01310-100"
        }
    ]
    
    for endereco_data in enderecos:
        endereco = Endereco(**endereco_data)
        db.add(endereco)
    
    db.commit()
    print("Enderecos populados!")

def populate_imoveis(db: Session):
    """Popula a tabela de imoveis"""
    print("Populando imoveis...")
    
    imoveis = [
        {
            "id_imovel": 1,
            "area_total": 120.50,
            "quarto": 3,
            "banheiro": 2,
            "vaga_garagem": 1,
            "valor": 450000.00,
            "tipo": "Apartamento",
            "desc_tipo_imovel": "Apartamento de 3 quartos no centro",
            "fk_id_status": 1,
            "fk_id_endereco": 1,
            "fk_id_corretor": 1
        },
        {
            "id_imovel": 2,
            "area_total": 200.00,
            "quarto": 4,
            "banheiro": 3,
            "vaga_garagem": 2,
            "valor": 800000.00,
            "tipo": "Casa",
            "desc_tipo_imovel": "Casa de 4 quartos na Paulista",
            "fk_id_status": 1,
            "fk_id_endereco": 2,
            "fk_id_corretor": 1
        }
    ]
    
    for imovel_data in imoveis:
        imovel = Imovel(**imovel_data)
        db.add(imovel)
    
    db.commit()
    print("Imoveis populados!")

def populate_visitas(db: Session):
    """Popula a tabela de visitas"""
    print("Populando visitas...")
    
    visitas = [
        {
            "id_visita": 1,
            "data_visita": date(2024, 1, 15),
            "hora_visita": time(14, 30),
            "status_visita": "Agendada",
            "fk_id_usuario": 3,
            "fk_id_corretor": 1,
            "fk_id_imovel": 1
        }
    ]
    
    for visita_data in visitas:
        visita = Visita(**visita_data)
        db.add(visita)
    
    db.commit()
    print("Visitas populadas!")

def populate_contratos(db: Session):
    """Popula as tabelas de contratos"""
    print("Populando contratos...")
    
    # Contrato de aluguel
    contrato_aluguel = ContratoAluguel(
        id_contrato_alug=1,
        tipo="Aluguel",
        data_inicio=date(2024, 2, 1),
        data_fim=date(2025, 1, 31),
        valor_mensalidade=2500.00,
        fk_id_usuario=3,
        fk_id_imovel=1
    )
    db.add(contrato_aluguel)
    
    # Contrato de venda
    contrato_venda = ContratoVenda(
        id_contrato_venda=1,
        tipo_venda="Venda",
        data_inicio=date(2024, 3, 1),
        data_fim=date(2024, 3, 1),
        valor_negociado=780000.00,
        fk_id_usuario=3,
        fk_id_imovel=2
    )
    db.add(contrato_venda)
    
    db.commit()
    print("Contratos populados!")

def main():
    """Funcao principal"""
    print("POPULANDO BANCO DE DADOS - IMOBILIARIA 3 IRMAOS")
    print("=" * 50)
    
    # Criar tabelas
    create_tables()
    
    # Conectar ao banco
    db = SessionLocal()
    
    try:
        # Popular tabelas
        populate_perfis(db)
        populate_usuarios(db)
        populate_corretores(db)
        populate_status_imovel(db)
        populate_enderecos(db)
        populate_imoveis(db)
        populate_visitas(db)
        populate_contratos(db)
        
        print("\n" + "=" * 50)
        print("SUCESSO: Banco de dados populado com dados de exemplo!")
        print("=" * 50)
        
    except Exception as e:
        print(f"ERRO: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()
