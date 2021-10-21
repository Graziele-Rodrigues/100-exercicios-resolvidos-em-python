# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador Perder #
from random import randint
qnt=0
tipo =''
print('=-'*20)
print('JOGO PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Digia um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    ParImpar = input('Par ou Ímpar [P/I]? ').upper().strip()
    if total%2==0:
        print('-'*50)
        print('Você jogou {} e o computador {}. Total de {} DEU PAR'.format(jogador,computador,total))
        print('-'*50)
        print('Você VENCEU.')
        print('Vamos jogar novamente...')
        print('=-'*20)
        qnt = qnt+1
    else: 
        print('-'*50)
        print('Você jogou {} e o computador {}. Total de {} DEU ÍMPAR'.format(jogador,computador,total))
        print('-'*50)
        print('Você PERDEU.')
        print('=-'*20)
        break
print('GAME OVER! Você venceu {} vezes'.format(qnt))
