#!/usr/bin/env python3
"""
Validação completa e abrangente do projeto Imobiliária 3 Irmãos
Como um desenvolvedor sênior analisaria o projeto
"""

import sys
import os
import subprocess
import traceback
from pathlib import Path
from typing import List, Dict, Any, Tuple

class ProjectValidator:
    """Classe para validação completa do projeto"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.success_count = 0
        self.total_tests = 0
        
    def log_success(self, message: str):
        """Registra sucesso"""
        print(f"  ✅ {message}")
        self.success_count += 1
        self.total_tests += 1
        
    def log_error(self, message: str):
        """Registra erro"""
        print(f"  ❌ {message}")
        self.errors.append(message)
        self.total_tests += 1
        
    def log_warning(self, message: str):
        """Registra aviso"""
        print(f"  ⚠️  {message}")
        self.warnings.append(message)
        
    def validate_file_structure(self) -> bool:
        """Valida estrutura de arquivos"""
        print("📁 Validando estrutura de arquivos...")
        
        required_files = [
            "main.py", "models.py", "schemas.py", "database.py",
            "requirements.txt", "config.env", "start_api.py"
        ]
        
        required_dirs = [
            "routers", "templatemo_591_villa_agency", "imagens"
        ]
        
        all_good = True
        
        for file in required_files:
            if Path(file).exists():
                self.log_success(f"Arquivo {file} encontrado")
            else:
                self.log_error(f"Arquivo {file} não encontrado")
                all_good = False
                
        for dir_name in required_dirs:
            if Path(dir_name).is_dir():
                self.log_success(f"Diretório {dir_name} encontrado")
            else:
                self.log_error(f"Diretório {dir_name} não encontrado")
                all_good = False
                
        return all_good
    
    def validate_python_imports(self) -> bool:
        """Valida imports Python"""
        print("\n🐍 Validando imports Python...")
        
        try:
            # Testar imports principais
            from main import app
            self.log_success("main.py importado com sucesso")
            
            from models import Perfil, Usuario, Corretor, StatusImovel, Endereco, Imovel, Visita, ContratoAluguel, ContratoVenda
            self.log_success("models.py importado com sucesso")
            
            from schemas import PerfilCreate, UsuarioCreate, CorretorCreate
            self.log_success("schemas.py importado com sucesso")
            
            from database import get_db, engine
            self.log_success("database.py importado com sucesso")
            
            # Testar imports dos routers
            from routers.Usuario import router as usuario_router
            from routers.Perfil import router as perfil_router
            from routers.Corretor import router as corretor_router
            from routers.Endereco import router as endereco_router
            from routers.Imovel import router as imovel_router
            from routers.Visita import router as visita_router
            from routers.ContratoAluguel import router as contrato_aluguel_router
            from routers.ContratoVenda import router as contrato_venda_router
            from routers.StatusImovel import router as status_imovel_router
            from routers.relatorios import router as relatorios_router
            from routers.consulta import router as consulta_router
            self.log_success("Todos os routers importados com sucesso")
            
            return True
            
        except ImportError as e:
            self.log_error(f"Erro de importação: {e}")
            return False
        except Exception as e:
            self.log_error(f"Erro inesperado: {e}")
            return False
    
    def validate_database_connection(self) -> bool:
        """Valida conexão com banco de dados"""
        print("\n🗄️  Validando conexão com banco de dados...")
        
        try:
            from database import engine
            with engine.connect() as conn:
                from sqlalchemy import text
                result = conn.execute(text("SELECT 1")).fetchone()
                if result:
                    self.log_success("Conexão com banco de dados OK")
                    return True
                else:
                    self.log_error("Falha na consulta de teste")
                    return False
        except Exception as e:
            self.log_error(f"Erro de conexão: {e}")
            return False
    
    def validate_api_routes(self) -> bool:
        """Valida rotas da API"""
        print("\n🛣️  Validando rotas da API...")
        
        try:
            from main import app
            
            # Verificar se todas as rotas estão registradas
            routes = [route.path for route in app.routes]
            expected_routes = [
                "/usuarios", "/perfis", "/corretores", "/enderecos",
                "/imoveis", "/visitas", "/contratos_aluguel", 
                "/contratos_venda", "/status_imovel", "/relatorios",
                "/consultas"
            ]
            
            all_routes_found = True
            for expected_route in expected_routes:
                if any(expected_route in route for route in routes):
                    self.log_success(f"Rota {expected_route} encontrada")
                else:
                    self.log_error(f"Rota {expected_route} não encontrada")
                    all_routes_found = False
            
            return all_routes_found
            
        except Exception as e:
            self.log_error(f"Erro na validação de rotas: {e}")
            return False
    
    def validate_pydantic_models(self) -> bool:
        """Valida modelos Pydantic"""
        print("\n📋 Validando modelos Pydantic...")
        
        try:
            from schemas import (
                PerfilCreate, UsuarioCreate, CorretorCreate, StatusImovelCreate,
                EnderecoCreate, ImovelCreate, VisitaCreate, ContratoAluguelCreate,
                ContratoVendaCreate
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
                    self.log_success(f"{schema_name} validado")
                except Exception as e:
                    self.log_error(f"{schema_name} falhou: {e}")
                    return False
            
            return True
            
        except Exception as e:
            self.log_error(f"Erro na validação Pydantic: {e}")
            return False
    
    def validate_dependencies(self) -> bool:
        """Valida dependências"""
        print("\n📦 Validando dependências...")
        
        required_packages = [
            'fastapi', 'pydantic', 'sqlalchemy', 'uvicorn',
            'dotenv', 'requests', 'httpx', 'mysql'
        ]
        
        all_installed = True
        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
                self.log_success(f"{package} instalado")
            except ImportError:
                self.log_error(f"{package} não instalado")
                all_installed = False
        
        return all_installed
    
    def validate_web_files(self) -> bool:
        """Valida arquivos web"""
        print("\n🌐 Validando arquivos web...")
        
        web_files = [
            "templatemo_591_villa_agency/index.html",
            "templatemo_591_villa_agency/contact.html",
            "templatemo_591_villa_agency/properties.html",
            "templatemo_591_villa_agency/property-details.html"
        ]
        
        all_exist = True
        for file in web_files:
            if Path(file).exists():
                self.log_success(f"Arquivo web {file} encontrado")
            else:
                self.log_error(f"Arquivo web {file} não encontrado")
                all_exist = False
        
        return all_exist
    
    def validate_notebooks(self) -> bool:
        """Valida notebooks Jupyter"""
        print("\n📓 Validando notebooks Jupyter...")
        
        notebooks = [
            "imobiliaria_analysis.ipynb",
            "relatorios_imobiliaria.ipynb"
        ]
        
        all_exist = True
        for notebook in notebooks:
            if Path(notebook).exists():
                self.log_success(f"Notebook {notebook} encontrado")
            else:
                self.log_error(f"Notebook {notebook} não encontrado")
                all_exist = False
        
        return all_exist
    
    def validate_docker_config(self) -> bool:
        """Valida configuração Docker"""
        print("\n🐳 Validando configuração Docker...")
        
        docker_files = [
            "Dockerfile",
            "docker-compose.yml",
            "docker-compose.jupyter.yml"
        ]
        
        all_exist = True
        for file in docker_files:
            if Path(file).exists():
                self.log_success(f"Arquivo Docker {file} encontrado")
            else:
                self.log_error(f"Arquivo Docker {file} não encontrado")
                all_exist = False
        
        return all_exist
    
    def validate_scripts(self) -> bool:
        """Valida scripts de utilidade"""
        print("\n🔧 Validando scripts de utilidade...")
        
        scripts = [
            "start_api.py",
            "start_api_improved.py",
            "test_api.py",
            "test_all_endpoints.py",
            "advanced_validation.py",
            "populate_database.py",
            "install_dependencies.py",
            "init_project.py"
        ]
        
        all_exist = True
        for script in scripts:
            if Path(script).exists():
                self.log_success(f"Script {script} encontrado")
            else:
                self.log_error(f"Script {script} não encontrado")
                all_exist = False
        
        return all_exist
    
    def run_comprehensive_validation(self) -> bool:
        """Executa validação completa"""
        print("🚀 VALIDAÇÃO COMPLETA DO PROJETO IMOBILIÁRIA 3 IRMÃOS")
        print("=" * 60)
        
        validations = [
            ("Estrutura de Arquivos", self.validate_file_structure),
            ("Dependências", self.validate_dependencies),
            ("Imports Python", self.validate_python_imports),
            ("Conexão BD", self.validate_database_connection),
            ("Rotas API", self.validate_api_routes),
            ("Modelos Pydantic", self.validate_pydantic_models),
            ("Arquivos Web", self.validate_web_files),
            ("Notebooks Jupyter", self.validate_notebooks),
            ("Configuração Docker", self.validate_docker_config),
            ("Scripts de Utilidade", self.validate_scripts)
        ]
        
        results = []
        for name, validation_func in validations:
            try:
                result = validation_func()
                results.append((name, result))
            except Exception as e:
                self.log_error(f"Erro no teste {name}: {e}")
                results.append((name, False))
        
        # Resumo final
        print("\n" + "=" * 60)
        print("RESUMO DA VALIDAÇÃO COMPLETA")
        print("=" * 60)
        
        passed = sum(1 for _, result in results if result)
        total = len(results)
        
        for name, result in results:
            status = "✅ PASSOU" if result else "❌ FALHOU"
            print(f"{name}: {status}")
        
        print(f"\nTotal: {passed}/{total} validações passaram")
        
        if self.warnings:
            print(f"\n⚠️  Avisos ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if self.errors:
            print(f"\n❌ Erros ({len(self.errors)}):")
            for error in self.errors:
                print(f"  - {error}")
        
        if passed == total:
            print("\n🎉 SUCESSO: Projeto completamente validado!")
            print("\n📋 Próximos passos:")
            print("1. Execute: python start_api_improved.py")
            print("2. Acesse: http://localhost:8000/docs")
            print("3. Execute: python test_all_endpoints.py")
            return True
        else:
            print(f"\n⚠️  ATENÇÃO: {total - passed} validações falharam")
            print("Corrija os problemas antes de continuar")
            return False

def main():
    """Função principal"""
    try:
        validator = ProjectValidator()
        success = validator.run_comprehensive_validation()
        return success
    except KeyboardInterrupt:
        print("\n\n⏹️  Validação interrompida pelo usuário")
        return False
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
