# 🏢 Imobiliária 3 Irmãos

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-005571?logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-20.10+-2496ED?logo=docker&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626?logo=jupyter&logoColor=white)

Sistema completo de gestão imobiliária com API REST, análise de dados e interface web.

## 📋 Sobre o Projeto

O sistema Imobiliária 3 Irmãos é uma solução completa para gerenciamento de imóveis, clientes, corretores e contratos. Desenvolvido com arquitetura moderna e boas práticas de programação, oferece:

- **API REST** com FastAPI para operações CRUD
- **Análise de dados** com JupyterLab
- **Banco de dados** SQLite (facilmente migrável para MySQL/PostgreSQL)
- **Containerização** com Docker
- **Interface web** responsiva

## 🚀 Funcionalidades

- ✅ Cadastro e gerenciamento de imóveis
- ✅ Cadastro e gestão de clientes/usuários
- ✅ Gerenciamento de corretores
- ✅ Contratos de aluguel e venda
- ✅ Agendamento de visitas
- ✅ Relatórios e análises de dados
- ✅ API documentada com Swagger/OpenAPI

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.10+, FastAPI, SQLAlchemy, Pydantic
- **Banco de dados**: SQLite (produção), MySQL (opcional)
- **Análise de dados**: JupyterLab, Pandas, Matplotlib, Plotly
- **Frontend**: HTML5, CSS3, JavaScript
- **Containerização**: Docker, Docker Compose
- **Documentação**: Swagger/OpenAPI

## 📂 Estrutura do Projeto

```
Imobiliaria-3-irmaos/
├── 📁 routers/                # Rotas da API organizadas por recurso
├── 📁 templates/              # Templates HTML
├── 📁 notebooks/              # Notebooks Jupyter para análise
├── 📁 data/                   # Dados para análise
├── 📁 reports/                # Relatórios gerados
├── 📄 main.py                 # Aplicação FastAPI principal
├── 📄 models.py               # Modelos SQLAlchemy (ORM)
├── 📄 schemas.py              # Schemas Pydantic para validação
├── 📄 database.py             # Configuração do banco de dados
├── 📄 requirements.txt        # Dependências do projeto
├── 📄 Dockerfile              # Configuração Docker da API
├── 📄 docker-compose.yml      # Orquestração de containers
└── 📄 README.md               # Este arquivo
```

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python 3.10+
- pip (gerenciador de pacotes Python)
- Docker e Docker Compose (opcional)

### Instalação Manual

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/Imobiliaria-3-irmaos.git
   cd Imobiliaria-3-irmaos
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicie a API**
   ```bash
   python start_api.py
   ```
   A API estará disponível em: http://localhost:8000
   Documentação Swagger: http://localhost:8000/docs

4. **Para análise de dados (opcional)**
   ```bash
   pip install -r requirements_jupyter.txt
   python start_jupyter.py
   ```
   O JupyterLab estará disponível em: http://localhost:8888

### Usando Docker

1. **Inicie todos os serviços**
   ```bash
   docker-compose up
   ```

2. **Apenas a API**
   ```bash
   docker-compose up api
   ```

3. **Apenas o JupyterLab**
   ```bash
   docker-compose -f docker-compose.jupyter.yml up
   ```

## 📊 Análise de Dados

O projeto inclui notebooks Jupyter para análise de dados imobiliários:

- **imobiliaria_analysis.ipynb**: Análise exploratória completa
- **relatorios_imobiliaria.ipynb**: Relatórios executivos e visualizações

Para acessar:
1. Inicie o JupyterLab conforme instruções acima
2. Acesse http://localhost:8888
3. Use o token: `imobiliaria123`

## 📚 API Endpoints

A API segue princípios RESTful com os seguintes endpoints principais:

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | /imoveis/ | Lista todos os imóveis |
| POST   | /imoveis/ | Cadastra novo imóvel |
| GET    | /imoveis/{id} | Detalhes de um imóvel |
| PUT    | /imoveis/{id} | Atualiza um imóvel |
| DELETE | /imoveis/{id} | Remove um imóvel |
| GET    | /usuarios/ | Lista todos os usuários |
| POST   | /visitas/ | Agenda uma visita |
| GET    | /contratos/ | Lista contratos |

Para documentação completa, acesse a interface Swagger em `/docs`.

## 🧪 Testes

Execute os testes automatizados com:

```bash
python -m pytest
```

Ou teste componentes específicos:

```bash
python test_api.py
python test_visita.py
```

## 🔧 Correções Recentes

- ✅ Corrigido o processamento de datas e horas nas visitas
- ✅ Melhorada a validação de dados nos formulários
- ✅ Otimizado o desempenho das consultas ao banco de dados
- ✅ Corrigidos problemas de codificação em caracteres especiais

## 👨‍💻 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato:
- Email: contato@imobiliaria3irmaos.com
- Website: www.imobiliaria3irmaos.com

---

Desenvolvido com ❤️ pela equipe Imobiliária 3 Irmãos


