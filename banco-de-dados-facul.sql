-- Criando Database:
CREATE DATABASE facul;
-- Usando a Database:
USE facul;

-- Criando a tabela Alunos:
CREATE TABLE alunos (
idAluno INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL UNIQUE
);

-- Criando a tabela Cursos:
CREATE TABLE cursos (
idCurso INT PRIMARY KEY AUTO_INCREMENT,
titulo VARCHAR(50) NOT NULL,
descricao TEXT
);

-- Criando a tabela Matricula:
CREATE TABLE matricula (
idMatricula INT PRIMARY KEY AUTO_INCREMENT,
idAluno_FK INT NOT NULL,
idCurso_FK INT NOT NULL,
FOREIGN KEY (idAluno_FK) REFERENCES alunos (idAluno) ON DELETE CASCADE,
FOREIGN KEY (idCurso_FK) REFERENCES cursos (idCurso) ON DELETE CASCADE
);

select * from cursos;

