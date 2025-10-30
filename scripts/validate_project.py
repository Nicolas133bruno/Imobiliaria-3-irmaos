#!/usr/bin/env python3
"""
Script de validacao completa do projeto Imobiliaria 3 Irmaos
"""

import sys
import subprocess
import importlib
import os
from pathlib import Path

def test_imports():
    """Testa importacoes essenciais"""
    print("Testando importacoes...")
    
    modules = [
        'fastapi', 'uvicorn', 'sqlalchemy', 'pandas', 
        'numpy', 'matplotlib', 'seaborn', 'plotly', 
        'requests', 'mysql.connector', 'dotenv'
    ]
    
    failed = []
    for module in modules:
        try:
            importlib.import_module(module)
            print(f"  OK: {module}")
        except ImportError:
            print(f"  ERRO: {module}")
            failed.append(module)
    
    return len(failed) == 0

def test_files():
    """Testa se arquivos essenciais existem"""
    print("\nTestando arquivos...")
    
    essential_files = [
        'main.py', 'database.py', 'models.py', 'schemas.py',
        'imobiliaria_analysis.ipynb', 'relatorios_imobiliaria.ipynb',
        'requirements.txt', 'requirements_jupyter.txt', 'config.env'
    ]
    
    missing = []
    for file in essential_files:
        if Path(file).exists():
            print(f"  OK: {file}")
        else:
            print(f"  ERRO: {file}")
            missing.append(file)
    
    return len(missing) == 0

def test_api_import():
    """Testa se a API pode ser importada"""
    print("\nTestando importacao da API...")
    
    try:
        from main import app
        print("  OK: API importada com sucesso")
        return True
    except Exception as e:
        print(f"  ERRO: {e}")
        return False

def test_database_config():
    """Testa configuracao do banco"""
    print("\nTestando configuracao do banco...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv("config.env")
        
        config = {
            'host': os.getenv("DB_HOST"),
            'port': os.getenv("DB_PORT"), 
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'database': os.getenv("DB_NAME")
        }
        
        for key, value in config.items():
            if value:
                print(f"  OK: {key}")
            else:
                print(f"  AVISO: {key} nao configurado")
        
        return True
    except Exception as e:
        print(f"  ERRO: {e}")
        return False

def main():
    """Funcao principal de validacao"""
    print("VALIDACAO COMPLETA DO PROJETO")
    print("=" * 50)
    
    tests = [
        ("Importacoes", test_imports),
        ("Arquivos", test_files),
        ("API", test_api_import),
        ("Banco", test_database_config)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"ERRO no teste {name}: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("RESULTADO DA VALIDACAO")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "PASSOU" if result else "FALHOU"
        print(f"{name}: {status}")
    
    print(f"\nTotal: {passed}/{total} testes passaram")
    
    if passed == total:
        print("\nSUCESSO: Projeto validado com sucesso!")
        print("\nProximos passos:")
        print("1. Execute: python start_api.py")
        print("2. Execute: jupyter lab")
        print("3. Acesse: http://localhost:8000/docs")
        return True
    else:
        print("\nERRO: Alguns testes falharam")
        print("Corrija os problemas antes de continuar")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
