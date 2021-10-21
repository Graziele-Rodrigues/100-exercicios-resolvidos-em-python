pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print('Ao todo temos {} pessoas cadastradas'.format(len(galera)))
media = soma/len(galera)
print('A media de idade é de {:5.2f}'.format(media))
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print('{}, '.format(p['nome']), end='')
print('\nLista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >=media:
        print('  ')
        for k,v in p.items():
            print('{} = {}'.format(k,v), end=' ')

print('ENCERRADO')