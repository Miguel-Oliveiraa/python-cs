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


# ///////////////////////////
def buscar(linha, palavra):
  # procurando a primeira letra da palavra
  for i in range(len(linha)):
    for j in range(len(linha[i])):
      if (linha[i][j] == palavra[0]):
        # se encontrou
        if (buscar_ao_redor(linha, palavra, i, j)):
          return True
  # se não encontrou
  return False


def buscar_ao_redor(linha, palavra, i, j):
  # se a palavra foi encontrada
  if (len(palavra) == 0):
    return True

  # se a posição atual na linha contém a próxima letra da palavra
  if (i < 0 or i >= len(linha) or j < 0 or j >= len(linha[i]) or linha[i][j] != palavra[0]):
    return False

  # marca a posição atual
  linha[i][j] = '*'

  # verifica baixo
  if (buscar_ao_redor(linha, palavra[1:], i + 1, j)):
    return True
  # verifica cima
  if (buscar_ao_redor(linha, palavra[1:], i - 1, j)):
    return True
  # verifica direita
  if (buscar_ao_redor(linha, palavra[1:], i, j + 1)):
    return True
  # verifica esquerda
  if (buscar_ao_redor(linha, palavra[1:], i, j - 1)):
    return True
  # verifica baixo-direita
  if (buscar_ao_redor(linha, palavra[1:], i + 1, j + 1)):
    return True
  # verifica baixo-esquerda
  if (buscar_ao_redor(linha, palavra[1:], i + 1, j - 1)):
    return True
  # verifica cima-direita
  if (buscar_ao_redor(linha, palavra[1:], i - 1, j + 1)):
    return True
  # verifica cima-esquerda
  if (buscar_ao_redor(linha, palavra[1:], i - 1, j - 1)):
    return True

  # se a palavra não pode ser formada retorna False
  linha[i][j] = palavra[0]
  return False


lista = []
n = int(input())
lista = []
for i in range(n):
  sequencia = input()
  sequencia = sequencia.split(" ")
  lista.append(sequencia)

if (buscar(lista, 'PINGUIM')):
  print(f'Isso!!! Encontramos uma pista, Pinguim está junto com o Charada.')
elif ((lista, 'CHARADA')):
  print(f'Isso!!! Encontramos uma pista, mas somente o Charada está envolvido.')
elif (buscar(lista, 'ARLEQUINA')):
  print(f'Isso!!! Encontramos uma pista, Arlequina está junto com o Charada.')
elif (buscar(lista, 'JOKER')):
  print(f'Isso!!! Encontramos uma pista, Joker está junto com o Charada.')
elif (buscar(lista, 'ESPANTALHO')):
  print(f'Isso!!! Encontramos uma pista, Espantalho está junto com o Charada.')
elif (buscar(lista, 'DUASCARAS')):
  print(f'Isso!!! Encontramos uma pista, Duas Caras está junto com o Charada.')
elif (buscar(lista, 'REIDOSCONDIMENTOS')):
  print(f'Isso!!! Encontramos uma pista, Rei Dos Condimentos está junto com o Charada.')
else:
  print('Poxa... acho que seguimos uma pista falsa.')