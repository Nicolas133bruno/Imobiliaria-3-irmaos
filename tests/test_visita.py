import requests
import json
from datetime import date

# URL base da API
BASE_URL = "http://localhost:8000"

def test_create_visita():
    """Testa a criação de uma visita com diferentes formatos de hora"""
    
    # Dados para teste com formato HH:MM:SS
    visita_data_1 = {
        "data_visita": str(date.today()),
        "hora_visita": "14:30:00",
        "status_visita": "Agendada",
        "fk_id_usuario": 1,
        "fk_id_corretor": 1,
        "fk_id_imovel": 1
    }
    
    # Dados para teste com formato HH:MM
    visita_data_2 = {
        "data_visita": str(date.today()),
        "hora_visita": "15:45",
        "status_visita": "Agendada",
        "fk_id_usuario": 1,
        "fk_id_corretor": 1,
        "fk_id_imovel": 1
    }
    
    # Teste com formato HH:MM:SS
    print("Testando criação de visita com formato de hora HH:MM:SS...")
    try:
        response = requests.post(f"{BASE_URL}/visitas/", json=visita_data_1)
        if response.status_code == 200:
            print("✅ Teste com formato HH:MM:SS passou!")
            print(f"Resposta: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"❌ Teste com formato HH:MM:SS falhou! Status: {response.status_code}")
            print(f"Erro: {response.text}")
    except Exception as e:
        print(f"❌ Erro ao executar teste: {str(e)}")
    
    # Teste com formato HH:MM
    print("\nTestando criação de visita com formato de hora HH:MM...")
    try:
        response = requests.post(f"{BASE_URL}/visitas/", json=visita_data_2)
        if response.status_code == 200:
            print("✅ Teste com formato HH:MM passou!")
            print(f"Resposta: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"❌ Teste com formato HH:MM falhou! Status: {response.status_code}")
            print(f"Erro: {response.text}")
    except Exception as e:
        print(f"❌ Erro ao executar teste: {str(e)}")

def test_update_visita():
    """Testa a atualização de uma visita com diferentes formatos de hora"""
    
    # Primeiro, vamos obter uma visita existente
    print("\nBuscando visitas existentes...")
    try:
        response = requests.get(f"{BASE_URL}/visitas/")
        if response.status_code == 200 and len(response.json()) > 0:
            visita_id = response.json()[0]["id_visita"]
            print(f"Visita encontrada com ID: {visita_id}")
            
            # Dados para atualização com formato HH:MM
            visita_update = {
                "data_visita": str(date.today()),
                "hora_visita": "16:15",
                "status_visita": "Confirmada",
                "fk_id_usuario": 1,
                "fk_id_corretor": 1,
                "fk_id_imovel": 1
            }
            
            print("\nTestando atualização de visita com formato de hora HH:MM...")
            update_response = requests.put(f"{BASE_URL}/visitas/{visita_id}", json=visita_update)
            
            if update_response.status_code == 200:
                print("✅ Teste de atualização passou!")
                print(f"Resposta: {json.dumps(update_response.json(), indent=2)}")
            else:
                print(f"❌ Teste de atualização falhou! Status: {update_response.status_code}")
                print(f"Erro: {update_response.text}")
        else:
            print("❌ Não foi possível encontrar visitas para testar a atualização")
    except Exception as e:
        print(f"❌ Erro ao executar teste de atualização: {str(e)}")

if __name__ == "__main__":
    print("Iniciando testes do router de visitas...")
    test_create_visita()
    test_update_visita()
    print("\nTestes concluídos!")