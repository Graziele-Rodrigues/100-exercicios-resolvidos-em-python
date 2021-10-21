num = int(input('Digite um número: '))
total = 0
for c in range(1,num+1):
    if num % c == 0:
        total = total+1
if total == 2:
    print('O número É PRIMO')
else: 
    print('O número {} foi divisivel {} vezes e por isso NÃO É PRIMO'.format(num,total))