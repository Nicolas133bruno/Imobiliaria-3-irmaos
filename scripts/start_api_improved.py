#!/usr/bin/env python3
"""
Script melhorado para iniciar a API da Imobiliária 3 Irmãos
Com validações e configurações otimizadas
"""

import uvicorn
import sys
import os
import time
from pathlib import Path

def check_dependencies():
    """Verifica se todas as dependências estão instaladas"""
    print("🔍 Verificando dependências...")
    
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
        print(f"\n📦 Pacotes faltando: {', '.join(missing_packages)}")
        print("💡 Execute: pip install -r requirements_fixed.txt")
        return False
    
    return True

def check_database():
    """Verifica se o banco de dados está acessível"""
    print("🔍 Verificando banco de dados...")
    
    try:
        from database import engine
        with engine.connect() as conn:
            from sqlalchemy import text
            result = conn.execute(text("SELECT 1")).fetchone()
            if result:
                print("  ✅ Banco de dados: OK")
                return True
    except Exception as e:
        print(f"  ❌ Banco de dados: ERRO - {e}")
        return False

def check_api_imports():
    """Verifica se a API pode ser importada"""
    print("🔍 Verificando imports da API...")
    
    try:
        from main import app
        print("  ✅ API imports: OK")
        return True
    except Exception as e:
        print(f"  ❌ API imports: ERRO - {e}")
        return False

def start_api():
    """Inicia a API FastAPI com configurações otimizadas"""
    print("🚀 INICIANDO API IMOBILIARIA 3 IRMAOS")
    print("=" * 50)
    
    # Verificações pré-inicialização
    if not check_dependencies():
        print("\n❌ ERRO: Dependências faltando")
        return False
    
    if not check_database():
        print("\n❌ ERRO: Problema com banco de dados")
        return False
    
    if not check_api_imports():
        print("\n❌ ERRO: Problema com imports da API")
        return False
    
    print("\n✅ Todas as verificações passaram!")
    print("\n📋 Informações da API:")
    print("  🌐 URL: http://localhost:8000")
    print("  📚 Documentação: http://localhost:8000/docs")
    print("  🔧 ReDoc: http://localhost:8000/redoc")
    print("  ⏹️  Para parar: Ctrl+C")
    print("=" * 50)
    
    try:
        # Configurações otimizadas para desenvolvimento
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info",
            access_log=True,
            use_colors=True,
            reload_dirs=["./"],
            reload_includes=["*.py"]
        )
    except KeyboardInterrupt:
        print("\n\n⏹️  API parada pelo usuário")
        return True
    except Exception as e:
        print(f"\n❌ Erro ao iniciar API: {e}")
        return False

def main():
    """Função principal"""
    try:
        success = start_api()
        return success
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
