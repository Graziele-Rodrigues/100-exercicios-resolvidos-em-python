# Leia o primeiro termo e a razão de uma PA e mostre os 1 termos usando a estrutura while # 
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: ' ))
razao = int(input('Razão da PA: '))
termo = primeiro
n = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while n <= total:
        print('{} -> '.format(termo+(n-1)*razao), end = '')
        n+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer contar  a mais? '))
print('Progressão aritmética finalizada com {} termos'.format(total))
