import sqlite3
from sqlite3 import Error

def check_database_integrity():
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect('imobiliaria.db')
        cursor = conn.cursor()
        
        print("🔍 Verificando integridade do banco de dados...")
        
        # Verificar se todas as tabelas existem
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"📊 Tabelas encontradas: {[table[0] for table in tables]}")
        
        # Verificar estrutura da tabela Usuario (com U maiúsculo)
        try:
            cursor.execute("PRAGMA table_info(Usuario)")
            columns = cursor.fetchall()
            print(f"\n📋 Colunas da tabela 'Usuario':")
            for col in columns:
                print(f"  - {col[1]} ({col[2]})")
        except Error as e:
            print(f"❌ Erro ao verificar tabela 'Usuario': {e}")
        
        # Verificar dados na tabela Usuario
        try:
            cursor.execute("SELECT COUNT(*) FROM Usuario")
            count = cursor.fetchone()[0]
            print(f"\n👥 Total de usuários: {count}")
            
            if count > 0:
                cursor.execute("SELECT * FROM Usuario LIMIT 5")
                users = cursor.fetchall()
                print(f"\n📝 Primeiros {len(users)} usuários:")
                for user in users:
                    print(f"  - ID: {user[0]}, Nome: {user[1]}")
                    
                # Verificar dados problemáticos
                print(f"\n🔍 Verificando dados específicos:")
                cursor.execute("SELECT id, nome, cpf, email, data_nascimento FROM Usuario")
                all_users = cursor.fetchall()
                for user in all_users:
                    user_id, nome, cpf, email, data_nascimento = user
                    print(f"  - ID {user_id}: {nome}, CPF: {cpf}, Email: {email}, Nasc: {data_nascimento}")
                    
        except Error as e:
            print(f"❌ Erro ao verificar dados em 'Usuario': {e}")
        
        # Verificar erros de chave estrangeira específicos
        try:
            cursor.execute("PRAGMA foreign_key_check")
            fk_errors = cursor.fetchall()
            if fk_errors:
                print(f"\n⚠️  Erros de chave estrangeira encontrados:")
                for error in fk_errors:
                    table, rowid, ref_table, ref_rowid = error
                    print(f"  - Tabela: {table}, Linha: {rowid}, Referência: {ref_table}.{ref_rowid}")
                    
                    # Verificar dados problemáticos
                    cursor.execute(f"SELECT * FROM {table} WHERE rowid = {rowid}")
                    problem_data = cursor.fetchone()
                    print(f"    Dados problemáticos: {problem_data}")
            else:
                print("\n✅ Nenhum erro de chave estrangeira encontrado")
        except Error as e:
            print(f"❌ Erro ao verificar chaves estrangeiras: {e}")
        
        conn.close()
        print("\n✅ Verificação de integridade concluída")
        
    except Error as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")

if __name__ == "__main__":
    check_database_integrity()