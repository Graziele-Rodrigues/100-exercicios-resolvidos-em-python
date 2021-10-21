# dentre 4 alunos, sorteie a ordem de apresentação do trabalho #
from random import shuffle
n1 = input('')
n2 = input('')
n3 = input('')
n4 = input('')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ', lista)