ContIdade = ContHomens = ContMulheres =0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        ContIdade += 1
    if sexo == 'M':
        ContHomens +=1
    if sexo == 'F' and idade > 20:
        ContMulheres+=1
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N': 
        break
print('No grupo existem {} pessoas com mais de 18 anos'.format(ContIdade))
print('No grupo existem {} homens'.format(ContHomens))
print('No grupo existem {} mulheres com mais de 20 anos'.format(ContMulheres))