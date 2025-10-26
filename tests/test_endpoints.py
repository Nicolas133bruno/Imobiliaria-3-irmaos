import requests
import json

def test_endpoint(url):
    try:
        print(f"\n🔍 Testando: {url}")
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Sucesso!")
            try:
                data = response.json()
                print(f"Resposta JSON: {json.dumps(data, indent=2, ensure_ascii=False)}")
            except:
                print(f"Resposta: {response.text}")
        else:
            print(f"❌ Erro: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    base_url = "http://127.0.0.1:8000"
    
    print("🧪 Testando endpoints da API...")
    
    # Testar endpoints que estão com problemas
    test_endpoint(f"{base_url}/usuarios/")
    test_endpoint(f"{base_url}/visitas/")
    
    # Testar endpoint raiz para ver se API está funcionando
    test_endpoint(f"{base_url}/")
    
    print("\n📋 Teste concluído!")