import sqlite3
import io

connection = sqlite3.connect('../data base/clientes.db')

with io.open('../data base/clientes_dump.sql', 'w') as f:
    for linha in connection.iterdump():
        f.write(f"{linha}\n")

print('Backup realizado com sucesso.')
print('Salvo como clientes_dump.sql')

connection.close()
