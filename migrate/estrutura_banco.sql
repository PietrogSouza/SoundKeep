CREATE DATABASE IF NOT EXISTS soundkeep;

USE soundkeep;

CREATE TABLE IF NOT EXISTS genero (
 nome VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME,
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30),
 CONSTRAINT fk_musica_genero FOREIGN KEY (nome_genero) REFERENCES genero (nome)
);




