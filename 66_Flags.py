# some todos os numeros até que o digitado seja 999 #
num = qnt = soma = 0
while True:
    num  = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma = soma+num
    qnt= qnt+1

print('Você digitou {} números e a soma deles é {}'.format(qnt,soma))