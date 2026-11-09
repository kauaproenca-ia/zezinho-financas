
CREATE DATABASE IF NOT EXISTS zezinho_financas;

USE zezinho_financas;

-- =========================================
-- TABELA: USUARIOS
-- =========================================

CREATE TABLE tb_usuarios (
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(200) NOT NULL,

    CONSTRAINT PK_tb_usuarios
        PRIMARY KEY (login)
) ENGINE=InnoDB;


-- =========================================
-- TABELA: CATEGORIAS
-- =========================================

CREATE TABLE tb_categorias (
    id_categoria SMALLINT NOT NULL AUTO_INCREMENT,
    nome_categoria VARCHAR(50) NOT NULL,
    login VARCHAR(50) NOT NULL,

    CONSTRAINT PK_tb_categorias
        PRIMARY KEY (id_categoria),

    -- Necessária para a chave estrangeira composta
    CONSTRAINT UK_categoria_usuario
        UNIQUE (id_categoria, login),

    CONSTRAINT FK_categoria_usuario
        FOREIGN KEY (login)
        REFERENCES tb_usuarios (login)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB;


-- =========================================
-- TABELA: DESPESAS
-- =========================================

CREATE TABLE tb_despesas (
    id_despesa SMALLINT NOT NULL AUTO_INCREMENT,
    valor DECIMAL(10,2) NOT NULL,
    dt_cadastro DATE NOT NULL,
    id_categoria SMALLINT NOT NULL,
    login VARCHAR(50) NOT NULL,

    CONSTRAINT PK_tb_despesas
        PRIMARY KEY (id_despesa),

    CONSTRAINT FK_despesa_categoria_usuario
        FOREIGN KEY (id_categoria, login)
        REFERENCES tb_categorias (id_categoria, login)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB;
