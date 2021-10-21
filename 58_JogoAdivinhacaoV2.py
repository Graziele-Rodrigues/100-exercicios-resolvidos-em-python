from random import randint
from time import sleep
computador = randint(0,10)
acertou = False
tentativa = 0
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
while acertou == False:
    tentativa = tentativa + 1
    jogador = int(input('Em qual número eu pensei? ' ))
    print('PROCESSANDO...')
    sleep(3)
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer com {} tentativas.'.format(tentativa))
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente outra vez')
        else:
            print('Mais... Tente outra vez')