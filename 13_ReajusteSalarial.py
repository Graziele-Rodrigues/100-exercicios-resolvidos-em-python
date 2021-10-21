# Faça um programa que leia o salario do funcionário e faça um reajuste de 15% #
salario = float(input('Wual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novo))