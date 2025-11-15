import sqlite3

#1 interação com usuario
#nome = input('Digite o nome que deseja dar ao seu banco: ')

#algoritmo para criação do banco de dados

#Cria um novo banco ou conecta um bando existente
conexao = sqlite3.connect('William will.sqlite')

#funcao Sqlite de manipulção script SQL
cursor = conexao.cursor()

comandoSQL = ''' 
CREATE TABLE IF NOT EXISTS produtos (
     id INTEGER,
     nome TEXT NOT NULL   
)
'''

conexao.execute(comandoSQL)
conexao.commit()
conexao.close()