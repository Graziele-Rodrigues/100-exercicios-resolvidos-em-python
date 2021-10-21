# Escreva um programa que pergunte a quantidade de km percorridos e a quantidades de dias.
# Após isso, calcule o preço a pagar, sabendo que o carro custa 60 por dia e 0.15 por km #
km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
total = 60*dias + km*0.15
print('O valor total a pagar pelo aluguel é R${:.1f}'.format(total))
