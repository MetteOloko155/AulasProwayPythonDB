import sqlite3
from time import sleep

#carregamento
for i in range(20):
    print("*", end="", flush=True)
    sleep(0.1)
print("\nSeja bem-vindo à Aula de Python com Banco de Dados!\n")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")

#Conexão com o banco
con = sqlite3.connect("Abobrinha.db")
cur = con.cursor()

# tabela
criar = input(f"{nome}, você deseja criar uma nova tabela? (s/n): ").lower()
if criar == "s":
    tabela = input("Digite o nome da tabela: ")
    cur.execute(f"CREATE TABLE IF NOT EXISTS {tabela} (id INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()
    print(f"Tabela '{tabela}' criada com sucesso!")

    deletar = input(f"{nome}, você deseja deletar a tabela '{tabela}'? (s/n): ").lower()
    if deletar == "s":
        cur.execute(f"DROP TABLE IF EXISTS {tabela}")
        con.commit()
        print(f"Tabela '{tabela}' foi deletada com sucesso!")

# Continuar ou sair
continuar = input("Deseja continuar no sistema? ( s/n ): ").lower()
if continuar != "s":
    print("Saindo do sistema...")

con.close()
