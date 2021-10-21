# Analise dados de 4 pessoas #
somaIdade = 0 
maior = 0
n = ''
quantidade = 0
for c in range(0,4):
    print('----- {}° PESSOA -----'.format(c+1))
    nome  = input('Nome: ')
    idade = float(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    somaIdade += idade
    if sexo == 'M':
        if c == 1:
            maior = idade
            n = nome
        if maior < idade:
            maior = idade
            n = nome
    if sexo == 'F':
        if idade < 20:
            quantidade = quantidade+1

print('A média de idade do grupo é de {:.1f} anos'.format(somaIdade/4))
print('O  homem mais velho tem {:.0f} anos e se chama {}'.format(maior,n))
print('Ao todo são {} mulheres com menos de 20 anos'.format(quantidade))