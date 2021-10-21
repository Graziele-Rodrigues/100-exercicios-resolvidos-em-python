# sorteie numeros e guarde em uma tupla e depois mostre o maior e menor #
from random import randint
n = (randint(1,10), randint(1,10), randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram: ', end='')
for i in n:
    print(i, end=' ')
print('\nO maior número é {} e o menor é {}'.format(max(n), min(n)))
