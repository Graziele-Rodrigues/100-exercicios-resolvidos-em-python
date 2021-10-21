valor=float(input('Qual o valor da casa? '))
salario=float(input('Qual o valor do seu salário? '))
tempo=int(input('Em quantos anos deseja pagar? '))
porcentagem=salario*30/100
parcela=valor/(tempo*12)
if(parcela>porcentagem):
    print('Empréstimo negado')
else:
    print('Emprestimo aprovado. Você deve pagar R${0:.2f} mensais, durante {1} anos'.format(parcela,tempo))