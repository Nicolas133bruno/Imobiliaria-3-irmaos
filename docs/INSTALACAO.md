# 🚀 Guia de Instalação - Imobiliária 3 Irmãos

## ⚡ Instalação Rápida

### 1. Instalar Dependências
```bash
# Instalar todas as dependências
python install_dependencies.py
```

### 2. Validar Instalação
```bash
# Testar se tudo está funcionando
python test_simple.py
```

### 3. Configurar Projeto
```bash
# Configuração automática
python init_project.py
```

### 4. Iniciar Serviços
```bash
# Windows
start_all.bat

# Linux/Mac
./start_all.sh
```

## 📋 Pré-requisitos

### Sistema Operacional
- **Windows 10/11** ou **Linux** ou **macOS**
- **Python 3.8+** (recomendado 3.11+)

### Software Necessário
- **Python 3.8+** com pip
- **MySQL 8.0+** (opcional, SQLite como fallback)
- **Git** (opcional, para controle de versão)

## 🔧 Instalação Detalhada

### 1. Verificar Python
```bash
python --version
# Deve mostrar Python 3.8 ou superior
```

### 2. Instalar Dependências
```bash
# Método 1: Script automático
python install_dependencies.py

# Método 2: Manual
pip install -r requirements.txt
pip install -r requirements_jupyter.txt
```

### 3. Configurar Banco de Dados

#### Opção A: MySQL (Recomendado)
1. Instale o MySQL 8.0+
2. Crie o banco de dados:
```sql
CREATE DATABASE imobiliaria_3_irmaos;
```
3. Configure as credenciais em `config.env`

#### Opção B: SQLite (Fallback)
- O sistema usará SQLite automaticamente se MySQL não estiver disponível

### 4. Configurar Variáveis de Ambiente
Edite o arquivo `config.env`:
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_NAME=imobiliaria_3_irmaos
```

### 5. Testar Configuração
```bash
python test_simple.py
```

## 🐳 Instalação com Docker

### 1. Instalar Docker
- Baixe e instale o Docker Desktop
- Certifique-se de que está rodando

### 2. Executar com Docker Compose
```bash
# Iniciar todos os serviços
docker-compose -f docker-compose.jupyter.yml up

# Ou apenas a API
docker-compose up
```

## 🚀 Iniciar o Projeto

### Método 1: Script Automático
```bash
# Windows
start_all.bat

# Linux/Mac
./start_all.sh
```

### Método 2: Manual
```bash
# Terminal 1: API
uvicorn main:app --reload --port=8000

# Terminal 2: JupyterLab
jupyter lab --ip=127.0.0.1 --port=8888
```

## 📊 Acessar os Serviços

Após iniciar, acesse:

- **API**: http://localhost:8000
- **Documentação API**: http://localhost:8000/docs
- **JupyterLab**: http://localhost:8888
- **Token JupyterLab**: `imobiliaria123`

## 🔍 Troubleshooting

### Problema: Dependências não instalam
```bash
# Atualizar pip
python -m pip install --upgrade pip

# Instalar manualmente
pip install fastapi uvicorn sqlalchemy pandas numpy matplotlib seaborn plotly requests mysql-connector-python python-dotenv
```

### Problema: MySQL não conecta
1. Verifique se o MySQL está rodando
2. Confirme as credenciais em `config.env`
3. Teste a conexão:
```bash
mysql -u root -p
```

### Problema: Porta já em uso
```bash
# Encontrar processo usando a porta
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # Linux/Mac

# Matar processo
taskkill /PID <PID> /F        # Windows
kill -9 <PID>                 # Linux/Mac
```

### Problema: JupyterLab não inicia
```bash
# Reinstalar JupyterLab
pip uninstall jupyterlab
pip install jupyterlab

# Ou usar conda
conda install jupyterlab
```

## ✅ Validação da Instalação

### 1. Teste de Dependências
```bash
python test_simple.py
```

### 2. Teste da API
```bash
curl http://localhost:8000/
```

### 3. Teste do JupyterLab
- Acesse http://localhost:8888
- Deve abrir a interface do JupyterLab

### 4. Teste dos Notebooks
- Abra `imobiliaria_analysis.ipynb`
- Execute a primeira célula
- Deve importar todas as bibliotecas sem erro

## 📚 Próximos Passos

Após a instalação bem-sucedida:

1. **Explore os Notebooks**:
   - `imobiliaria_analysis.ipynb` - Análise principal
   - `relatorios_imobiliaria.ipynb` - Relatórios executivos

2. **Use a API**:
   - Documentação em http://localhost:8000/docs
   - Teste os endpoints

3. **Configure o Banco**:
   - Importe o arquivo SQL se necessário
   - Adicione dados de teste

4. **Desenvolva**:
   - Adicione novos endpoints
   - Crie novos notebooks
   - Implemente funcionalidades

## 🆘 Suporte

Se encontrar problemas:

1. **Verifique os logs** no terminal
2. **Consulte a documentação** em `README_FINAL.md`
3. **Execute os testes** com `python test_simple.py`
4. **Verifique as configurações** em `config.env`

---

**Instalação concluída com sucesso! 🎉**

*O projeto está pronto para uso e desenvolvimento.*
