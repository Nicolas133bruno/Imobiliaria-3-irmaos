#!/usr/bin/env python3
"""
Script de inicialização completo para o projeto Imobiliária 3 Irmãos
Este script configura todo o ambiente de desenvolvimento
"""

import subprocess
import sys
import os
import platform
from pathlib import Path

def print_banner():
    """Exibe banner do projeto"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🏠 IMOBILIÁRIA 3 IRMÃOS 🏠                ║
    ║                                                              ║
    ║              JupyterLab + FastAPI + MySQL                    ║
    ║                                                              ║
    ║              Configuração Automática do Projeto              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Verifica versão do Python"""
    print("🐍 Verificando versão do Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ é necessário!")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True

def install_requirements():
    """Instala todos os requisitos"""
    print("\n📦 Instalando dependências...")
    
    requirements_files = [
        "requirements.txt",
        "requirements_jupyter.txt"
    ]
    
    for req_file in requirements_files:
        if Path(req_file).exists():
            print(f"   📋 Instalando {req_file}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
                print(f"   ✅ {req_file} instalado com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"   ❌ Erro ao instalar {req_file}: {e}")
                return False
        else:
            print(f"   ⚠️ {req_file} não encontrado")
    
    return True

def create_directories():
    """Cria diretórios necessários"""
    print("\n📁 Criando estrutura de diretórios...")
    
    directories = [
        "notebooks",
        "data",
        "reports",
        "logs",
        "backups"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"   ✅ Diretório {directory}/ criado")

def create_env_file():
    """Cria arquivo .env com configurações padrão"""
    print("\n⚙️ Criando arquivo de configuração .env...")
    
    env_content = """# Configurações do Banco de Dados MySQL
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=root123
DB_NAME=imobiliaria_3_irmaos

# Configurações da API
API_BASE_URL=http://localhost:8000
API_TIMEOUT=30

# Configurações do JupyterLab
JUPYTER_PORT=8888
JUPYTER_IP=127.0.0.1
JUPYTER_TOKEN=imobiliaria123

# Configurações de Desenvolvimento
DEBUG=True
LOG_LEVEL=INFO

# Configurações de Segurança
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("   ✅ Arquivo .env criado com configurações padrão")

def setup_git():
    """Configura Git se necessário"""
    print("\n🔧 Configurando Git...")
    
    if not Path(".git").exists():
        try:
            subprocess.check_call(["git", "init"])
            print("   ✅ Repositório Git inicializado")
        except subprocess.CalledProcessError:
            print("   ⚠️ Git não encontrado ou erro na inicialização")
    else:
        print("   ✅ Repositório Git já existe")

def create_gitignore():
    """Cria arquivo .gitignore"""
    print("\n📝 Criando .gitignore...")
    
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Jupyter
.ipynb_checkpoints/

# Environment
.env
.env.local
.env.production

# Database
*.db
*.sqlite3

# Logs
logs/
*.log

# Data
data/
reports/
backups/

# OS
.DS_Store
Thumbs.db
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    
    print("   ✅ .gitignore criado")

def create_startup_scripts():
    """Cria scripts de inicialização"""
    print("\n🚀 Criando scripts de inicialização...")
    
    # Script para Windows
    windows_script = """@echo off
echo 🚀 Iniciando Imobiliária 3 Irmãos
echo =================================

echo 🔧 Iniciando MySQL...
start "MySQL" docker run -d --name mysql-imobiliaria -e MYSQL_ROOT_PASSWORD=root123 -e MYSQL_DATABASE=imobiliaria_3_irmaos -p 3306:3306 mysql:8.0

echo ⏳ Aguardando MySQL inicializar...
timeout /t 10 /nobreak

echo 🌐 Iniciando API...
start "API" uvicorn main:app --reload --host 0.0.0.0 --port 8000

echo ⏳ Aguardando API inicializar...
timeout /t 5 /nobreak

echo 📊 Iniciando JupyterLab...
start "JupyterLab" jupyter lab --ip=127.0.0.1 --port=8888 --no-browser

echo ✅ Todos os serviços iniciados!
echo 📝 API: http://localhost:8000
echo 📊 JupyterLab: http://localhost:8888
echo 🔑 Token JupyterLab: imobiliaria123

pause
"""
    
    with open("start_all.bat", "w") as f:
        f.write(windows_script)
    
    # Script para Linux/Mac
    unix_script = """#!/bin/bash
echo "🚀 Iniciando Imobiliária 3 Irmãos"
echo "================================="

echo "🔧 Iniciando MySQL..."
docker run -d --name mysql-imobiliaria -e MYSQL_ROOT_PASSWORD=root123 -e MYSQL_DATABASE=imobiliaria_3_irmaos -p 3306:3306 mysql:8.0

echo "⏳ Aguardando MySQL inicializar..."
sleep 10

echo "🌐 Iniciando API..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
API_PID=$!

echo "⏳ Aguardando API inicializar..."
sleep 5

echo "📊 Iniciando JupyterLab..."
jupyter lab --ip=127.0.0.1 --port=8888 --no-browser &
JUPYTER_PID=$!

echo "✅ Todos os serviços iniciados!"
echo "📝 API: http://localhost:8000"
echo "📊 JupyterLab: http://localhost:8888"
echo "🔑 Token JupyterLab: imobiliaria123"

# Função para parar serviços
cleanup() {
    echo "🛑 Parando serviços..."
    kill $API_PID $JUPYTER_PID 2>/dev/null
    docker stop mysql-imobiliaria 2>/dev/null
    docker rm mysql-imobiliaria 2>/dev/null
    exit
}

# Capturar Ctrl+C
trap cleanup SIGINT

# Manter script rodando
wait
"""
    
    with open("start_all.sh", "w") as f:
        f.write(unix_script)
    
    # Tornar executável no Unix
    if platform.system() != "Windows":
        os.chmod("start_all.sh", 0o755)
    
    print("   ✅ Scripts de inicialização criados")

def main():
    """Função principal"""
    print_banner()
    
    # Verificações iniciais
    if not check_python_version():
        return False
    
    # Instalação de dependências
    if not install_requirements():
        print("❌ Falha na instalação de dependências")
        return False
    
    # Configuração do projeto
    create_directories()
    create_env_file()
    setup_git()
    create_gitignore()
    create_startup_scripts()
    
    # Mensagem final
    print("\n" + "="*60)
    print("🎉 CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)
    print("\n📋 Próximos passos:")
    print("1. Edite o arquivo .env com suas configurações")
    print("2. Execute o script de inicialização:")
    if platform.system() == "Windows":
        print("   start_all.bat")
    else:
        print("   ./start_all.sh")
    print("3. Acesse:")
    print("   📝 API: http://localhost:8000")
    print("   📊 JupyterLab: http://localhost:8888")
    print("   🔑 Token: imobiliaria123")
    print("\n📚 Documentação:")
    print("   README.md - Documentação principal")
    print("   README_JUPYTER.md - Documentação do JupyterLab")
    print("   HELP.md - Ajuda e troubleshooting")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
