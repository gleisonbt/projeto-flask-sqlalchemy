CREATE DATABASE IF NOT EXISTS escola_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE escola_db;

CREATE TABLE IF NOT EXISTS professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    disciplina VARCHAR(100) NOT NULL,
    ativo TINYINT(1) NOT NULL DEFAULT 1
);

INSERT INTO professores (nome, email, disciplina, ativo) VALUES
('Ana Silva', 'ana.silva@escola.com', 'Banco de Dados', 1),
('Carlos Souza', 'carlos.souza@escola.com', 'Projeto de Software', 1),
('Marina Costa', 'marina.costa@escola.com', 'Banco de Dados', 1),
('João Pereira', 'joao.pereira@escola.com', 'Projeto de Software', 0);

DROP PROCEDURE IF EXISTS sp_professores_por_disciplina;

DELIMITER //
CREATE PROCEDURE sp_professores_por_disciplina(
    IN p_disciplina VARCHAR(100)
)
BEGIN
    SELECT id, nome, email, disciplina, ativo
    FROM professores
    WHERE disciplina = p_disciplina
      AND ativo = 1
    ORDER BY nome;
END //
DELIMITER ;
