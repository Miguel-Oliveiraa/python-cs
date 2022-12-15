nome1 = str(input())
nome2 = str(input())
gols1 = 0
gols2 = 0

podeSeguir = True
# 1º rodada de penaltis
entrada1 = str(input())
if entrada1 == "Gol":
    gols1 += 1
entrada2 = str(input())
if entrada2 == "Gol":
    gols2 += 1

# 2º rodada de penaltis
entrada3 = str(input())
if entrada3 == "Gol":
    gols1 += 1
entrada4 = str(input())
if entrada4 == "Gol":
    gols2 += 1

# 3º rodada de penaltis
entrada5 = str(input())
if entrada5 == "Gol":
    gols1 += 1
entrada6 = str(input())
if entrada6 == "Gol":
    gols2 += 1
if gols1 > 2 + gols2:
    podeSeguir = False
elif gols2 > 2 + gols1:
    podeSeguir = False

# 4º rodada de penaltis
if podeSeguir == True:
    entrada7 = str(input())
    if entrada7 == "Gol":
        gols1 += 1
    if gols1 > 2 + gols2:
        podeSeguir = False
    if gols2 > 1 + gols1:
        podeSeguir = False
if podeSeguir == True:
    entrada8 = input()
    if entrada8 == "Gol":
        gols2 += 1
    if gols2 > 1 + gols1:
        podeSeguir = False
    if gols1 > 1 + gols2:
        podeSeguir = False

# 5º rodada de penaltis
if podeSeguir == True:
    entrada9 = str(input())
    if entrada9 == "Gol":
        gols1 += 1
    if gols1 > 1 + gols2:
        podeSeguir = False
    if gols2 > gols1:
        podeSeguir = False
if podeSeguir == True:
    entrada10 = str(input())
    if entrada10 == "Gol":
        gols2 += 1

if gols1 > gols2:
    print(f"{nome1} vence a disputa de pênaltis por {gols1} a {gols2} e avança de fase!")
elif gols2 > gols1:
    print(f"{nome2} vence a disputa de pênaltis por {gols2} a {gols1} e avança de fase!")
else:
    print(f"Ambas as seleções terminaram com {gols1} gols, mas o desempate vai ficar para outro dia.")