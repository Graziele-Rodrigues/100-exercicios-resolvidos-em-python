def area(l,c):
    a = l*c
    print('A area vale {:.2f} m²'.format(a))


# principal
print('Contole de Terreno')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)