# 🏢 Sistema Imobiliária 3 Irmãos

![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi\&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql\&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker\&logoColor=white)

Sistema de gestão para uma imobiliária, permitindo gerenciar imóveis, clientes, corretores e contratos de vendas ou aluguel.

O projeto é dividido em **backend (FastAPI + MySQL)** e **frontend simples (HTML, CSS, JS)**.

---

## 📂 Estrutura do Projeto

```
Imobiliaria-3-irmaos/
├── backend/
│   ├── main.py           # Arquivo principal da API
│   ├── models.py         # Models SQLAlchemy
│   ├── schemas.py        # Schemas Pydantic
│   ├── database.py       # Conexão com o banco
│   ├── routers/          # Rotas da API (Imóvel, Usuario, Contrato, etc.)
│   └── requirements.txt  # Dependências do Python
├── frontend/
│   ├── index.html        # Página inicial
│   ├── style.css         # Estilos
│   └── script.js         # Scripts JS
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* **Backend**: Python, FastAPI, SQLAlchemy
* **Banco de dados**: MySQL
* **Frontend**: HTML, CSS e JavaScript
* **Containerização**: Docker e Docker Compose

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/Nicolas133bruno/Imobiliaria-3-irmaos.git
cd Imobiliaria-3-irmaos
```

### 2️⃣ Configurar o Banco de Dados

* Crie um banco no MySQL chamado `imobiliaria`.
* Importe as tabelas e dados usando o script SQL fornecido (`imobiliaria.sql` se existir).

### 3️⃣ Rodar Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

### 4️⃣ Rodar Frontend

* Abra `frontend/index.html` em seu navegador.

### 5️⃣ Rodar via Docker (opcional)

```bash
docker-compose up --build
```

Isso vai subir o backend e o banco MySQL em containers.

---

## 📝 Funcionalidades

* **Cadastro e gerenciamento de imóveis**: tipo, localização, preço, status.
* **Cadastro de clientes**: informações pessoais e histórico de contratos.
* **Gerenciamento de contratos**: aluguel e venda, com datas e status.
* **Gestão de corretores**: registro de informações e comissões.
* **Relatórios**: estatísticas de imóveis, clientes e contratos.

---

## 🔗 Rotas Principais da API (exemplos)

* `GET /imovel/` → Listar todos os imóveis
* `POST /imovel/` → Criar um novo imóvel
* `GET /usuario/` → Listar todos os usuários
* `POST /contrato/` → Criar contrato de venda/aluguel
* `GET /relatorios/` → Gerar relatórios de contratos e imóveis

*(Todas as rotas estão documentadas automaticamente no Swagger em `/docs`)*

---

## 🤝 Contribuindo

1. Faça um fork deste repositório
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)
3. Faça commit das alterações (`git commit -m "Adiciona nova feature"`)
4. Faça push para sua branch (`git push origin minha-feature`)
5. Abra um Pull Request

---

## 📬 Contato

* **Felipe Marques:** [GitHub](https://github.com/Felipe-flp)
* **Nicolas Bruno:** [GitHub](https://github.com/Nicolas133bruno)
* **Heitor Moreira:** [GitHub](https://github.com/heitormoreira1)


