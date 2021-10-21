# Leia 6 numeros e mostre a soma apenas dos pares #
soma = 0 
for num in range(1,7):
    num = int(input('Digite um número: '))
    if num%2==0:
        soma+=num
print(soma)