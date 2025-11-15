from time import sleep

def animacao():
    for animacao in range(20):
        sleep(0.1)
        print('+')

def interacaoBanco(nome, sobrenome, cursor, conexao):
    #bloco 06
    repeticao = True

    while repeticao != False :

        novaTabela = int(input(f'{nome} {sobrenome}, deseja criar uma nova tabela\nDigite 1 para sim e 2 para não: '))

        if novaTabela == 2:
            repeticao = False

        elif novaTabela == 1:
            repeticao = True

            nomeTabela = input(f'{nome} {sobrenome}, informe o nome da tabela que deseja usar')

            comandoCriaTabela = f'''
             Tabela is not FULL

            '''