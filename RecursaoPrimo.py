# funcao 
def Primo(n, i = 2): 
    # caso base 
    if n <= 2: 
        if n==2: return True 
        else: return False

    if (n % i == 0): 
        return False
        
    if (i * i >= n): 
        return True 

    #checando proximo divisor
    return Primo(n, i + 1) 
  
# principal
n = int(input('Digite um número: '))
print(Primo(n))

''' def primo(x, d = 0):
    tupla = (2, 3, 5, 7)
    if (d < 4) and (x != 1):
        if (x % tupla[d] != 0) or (x in tupla):
            primo(x,d = d+1)
        else:
            return print('O numero {} nao e primo'.format(x))
    elif x != 1:
        return print('O numero {} e primo'.format(x))
    else:
        return print('O numero {} nao e primo'.format(x))
print(primo(10103)) ''' 