# Leia 4 numeros, adicione em uma tupla e analise-os #
qnt=0
apareceu = False
num = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')),
)
print('O valor 9 apareceu {} vez(es)'.format( num.count(9)))
for n in num:
    if n==3:
        apareceu = True
    if n%2==0:
        qnt=qnt+1
if apareceu == True:
    print('O primeiro valor 3 apareceu na {}° posição'.format(num.index(3)+1))
else:
    print('O valor 3 não foi lido')
print('Aparecer(am) {} valores pares'.format(qnt))