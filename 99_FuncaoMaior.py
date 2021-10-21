from time import sleep
def maior(*num):
    cont = maior = 0
    print('-='*30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush='True')
        sleep(3)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont +=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')




#principal
maior(2,9,4,5,6,7,1)