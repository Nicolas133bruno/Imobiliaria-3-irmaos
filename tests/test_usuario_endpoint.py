import requests
import json

def test_usuario_endpoint():
    url = "http://localhost:8000/usuarios/"
    
    print(f"🔍 Testando endpoint: {url}")
    
    try:
        response = requests.get(url)
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Sucesso!")
            usuarios = response.json()
            print(f"📝 Total de usuários: {len(usuarios)}")
            for usuario in usuarios:
                print(f"  - ID: {usuario.get('id_usuario')}, Nome: {usuario.get('nome')}")
        else:
            print(f"❌ Erro: {response.status_code}")
            print(f"📄 Response: {response.text}")
            
            # Tentar obter detalhes do erro se for JSON
            try:
                error_details = response.json()
                print(f"🔍 Detalhes do erro: {json.dumps(error_details, indent=2)}")
            except:
                pass
                
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à API. Verifique se o servidor está rodando.")
    except requests.exceptions.Timeout:
        print("❌ Timeout ao conectar à API.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    test_usuario_endpoint()