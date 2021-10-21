lista = []
listaPares = []
n = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper().strip()
    if r == 'N':
        break
print('A lista completa é ', lista)
for x in range(len(lista)):
    if lista[x]%2==0:
        listaPares.append(lista[x])
print('A lista de pares é ', listaPares)