# CRUD Biblioteca com POO e PostgreSQL

Projeto desenvolvido em Python para praticar Programação Orientada a Objetos (POO) e integração com banco de dados PostgreSQL.

## Funcionalidades

### Usuários
- Cadastrar usuário
- Listar usuários
- Buscar usuário
- Atualizar usuário
- Remover usuário

### Livros
- Adicionar livro
- Listar livros
- Buscar livro
- Atualizar livro
- Remover livro

### Empréstimos
- Registrar empréstimo
- Listar empréstimos
- Buscar empréstimo
- Registrar devolução

## Conceitos aplicados

- Programação Orientada a Objetos (POO)
- Herança (`Pessoa -> Usuario`)
- Composição (`Emprestimo -> Usuario + Livro`)
- CRUD
- PostgreSQL
- Python + Psycopg2
- Separação em camadas (Models, Services, UI)
- Git e GitHub
- Variáveis de ambiente com `.env`

## Estrutura do projeto

```text
crud_biblioteca_poo/
│
├── database/
├── models/
├── services/
├── ui/
├── main.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Tecnologias utilizadas

- Python 3
- PostgreSQL
- Psycopg2
- Python-dotenv

## Objetivo

Projeto criado com foco em aprendizado de Programação Orientada a Objetos, persistência de dados com PostgreSQL e organização de projetos Python.