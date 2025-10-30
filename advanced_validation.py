#!/usr/bin/env python3
"""
Script de validação avançada para identificar problemas específicos na API
"""

import sys
import traceback
from typing import List, Dict, Any

def validate_pydantic_models():
    """Valida se os modelos Pydantic estão corretos"""
    print("🔍 Validando modelos Pydantic...")
    
    try:
        from schemas import (
            Perfil, PerfilCreate, Usuario, UsuarioCreate,
            Corretor, CorretorCreate, StatusImovel, StatusImovelCreate,
            Endereco, EnderecoCreate, Imovel, ImovelCreate,
            Visita, VisitaCreate, ContratoAluguel, ContratoAluguelCreate,
            ContratoVenda, ContratoVendaCreate
        )
        
        # Teste de criação de objetos
        test_data = {
            'PerfilCreate': {'tipo_perf': 'Teste'},
            'UsuarioCreate': {
                'nome': 'Teste', 'cpf': '123.456.789-00', 'telefone': '123456789',
                'email': 'teste@teste.com', 'data_nascimento': '1990-01-01',
                'sexo': 'M', 'login_usu': 'teste', 'senha_usu': 'senha123',
                'fk_Perfil_id': 1
            },
            'CorretorCreate': {'creci': 'MG-12345', 'fk_usuario_id': 1},
            'StatusImovelCreate': {'descricao_status': 'Teste'},
            'EnderecoCreate': {
                'logradouro': 'Rua Teste', 'numero': '123', 'bairro': 'Centro',
                'cidade': 'Teste', 'estado': 'MG', 'cep': '12345-678'
            },
            'ImovelCreate': {
                'area_total': 100.0, 'quarto': 3, 'banheiro': 2, 'vaga_garagem': 1,
                'valor': 300000.0, 'tipo': 'Casa', 'desc_tipo_imovel': 'Casa teste',
                'fk_id_status': 1, 'fk_id_endereco': 1, 'fk_id_corretor': 1
            },
            'VisitaCreate': {
                'data_visita': '2024-01-01', 'hora_visita': '14:00:00',
                'status_visita': 'Agendada', 'fk_id_usuario': 1,
                'fk_id_corretor': 1, 'fk_id_imovel': 1
            },
            'ContratoAluguelCreate': {
                'tipo': 'Residencial', 'data_inicio': '2024-01-01',
                'data_fim': '2024-12-31', 'valor_mensalidade': 1500.0,
                'fk_id_usuario': 1, 'fk_id_imovel': 1
            },
            'ContratoVendaCreate': {
                'tipo_venda': 'À vista', 'data_inicio': '2024-01-01',
                'data_fim': '2024-01-01', 'valor_negociado': 300000.0,
                'fk_id_usuario': 1, 'fk_id_imovel': 1
            }
        }
        
        schema_classes = {
            'PerfilCreate': PerfilCreate,
            'UsuarioCreate': UsuarioCreate,
            'CorretorCreate': CorretorCreate,
            'StatusImovelCreate': StatusImovelCreate,
            'EnderecoCreate': EnderecoCreate,
            'ImovelCreate': ImovelCreate,
            'VisitaCreate': VisitaCreate,
            'ContratoAluguelCreate': ContratoAluguelCreate,
            'ContratoVendaCreate': ContratoVendaCreate
        }
        
        for schema_name, data in test_data.items():
            try:
                schema_class = schema_classes[schema_name]
                obj = schema_class(**data)
                print(f"  ✅ {schema_name}: OK")
            except Exception as e:
                print(f"  ❌ {schema_name}: ERRO - {e}")
                return False
        
        return True
        
    except ImportError as e:
        print(f"  ❌ Erro de importação: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Erro inesperado: {e}")
        traceback.print_exc()
        return False

def validate_sqlalchemy_models():
    """Valida se os modelos SQLAlchemy estão corretos"""
    print("🔍 Validando modelos SQLAlchemy...")
    
    try:
        from models import (
            Perfil, Usuario, Corretor, StatusImovel, Endereco,
            Imovel, Visita, ContratoAluguel, ContratoVenda
        )
        
        # Verificar se as tabelas estão definidas
        models = [Perfil, Usuario, Corretor, StatusImovel, Endereco, 
                 Imovel, Visita, ContratoAluguel, ContratoVenda]
        
        for model in models:
            if not hasattr(model, '__tablename__'):
                print(f"  ❌ {model.__name__}: Sem __tablename__")
                return False
            print(f"  ✅ {model.__name__}: {model.__tablename__}")
        
        return True
        
    except ImportError as e:
        print(f"  ❌ Erro de importação: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Erro inesperado: {e}")
        traceback.print_exc()
        return False

def validate_database_connection():
    """Valida a conexão com o banco de dados"""
    print("🔍 Validando conexão com banco de dados...")
    
    try:
        from database import get_db, engine
        
        # Teste de conexão
        with engine.connect() as conn:
            from sqlalchemy import text
            result = conn.execute(text("SELECT 1")).fetchone()
            if result:
                print("  ✅ Conexão com banco: OK")
                return True
            else:
                print("  ❌ Conexão com banco: FALHOU")
                return False
                
    except Exception as e:
        print(f"  ❌ Erro de conexão: {e}")
        return False

def validate_api_routes():
    """Valida se as rotas da API estão configuradas corretamente"""
    print("🔍 Validando rotas da API...")
    
    try:
        from main import app
        
        # Verificar se os routers estão incluídos
        routes = [route.path for route in app.routes]
        expected_routes = [
            "/usuarios", "/perfis", "/corretores", "/enderecos",
            "/imoveis", "/visitas", "/contratos_aluguel", 
            "/contratos_venda", "/status_imovel", "/relatorios"
        ]
        
        for expected_route in expected_routes:
            if any(expected_route in route for route in routes):
                print(f"  ✅ Rota {expected_route}: OK")
            else:
                print(f"  ❌ Rota {expected_route}: NÃO ENCONTRADA")
                return False
        
        return True
        
    except Exception as e:
        print(f"  ❌ Erro na validação de rotas: {e}")
        traceback.print_exc()
        return False

def validate_requirements():
    """Valida se as dependências estão corretas"""
    print("🔍 Validando dependências...")
    
    required_packages = [
        'fastapi', 'pydantic', 'sqlalchemy', 'uvicorn',
        'dotenv', 'requests', 'httpx'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✅ {package}: OK")
        except ImportError:
            print(f"  ❌ {package}: NÃO INSTALADO")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n  📦 Pacotes faltando: {', '.join(missing_packages)}")
        print("  💡 Execute: pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Função principal de validação avançada"""
    print("🚀 VALIDAÇÃO AVANÇADA DO PROJETO")
    print("=" * 50)
    
    tests = [
        ("Dependências", validate_requirements),
        ("Modelos Pydantic", validate_pydantic_models),
        ("Modelos SQLAlchemy", validate_sqlalchemy_models),
        ("Conexão BD", validate_database_connection),
        ("Rotas API", validate_api_routes)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
            print()
        except Exception as e:
            print(f"  ❌ ERRO no teste {name}: {e}")
            results.append((name, False))
            print()
    
    print("=" * 50)
    print("RESULTADO DA VALIDAÇÃO AVANÇADA")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{name}: {status}")
    
    print(f"\nTotal: {passed}/{total} testes passaram")
    
    if passed == total:
        print("\n🎉 SUCESSO: Projeto validado completamente!")
        print("\n📋 Próximos passos:")
        print("1. Execute: python start_api.py")
        print("2. Acesse: http://localhost:8000/docs")
        print("3. Teste os endpoints da API")
        return True
    else:
        print("\n⚠️  ATENÇÃO: Alguns testes falharam")
        print("Corrija os problemas antes de continuar")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
