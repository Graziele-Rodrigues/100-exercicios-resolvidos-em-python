valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper().strip()
    if r == 'N':
        break
print('Foram digitados {} números'.format(len(valores)))
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')