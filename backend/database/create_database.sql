CREATE DATABASE IF NOT EXISTS escola_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE escola_db;

CREATE TABLE IF NOT EXISTS professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    disciplina VARCHAR(100) NOT NULL
);

INSERT INTO professores (nome, email, disciplina) VALUES
('Ana Silva', 'ana.silva@escola.com', 'Banco de Dados'),
('Carlos Souza', 'carlos.souza@escola.com', 'Projeto de Software');
