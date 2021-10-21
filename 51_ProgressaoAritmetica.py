# Desenvolva um programa que leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros #
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro,decimo+razao,razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')