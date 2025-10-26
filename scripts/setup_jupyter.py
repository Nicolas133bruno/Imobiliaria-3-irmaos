#!/usr/bin/env python3
"""
Script de configuração para JupyterLab - Imobiliária 3 Irmãos
Este script configura o ambiente JupyterLab para desenvolvimento sênior
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Instala os requisitos do JupyterLab"""
    print("🔧 Instalando requisitos do JupyterLab...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_jupyter.txt"])
        print("✅ Requisitos instalados com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar requisitos: {e}")
        return False

def setup_jupyter_extensions():
    """Configura extensões do JupyterLab"""
    print("🔧 Configurando extensões do JupyterLab...")
    
    extensions = [
        "jupyterlab-git",
        "jupyterlab-lsp",
        "jupyterlab-code-formatter"
    ]
    
    for extension in extensions:
        try:
            subprocess.check_call([sys.executable, "-m", "jupyter", "labextension", "install", extension])
            print(f"✅ Extensão {extension} instalada!")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Erro ao instalar {extension}: {e}")

def create_jupyter_config():
    """Cria configuração personalizada do JupyterLab"""
    print("🔧 Criando configuração do JupyterLab...")
    
    config_dir = Path.home() / ".jupyter"
    config_dir.mkdir(exist_ok=True)
    
    # Configuração do JupyterLab
    lab_config = """
{
  "ServerApp": {
    "port": 8888,
    "ip": "127.0.0.1",
    "open_browser": true,
    "allow_root": false
  },
  "LabApp": {
    "dev_mode": false,
    "watch": false
  }
}
"""
    
    config_file = config_dir / "jupyter_lab_config.json"
    with open(config_file, "w") as f:
        f.write(lab_config)
    
    print(f"✅ Configuração salva em: {config_file}")

def create_env_file():
    """Cria arquivo .env para configurações sensíveis"""
    print("🔧 Criando arquivo de configuração .env...")
    
    env_content = """# Configurações do Banco de Dados MySQL
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_NAME=imobiliaria_3_irmaos

# Configurações da API
API_BASE_URL=http://localhost:8000
API_TIMEOUT=30

# Configurações do JupyterLab
JUPYTER_PORT=8888
JUPYTER_IP=127.0.0.1

# Configurações de Desenvolvimento
DEBUG=True
LOG_LEVEL=INFO
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ Arquivo .env criado!")
    print("⚠️ IMPORTANTE: Edite o arquivo .env com suas configurações reais!")

def main():
    """Função principal de configuração"""
    print("🚀 Configurando JupyterLab para Imobiliária 3 Irmãos")
    print("=" * 60)
    
    # Verificar se estamos no diretório correto
    if not Path("main.py").exists():
        print("❌ Execute este script no diretório raiz do projeto!")
        return False
    
    # Instalar requisitos
    if not install_requirements():
        return False
    
    # Configurar extensões
    setup_jupyter_extensions()
    
    # Criar configurações
    create_jupyter_config()
    create_env_file()
    
    print("\n🎉 Configuração concluída com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Edite o arquivo .env com suas configurações de banco")
    print("2. Execute: jupyter lab")
    print("3. Abra o notebook: imobiliaria_analysis.ipynb")
    print("4. Configure a conexão MySQL no notebook")
    
    return True

if __name__ == "__main__":
    main()
