# faça um programa que identifique se a cidade começa ou não com a palavra Santo #
cidade = input('Digite o nome da cidade que você nasceu: ').upper().strip()
inicio = cidade.split()
print('SANTO' in inicio[0])