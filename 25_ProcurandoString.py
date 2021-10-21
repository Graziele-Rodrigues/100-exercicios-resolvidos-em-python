# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome #
nome =input('Qual o seu nome completo? ').upper().strip()
print("Em seu nome tem Silva?", 'SILVA' in nome)