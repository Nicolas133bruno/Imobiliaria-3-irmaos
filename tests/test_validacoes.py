#!/usr/bin/env python3
"""
Script para testar as validações implementadas nos schemas Pydantic
"""

from datetime import date, datetime
from decimal import Decimal
from schemas import (
    UsuarioCreate, CorretorCreate, EnderecoCreate, 
    ImovelCreate, VisitaCreate
)

def test_validacoes_usuario():
    """Testa validações do schema Usuario"""
    print("🧪 Testando validações de Usuário...")
    
    # Teste 1: CPF válido
    try:
        usuario = UsuarioCreate(
            nome="João Silva",
            cpf="123.456.789-09",  # CPF válido (fictício)
            telefone="(31) 99999-9999",
            email="joao@email.com",
            data_nascimento=date(1990, 1, 1),
            sexo="M",
            login_usu="joao123",
            senha_usu="senha123",
            fk_Perfil_id=1
        )
        print("  ✅ CPF válido - OK")
    except Exception as e:
        print(f"  ❌ CPF válido - ERRO: {e}")
    
    # Teste 2: CPF inválido
    try:
        usuario = UsuarioCreate(
            nome="João Silva",
            cpf="111.111.111-11",  # CPF inválido (sequência repetida)
            telefone="(31) 99999-9999",
            email="joao@email.com",
            data_nascimento=date(1990, 1, 1),
            sexo="M",
            login_usu="joao123",
            senha_usu="senha123",
            fk_Perfil_id=1
        )
        print("  ❌ CPF inválido - DEVERIA FALHAR")
    except Exception as e:
        print(f"  ✅ CPF inválido - OK: {e}")

def test_validacoes_corretor():
    """Testa validações do schema Corretor"""
    print("\n🧪 Testando validações de Corretor...")
    
    # Teste 1: CRECI válido
    try:
        corretor = CorretorCreate(
            creci="MG-12345",
            fk_usuario_id=1
        )
        print("  ✅ CRECI válido - OK")
    except Exception as e:
        print(f"  ❌ CRECI válido - ERRO: {e}")
    
    # Teste 2: CRECI inválido
    try:
        corretor = CorretorCreate(
            creci="12345",  # Formato inválido
            fk_usuario_id=1
        )
        print("  ❌ CRECI inválido - DEVERIA FALHAR")
    except Exception as e:
        print(f"  ✅ CRECI inválido - OK: {e}")

def test_validacoes_endereco():
    """Testa validações do schema Endereco"""
    print("\n🧪 Testando validações de Endereço...")
    
    # Teste 1: Endereço válido
    try:
        endereco = EnderecoCreate(
            logradouro="Rua das Flores",
            numero="123",
            bairro="Centro",
            cidade="Belo Horizonte",
            estado="MG",
            cep="30130-123"
        )
        print("  ✅ Endereço válido - OK")
    except Exception as e:
        print(f"  ❌ Endereço válido - ERRO: {e}")
    
    # Teste 2: Estado inválido
    try:
        endereco = EnderecoCreate(
            logradouro="Rua das Flores",
            numero="123",
            bairro="Centro",
            cidade="Belo Horizonte",
            estado="XX",  # Estado inválido
            cep="30130-123"
        )
        print("  ❌ Estado inválido - DEVERIA FALHAR")
    except Exception as e:
        print(f"  ✅ Estado inválido - OK: {e}")

def test_validacoes_imovel():
    """Testa validações do schema Imovel"""
    print("\n🧪 Testando validações de Imóvel...")
    
    # Teste 1: Imóvel válido
    try:
        imovel = ImovelCreate(
            area_total=Decimal("100.00"),
            quarto=3,
            banheiro=2,
            vaga_garagem=1,
            valor=Decimal("300000.00"),
            tipo="Casa",
            desc_tipo_imovel="Casa com 3 quartos",
            fk_id_status=1,
            fk_id_endereco=1,
            fk_id_corretor=1
        )
        print("  ✅ Imóvel válido - OK")
    except Exception as e:
        print(f"  ❌ Imóvel válido - ERRO: {e}")
    
    # Teste 2: Tipo de imóvel inválido
    try:
        imovel = ImovelCreate(
            area_total=Decimal("100.00"),
            quarto=3,
            banheiro=2,
            vaga_garagem=1,
            valor=Decimal("300000.00"),
            tipo="Mansão",  # Tipo inválido
            desc_tipo_imovel="Mansão enorme",
            fk_id_status=1,
            fk_id_endereco=1,
            fk_id_corretor=1
        )
        print("  ❌ Tipo inválido - DEVERIA FALHAR")
    except Exception as e:
        print(f"  ✅ Tipo inválido - OK: {e}")

def test_validacoes_visita():
    """Testa validações do schema Visita"""
    print("\n🧪 Testando validações de Visita...")
    
    # Teste 1: Visita válida
    try:
        visita = VisitaCreate(
            data_visita=date(2026, 1, 15),  # Data realmente futura
            hora_visita="14:30",
            status_visita="Agendada",
            fk_id_usuario=1,
            fk_id_corretor=1,
            fk_id_imovel=1
        )
        print("  ✅ Visita válida - OK")
    except Exception as e:
        print(f"  ❌ Visita válida - ERRO: {e}")
    
    # Teste 2: Data de visita no passado
    try:
        visita = VisitaCreate(
            data_visita=date(2023, 1, 1),  # Data passada
            hora_visita="14:30",
            status_visita="Agendada",
            fk_id_usuario=1,
            fk_id_corretor=1,
            fk_id_imovel=1
        )
        print("  ❌ Data passada - DEVERIA FALHAR")
    except Exception as e:
        print(f"  ✅ Data passada - OK: {e}")

def main():
    """Função principal de teste"""
    print("🚀 TESTE DAS VALIDAÇÕES DA API")
    print("=" * 50)
    
    test_validacoes_usuario()
    test_validacoes_corretor()
    test_validacoes_endereco()
    test_validacoes_imovel()
    test_validacoes_visita()
    
    print("\n" + "=" * 50)
    print("✅ Testes completados!")
    print("📋 Verifique se todas as validações estão funcionando corretamente")

if __name__ == "__main__":
    main()