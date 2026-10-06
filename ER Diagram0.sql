create database zezinho_financas;

CREATE TABLE if not exists tb_usuarios (
 login VARCHAR(100) NOT NULL,
 senha VARCHAR(10) NOT NULL
);

ALTER TABLE tb_usuarios ADD CONSTRAINT PK_tb_usuarios PRIMARY KEY (login);


CREATE TABLE if not exists tb_categorias (
 id_categoria smallint not null,
 nome VARCHAR(1000),
 login VARCHAR(100)
);

ALTER TABLE tb_categorias ADD CONSTRAINT PK_tb_categorias PRIMARY KEY (id_categoria);


CREATE TABLE if not exists tb_despesas (
 id_despesa int,
 id_categoria_0 smallint ,
 dt_cadastro DATETIME,
 valor DECIMAL(10, 2),
 descricao VARCHAR(1000),
 id_categoria smallint(10),
 login VARCHAR(100)
);

ALTER TABLE tb_despesas ADD CONSTRAINT PK_tb_despesas PRIMARY KEY (id_despesa,id_categoria_0);


ALTER TABLE tb_categorias ADD CONSTRAINT FK_tb_categorias_0 FOREIGN KEY (login_0) REFERENCES tb_usuarios (login);


ALTER TABLE tb_despesas ADD CONSTRAINT FK_tb_despesas_0 FOREIGN KEY (id_categoria_0) REFERENCES tb_categorias (id_categoria);


