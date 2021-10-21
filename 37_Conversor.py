# faça a conversor de base decimal, escolhendo entre binario, octal e hexadecimal #
print('-=-'*20)
print('TECLADO - Opções para conversão')
print('1 - binário')
print('2 - octal')
print('3 - hexadecimal')
print('-=-'*20)
num = int(input('Digite um número decimal: '))
opcao = int(input('Digite opção de conversão: '))
if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])
else: 
    print("Opção não existe")