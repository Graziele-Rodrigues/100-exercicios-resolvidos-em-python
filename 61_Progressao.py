# Leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos usando a estrutura while # 
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: ' ))
razao = int(input('Razão da PA: '))
termo = primeiro
n = 1
while n <=10:
    print('{} -> '.format(termo+(n-1)*razao), end = '')
    n +=1
print('FIM')