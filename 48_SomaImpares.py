# Faça a soma entre todos os multiplos impares que são multiplos de 3, no intervalo de 1 a 500 #
total = 0 
for n in range(1,501):
    if n%2 !=0:
        if n%3==0:
            total +=n
print(total)
