# Imobiliária 3 Irmãos - Sistema de Gerenciamento Imobiliário

**Autores:**  
Felipe Marques  
Nicolas Bruno  
Heitor Moreira

**Local:** Uberlândia, Minas Gerais  
**Ano:** 2025

---

## Sumário

1. Introdução  
2. Sistema de Gerenciamento Imobiliário  
3. Características do Sistema  
   - Objetivos  
   - Funcionalidades principais  
4. Logo  
5. Modelo Conceitual  
6. Modelo Lógico Relacional  
7. Modelo Lógico Reverso  
8. MySQL - Script do Banco de Dados  
9. Consultas (SELECT)  
10. Engenharia Reversa do MySQL  

---

## 1. Introdução

A Imobiliária 3 Irmãos é uma empresa inovadora no setor de intermediação imobiliária, criada para oferecer um serviço moderno, eficiente e confiável na compra, venda e aluguel de imóveis. Fundada por três empreendedores visionários, tem como compromisso transformar a experiência dos clientes com tecnologia e atendimento personalizado.

Com sede em Uberlândia, o sistema de gerenciamento imobiliário robusto baseado em banco de dados relacional permite controle total sobre clientes, corretores, imóveis, visitas e contratos, buscando transparência e satisfação nas negociações.

---

## 2. Sistema de Gerenciamento Imobiliário

Projeto de banco de dados relacional para organizar e controlar informações relacionadas à compra e venda de imóveis. Permite cadastro de clientes, corretores, imóveis, visitas e contratos, garantindo integridade e eficiência.

---

## 3. Características do Sistema

### Objetivos

- Armazenar dados de clientes, corretores, imóveis e contratos;  
- Registrar visitas e agendamentos;  
- Controlar informações contratuais;  
- Associar imóveis aos proprietários;  
- Estruturar banco de dados padronizado e normalizado.

### Funcionalidades principais

- Cadastro de Clientes;  
- Cadastro de Corretores;  
- Gerenciamento de Imóveis;  
- Controle de visitas e agendamentos;  
- Relacionamento entre entidades;  
- Sistema de relatórios e consultas;  
- Banco de dados padronizado.

---

## 4. Logo

<a href="https://imgbb.com/"><img src="https://i.ibb.co/67Ftgptv/Captura-de-tela-2025-07-04-215039-removebg-preview.png" alt="Captura-de-tela-2025-07-04-215039-removebg-preview" border="0"></a>

---

## 5. Modelo Conceitual

*(espaço reservado para o modelo conceitual)*

---

## 6. Modelo Lógico Relacional

**Tabelas principais e relacionamentos:**

- Perfil (id_perf, tipo)  
- Usuário (id_usuario, nome, cpf, telefone, email, sexo, data_nascimento, login_usu, senha_usu, id_perf)  
- Corretor (id_corretor, CRECI, id_usuario)  
- Status_Imovel (id_status, descricao_status)  
- Endereco (id_endereco, logradouro, numero, bairro, complemento, cidade, estado, cep)  
- Imovel (id_imovel, id_status, area_total, quartos, banheiros, vagas_garagem, valor_imovel, id_endereco, id_corretor)  
- Visita (id_visita, data_visita, hora_visita, status_visita, id_corretor, id_usuario, id_imovel)  
- Contrato_Aluguel (id_contrato_aluguel, tipo, data_inicio, data_fim, valor_mensalidade, id_usuario, id_imovel)  
- Contrato_Venda (id_contrato, tipo, data_inicio, data_fim, valor_negociado, id_usuario, id_imovel)

---

## 7. Modelo Lógico Reverso

*(espaço reservado para modelo lógico reverso)*

---

## 8. MySQL - Script do Banco de Dados

*(Inserir aqui o script completo para criação das tabelas e inserção de dados que você enviou.)*

---

## 9. Consultas (SELECT)

```sql
SELECT i.id_imovel, i.tipo, i.valor, s.descricao_status 
FROM Imovel i 
JOIN Status_Imovel s ON i.fk_id_status = s.id_status 
WHERE s.descricao_status = 'Disponível para venda';

## 10. Engenharia Reversa do MySQL

*(espaço reservado para documentação da engenharia reversa)*
