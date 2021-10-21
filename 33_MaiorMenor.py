# Leia 3 numeros e diga qual é o maior e menor entre eles #
n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))
if n1>n2 and n1>n3:
    print('O maior número é {}'.format(n1))
    if n2 > n3:
        print('O menor número é {}'.format(n3))
    else: 
        print('O menor número é {}'.format(n2))

elif n2>n1 and n2>n3:
    print('O maior número é {}'.format(n2))
    if n1 > n3:
        print('O menor número é {}'.format(n3))
    else: 
        print('O menor número é {}'.format(n1))
else: 
    print('O maior número é {}'.format(n3))
    if n2 > n1:
        print('O menor número é {}'.format(n1))
    else: 
        print('O menor número é {}'.format(n2))
