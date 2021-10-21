# Leia a data de nascimento de 7 pessoas e diga quais sao as maiores #
maior = 0
menor = 0
for c in range(0,7):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(c+1)))
    x = 2021 - nascimento
    if x > 18:
        maior = maior+1
    else:
        menor = menor+1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também {} pessoas menores de idade'.format(menor))
    