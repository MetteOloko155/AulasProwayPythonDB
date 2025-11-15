from time import sleep

inicio = int(input("Digite o numero que deseja iniciar"))

fim = int(input("Digite o numero final"))

passo = int(input("Digite o valor do passo"))

for Cronometro in range(inicio, fim, +passo):
    sleep(1)
    print(Cronometro)
