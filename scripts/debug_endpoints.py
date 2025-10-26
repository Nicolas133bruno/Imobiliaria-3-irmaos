import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi.testclient import TestClient
from main import app
from database import SessionLocal
from sqlalchemy import text

def test_database_connection():
    """Testar conexão com o banco de dados"""
    print("🔍 Testando conexão com o banco de dados...")
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT 1")).scalar()
        db.close()
        print(f"✅ Conexão com banco OK: {result}")
        return True
    except Exception as e:
        print(f"❌ Erro na conexão com banco: {e}")
        return False

def test_usuario_endpoint():
    """Testar endpoint /usuarios/ diretamente"""
    print("\n🔍 Testando endpoint /usuarios/...")
    
    try:
        from routers.Usuario import get_usuarios
        from database import get_db
        
        # Criar cliente de teste
        client = TestClient(app)
        
        # Testar conexão com banco primeiro
        if not test_database_connection():
            return
        
        # Testar o endpoint
        response = client.get("/usuarios/")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Endpoint /usuarios/ funcionando!")
            print(f"Resposta: {response.json()}")
        else:
            print(f"❌ Erro no endpoint: {response.text}")
            
    except Exception as e:
        print(f"❌ Erro ao testar endpoint /usuarios/: {e}")
        import traceback
        traceback.print_exc()

def test_visita_endpoint():
    """Testar endpoint /visitas/ diretamente"""
    print("\n🔍 Testando endpoint /visitas/...")
    
    try:
        from routers.Visita import get_visitas
        from database import get_db
        
        # Criar cliente de teste
        client = TestClient(app)
        
        # Testar conexão com banco primeiro
        if not test_database_connection():
            return
        
        # Testar o endpoint
        response = client.get("/visitas/")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Endpoint /visitas/ funcionando!")
            print(f"Resposta: {response.json()}")
        else:
            print(f"❌ Erro no endpoint: {response.text}")
            
    except Exception as e:
        print(f"❌ Erro ao testar endpoint /visitas/: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🧪 Debug detalhado dos endpoints...")
    
    # Testar conexão com banco
    test_database_connection()
    
    # Testar endpoints
    test_usuario_endpoint()
    test_visita_endpoint()
    
    print("\n📋 Debug concluído!")