@echo off
echo 🚀 Iniciando JupyterLab para Imobiliária 3 Irmãos
echo ================================================

REM Verificar se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado! Instale o Python primeiro.
    pause
    exit /b 1
)

REM Verificar se os requisitos estão instalados
echo 🔍 Verificando dependências...
pip show jupyterlab >nul 2>&1
if errorlevel 1 (
    echo ⚠️ JupyterLab não encontrado. Instalando dependências...
    pip install -r requirements_jupyter.txt
)

REM Criar diretório de trabalho se não existir
if not exist "notebooks" mkdir notebooks
if not exist "data" mkdir data
if not exist "reports" mkdir reports

REM Iniciar JupyterLab
echo 🎯 Iniciando JupyterLab...
echo 📝 Acesse: http://localhost:8888
echo 🔑 Token será exibido abaixo
echo.
echo ⚠️ Para parar o servidor, pressione Ctrl+C
echo.

jupyter lab --ip=127.0.0.1 --port=8888 --no-browser --allow-root

pause
