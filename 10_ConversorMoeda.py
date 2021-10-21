# Digite um valor e mostre quanto dólar a pessoa pode comprar #
reais = float(input('Quanto você tem na carteira? R$'))
print("R${} reais equivale a ${:.2f} dólares".format(reais, reais/5.37))