numero = int(input('Digite o valor que deseja saber da tabuda: '))

for c in range(1,11):
    print('{} X {} = {}'.format(numero, c, numero*c))