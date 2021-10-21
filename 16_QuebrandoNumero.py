# Crie um pograma que leia um número real e mostre sua porçao inteira #
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))