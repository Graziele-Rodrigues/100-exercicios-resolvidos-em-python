numeros  = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ' )).upper().strip()
    if r in 'N':
        break
print('='*30)
print('Lista: ', numeros)