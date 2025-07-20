import sqlite3

# conecta ao banco de dados (cria um se ainda não existe)
connection = sqlite3.connect('../data base/clientes.db')

# cursor: iterador que permite navegar e manipular os registros do bd
cursor = connection.cursor()


# execute: lê e executa comandos sql puro diretamente no bd
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

print("table clientes criada.")

connection.close()  # encerra conexão com banco de dados
