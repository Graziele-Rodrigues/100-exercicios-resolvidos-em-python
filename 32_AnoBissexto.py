# Leia um ano e diga se ele é bissexto ou não # 
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 !=0 or ano % 400==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
