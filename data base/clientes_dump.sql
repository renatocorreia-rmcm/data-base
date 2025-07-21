BEGIN TRANSACTION;
CREATE TABLE clientes (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		nome TEXT NOT NULL,
		idade INTEGER,
		cpf VARCHAR(11) NOT NULL,
		email TEXT NOT NULL,
		fone TEXT,
		cidade TEXT,
		uf VARCHAR(2) NOT NULL,
		criado_em DATE NOT NULL
	);
INSERT INTO "clientes" VALUES(1,'Fabio',23,'44444444444','fabio@email.com','1234-5678','Belo Horizonte','MG','2014-06-09');
INSERT INTO "clientes" VALUES(2,'Joao',21,'55555555555','joao@email.com','11-1234-5600','Sao Paulo','SP','2014-06-09');
INSERT INTO "clientes" VALUES(3,'Xavier',24,'66666666666','xavier@email.com','12-1234-5601','Campinas','SP','2014-06-10');
INSERT INTO "clientes" VALUES(4,'Renato',19,'00000000000','renatocorreia12144@gmail.com','79-0000-0000','Aracaju','SE','2006-00-00');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',4);
COMMIT;
