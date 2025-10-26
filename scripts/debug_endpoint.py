#!/usr/bin/env python3
"""
Script para debug do endpoint /usuarios/ e identificar o Internal Server Error
"""

import requests
import json

def test_usuario_endpoint():
    url = "http://localhost:8000/usuarios/"
    
    try:
        print(f"Testando endpoint: {url}")
        
        # Primeiro teste simples
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Endpoint funcionando!")
            usuarios = response.json()
            print(f"Total de usuários: {len(usuarios)}")
            for usuario in usuarios[:3]:  # Mostrar apenas os primeiros 3
                print(f"  - {usuario.get('nome', 'N/A')} ({usuario.get('email', 'N/A')})")
        else:
            print(f"❌ Erro: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à API. Verifique se a API está rodando.")
    except requests.exceptions.Timeout:
        print("❌ Timeout ao tentar acessar o endpoint.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao decodificar JSON: {e}")
        print(f"Response raw: {response.text}")

if __name__ == "__main__":
    test_usuario_endpoint()