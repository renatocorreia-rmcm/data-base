import sqlite3
import io

connection = sqlite3.connect('../data base/clientes_recuperado.db')
cursor = connection.cursor()

f = io.open('../data base/clientes_dump.sql', 'r')
sql = f.read()
cursor.executescript(sql)

print('Banco de dados recuperado com sucesso.')
print('Salvo como clientes_recuperado.db')

connection.close()
