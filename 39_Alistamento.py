# leia a data de nascimento e veja se a pessoa deve se alistar #
ano = int(input('Digite a data do seu nascimento: '))
alistamento = 2021 - ano
if alistamento == 18:
    print('Está na hora de se alistar')
elif alistamento > 18:
    print('Passou da hora de se alistar')
else:
    print('Ainda não chegou a hora de se alistar')