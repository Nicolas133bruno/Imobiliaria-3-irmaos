import requests
import time
import socket

def test_connection():
    """Testa a conexão com a API de várias formas"""
    
    print("🔍 Testando conectividade com a API...")
    
    # Testar se a porta está aberta
    print("1. Testando se a porta 8000 está aberta...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex(('127.0.0.1', 8000))
        if result == 0:
            print("   ✅ Porta 8000 está aberta")
        else:
            print(f"   ❌ Porta 8000 não está respondendo (código: {result})")
        sock.close()
    except Exception as e:
        print(f"   ❌ Erro ao testar porta: {e}")
    
    # Testar endpoint raiz
    print("\n2. Testando endpoint raiz (/)")
    try:
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        print(f"   ✅ Status: {response.status_code}")
        print(f"   📄 Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("   ❌ Não foi possível conectar à API")
    except requests.exceptions.Timeout:
        print("   ❌ Timeout ao conectar à API")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
    
    # Testar endpoint /usuarios/
    print("\n3. Testando endpoint /usuarios/")
    try:
        response = requests.get("http://127.0.0.1:8000/usuarios/", timeout=5)
        print(f"   ✅ Status: {response.status_code}")
        if response.status_code == 200:
            usuarios = response.json()
            print(f"   📊 Total de usuários: {len(usuarios)}")
        else:
            print(f"   📄 Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("   ❌ Não foi possível conectar à API")
    except requests.exceptions.Timeout:
        print("   ❌ Timeout ao conectar à API")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        
    # Testar com diferentes hosts
    print("\n4. Testando com diferentes hosts...")
    hosts = ['127.0.0.1', 'localhost', '0.0.0.0']
    
    for host in hosts:
        print(f"   🔗 Testando {host}:8000...")
        try:
            response = requests.get(f"http://{host}:8000/", timeout=3)
            print(f"      ✅ {host}: {response.status_code}")
        except:
            print(f"      ❌ {host}: Não conectou")

if __name__ == "__main__":
    test_connection()