lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c ==0 or n>lista[-1]:
        lista.append(n)
    else:
        for pos in range(len(lista)):
            if n <= lista[pos]:
                lista.insert(pos,n) #inserir na posição pos o valor n
                break
print('=-'*30)
print('Os valores digitados foram ', lista)
