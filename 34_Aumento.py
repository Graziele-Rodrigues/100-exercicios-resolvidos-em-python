# Escreva um programa que calcule o aumento para funcionarios que recebem 1250 reais ou inferior a isso #
salario = float(input('Digite o salário: '))
if salario > 1250:
    novo = salario*10/100 + salario
    print('Seu novo salário é R${:.2f}'.format(novo))
else:
    novo = salario*15/100 + salario
    print('Seu novo salário é R${:.2f}'.format(novo))
