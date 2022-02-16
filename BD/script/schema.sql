CREATE TABLE curso(
	ID int(6) PRIMARY KEY,
	nombre varchar(20) NOT NULL,
	apellidoP varchar(20) NOT NULL,
	apellidoM varchar(20) NOT NULL,
	fechaNac DATE NOT NULL,
	nota_1 int NOT NULL,
	nota_2 int NOT NULL,
	nota_3 int NOT NULL,
	nota_4 int NOT NULL
);