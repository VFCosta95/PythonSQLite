# Banco de Dados
# DB API

import sqlite3

# Conexão
con = sqlite3.connect("clientes.db")

# Cursor
cur = con.cursor()

# Executar comandos na DB
def criar_table(conexao, cursor):
    cur.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    con.commit()

# Inserir os dados
def inserir_dados(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes(nome, email)  VALUES(?, ?);", data)
    conexao.commit()

# Atualizando Registros
def atualizar_dados(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data )
    conexao.commit()

# Removendo Registros
def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()


##########################################################################

# Ver a tabela
cur.execute("SELECT * FROM clientes")

# Mostrar no console os Dados
print(cur.fetchall())