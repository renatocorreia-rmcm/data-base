import sqlite3

connection = sqlite3.connect('data base/clientes.db')
cursor = connection.cursor()


query: str = """
	DELETE FROM clientes
	WHERE id=4
"""
cursor.execute(query)
connection.commit()


connection.close()
