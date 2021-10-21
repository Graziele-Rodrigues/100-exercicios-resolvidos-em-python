# simulação de um caixa eletronico #
cedula_a = cedula_b = cedula_c = cedula_d = 0
print('=-'*20)
print('    CAIXA ELETRÔNICO    ')
print('=-'*20)
dinheiro = int(input('Quanto dinheiro você quer sacar? '))
while dinheiro > 0:
    cedula_a = int(dinheiro/50)
    dinheiro = dinheiro - cedula_a*50
    cedula_b = int(dinheiro/20)
    dinheiro = dinheiro - cedula_b*20
    cedula_c = int(dinheiro/10)
    dinheiro = dinheiro - cedula_c*10
    cedula_d = int(dinheiro/1)
    dinheiro = dinheiro - cedula_d*1
print('''{} cédulas de R$50
{} cédulas de R$20
{} cédulas de R$10
{} cédulas de R$1'''.format(cedula_a,cedula_b,cedula_c,cedula_d) )