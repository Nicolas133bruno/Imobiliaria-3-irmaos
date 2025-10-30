#!/usr/bin/env python3
"""
Script para verificar a estrutura do banco de dados imobiliaria.db
"""

import sqlite3

def check_database_structure():
    try:
        conn = sqlite3.connect('imobiliaria.db')
        cursor = conn.cursor()
        
        # Verificar tabelas
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
        tables = cursor.fetchall()
        
        print('=== ESTRUTURA DO BANCO DE DADOS ===')
        print(f'Tabelas encontradas: {len(tables)}')
        
        for table in tables:
            table_name = table[0]
            print(f'\n--- Tabela: {table_name} ---')
            
            # Verificar colunas
            cursor.execute(f'PRAGMA table_info({table_name})')
            columns = cursor.fetchall()
            
            print('Colunas:')
            for col in columns:
                print(f'  {col[1]} ({col[2]}) - PK: {col[5]}, Not Null: {col[3]}')
            
            # Verificar dados de exemplo
            cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
            count = cursor.fetchone()[0]
            print(f'Total de registros: {count}')
            
            if count > 0:
                cursor.execute(f'SELECT * FROM {table_name} LIMIT 3')
                sample_data = cursor.fetchall()
                print('Amostra de dados:')
                for i, row in enumerate(sample_data):
                    print(f'  [{i+1}] {row}')
        
        conn.close()
        print('\n=== VERIFICAÇÃO CONCLUÍDA ===')
        
    except Exception as e:
        print(f'Erro ao verificar banco de dados: {e}')

if __name__ == "__main__":
    check_database_structure()