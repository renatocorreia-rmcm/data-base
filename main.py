import sqlite3

# conecta ao banco de dados (cria um se ainda não existe)
connection = sqlite3.connect('clientes.db')


connection.close()  # encerra conexão com banco de dados
