#Leia o peso em kg e altura da pessoa e mostre seu IMC#
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso em Kg? '))
imc = peso / (altura**2)
if imc <18.5:
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso normal')
elif imc>=25 and imc<=30:
    print('Sobrepeso')
elif imc>30 and imc<=40:
    print('Obesidade')
else:
    print('Obesidade mórbida')