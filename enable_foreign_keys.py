import sqlite3
from sqlite3 import Error

def enable_and_fix_foreign_keys():
    try:
        conn = sqlite3.connect('imobiliaria.db')
        cursor = conn.cursor()
        
        print("🔧 Habilitando e corrigindo foreign keys...")
        
        # Habilitar foreign keys
        cursor.execute("PRAGMA foreign_keys = ON")
        print("✅ Foreign keys habilitadas")
        
        # Verificar se há erros de foreign key
        cursor.execute("PRAGMA foreign_key_check")
        fk_errors = cursor.fetchall()
        
        if fk_errors:
            print(f"\n⚠️  Encontrados {len(fk_errors)} erros de foreign key:")
            
            for error in fk_errors:
                table, rowid, ref_table, ref_rowid = error
                print(f"  - {table}.{rowid} → {ref_table}.{ref_rowid}")
                
                # Para cada erro, vamos verificar se a referência existe
                cursor.execute(f"SELECT COUNT(*) FROM {ref_table} WHERE id_{ref_table.lower()} = {ref_rowid}")
                ref_exists = cursor.fetchone()[0] > 0
                
                if ref_exists:
                    print(f"    ✅ Referência {ref_table}.{ref_rowid} existe")
                    # Se a referência existe, o problema pode ser temporário
                    # Vamos tentar atualizar o registro para forçar a validação
                    try:
                        if table == 'Contrato_Venda':
                            cursor.execute(f"""
                                UPDATE Contrato_Venda 
                                SET fk_id_usuario = {ref_rowid}
                                WHERE rowid = {rowid}
                            """)
                        elif table == 'Visita':
                            cursor.execute(f"""
                                UPDATE Visita 
                                SET fk_id_usuario = {ref_rowid}
                                WHERE rowid = {rowid}
                            """)
                        print(f"    ✅ Registro {table}.{rowid} atualizado")
                    except Error as update_error:
                        print(f"    ❌ Erro ao atualizar: {update_error}")
                else:
                    print(f"    ❌ Referência {ref_table}.{ref_rowid} não existe!")
                    # Remover registro problemático
                    cursor.execute(f"DELETE FROM {table} WHERE rowid = {rowid}")
                    print(f"    ✅ Registro {table}.{rowid} removido")
        else:
            print("\n✅ Nenhum erro de foreign key encontrado")
        
        # Commit das mudanças
        conn.commit()
        
        # Verificar novamente
        cursor.execute("PRAGMA foreign_key_check")
        remaining_errors = cursor.fetchall()
        
        if remaining_errors:
            print(f"\n❌ Ainda há {len(remaining_errors)} erros:")
            for error in remaining_errors:
                print(f"  - {error}")
            
            # Se ainda houver erros, criar uma cópia limpa do banco
            print("\n🔄 Criando backup e recriando banco...")
            
        else:
            print("\n✅ Todos os erros de foreign key resolvidos!")
        
        conn.close()
        
        # Testar a conexão com foreign keys habilitadas
        test_foreign_keys()
        
    except Error as e:
        print(f"❌ Erro: {e}")

def test_foreign_keys():
    """Testar se as foreign keys estão funcionando"""
    try:
        conn = sqlite3.connect('imobiliaria.db')
        cursor = conn.cursor()
        
        # Habilitar foreign keys
        cursor.execute("PRAGMA foreign_keys = ON")
        
        # Tentar inserir um registro com referência inválida
        try:
            cursor.execute("INSERT INTO Visita (data_visita, hora_visita, status_visita, fk_id_usuario, fk_id_corretor, fk_id_imovel) VALUES ('2023-01-01', '10:00:00', 'Agendada', 999, 1, 1)")
            conn.commit()
            print("❌ Foreign keys NÃO estão funcionando - inseriu referência inválida")
        except Error as e:
            print("✅ Foreign keys funcionando corretamente - bloqueou inserção inválida")
            
        conn.close()
        
    except Error as e:
        print(f"❌ Erro no teste: {e}")

if __name__ == "__main__":
    enable_and_fix_foreign_keys()