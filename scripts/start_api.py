#!/usr/bin/env python3
"""
Script para iniciar a API da Imobiliaria 3 Irmaos
"""

import uvicorn
import sys
import os

def start_api():
    """Inicia a API FastAPI"""
    print("INICIANDO API IMOBILIARIA 3 IRMAOS")
    print("=" * 40)
    print("API: http://localhost:8000")
    print("Documentacao: http://localhost:8000/docs")
    print("Para parar: Ctrl+C")
    print("=" * 40)
    
    try:
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\nAPI parada pelo usuario")
    except Exception as e:
        print(f"Erro ao iniciar API: {e}")

if __name__ == "__main__":
    start_api()
