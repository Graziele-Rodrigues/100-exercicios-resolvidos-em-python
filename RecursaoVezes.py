# ESCREVA UMA RECURSAO QUE RETORNE O NUMERO DE VEZES QUE 3 E 4 APARECERAM #

def conta(n):
    if n == 0:
        return 0
    else:
        ultimo = n%10 #ultimo digito
        if ultimo == 3 or ultimo==4:
            return 1 +conta(n//10)
        else:
            return conta(n//10)
            
print(conta(12345654))
