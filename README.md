# Sistema de Gerenciamento Acadêmico - Pojeto de API RESTful

Este projeto consiste no desevolvimento de uma API RESTful para gerenciamento dos dados. A aplicação permite a criação, leitura, atualização e exclusão (CRUD) das entidades principais, além da associação entre alunos e cursos por meio do conceito de matrícula.

------

## Integrantes

- Ana Carolina (Matrícula: 03349047)
- Alana Alexia (Matrícula: 03348970)

------

## Objetivo

O objetivo deste projeto é colocar em prática e avaliar os conhecimentos que aprendemos durante as aulas, especialmente sobre como criar APIs RESTful e usar JSON para comunicação. Com esse SOFTWARE, queremos entender melhor como aplicar esses conceitos na prática, fazendo operações básicas de cadastro, consulta, atualização e exclusão de dados, além de trabalhar com o relacionamento entre alunos e cursos.

------

## Tecnologias Utilizadas

- Python
- Flask
- MySQL
- PyMySQL

------

## Estrutura do Banco de Dados

- **alunos**: Armazena os dados dos alunos (id, nome, email).  
- **cursos**: Armazena os dados dos cursos (id, título, descrição).  
- **matricula**: Relação entre alunos e cursos, registrando as matrículas.

## Configuração da API

Ajuste as variáveis de conexão com o banco MySQL de acordo com sua máquina

*db_host = 'localhost'*         # Host do servidor MySQL
*db_user = 'root'*              # Usuário MySQL
*db_password = 'sua_senha'*     # Senha do usuário MySQL
*db_nome = 'facul'*             # Nome do banco de dados criado
