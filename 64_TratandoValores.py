# Faça um programa que leia números e faça a soma deles e até que o número digitado seja 9 #
valor = total = qnt = 0
valor = int(input('Digite um número [999 para parar]: '))
while valor != 999:
    total = total+ valor
    qnt = qnt+1
    valor = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(qnt,total))
 