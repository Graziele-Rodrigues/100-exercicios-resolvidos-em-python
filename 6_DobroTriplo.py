# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada #
import math
num = int(input('Digite um número: '))
dobro = num*2
triplo = num*3
raiz = math.isqrt(num)
print('O dobro do número {} é {}'.format(num,dobro))
print('O triplo do número {} é {}'.format(num,triplo))
print('A raiz quadrada do número {} é {}'.format(num,raiz))