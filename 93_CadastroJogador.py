jogador = {"Jogador": input("Nome do Jogador:"),"gols": [],"total":0}
for c in range(1,int(input(f"Quantas prtidas {jogador['Jogador']} jogou?:"))+1):
    jogador["gols"].append(int(input(f"Quantos gols na {c}º partida?: ")))
    jogador["total"] += jogador["gols"][c-1]
print("=-"*30)
print(jogador)
print("=-"*30)
for k,v in jogador.items():
    print(f"O campo {k} tem valor {v}.")
print("=-"*30)
print(f"O jogador {jogador['Jogador']} jogou {len(jogador['gols'])} partidas")
for e,n in enumerate(jogador["gols"]):
    print(f"{'=>':>5}Na {e+1}º partida, fez {n} gols. ")
print(f"Foi um total de {jogador['total']} gols.")