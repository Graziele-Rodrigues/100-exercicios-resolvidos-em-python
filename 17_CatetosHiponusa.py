# faça um programa que leia os valores dos catetos e calcule a hipotenusa #
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print('A hipotenusa vale {:.2f}'.format(hi))