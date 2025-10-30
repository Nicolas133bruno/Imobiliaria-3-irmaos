#!/usr/bin/env python3
"""
Script de teste simplificado para validar a configuração do projeto
"""

import sys
import importlib
from pathlib import Path

def test_python_version():
    """Testa versão do Python"""
    print("Testando versao do Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"ERRO: Python {version.major}.{version.minor} nao e suportado. Use Python 3.8+")
        return False
    print(f"OK: Python {version.major}.{version.minor}.{version.micro}")
    return True

def test_imports():
    """Testa importações das bibliotecas"""
    print("\nTestando importacoes...")
    
    required_modules = [
        'fastapi',
        'uvicorn',
        'sqlalchemy',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'plotly',
        'requests',
        'mysql.connector',
        'dotenv'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"   OK: {module}")
        except ImportError as e:
            print(f"   ERRO: {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\nAVISO: Modulos nao encontrados: {', '.join(failed_imports)}")
        print("Execute: pip install -r requirements_jupyter.txt")
        return False
    
    print("OK: Todas as importacoes")
    return True

def test_files():
    """Testa se os arquivos necessários existem"""
    print("\nTestando arquivos do projeto...")
    
    required_files = [
        'main.py',
        'database.py',
        'models.py',
        'schemas.py',
        'imobiliaria_analysis.ipynb',
        'relatorios_imobiliaria.ipynb',
        'requirements.txt',
        'requirements_jupyter.txt',
        'config.env',
        'setup_jupyter.py',
        'init_project.py'
    ]
    
    missing_files = []
    
    for file in required_files:
        if Path(file).exists():
            print(f"   OK: {file}")
        else:
            print(f"   ERRO: {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\nAVISO: Arquivos nao encontrados: {', '.join(missing_files)}")
        return False
    
    print("OK: Todos os arquivos")
    return True

def test_database_config():
    """Testa configuração do banco"""
    print("\nTestando configuracao do banco...")
    
    try:
        from dotenv import load_dotenv
        import os
        
        load_dotenv("config.env")
        
        db_config = {
            'host': os.getenv("DB_HOST"),
            'port': os.getenv("DB_PORT"),
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'database': os.getenv("DB_NAME")
        }
        
        for key, value in db_config.items():
            if value:
                print(f"   OK: {key}: {value}")
            else:
                print(f"   AVISO: {key}: nao configurado")
        
        return True
        
    except Exception as e:
        print(f"   ERRO: {e}")
        return False

def test_api_import():
    """Testa se a API pode ser importada"""
    print("\nTestando importacao da API...")
    
    try:
        from main import app
        print("   OK: API FastAPI importada com sucesso")
        return True
    except Exception as e:
        print(f"   ERRO: {e}")
        return False

def main():
    """Função principal de teste"""
    print("TESTE DE CONFIGURACAO - IMOBILIARIA 3 IRMAOS")
    print("=" * 60)
    
    tests = [
        test_python_version,
        test_imports,
        test_files,
        test_database_config,
        test_api_import
    ]
    
    results = []
    
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"ERRO no teste: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("RESULTADO DOS TESTES")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print("SUCESSO: TODOS OS TESTES PASSARAM!")
        print("O projeto esta configurado corretamente")
        print("\nProximos passos:")
        print("1. Configure o MySQL com as credenciais do config.env")
        print("2. Execute: python init_project.py")
        print("3. Inicie os servicos: start_all.bat (Windows) ou ./start_all.sh (Linux/Mac)")
    else:
        print(f"AVISO: {passed}/{total} testes passaram")
        print("Alguns problemas foram encontrados")
        print("\nSolucoes:")
        print("1. Instale as dependencias: pip install -r requirements_jupyter.txt")
        print("2. Verifique se todos os arquivos estao presentes")
        print("3. Configure o arquivo config.env")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
