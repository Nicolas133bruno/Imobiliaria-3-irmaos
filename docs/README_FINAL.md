# 🏠 Imobiliária 3 Irmãos - Projeto Completo

## 🎯 Visão Geral

Este é um projeto completo de sistema imobiliário desenvolvido com as melhores práticas de desenvolvimento sênior, incluindo:

- **FastAPI** para API REST
- **MySQL** para banco de dados
- **JupyterLab** para análise de dados
- **Docker** para containerização
- **Análise de dados** com pandas, plotly e matplotlib

## 📁 Estrutura do Projeto

```
Imobiliaria-3-irmaos-main/
├── 📊 NOTEBOOKS JUPYTERLAB
│   ├── imobiliaria_analysis.ipynb      # Notebook principal de análise
│   └── relatorios_imobiliaria.ipynb    # Notebook de relatórios executivos
│
├── 🚀 SCRIPTS DE CONFIGURAÇÃO
│   ├── init_project.py                 # Inicialização completa do projeto
│   ├── setup_jupyter.py               # Setup específico do JupyterLab
│   ├── test_setup.py                  # Testes de validação
│   ├── start_jupyter.bat/.sh          # Scripts de inicialização
│   └── start_all.bat/.sh              # Inicia todos os serviços
│
├── 🐳 DOCKER
│   ├── Dockerfile                      # Container da API
│   ├── Dockerfile.jupyter              # Container do JupyterLab
│   ├── docker-compose.yml              # Compose da API
│   └── docker-compose.jupyter.yml      # Compose completo
│
├── 📦 DEPENDÊNCIAS
│   ├── requirements.txt                # Dependências da API
│   └── requirements_jupyter.txt        # Dependências do JupyterLab
│
├── ⚙️ CONFIGURAÇÃO
│   ├── config.env                      # Variáveis de ambiente
│   ├── database.py                     # Configuração do banco
│   ├── models.py                       # Modelos SQLAlchemy
│   ├── schemas.py                      # Schemas Pydantic
│   └── main.py                         # Aplicação FastAPI
│
├── 📚 DOCUMENTAÇÃO
│   ├── README.md                       # Documentação principal
│   ├── README_JUPYTER.md               # Documentação JupyterLab
│   ├── README_FINAL.md                 # Este arquivo
│   ├── INSTRUCOES_USO.md               # Instruções de uso
│   └── HELP.md                         # Ajuda e troubleshooting
│
└── 🗄️ BANCO DE DADOS
    └── A empresa Imobilária 3irmãos.sql # Script SQL do banco
```

## 🚀 Início Rápido

### 1. Configuração Automática
```bash
# Execute o script de inicialização
python init_project.py
```

### 2. Teste a Configuração
```bash
# Valide se tudo está funcionando
python test_setup.py
```

### 3. Inicie Todos os Serviços
```bash
# Windows
start_all.bat

# Linux/Mac
./start_all.sh
```

### 4. Acesse os Serviços
- **API**: http://localhost:8000
- **Documentação API**: http://localhost:8000/docs
- **JupyterLab**: http://localhost:8888
- **Token JupyterLab**: `imobiliaria123`

## 📊 Funcionalidades dos Notebooks

### Notebook Principal (`imobiliaria_analysis.ipynb`)

#### 🔗 Conexão com MySQL
- Teste de conectividade
- Configuração SQLAlchemy
- Carregamento de dados
- Validação de integridade

#### 📈 Análise de Dados
- Análise exploratória
- Estatísticas descritivas
- Validação de dados
- Relatórios de qualidade

#### 🌐 Integração com API
- Cliente HTTP completo
- Operações CRUD
- Testes de endpoints
- Tratamento de erros

#### 📊 Visualizações
- Dashboards interativos
- Gráficos com Plotly
- Relatórios de performance
- Análise de tendências

#### 🧪 Testes e Validações
- Testes de integridade
- Validação de API
- Relatórios de qualidade

### Notebook de Relatórios (`relatorios_imobiliaria.ipynb`)

#### 📈 Análise de Performance
- Performance de corretores
- Análise de vendas
- Métricas de conversão
- KPIs principais

#### 📊 Dashboards Executivos
- Relatórios executivos
- Tendências de mercado
- Análise comparativa
- Previsões

## 🛠️ Desenvolvimento

### Configuração do Ambiente

#### 1. Python 3.8+
```bash
python --version  # Deve ser 3.8 ou superior
```

#### 2. Dependências
```bash
# API
pip install -r requirements.txt

# JupyterLab
pip install -r requirements_jupyter.txt
```

#### 3. Banco de Dados
- **MySQL 8.0+** recomendado
- **SQLite** como fallback
- Configuração em `config.env`

### Estrutura da API

#### Endpoints Principais
- `GET /` - Status da API
- `GET /docs` - Documentação Swagger
- `GET /usuarios/` - Listar usuários
- `GET /imoveis/` - Listar imóveis
- `GET /corretores/` - Listar corretores
- `GET /visitas/` - Listar visitas
- `GET /contratos/` - Listar contratos

#### Modelos de Dados
- **Usuario** - Dados dos usuários
- **Imovel** - Propriedades
- **Corretor** - Corretores
- **Visita** - Agendamentos
- **Contrato** - Aluguéis e vendas

### Análise de Dados

#### Bibliotecas Utilizadas
- **pandas** - Manipulação de dados
- **numpy** - Computação numérica
- **matplotlib** - Gráficos estáticos
- **seaborn** - Visualizações estatísticas
- **plotly** - Gráficos interativos

#### Tipos de Análise
- Análise exploratória
- Estatísticas descritivas
- Visualizações interativas
- Relatórios executivos
- Análise de tendências

## 🐳 Docker

### Container da API
```bash
docker build -t imobiliaria-api .
docker run -p 8000:8000 imobiliaria-api
```

### Container do JupyterLab
```bash
docker build -f Dockerfile.jupyter -t imobiliaria-jupyter .
docker run -p 8888:8888 imobiliaria-jupyter
```

### Compose Completo
```bash
docker-compose -f docker-compose.jupyter.yml up
```

## 📈 Exemplos de Uso

### 1. Análise de Usuários
```python
# No notebook
usuarios = api_client.get_usuarios(limit=100)
usuarios_df = pd.DataFrame(usuarios['items'])
print(f"Total de usuários: {len(usuarios_df)}")
```

### 2. Análise de Imóveis
```python
# No notebook
imoveis = api_client.get_imoveis(limit=100)
imoveis_df = pd.DataFrame(imoveis['items'])
preco_medio = imoveis_df['valor'].mean()
print(f"Preço médio: R$ {preco_medio:,.2f}")
```

### 3. Relatório de Performance
```python
# No notebook
report = generate_performance_report()
print(f"Valor total do portfólio: R$ {report['summary']['valor_total_portfolio']:,.2f}")
```

## 🔍 Troubleshooting

### Problemas Comuns

#### 1. Erro de Conexão MySQL
```
❌ Erro ao conectar com MySQL: Access denied
```
**Solução:**
- Verifique as credenciais em `config.env`
- Certifique-se de que o MySQL está rodando
- Teste: `mysql -u root -p`

#### 2. API não Responde
```
❌ Erro ao conectar com API: Connection refused
```
**Solução:**
- Verifique se a API está rodando na porta 8000
- Execute: `uvicorn main:app --reload --port=8000`
- Teste: `curl http://localhost:8000/`

#### 3. JupyterLab não Inicia
```
❌ JupyterLab não encontrado
```
**Solução:**
- Instale: `pip install jupyterlab`
- Verifique: `jupyter --version`
- Reinstale: `pip install -r requirements_jupyter.txt`

#### 4. Dependências Faltando
```
❌ ModuleNotFoundError: No module named 'plotly'
```
**Solução:**
- Instale: `pip install plotly`
- Ou reinstale tudo: `pip install -r requirements_jupyter.txt`

### Logs e Debug
- Ative debug em `config.env`: `DEBUG=True`
- Verifique logs no terminal
- Use `print()` para debug nos notebooks

## 🎯 Próximos Passos

### Melhorias Planejadas
- [ ] Autenticação JWT
- [ ] Cache Redis
- [ ] Machine Learning para previsões
- [ ] Integração com BI tools
- [ ] Relatórios automatizados
- [ ] API de upload de imagens
- [ ] Sistema de notificações
- [ ] Dashboard web

### Contribuições
1. Fork o projeto
2. Crie uma branch para sua feature
3. Implemente e teste
4. Abra um Pull Request

## 📞 Suporte

### Recursos de Ajuda
- 📖 `README.md` - Documentação principal
- 📊 `README_JUPYTER.md` - Documentação JupyterLab
- 🆘 `HELP.md` - Ajuda e troubleshooting
- 📝 API Docs - http://localhost:8000/docs

### Comandos Úteis
```bash
# Testar configuração
python test_setup.py

# Inicializar projeto
python init_project.py

# Iniciar JupyterLab
jupyter lab --ip=127.0.0.1 --port=8888

# Iniciar API
uvicorn main:app --reload --port=8000

# Instalar dependências
pip install -r requirements_jupyter.txt
```

## 🏆 Desenvolvido como Dev Sênior

Este projeto demonstra as melhores práticas de desenvolvimento sênior:

### ✅ Qualidade de Código
- Código limpo e bem documentado
- Tratamento robusto de erros
- Configuração flexível e segura
- Testes automatizados

### ✅ Arquitetura
- Separação de responsabilidades
- Configuração por ambiente
- Containerização com Docker
- Estrutura escalável

### ✅ Documentação
- Documentação completa
- Exemplos práticos
- Troubleshooting detalhado
- Instruções passo a passo

### ✅ Ferramentas
- FastAPI para API moderna
- SQLAlchemy para ORM
- JupyterLab para análise
- Docker para deployment

---

**Desenvolvido com ❤️ para a Imobiliária 3 Irmãos**

*Este projeto está pronto para uso em produção e pode ser facilmente adaptado para diferentes necessidades.*
