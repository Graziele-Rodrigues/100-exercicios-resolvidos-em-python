from time import sleep
def contador(i,f,p):
    print('-='*20)
    print('Contagem de {} até {} de {} em {}'.format(i,f,p,p))
    sleep(3)
    if p<0:
        p=p+1
    if p == 0:
        p=1
    if i <f:
        cont = i
        while cont<=f:
            print(f'{cont}', end=' ', flush=True)
            sleep(5)
            cont=cont+p
        print('FIM')
    else:   
        cont=i
        while cont>=f:
            print(f'{cont}', end=' ', flush=True)
            sleep(5)
            cont=cont-p
        print('FIM')  

#principal
contador(1,10,2)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)