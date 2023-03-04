def imprimeResumo(vitoria, derrotas, empates):
  if vitorias == 3:
    print("Nenhum dos 3 inimigos foram capazes de derrotar o Denji!")
  elif derrotas == 3:
    print("Hoje não foi um dia bom para o Denji, perdeu todas as batalhas")
  elif vitorias == 1 and derrotas == 1:
    print("Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar")
  elif vitorias > derrotas and vitorias > empates:
    print("Denji conseguiu derrotar a maioria de seus inimigos")
  elif derrotas > vitorias and derrotas > empates:
    print("Dia péssimo para o Denji, perdeu a maioria de suas batalhas")
  elif empates > derrotas and empates > vitorias:
    print("Dia duro para o Denji, empatou de mais")

def transformacaoDenji(energia, controle, precisao):
  if energia>=750 and controle>=7 and precisao>= 8:
    return "Motosserra Suprema"
  elif energia>=500 and controle >= 6 and precisao>= 6:
    return "Motosserra Avançada"
  else:
    return "Motosserra Normal"

def inimigoRodada(rodada):
  if rodada == 1:
    return "Makima"
  elif rodada == 2:
    return "Reze"
  return "Santa Claus"

def vencedorBatalha(forcaDenji, forcaVilao):
  if forcaDenji > forcaVilao:
    return "denji"
  elif forcaVilao > forcaDenji:
    return "vilao"
  return "empate"

historicoBatalhas = []
vitorias = 0
derrotas = 0
empates = 0

for rodada in range(1, 4):

  # dados do denji
  energia = int(input())
  controle = int(input())
  precisao = int(input())
  transformacao = transformacaoDenji(energia, controle, precisao)
  forcaDenji = energia + (controle * precisao)

  # dados do inimigo
  forcaInimigo = int(input())
  nomeVilao = inimigoRodada(rodada)

  print(f"### Rodada {rodada} - {nomeVilao} ###")
  print(f"O Denji ira se transformar na {transformacao} para enfrentar o {nomeVilao}")

  # verifica quem venceu a batalha, coloca no historico e incrementa vitorias, derrotas ou empates
  vencedorRodada = vencedorBatalha(forcaDenji, forcaInimigo)
  if vencedorRodada == "denji":
    print(f"Denji saiu vitorioso nessa batalha contra o {nomeVilao}")
    historicoBatalhas.append([rodada, transformacao, "Vitoria"])
    vitorias += 1
  elif vencedorRodada == "vilao":
    print(f"Denji não conseguiu força o suficiente para derrotar o {nomeVilao}")
    historicoBatalhas.append([rodada, transformacao, "Derrota"])
    derrotas += 1
  elif vencedorRodada == "empate":
    print(f"Como pode ser possível?? Denji possui a mesma força que o {nomeVilao}")
    historicoBatalhas.append([rodada, transformacao, "Empate"])
    empates += 1

print("### Resultado Final ###")
for i in historicoBatalhas:
  print(f"Rodada {i[0]}: {i[1]} - {i[2]}")

imprimeResumo(vitorias, derrotas, empates)
