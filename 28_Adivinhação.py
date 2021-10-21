# faça um programa para o usuario tentar aidivnhar o número escolhido pelo computador entre 0 e 5 #
from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em qual número eu pensei?' ))
print('PROCESSANDO..')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))