# 🏠 JupyterLab - Imobiliária 3 Irmãos

Este projeto inclui notebooks JupyterLab para análise de dados, integração com API e geração de relatórios para a Imobiliária 3 Irmãos.

## 📋 Arquivos Incluídos

### Notebooks
- `imobiliaria_analysis.ipynb` - Notebook principal com análise completa
- `relatorios_imobiliaria.ipynb` - Notebook focado em relatórios executivos

### Scripts de Configuração
- `setup_jupyter.py` - Script de configuração automática
- `start_jupyter.bat` - Script para Windows
- `start_jupyter.sh` - Script para Linux/Mac
- `requirements_jupyter.txt` - Dependências específicas do JupyterLab

## 🚀 Instalação Rápida

### Windows
```bash
# 1. Execute o script de configuração
python setup_jupyter.py

# 2. Inicie o JupyterLab
start_jupyter.bat
```

### Linux/Mac
```bash
# 1. Execute o script de configuração
python3 setup_jupyter.py

# 2. Inicie o JupyterLab
./start_jupyter.sh
```

### Manual
```bash
# 1. Instalar dependências
pip install -r requirements_jupyter.txt

# 2. Iniciar JupyterLab
jupyter lab --ip=127.0.0.1 --port=8888
```

## 🔧 Configuração

### 1. Configurar Banco de Dados
Edite o arquivo `.env` criado pelo script de configuração:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_NAME=imobiliaria_3_irmaos
```

### 2. Configurar API
Certifique-se de que a API FastAPI está rodando:

```bash
# No diretório do projeto
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📊 Funcionalidades dos Notebooks

### Notebook Principal (`imobiliaria_analysis.ipynb`)

#### 🔗 Conexão com MySQL
- Teste de conectividade
- Configuração SQLAlchemy
- Validação de dados

#### 📈 Análise de Dados
- Carregamento de dados
- Análise exploratória
- Validação de integridade

#### 🌐 Integração com API
- Cliente HTTP para FastAPI
- Testes de endpoints
- Operações CRUD

#### 📊 Visualizações
- Dashboards interativos
- Gráficos com Plotly
- Relatórios de performance

#### 🧪 Testes e Validações
- Testes de integridade
- Validação de API
- Relatórios de qualidade

### Notebook de Relatórios (`relatorios_imobiliaria.ipynb`)

#### 📈 Análise de Performance
- Performance de corretores
- Análise de vendas
- Métricas de conversão

#### 📊 Dashboards Executivos
- KPIs principais
- Tendências de mercado
- Análise comparativa

#### 🔮 Previsões
- Análise de tendências
- Projeções de vendas
- Análise sazonal

## 🛠️ Desenvolvimento

### Estrutura de Pastas
```
├── notebooks/           # Notebooks adicionais
├── data/               # Dados exportados
├── reports/            # Relatórios gerados
├── imobiliaria_analysis.ipynb
├── relatorios_imobiliaria.ipynb
└── requirements_jupyter.txt
```

### Extensões Recomendadas
- `jupyterlab-git` - Controle de versão
- `jupyterlab-lsp` - Language Server Protocol
- `jupyterlab-code-formatter` - Formatação de código

## 📚 Exemplos de Uso

### 1. Análise de Usuários
```python
# Carregar dados de usuários
usuarios = api_client.get_usuarios(limit=100)

# Análise por perfil
usuarios_df = pd.DataFrame(usuarios['items'])
perfil_analysis = usuarios_df.groupby('fk_perfil_id').size()
```

### 2. Análise de Imóveis
```python
# Carregar dados de imóveis
imoveis = api_client.get_imoveis(limit=100)

# Análise de preços
imoveis_df = pd.DataFrame(imoveis['items'])
preco_medio = imoveis_df.groupby('tipo')['valor'].mean()
```

### 3. Relatório de Performance
```python
# Gerar relatório
report = generate_performance_report()
print(f"Total de usuários: {report['summary']['total_usuarios']}")
print(f"Valor total do portfólio: R$ {report['summary']['valor_total_portfolio']:,.2f}")
```

## 🔍 Troubleshooting

### Problemas Comuns

#### 1. Erro de Conexão MySQL
```
❌ Erro ao conectar com MySQL: Access denied
```
**Solução:** Verifique as credenciais no arquivo `.env`

#### 2. API não Responde
```
❌ Erro ao conectar com API: Connection refused
```
**Solução:** Certifique-se de que a API está rodando na porta 8000

#### 3. Dependências Faltando
```
❌ ModuleNotFoundError: No module named 'plotly'
```
**Solução:** Execute `pip install -r requirements_jupyter.txt`

### Logs e Debug
- Ative o modo debug no arquivo `.env`: `DEBUG=True`
- Verifique os logs do JupyterLab no terminal
- Use `print()` para debug nos notebooks

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique este README
2. Consulte a documentação da API: `http://localhost:8000/docs`
3. Verifique os logs de erro
4. Teste a conectividade com banco e API

## 🎯 Próximos Passos

### Melhorias Planejadas
- [ ] Autenticação JWT nos notebooks
- [ ] Cache Redis para performance
- [ ] Relatórios automatizados
- [ ] Integração com BI tools
- [ ] Machine Learning para previsões

### Contribuições
1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

---

**Desenvolvido com ❤️ para a Imobiliária 3 Irmãos**
