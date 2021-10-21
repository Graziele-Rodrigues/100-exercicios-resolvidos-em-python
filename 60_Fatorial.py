# Faça um programa que leia um número qualquer e mostre seu fatorial # 
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
total = 1
while c > 1:
    total =  total * c 
    c = c-1
print('O fatorial de {}! é {} '.format(n,total))