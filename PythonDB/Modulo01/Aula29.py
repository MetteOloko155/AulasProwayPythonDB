#iremos criar um loop dinamico onde o usuario interage com as opcoes de continuar ou sair
# escolha 1 para continuar e 2 para sair
# se o usuario continuar ele ira interagir com a opcao de digitar o numero da tabuada se nao ele ira sair do sistema

while True:
    print("\nDigite 1 para continuar a tabuada: ")
    print("Digite 2 para sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        numero = int(input("Digite qual número deseja da tabuada: "))
        print(f"\nTabuada do {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    elif escolha == "2":
        print("Tabuada encerrada")
        break