lista = []
for i in range(0,5):
    valor = int(input('Digite um valor para Posição {}: '.format(i)))
    lista.append(valor)

print('Você digitou os valores ', lista)
lista.sort()
print('O maior número da lista é {}'.format(lista[-1]))
print('O menor número da lista é {}'.format(lista[0]))
