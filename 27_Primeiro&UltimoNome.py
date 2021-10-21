#Faça um programa que leia o nome completo e mostre o primeiro e ultimo separadamento#
n = input("Digite seu nome completo: ").strip()
nome = n.split()
print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome[-1]))