def calcularDemonio(demonios):
  posicao = len(demonios) - 1
  return posicao

def verificaBonus(vidaDenji, ataqueDenji, vidaDemonios, ataqueDemonios, qtdDemonios, mensagem):
  if mensagem == "Denji ganhou um beijo de Makima":
    vidaDenji += 50
  elif mensagem == "Pochita chegou para a batalha!":
    ataqueDenji += 50
  elif mensagem == "Makima disse que ME AMA!!!":
    vidaDenji *= 1.5
  elif mensagem == "O demônio achou um escudo no chão!":
    vidaDemonios += 25
  elif mensagem == "Onde ele arrumou essa espada?":
    ataqueDemonios += 20
  elif mensagem == "Como assim ele se duplicou??!!":
    vidaDemonios *= 2
    ataqueDemonios *= 2
    qtdDemonios *= 2
  return vidaDenji, ataqueDenji, vidaDemonios, ataqueDemonios

def batalha(vidaDenji, ataqueDenji, demonios, posicaoDemonio, qtdDemonios):
  if (demonios[posicaoDemonio][0] - ataqueDenji) > 0:
    if qtdDemonios != 1:
      print("DENJI")
      print(f"Vida: {vidaDenji}")
      print(f"Ataque atual: {ataqueDenji}")
      print("DEMÔNIO")
      print(f"Vida: {demonios[posicaoDemonio-1][0]}")
      print(f"Ataque atual: {demonios[posicaoDemonio-1][1]}")
  else:
    print("DENJI")
    print(f"Vida: {vidaDenji}")
    print(f"Ataque atual: {ataqueDenji}")
    print("DEMÔNIO")
    print(f"Vida: {demonios[posicaoDemonio][0]}")
    print(f"Ataque atual: {demonios[posicaoDemonio][1]}")
  demonios[posicaoDemonio][0] -= ataqueDenji
  vidaDenji -= demonios[posicaoDemonio][1]
  return vidaDenji, demonios[posicaoDemonio][0]

qtdDemonios = int(input())
demoniosMortos = 0
demonios = []

if qtdDemonios>0:
  vidaDenji = int(input())
  vidaDemonios = int(input())
  ataqueDenji = int(input())
  ataqueDemonios = int(input())

  for i in range(qtdDemonios):
    demonios.append([vidaDemonios, ataqueDemonios])

  while len(demonios)>0 and vidaDenji>0:
    posicaoDemonio = calcularDemonio(demonios)

    # batalha
    vidaDenji, demonios[posicaoDemonio][0] = batalha(vidaDenji, ataqueDenji, demonios, posicaoDemonio, len(demonios))
    # verifica se o demonio morreu
    if demonios[posicaoDemonio][0] <= 0:
      if len(demonios) != 1:
        print("Matei um!!!")
      demonios.pop(posicaoDemonio)
      posicaoDemonio -= 1
      demoniosMortos += 1

    # verificacao de bonus
    acaoDenji = input()
    vidaDenji, ataqueDenji, demonios[posicaoDemonio][0], demonios[posicaoDemonio][1] = verificaBonus(vidaDenji, ataqueDenji, demonios[posicaoDemonio][0], demonios[posicaoDemonio][1], qtdDemonios, acaoDenji)
    acaoDemonio = input()
    vidaDenji, ataqueDenji, demonios[posicaoDemonio][0], demonios[posicaoDemonio][1] = verificaBonus(vidaDenji, ataqueDenji, demonios[posicaoDemonio][0], demonios[posicaoDemonio][1], qtdDemonios, acaoDemonio)

else:
  print("Uhuuul um dia só para relaxar!")

if vidaDenji<=0:
  print("Infelizmente Denji foi de comes e bebes :(")
elif len(demonios)==0:
  if demoniosMortos == qtdDemonios:
    print("Ufa, agora posso descansar em paz!")
  else:
    print("Foi mais do que eu esperava mas finalmente terminei…")
