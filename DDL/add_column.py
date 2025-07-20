import sqlite3

connection = sqlite3.connect('../data base/clientes.db')

cursor = connection.cursor()

cursor.execute(
	"""
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
	"""
)

cursor.execute(
	"""
	ALTER TABLE clientes
	ADD COLUMN bloqueado BOOLEAN;
	"""
)

connection.commit()

connection.close()
