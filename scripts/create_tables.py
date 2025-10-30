#!/usr/bin/env python3
"""
Script para criar tabelas no banco de dados SQLite usando SQLAlchemy
"""
import sys
import os

# Adicionar o diretório src ao path para importações
sys.path.insert(0, os.path.abspath('.'))

from src.database.database import Base, engine

def create_tables():
    """Cria todas as tabelas no banco de dados"""
    try:
        print("🔧 Criando tabelas no banco de dados SQLite...")
        Base.metadata.create_all(bind=engine)
        print("✅ Tabelas criadas com sucesso!")
        
        # Verificar tabelas criadas
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("📋 Tabelas criadas:")
        for table in tables:
            print(f"  - {table}")
            
    except Exception as e:
        print(f"❌ Erro ao criar tabelas: {e}")

if __name__ == "__main__":
    create_tables()