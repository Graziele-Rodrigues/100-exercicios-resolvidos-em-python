import random,time
def sorteia(f):
    print('sorteando 5 valores na lista :', end='')
    for i in range(0,5):
        p=random.randint(0,10)
        f.append(p)
        print(p, end=' ', flush=True)
        time.sleep(0.5) 
    

def somapar(f):
    print()
    soma=0
    for c in f:
        if c % 2==0: 
            soma+=c
    print('somando os valores pares de {}:'.format(f),end=' ')
    print('{}'.format(soma))

#principal
f=[]
sorteia(f) 
somapar(f)