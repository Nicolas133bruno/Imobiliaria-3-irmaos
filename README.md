
# Sistema de Gerenciamento Imobiliário - Imobiliária 3 Irmãos

**Autores:** Felipe Marques, Nicolas Bruno, Heitor Moreira  
**Local:** Uberlândia, Minas Gerais  
**Ano:** 2025

---

## Sumário

1. Introdução  
2. Sistema de Gerenciamento Imobiliário  
3. Características do Sistema  
4. Logo  
5. Modelo Conceitual  
6. Modelo Lógico Relacional  
7. Modelo Lógico Reverso  
8. Scripts MySQL  
9. Consultas SQL  

---

## 1. Introdução

A Imobiliária 3 Irmãos é uma empresa inovadora no setor de intermediação imobiliária, criada com o propósito de oferecer um serviço moderno, eficiente e confiável na compra, venda e aluguel de imóveis. Fundada por três empreendedores visionários, a empresa nasce com o compromisso de transformar a experiência dos clientes por meio do uso inteligente da tecnologia e de um atendimento personalizado. Com sede em Uberlândia, a Imobiliária 3 Irmãos aposta em um sistema de gerenciamento imobiliário robusto, baseado em um banco de dados relacional, que permite o controle completo de informações fundamentais como cadastro de clientes, corretores, imóveis, agendamentos de visitas e contratos.

O objetivo é ser referência em qualidade e inovação no mercado imobiliário, promovendo a transparência nas negociações e a satisfação de todas as partes envolvidas. Acreditamos que, ao unir tecnologia, gestão eficiente e relacionamento humano, conseguimos construir uma empresa sólida e preparada para os desafios do setor. A Imobiliária 3 Irmãos não é apenas uma intermediadora de imóveis, mas uma parceira confiável na realização de sonhos e investimentos, sempre comprometida com a ética, a excelência e a evolução constante.

---

## 2. Sistema de Gerenciamento Imobiliário

O sistema de gerenciamento imobiliário é um projeto de banco de dados relacional desenvolvido com o objetivo de organizar e controlar informações relacionadas à compra e venda de imóveis. Ele permite o cadastro de clientes, corretores, imóveis, visitas e contratos de venda, além do acompanhamento de negociações realizadas.

Este sistema busca garantir a integridade dos dados armazenados e a eficiência no processo de intermediação imobiliária, contribuindo para o controle e registro das transações realizadas em uma imobiliária.

---

## 3. Características do Sistema

### Objetivos
- Armazenar dados de clientes, corretores, imóveis e contratos;
- Registrar visitas e agendamentos de imóveis;
- Controlar informações contratuais relacionadas às vendas;
- Associar corretamente cada imóvel ao seu respectivo proprietário;
- Fornecer uma estrutura padronizada e normalizada de banco de dados.

### Funcionalidades principais
- Cadastro de Clientes;
- Cadastro de Corretores;
- Gerenciamento de Imóveis;
- Controle de visitas e agendamento;
- Relacionamento entre Entidades;
- Sistema de Relatórios e Consultas.

---

## 4. Logo

![Logo da Imobiliária](imagens/Captura_de_tela_2025-07-04_215039-removebg-preview.png)

---

## 5. Modelo Conceitual

(Adicionar modelo conceitual)

---

## 6. Modelo Lógico Relacional

(Adicionar modelo lógico relacional)

---

## 7. Modelo Lógico Reverso

(Adicionar modelo lógico reverso)

---

## 8. Scripts MySQL

(Adicionar scripts MySQL do banco de dados)

---

## 9. Consultas SQL

Exemplo de consulta para listar imóveis disponíveis para venda:

```sql
SELECT i.id_imovel, i.tipo, i.valor, s.descricao_status
FROM Imovel i
JOIN Status_Imovel s ON i.fk_id_status = s.id_status
WHERE s.descricao_status = 'Disponível para venda';
```
