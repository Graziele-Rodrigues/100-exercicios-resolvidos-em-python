#Faça a tabuada de um número escolhido pelo usuario usando o laço for#
num = int(input('Digite um número para ver sua tabuda: '))
for c in range(1,11):
    print('{} x {} = {}'.format(num,c,num*c))