import sqlite3

connection = sqlite3.connect('data base/clientes.db')
cursor = connection.cursor()

NOME_TABELA = "clientes"


print("\nALL DATABASE TABLES")
cursor.execute(
	"""
	SELECT name 
	FROM sqlite_master 
	WHERE type='table' 
	"""
)
for table in cursor.fetchall():
	print(table)


print(f"\n'{NOME_TABELA}' TABLE SCHEMA")
cursor.execute(
	"""
	SELECT sql 
	FROM sqlite_master 
	WHERE (type='table' AND name=?)
	""",
	(NOME_TABELA,)
)
print(cursor.fetchall())


print(f"\n'{NOME_TABELA}' TABLE COLUMNS")
cursor.execute(f"PRAGMA table_info({NOME_TABELA})")
for coluna in cursor.fetchall():
	print(coluna)


connection.close()
