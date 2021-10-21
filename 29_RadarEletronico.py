# Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80km/h aplique multa de 7 reais por cada km#
velocidade = float(input('Velocidade atual do carro: ')) 
if (velocidade <=80):
    print('Tenha um bom dia! Dirija com segurança.')
else:
    multa = 7*(velocidade - 80)
    print('Você ultrapassou o limite de 80km/h. Assim, deverá pagar uma multa de R${:.2f}'.format(multa))