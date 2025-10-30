#!/usr/bin/env python3
"""
Script para testar a API da Imobiliaria 3 Irmaos
"""

import requests
import time
import sys

def test_api():
    """Testa se a API está funcionando"""
    print("TESTANDO API IMOBILIARIA 3 IRMAOS")
    print("=" * 40)
    
    api_url = "http://localhost:8000"
    
    # Aguardar API inicializar
    print("Aguardando API inicializar...")
    time.sleep(2)
    
    try:
        # Teste do endpoint raiz
        response = requests.get(f"{api_url}/", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"OK: API funcionando - {data.get('message', 'Sem mensagem')}")
            
            # Teste da documentação
            docs_response = requests.get(f"{api_url}/docs", timeout=5)
            if docs_response.status_code == 200:
                print("OK: Documentacao disponivel em http://localhost:8000/docs")
            else:
                print("AVISO: Documentacao nao acessivel")
            
            return True
        else:
            print(f"ERRO: API retornou status {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("ERRO: Nao foi possivel conectar com a API")
        print("Certifique-se de que a API esta rodando em http://localhost:8000")
        return False
    except Exception as e:
        print(f"ERRO: {e}")
        return False

def main():
    """Função principal"""
    success = test_api()
    
    if success:
        print("\nSUCESSO: API esta funcionando corretamente!")
        print("Acesse: http://localhost:8000/docs")
    else:
        print("\nERRO: API nao esta funcionando")
        print("Execute: python start_api.py")
        sys.exit(1)

if __name__ == "__main__":
    main()
