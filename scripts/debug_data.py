#!/usr/bin/env python3
"""
Script de debug para verificar a validação de data
"""

from datetime import date
from schemas import VisitaCreate

# Teste com data futura (deve passar)
print("Testando data futura (2025-01-15):")
try:
    visita = VisitaCreate(
        data_visita=date(2025, 1, 15),
        hora_visita="14:30",
        status_visita="Agendada",
        fk_id_usuario=1,
        fk_id_corretor=1,
        fk_id_imovel=1
    )
    print("✅ Data futura - OK")
    print(f"Data validada: {visita.data_visita}")
except Exception as e:
    print(f"❌ Data futura - ERRO: {e}")

print("\nTestando data passada (2023-01-01):")
try:
    visita = VisitaCreate(
        data_visita=date(2023, 1, 1),
        hora_visita="14:30",
        status_visita="Agendada",
        fk_id_usuario=1,
        fk_id_corretor=1,
        fk_id_imovel=1
    )
    print("❌ Data passada - DEVERIA FALHAR mas passou")
except Exception as e:
    print(f"✅ Data passada - OK (bloqueada corretamente): {e}")

print(f"\nData de hoje: {date.today()}")