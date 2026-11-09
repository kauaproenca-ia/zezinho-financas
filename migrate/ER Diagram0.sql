CREATE DATABASE zezinho_financas;
USE zezinho_financas;

CREATE TABLE tb_usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    nome VARCHAR(100)
);

CREATE TABLE tb_categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nome_categoria VARCHAR(80) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario)
);

CREATE TABLE tb_despesas (
    id_despesa INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_categoria INT,
    descricao VARCHAR(200) NOT NULL,
    valor DECIMAL(12,2) NOT NULL,
    data_despesa DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES tb_categorias(id_categoria)
);