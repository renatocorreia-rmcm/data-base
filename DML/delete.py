import sqlite3

connection = sqlite3.connect('../clientes.db')
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

registros = [
	('Fabio', 23, '44444444444', 'fabio@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2014-06-09'),
    ('Joao', 21, '55555555555', 'joao@email.com', '11-1234-5600', 'Sao Paulo', 'SP', '2014-06-09'),
    ('Xavier', 24, '66666666666', 'xavier@email.com', '12-1234-5601', 'Campinas', 'SP', '2014-06-10')
]
cursor.executemany(
	"""
	INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?)
	""",
	registros
)
connection.commit()


cursor.execute(
	"""
	DELETE FROM clientes
	WHERE (id=?)
	""",
	'2'
)
connection.commit()


connection.close()
