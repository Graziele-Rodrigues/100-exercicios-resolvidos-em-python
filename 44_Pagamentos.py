#Elabore um programa que calcule o valor a ser pago#
print('========= LOJA ========')
valor = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor*10/100)
    print('O valor da sua compra será R${:.2f}'.format(total))
elif opcao == 2:
    total = valor - (valor*5/100)
    print('O valor da sua compra será R${:.2f}'.format(total))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} - sem juros'.format(valor/2))
else:
    total = valor + (valor*20/100)
    parcela = int(input('Quantas parcelas quer dividir? '))
    print('Sua compra será parcelada em {}x de R${:.2f} - juros de 20%'.format(parcela,total/parcela))
