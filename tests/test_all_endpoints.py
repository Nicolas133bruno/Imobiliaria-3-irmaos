#!/usr/bin/env python3
"""
Script para testar todos os endpoints da API da Imobiliária 3 Irmãos
"""

import requests
import json
import time
from datetime import date, datetime

def test_endpoint(method, url, data=None, expected_status=200):
    """Testa um endpoint específico"""
    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=10)
        elif method.upper() == "POST":
            response = requests.post(url, json=data, timeout=10)
        elif method.upper() == "PUT":
            response = requests.put(url, json=data, timeout=10)
        elif method.upper() == "DELETE":
            response = requests.delete(url, timeout=10)
        
        if response.status_code == expected_status:
            print(f"  ✅ {method} {url}: OK ({response.status_code})")
            return True, response.json() if response.content else {}
        else:
            print(f"  ❌ {method} {url}: ERRO ({response.status_code})")
            if response.content:
                print(f"      Resposta: {response.text[:200]}...")
            return False, {}
            
    except requests.exceptions.ConnectionError:
        print(f"  ❌ {method} {url}: SEM CONEXÃO")
        return False, {}
    except Exception as e:
        print(f"  ❌ {method} {url}: ERRO - {e}")
        return False, {}

def test_all_endpoints():
    """Testa todos os endpoints da API"""
    print("🚀 TESTANDO TODOS OS ENDPOINTS DA API")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    # Aguardar API inicializar
    print("Aguardando API inicializar...")
    time.sleep(3)
    
    # Teste do endpoint raiz
    print("\n📋 Testando endpoint raiz...")
    success, _ = test_endpoint("GET", f"{base_url}/")
    
    if not success:
        print("❌ API não está funcionando. Execute: python start_api.py")
        return False
    
    # Dados de teste
    test_data = {
        "perfil": {"tipo_perf": "Teste API"},
        "usuario": {
            "nome": "Teste API",
            "cpf": "123.456.789-00",
            "telefone": "123456789",
            "email": "teste@api.com",
            "data_nascimento": "1990-01-01",
            "sexo": "M",
            "login_usu": "teste_api",
            "senha_usu": "senha123",
            "fk_Perfil_id": 1
        },
        "corretor": {"creci": "MG-TESTE", "fk_usuario_id": 1},
        "status_imovel": {"descricao_status": "Teste API"},
        "endereco": {
            "logradouro": "Rua Teste API",
            "numero": "123",
            "bairro": "Centro",
            "cidade": "Teste",
            "estado": "MG",
            "cep": "12345-678"
        },
        "imovel": {
            "area_total": 100.0,
            "quarto": 3,
            "banheiro": 2,
            "vaga_garagem": 1,
            "valor": 300000.0,
            "tipo": "Casa",
            "desc_tipo_imovel": "Casa teste API",
            "fk_id_status": 1,
            "fk_id_endereco": 1,
            "fk_id_corretor": 1
        },
        "visita": {
            "data_visita": "2024-01-01",
            "hora_visita": "14:00:00",
            "status_visita": "Agendada",
            "fk_id_usuario": 1,
            "fk_id_corretor": 1,
            "fk_id_imovel": 1
        },
        "contrato_aluguel": {
            "tipo": "Residencial",
            "data_inicio": "2024-01-01",
            "data_fim": "2024-12-31",
            "valor_mensalidade": 1500.0,
            "fk_id_usuario": 1,
            "fk_id_imovel": 1
        },
        "contrato_venda": {
            "tipo_venda": "À vista",
            "data_inicio": "2024-01-01",
            "data_fim": "2024-01-01",
            "valor_negociado": 300000.0,
            "fk_id_usuario": 1,
            "fk_id_imovel": 1
        }
    }
    
    # Endpoints para testar
    endpoints = [
        # Perfis
        ("GET", "/perfis"),
        ("POST", "/perfis", test_data["perfil"]),
        ("GET", "/perfis/1"),
        
        # Usuários
        ("GET", "/usuarios"),
        ("POST", "/usuarios", test_data["usuario"]),
        ("GET", "/usuarios/1"),
        
        # Corretores
        ("GET", "/corretores"),
        ("POST", "/corretores", test_data["corretor"]),
        ("GET", "/corretores/1"),
        
        # Status Imóvel
        ("GET", "/status_imovel"),
        ("POST", "/status_imovel", test_data["status_imovel"]),
        ("GET", "/status_imovel/1"),
        
        # Endereços
        ("GET", "/enderecos"),
        ("POST", "/enderecos", test_data["endereco"]),
        ("GET", "/enderecos/1"),
        ("GET", "/enderecos/cidade/Teste"),
        ("GET", "/enderecos/estado/MG"),
        
        # Imóveis
        ("GET", "/imoveis"),
        ("POST", "/imoveis", test_data["imovel"]),
        ("GET", "/imoveis/1"),
        
        # Visitas
        ("GET", "/visitas"),
        ("POST", "/visitas", test_data["visita"]),
        ("GET", "/visitas/1"),
        
        # Contratos Aluguel
        ("GET", "/contratos_aluguel"),
        ("POST", "/contratos_aluguel", test_data["contrato_aluguel"]),
        ("GET", "/contratos_aluguel/1"),
        
        # Contratos Venda
        ("GET", "/contratos_venda"),
        ("POST", "/contratos_venda", test_data["contrato_venda"]),
        ("GET", "/contratos_venda/1"),
        
        # Relatórios
        ("GET", "/relatorios/usuarios_com_contratos"),
        ("GET", "/relatorios/imoveis_com_status"),
        ("GET", "/relatorios/visitas_por_corretor"),
        ("GET", "/relatorios/contratos_aluguel_ativos"),
        ("GET", "/relatorios/contratos_venda"),
        ("GET", "/relatorios/imoveis_por_status"),
        ("GET", "/relatorios/usuarios_com_perfil"),
    ]
    
    results = []
    
    for method, endpoint, *data in endpoints:
        url = f"{base_url}{endpoint}"
        data = data[0] if data else None
        
        print(f"\n🔍 Testando {method} {endpoint}...")
        success, response = test_endpoint(method, url, data)
        results.append((method, endpoint, success))
        
        # Pequena pausa entre requests
        time.sleep(0.5)
    
    # Resumo dos resultados
    print("\n" + "=" * 50)
    print("RESUMO DOS TESTES")
    print("=" * 50)
    
    passed = sum(1 for _, _, success in results if success)
    total = len(results)
    
    for method, endpoint, success in results:
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"{method} {endpoint}: {status}")
    
    print(f"\nTotal: {passed}/{total} testes passaram")
    
    if passed == total:
        print("\n🎉 SUCESSO: Todos os endpoints estão funcionando!")
        print("\n📋 Próximos passos:")
        print("1. Acesse: http://localhost:8000/docs")
        print("2. Teste a documentação interativa")
        print("3. Use os endpoints em sua aplicação")
        return True
    else:
        print(f"\n⚠️  ATENÇÃO: {total - passed} endpoints falharam")
        print("Verifique os logs da API para mais detalhes")
        return False

def main():
    """Função principal"""
    try:
        success = test_all_endpoints()
        return success
    except KeyboardInterrupt:
        print("\n\n⏹️  Teste interrompido pelo usuário")
        return False
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
