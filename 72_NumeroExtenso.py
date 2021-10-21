#mostrar o numero digitado por extenso
cont  = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze','catorze', 'quinze', 
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
num=0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0<=num <=20:
        break
    print('Tente novamente. ', end='')
print('O número {} por extenso é {}'.format(num, cont[num]))