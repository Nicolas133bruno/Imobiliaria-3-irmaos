import requests
import json
import traceback

def debug_api():
    url = "http://127.0.0.1:8000/usuarios/"
    
    print(f"🔍 Testando endpoint: {url}")
    
    try:
        # Fazer requisição com timeout
        response = requests.get(url, timeout=10)
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Sucesso!")
            usuarios = response.json()
            print(f"📝 Total de usuários: {len(usuarios)}")
            for usuario in usuarios:
                print(f"  - ID: {usuario.get('id_usuario')}, Nome: {usuario.get('nome')}")
        else:
            print(f"❌ Erro HTTP: {response.status_code}")
            print(f"📄 Response Text: {response.text}")
            
            # Tentar obter detalhes do erro se for JSON
            try:
                error_details = response.json()
                print(f"🔍 Detalhes do erro (JSON): {json.dumps(error_details, indent=2, ensure_ascii=False)}")
            except json.JSONDecodeError:
                print("⚠️  A resposta não é um JSON válido")
            except Exception as e:
                print(f"⚠️  Erro ao parsear JSON: {e}")
                
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à API. Verifique se o servidor está rodando.")
    except requests.exceptions.Timeout:
        print("❌ Timeout ao conectar à API (10 segundos).")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de requisição: {e}")
        print(f"🔍 Traceback completo:")
        traceback.print_exc()
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        print(f"🔍 Traceback completo:")
        traceback.print_exc()

if __name__ == "__main__":
    debug_api()