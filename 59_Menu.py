# Crie um programa que leia dois valores e mostre um menu #
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao !=5: 
    print('=-'*20)
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    print('=-'*20)
    opcao = int(input('Qual é a sua opção? '))
    if opcao==1:
        print(n1+n2)
    elif opcao==2:
        print(n1*n2)
    elif opcao==3:
        if n1>n2:
            print(n1)
        else:
            print(n2)
    elif opcao==4:
         n1 = int(input('Primeiro valor: '))
         n2 = int(input('Segundo valor: '))
    elif opcao==5:
        pass
    else:
        print('Número inválido')