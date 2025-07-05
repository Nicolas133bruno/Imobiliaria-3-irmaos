
# Projeto Banco de Dados Imobiliária

## Descrição
Este projeto cria um banco de dados para uma imobiliária, com tabelas para perfis, usuários, corretores, imóveis, status, endereços, visitas e contratos (aluguel e venda).

## Estrutura das Tabelas

- **Perfil**: Tipos de perfil (Administrador, Corretor, Cliente).
- **Usuario**: Cadastro de usuários com informações pessoais.
- **Corretor**: Dados específicos dos corretores.
- **Status_Imovel**: Status dos imóveis (disponível, vendido, alugado, etc).
- **Endereco**: Endereços dos imóveis.
- **Imovel**: Informações dos imóveis.
- **Visita**: Registros de visitas aos imóveis.
- **Contrato_Aluguel**: Contratos de aluguel.
- **Contrato_Venda**: Contratos de venda.

## Como usar

1. Criar o banco de dados e tabelas usando o script SQL fornecido.
2. Inserir dados iniciais com os comandos INSERT fornecidos.
3. Executar consultas para gerar relatórios, utilizando operadores SQL como `=`, `<`, `>`, `>=`, `<=`, `IN`, `BETWEEN`, `LIKE`.

## Exemplo de consulta

```sql
SELECT i.id_imovel, i.tipo, i.valor, s.descricao_status
FROM Imovel i
JOIN Status_Imovel s ON i.fk_id_status = s.id_status
WHERE s.id_status IN (1, 3);
```

## Requisitos do projeto

- Criar relatórios usando operadores SQL.
- Pelo menos 1 relatório individual e 2 em grupo.

## Contato

Para dúvidas, entre em contato com o responsável pelo projeto.

---
