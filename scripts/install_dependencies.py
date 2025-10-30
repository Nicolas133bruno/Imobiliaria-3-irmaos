#!/usr/bin/env python3
"""
Script para instalar todas as dependências do projeto
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala os requisitos"""
    print("Instalando dependencias do projeto...")
    
    requirements_files = [
        "requirements.txt",
        "requirements_jupyter.txt"
    ]
    
    for req_file in requirements_files:
        if os.path.exists(req_file):
            print(f"\nInstalando {req_file}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
                print(f"OK: {req_file} instalado com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"ERRO ao instalar {req_file}: {e}")
                return False
        else:
            print(f"AVISO: {req_file} nao encontrado")
    
    return True

def main():
    """Função principal"""
    print("INSTALACAO DE DEPENDENCIAS - IMOBILIARIA 3 IRMAOS")
    print("=" * 60)
    
    if install_requirements():
        print("\nSUCESSO: Todas as dependencias foram instaladas!")
        print("\nProximos passos:")
        print("1. Execute: python test_simple.py (para validar)")
        print("2. Execute: python init_project.py (para configurar)")
        print("3. Inicie os servicos: start_all.bat ou ./start_all.sh")
    else:
        print("\nERRO: Falha na instalacao das dependencias")
        print("Verifique se o pip esta funcionando corretamente")
    
    return True

if __name__ == "__main__":
    main()
