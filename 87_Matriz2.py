matrix = [[], [], []]
par=sc3=0
for t in range(0,3):
    for r in range(0,3):
        matrix[t].append(int(input(f"Digita um valor para [{t}, {r}]:")))
        if matrix[t][r]%2==0:
            par+=matrix[t][r]
    sc3 += matrix [t] [2]
print("=-"*20)
for e in matrix:
    for d,r in enumerate(e):
        print(f"[{r:^5}]", end=" ")
    print()
print("=-"*20)
print(f"A soma dos valores pares é {par}.")
print(f"A soma dos valores da terceira coluna é {sc3}.")
print(f"O maior valor da segunda linha é {max(matrix[1])}.")