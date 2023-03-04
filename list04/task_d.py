def verificaBonus(vidaDenji, vidaDemonios, ataqueDenji, ataqueDemonios, qtdDemonios, mensagem):
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

qtdDemonios = int(input())

if qtdDemonios>0:
  vidaDenji = int(input())
  vidaDemonios = int(input())
  ataqueDenji = int(input())
  ataqueDemonios = int(input())


  acaoDenji = input()
  verificaBonus(vidaDenji, vidaDemonios, ataqueDenji, ataqueDemonios, qtdDemonios, acaoDenji)
  acaoDemonio = input()
  verificaBonus(vidaDenji, vidaDemonios, ataqueDenji, ataqueDemonios, qtdDemonios, acaoDemonio)
else:
  print("Uhuuul um dia só para relaxar!")