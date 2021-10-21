# Faça um algoritmo que leia o preço de um produto, seu desconto e mostre seu novo preço#
preço = float(input("Digite o valor do produto: "))
desconto = int(input("Digite o valor do desconto: "))
resultado = preço - (preço * desconto/100)
print("O novo valor do produto é {:.1f}". format(resultado))