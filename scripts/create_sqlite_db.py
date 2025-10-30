import os
import sqlite3

# Remover arquivo corrompido se existir
if os.path.exists('imobiliaria.db'):
    try:
        os.remove('imobiliaria.db')
        print("Arquivo corrompido removido")
    except:
        print("Não foi possível remover o arquivo, continuando...")

# Criar novo banco de dados SQLite
conn = sqlite3.connect('imobiliaria.db')
print("Novo banco de dados SQLite criado com sucesso!")

# Ler e executar o SQL do arquivo original
with open('A empresa Imobilária 3irmãos.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Executar o script SQL
cursor = conn.cursor()
try:
    cursor.executescript(sql_script)
    conn.commit()
    print("Script SQL executado com sucesso!")
    
    # Verificar tabelas criadas
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print("Tabelas criadas:", tables)
    
except Exception as e:
    print(f"Erro ao executar script SQL: {e}")

conn.close()