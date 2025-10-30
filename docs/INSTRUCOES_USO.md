# 🚀 Instruções de Uso - Imobiliária 3 Irmãos

## ⚡ Início Rápido

### 1. Configuração Automática
```bash
# Execute o script de inicialização
python init_project.py
```

### 2. Iniciar Todos os Serviços
```bash
# Windows
start_all.bat

# Linux/Mac
./start_all.sh
```

### 3. Acessar os Serviços
- **API**: http://localhost:8000
- **JupyterLab**: http://localhost:8888
- **Token JupyterLab**: `imobiliaria123`

## 📊 Usando o JupyterLab

### Notebook Principal
1. Abra `imobiliaria_analysis.ipynb`
2. Configure a conexão MySQL na célula 2
3. Execute as células sequencialmente
4. Explore os dados e análises

### Notebook de Relatórios
1. Abra `relatorios_imobiliaria.ipynb`
2. Execute para gerar relatórios executivos
3. Visualize dashboards interativos

## 🔧 Configurações Importantes

### Banco de Dados
- **Host**: localhost
- **Porta**: 3306
- **Usuário**: root
- **Senha**: root123 (padrão)
- **Database**: imobiliaria_3_irmaos

### API
- **URL**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **Timeout**: 30 segundos

## 📈 Funcionalidades Disponíveis

### Análise de Dados
- ✅ Conexão com MySQL
- ✅ Carregamento de dados
- ✅ Análise exploratória
- ✅ Validação de integridade

### Integração com API
- ✅ Cliente HTTP completo
- ✅ Operações CRUD
- ✅ Testes de endpoints
- ✅ Tratamento de erros

### Visualizações
- ✅ Dashboards interativos
- ✅ Gráficos com Plotly
- ✅ Relatórios de performance
- ✅ Análise de tendências

### Relatórios
- ✅ Performance de corretores
- ✅ Análise de vendas
- ✅ Métricas de negócio
- ✅ KPIs principais

## 🛠️ Desenvolvimento

### Estrutura de Arquivos
```
├── imobiliaria_analysis.ipynb      # Notebook principal
├── relatorios_imobiliaria.ipynb    # Notebook de relatórios
├── requirements_jupyter.txt         # Dependências JupyterLab
├── setup_jupyter.py                # Script de configuração
├── init_project.py                 # Inicialização completa
├── start_all.bat/.sh               # Scripts de inicialização
├── Dockerfile.jupyter              # Docker para JupyterLab
├── docker-compose.jupyter.yml      # Compose completo
└── README_JUPYTER.md               # Documentação detalhada
```

### Comandos Úteis
```bash
# Instalar dependências
pip install -r requirements_jupyter.txt

# Iniciar apenas JupyterLab
jupyter lab --ip=127.0.0.1 --port=8888

# Iniciar apenas API
uvicorn main:app --reload --port=8000

# Iniciar com Docker
docker-compose -f docker-compose.jupyter.yml up
```

## 🔍 Troubleshooting

### Problemas Comuns

#### 1. Erro de Conexão MySQL
```
❌ Erro ao conectar com MySQL: Access denied
```
**Solução:**
- Verifique se o MySQL está rodando
- Confirme as credenciais no arquivo `.env`
- Teste a conexão: `mysql -u root -p`

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
- Reinstale dependências: `pip install -r requirements_jupyter.txt`

#### 4. Dependências Faltando
```
❌ ModuleNotFoundError: No module named 'plotly'
```
**Solução:**
- Instale: `pip install plotly`
- Ou reinstale tudo: `pip install -r requirements_jupyter.txt`

### Logs e Debug
- Ative debug no `.env`: `DEBUG=True`
- Verifique logs no terminal
- Use `print()` para debug nos notebooks

## 📚 Exemplos Práticos

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

## 🎯 Próximos Passos

### Melhorias Sugeridas
1. **Autenticação**: Implementar JWT nos notebooks
2. **Cache**: Adicionar Redis para performance
3. **ML**: Implementar machine learning para previsões
4. **BI**: Integrar com ferramentas de BI
5. **Automation**: Automatizar relatórios

### Contribuições
1. Fork o projeto
2. Crie uma branch
3. Implemente sua feature
4. Teste completamente
5. Abra um Pull Request

## 📞 Suporte

### Recursos de Ajuda
- 📖 README.md - Documentação principal
- 📊 README_JUPYTER.md - Documentação JupyterLab
- 🆘 HELP.md - Ajuda e troubleshooting
- 📝 API Docs - http://localhost:8000/docs

### Contato
- 🐛 Issues: Use o sistema de issues do GitHub
- 💬 Discussões: Use as discussões do repositório
- 📧 Email: [seu-email@exemplo.com]

---

**Desenvolvido com ❤️ para a Imobiliária 3 Irmãos**

*Este projeto demonstra as melhores práticas de desenvolvimento sênior com Python, FastAPI, MySQL e JupyterLab.*
