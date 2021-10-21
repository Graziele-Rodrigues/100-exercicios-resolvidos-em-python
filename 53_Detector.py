# crie um programa que leia uma frase e diga se ela é um palindromo #
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separa em uma lista
junto = ''.join(palavras) #retirar os espaços entre as frases
inverso = ''
for letra in range(len(junto)-1,-1,-1):
       inverso = inverso + junto[letra]
if inverso == junto:
    print('A palavra é palíndromo')
else:
    print('A palavra não é palíndromo')

