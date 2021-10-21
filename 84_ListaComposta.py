# faça um programa que leia nome e peso, guarde em uma lista e analise #
temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('=-'*30)
print(princ)
print('Ao todo foram cadastrados {} pessoas'.format(len(princ)))
