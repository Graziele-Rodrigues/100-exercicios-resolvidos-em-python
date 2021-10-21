palavras = ('aprender', 'programar', 'linguagem', 'arara')
for p in palavras: 
    print('\nNa palavra {} temos '.format(p), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
