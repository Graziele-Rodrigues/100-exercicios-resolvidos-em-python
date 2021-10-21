# Faça um programa que leia o sexo de uma pessoa, mas aceite apenas os valores 'M' OU 'F' #
sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválido. Por favor, informe seu sexo: [M/F]: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(sexo))