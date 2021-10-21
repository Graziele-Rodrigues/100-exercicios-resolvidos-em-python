# crie um programa que leia o nome e o preço de vários produtos # 
total = qnt = menor =cont = 0
nome = 'nome'
while True:
    cont +=1
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        qnt+=1
    if cont == 1:
        menor = preco
        nome = produto
    else:
        if menor > preco:
            menor = preco
            nome = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer contnuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R${:.2f}'.format(total))
print('{} produtos custam mais de R$1000'.format(qnt))
print('O produto mais barato é o {}'.format(nome))