import sqlite3
from sqlite3 import Error

def fix_database_issues():
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect('imobiliaria.db')
        cursor = conn.cursor()
        
        print("🔧 Corrigindo problemas do banco de dados...")
        
        # Verificar e corrigir erros de chave estrangeira
        cursor.execute("PRAGMA foreign_key_check")
        fk_errors = cursor.fetchall()
        
        if fk_errors:
            print(f"\n⚠️  Encontrados {len(fk_errors)} erros de chave estrangeira:")
            
            for error in fk_errors:
                table, rowid, ref_table, ref_rowid = error
                print(f"  - {table}.{rowid} → {ref_table}.{ref_rowid}")
                
                # Verificar se a referência existe
                cursor.execute(f"SELECT COUNT(*) FROM {ref_table} WHERE id_{ref_table.lower()} = {ref_rowid}")
                ref_exists = cursor.fetchone()[0] > 0
                
                if not ref_exists:
                    print(f"    ❌ Referência {ref_table}.{ref_rowid} não existe!")
                    # Remover registro problemático
                    cursor.execute(f"DELETE FROM {table} WHERE rowid = {rowid}")
                    print(f"    ✅ Registro {table}.{rowid} removido")
                else:
                    print(f"    ✅ Referência {ref_table}.{ref_rowid} existe")
                    # Pode ser um problema de validação, vamos verificar os dados
                    cursor.execute(f"SELECT * FROM {table} WHERE rowid = {rowid}")
                    problem_data = cursor.fetchone()
                    print(f"    📊 Dados: {problem_data}")
        else:
            print("\n✅ Nenhum erro de chave estrangeira encontrado")
        
        # Commit das mudanças
        conn.commit()
        
        # Verificar se ainda há erros
        cursor.execute("PRAGMA foreign_key_check")
        remaining_errors = cursor.fetchall()
        
        if remaining_errors:
            print(f"\n❌ Ainda há {len(remaining_errors)} erros após correção:")
            for error in remaining_errors:
                print(f"  - {error}")
        else:
            print("\n✅ Todos os erros de chave estrangeira foram resolvidos!")
        
        conn.close()
        print("\n✅ Correção do banco de dados concluída")
        
    except Error as e:
        print(f"❌ Erro ao corrigir banco de dados: {e}")

if __name__ == "__main__":
    fix_database_issues()