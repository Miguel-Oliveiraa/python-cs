def verificaVilao(contadorA,contadorR,contadorL,contadorE,contadorQ,contadorU,contadorI,contadorN,contadorP,contadorG,contadorM,contadorJ,contadorO,contadorK,contadorS,contadorT,contadorH,contadorD,contadorC):
  resutaldo = ""
  if contadorA >= 2 and contadorR >= 1 and contadorL >= 1 and contadorE >= 1 and contadorQ >= 1 and contadorU >= 1 and contadorI >= 1 and contadorN >= 1:
    resutaldo += "Arlequina"
  if contadorP >= 1 and contadorI >= 2 and contadorN >= 1 and contadorG >= 1 and contadorU >= 1 and contadorM >=1:
    resutaldo += "Pinguim"
  if contadorJ >= 1 and contadorO >= 1 and contadorK >= 1 and contadorE >= 1 and contadorR >= 1:
    resutaldo += "Joker"
  if contadorE >= 1 and contadorS >= 1 and contadorA >= 2 and contadorN >= 1 and contadorT >= 1 and contadorL >= 1 and contadorH >= 1 and contadorO >= 1:
    resutaldo += "Espantalho"
  if contadorD >= 1 and contadorU >= 1 and contadorA >= 3 and contadorS >= 2 and contadorC >= 1 and contadorR >= 1:
    resutaldo += "Duas Caras"
  if contadorR >= 1 and contadorE >= 2 and contadorI >= 2 and contadorD >= 2 and contadorO >= 3 and contadorS >= 2 and contadorC >= 1 and contadorN >= 2 and contadorM>=1 and contadorT>=1:
    resutaldo += "Rei dos Condimentos"
  return resutaldo

tamanhoMatriz = int(input())

matriz = []
for i in range(tamanhoMatriz):
  matriz.append(input().split((" ")))

contadorA = 0
contadorR = 0
contadorL = 0
contadorE = 0
contadorQ = 0
contadorU = 0
contadorI = 0
contadorN = 0
contadorP = 0
contadorG = 0
contadorM = 0
contadorJ = 0
contadorO = 0
contadorK = 0
contadorS = 0
contadorT = 0
contadorH = 0
contadorD = 0
contadorC = 0

for i in range(tamanhoMatriz):
  for j in range(tamanhoMatriz):
    if matriz[i][j] == "A":
      contadorA += 1
    elif matriz[i][j] == "R":
      contadorR += 1
    elif matriz[i][j] == "L":
      contadorL += 1
    elif matriz[i][j] == "E":
      contadorE += 1
    elif matriz[i][j] == "Q":
      contadorQ += 1
    elif matriz[i][j] == "U":
      contadorU += 1
    elif matriz[i][j] == "I":
      contadorI += 1
    elif matriz[i][j] == "N":
      contadorN += 1
    elif matriz[i][j] == "P":
      contadorP += 1
    elif matriz[i][j] == "G":
      contadorG += 1
    elif matriz[i][j] == "M":
      contadorM += 1
    elif matriz[i][j] == "J":
      contadorJ += 1
    elif matriz[i][j] == "O":
      contadorO += 1
    elif matriz[i][j] == "K":
      contadorK += 1
    elif matriz[i][j] == "S":
      contadorS += 1
    elif matriz[i][j] == "T":
      contadorT += 1
    elif matriz[i][j] == "H":
      contadorH += 1
    elif matriz[i][j] == "D":
      contadorD += 1
    elif matriz[i][j] == "C":
      contadorC += 1


print(verificaVilao(contadorA,contadorR,contadorL,contadorE,contadorQ,contadorU,contadorI,contadorN,contadorP,contadorG,contadorM,contadorJ,contadorO,contadorK, contadorS,contadorT,contadorH,contadorD,contadorC))