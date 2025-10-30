import sqlite3
from sqlite3 import Error

def debug_foreign_keys():
    try:
        conn = sqlite3.connect('imobiliaria.db')
        cursor = conn.cursor()
        
        print("🔍 Debug de chaves estrangeiras...")
        
        # Verificar se foreign keys estão habilitadas
        cursor.execute("PRAGMA foreign_keys")
        fk_enabled = cursor.fetchone()[0]
        print(f"🔧 Foreign keys habilitadas: {fk_enabled == 1}")
        
        if fk_enabled != 1:
            cursor.execute("PRAGMA foreign_keys = ON")
            print("✅ Foreign keys habilitadas")
        
        # Verificar estrutura das tabelas problemáticas
        tables_to_check = ['Contrato_Venda', 'Visita']
        
        for table in tables_to_check:
            print(f"\n📋 Estrutura da tabela {table}:")
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            for col in columns:
                col_name, col_type, not_null, default_val, pk = col[1], col[2], col[3], col[4], col[5]
                print(f"  - {col_name} ({col_type}) {'NOT NULL' if not_null else ''} {'PK' if pk else ''}")
        
        # Verificar constraints de foreign key
        print(f"\n🔗 Constraints de foreign key:")
        cursor.execute("PRAGMA foreign_key_list('Contrato_Venda')")
        fk_list = cursor.fetchall()
        for fk in fk_list:
            print(f"  - Contrato_Venda.{fk[3]} → {fk[2]}.{fk[4]}")
        
        cursor.execute("PRAGMA foreign_key_list('Visita')")
        fk_list = cursor.fetchall()
        for fk in fk_list:
            print(f"  - Visita.{fk[3]} → {fk[2]}.{fk[4]}")
        
        # Verificar dados específicos problemáticos
        print(f"\n🔍 Dados problemáticos:")
        
        # Contrato_Venda rowid 1
        cursor.execute("SELECT * FROM Contrato_Venda WHERE rowid = 1")
        contrato_data = cursor.fetchone()
        print(f"Contrato_Venda.1: {contrato_data}")
        
        # Verificar referência
        cursor.execute("SELECT * FROM Usuario WHERE id_usuario = 1")
        usuario_ref = cursor.fetchone()
        print(f"Usuario.1: {usuario_ref}")
        
        # Visita rowid 4
        cursor.execute("SELECT * FROM Visita WHERE rowid = 4")
        visita_data = cursor.fetchone()
        print(f"Visita.4: {visita_data}")
        
        # Verificar referência
        cursor.execute("SELECT * FROM Usuario WHERE id_usuario = 2")
        usuario_ref2 = cursor.fetchone()
        print(f"Usuario.2: {usuario_ref2}")
        
        conn.close()
        
    except Error as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    debug_foreign_keys()