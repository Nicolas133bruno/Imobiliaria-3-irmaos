import subprocess
import time
import requests
import sys

def start_api():
    """Inicia a API em um processo separado"""
    print("🚀 Iniciando API...")
    
    # Comando para iniciar a API
    cmd = [
        sys.executable, "-m", "uvicorn", 
        "main:app", 
        "--host", "127.0.0.1", 
        "--port", "8000"
    ]
    
    # Iniciar processo
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Aguardar inicialização
    time.sleep(3)
    
    return process

def test_endpoints():
    """Testa os endpoints da API"""
    print("\n🔍 Testando endpoints...")
    
    # Testar endpoint raiz
    print("1. Testando endpoint raiz (/)")
    try:
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        print(f"   ✅ Status: {response.status_code}")
        print(f"   📄 Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False
    
    # Testar endpoint /usuarios/
    print("\n2. Testando endpoint /usuarios/")
    try:
        response = requests.get("http://127.0.0.1:8000/usuarios/", timeout=5)
        print(f"   ✅ Status: {response.status_code}")
        
        if response.status_code == 200:
            usuarios = response.json()
            print(f"   📊 Total de usuários: {len(usuarios)}")
            for usuario in usuarios[:3]:  # Mostrar apenas os primeiros 3
                print(f"     - ID: {usuario.get('id_usuario')}, Nome: {usuario.get('nome')}")
        else:
            print(f"   📄 Response: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False
    
    return True

def main():
    """Função principal"""
    
    # Iniciar API
    api_process = start_api()
    
    try:
        # Testar endpoints
        success = test_endpoints()
        
        if success:
            print("\n🎉 Todos os testes passaram!")
        else:
            print("\n❌ Alguns testes falharam")
            
            # Capturar stderr da API
            _, stderr = api_process.communicate()
            if stderr:
                print(f"\n🔍 Logs de erro da API:")
                print(stderr)
                
    finally:
        # Finalizar processo da API
        api_process.terminate()
        api_process.wait()
        print("\n🛑 API finalizada")

if __name__ == "__main__":
    main()