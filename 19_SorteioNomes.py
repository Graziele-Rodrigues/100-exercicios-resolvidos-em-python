# leia 4 nomes e sorteie um #
import random
n1 = input('')
n2 = input('')
n3 = input('')
n4 = input('')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))