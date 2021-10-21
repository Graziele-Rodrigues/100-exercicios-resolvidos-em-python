ficha  = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"N°.":<4}{"Nome":<10}{"MÉDIA":>9}') #formatando
print('-'*28)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Fechando...')
        break
    elif opc<=len(ficha)-1:
        print('Notas de {} são {}'.format(ficha[opc][0],ficha[opc][1]))
    else:
        print('Não há aluno com esse número')
print('Volte sempre')