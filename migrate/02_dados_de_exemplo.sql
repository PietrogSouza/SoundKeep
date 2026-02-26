USE soundkeep;

INSERT INTO `soundkeep`.`genero` (`nome`, `icone`, `cor`) 
VALUES 
("Rock", "", "red"),
("Pop", "", "blue"),
("Pagode", "", "yellow");


INSERT INTO `soundkeep`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
("Seu Jorge",
"00:03:38",
"Amiga da minha mulher",
"https://upload.wikimedia.org/wikipedia/pt/6/6d/Capa_de_M%C3%BAsicas_para_Churrasco%2C_Vol._1.jpg",
"Pagode");



INSERT INTO `soundkeep`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
("System of a down",
"00:03:30",
"Chop Suey",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0ueRJXSpAr2Z5rMYaIubJe1bHuigl2GNGeA&s",
"Rock");
