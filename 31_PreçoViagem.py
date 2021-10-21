# Faça um programa que cobre 0.5 para viagens de até 200km e 0.45 para mais longas #
distancia = float(input('Qual foi a distância percorrida? '))
if(distancia > 200):
    print("O total da viagem é R${:.2f}".format(distancia*0.45))
else: 
    print("O total da viagem é R${:.2f}".format(distancia*0.5))
