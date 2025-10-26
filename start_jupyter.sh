#!/bin/bash

echo "🚀 Iniciando JupyterLab para Imobiliária 3 Irmãos"
echo "================================================"

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado! Instale o Python primeiro."
    exit 1
fi

# Verificar se os requisitos estão instalados
echo "🔍 Verificando dependências..."
if ! pip3 show jupyterlab &> /dev/null; then
    echo "⚠️ JupyterLab não encontrado. Instalando dependências..."
    pip3 install -r requirements_jupyter.txt
fi

# Criar diretórios de trabalho se não existirem
mkdir -p notebooks data reports

# Iniciar JupyterLab
echo "🎯 Iniciando JupyterLab..."
echo "📝 Acesse: http://localhost:8888"
echo "🔑 Token será exibido abaixo"
echo ""
echo "⚠️ Para parar o servidor, pressione Ctrl+C"
echo ""

jupyter lab --ip=127.0.0.1 --port=8888 --no-browser --allow-root
