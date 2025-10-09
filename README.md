# 🏢 Sistema Imobiliária 3 Irmãos

![Java](https://img.shields.io/badge/Java-ED8B00?logo=java\&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql\&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?logo=spring\&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker\&logoColor=white)

**Autores:** Felipe Marques, Nicolas Bruno, Heitor Moreira
**Instituição:** IFTM – Uberlândia, MG
**Disciplina/Trabalho Acadêmico:** Desenvolvimento de Sistemas / Projeto de Sistema de Gestão Imobiliária

---

## 📖 Descrição do Projeto

O Sistema Imobiliária 3 Irmãos é uma aplicação desktop/web voltada para **gerenciamento completo de uma imobiliária**, permitindo:

* Cadastro de imóveis, locatários e contratos
* Controle de locações e pagamentos
* Emissão de relatórios financeiros
* Administração de usuários e permissões

O projeto foi desenvolvido como trabalho acadêmico, com foco em **Boas Práticas de Desenvolvimento, Padrões de Projeto e Persistência de Dados com MySQL**.

---

## 🛠 Tecnologias Utilizadas

| Tecnologia  | Uso no projeto                            |
| ----------- | ----------------------------------------- |
| Java        | Linguagem principal                       |
| Spring Boot | Framework para desenvolvimento do backend |
| MySQL       | Banco de dados relacional                 |
| Maven       | Gerenciamento de dependências             |
| Docker      | Containerização do ambiente               |
| HTML/CSS/JS | Interface administrativa (caso Web)       |

---

## 📂 Estrutura do Projeto

```
Imobiliaria-3-irmaos/
│
├─ src/
│   ├─ main/
│   │   ├─ java/            # Código-fonte Java
│   │   └─ resources/       # Configurações, templates, SQL
│   └─ test/                # Testes unitários e de integração
├─ docker/                  # Arquivos para Docker e Docker Compose
├─ pom.xml                  # Configuração Maven
└─ README.md
```

Principais pacotes:

* `domain` — Entidades do sistema (Imóvel, Usuário, Perfil, Contrato)
* `repository` — Interfaces de acesso ao banco de dados
* `controller` — Classes REST/Controllers para gerenciar rotas
* `service` — Regras de negócio

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* JDK 11 ou superior
* Maven
* MySQL
* Docker (opcional, para ambiente isolado)

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/Nicolas133bruno/Imobiliaria-3-irmaos.git
cd Imobiliaria-3-irmaos
```

### Passo 2: Configurar o Banco de Dados

1. Crie um banco de dados chamado `Imobiliaria` no MySQL
2. Importe o arquivo SQL `A empresa Imobilária 3irmãos.sql`

```sql
CREATE DATABASE Imobiliaria;
USE Imobiliaria;
-- Execute o script SQL disponível
```

3. Configure as variáveis de ambiente no `.env` ou no `application.properties`:

```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=Imobiliaria
DB_USER=root
DB_PASS=senha
```

### Passo 3: Executar o Projeto

Com Maven:

```bash
./mvnw clean install
./mvnw spring-boot:run
```

Com Docker Compose:

```bash
docker-compose up --build
```

Acesse o sistema em: `http://localhost:8080` (caso Web)

---

## 🧪 Testes

Para rodar os testes unitários e de integração:

```bash
./mvnw test
```

---

## 📄 Funcionalidades

* Cadastro e gerenciamento de **Imóveis**
* Cadastro e gerenciamento de **Usuários e Perfis**
* Gestão de **Contratos de Locação**
* Relatórios financeiros detalhados
* Controle de permissões de acesso

---

## 📊 Próximas Melhorias

* Implementar autenticação JWT
* Painel web com dashboard interativo
* Integração com API de pagamento
* Backup automático do banco de dados

---

## 📬 Contato

* **Felipe Marques:** [GitHub](https://github.com/FelipeMarques)
* **Nicolas Bruno:** [GitHub](https://github.com/Nicolas133bruno)
* **Heitor Moreira:** [GitHub](https://github.com/HeitorMoreira)
