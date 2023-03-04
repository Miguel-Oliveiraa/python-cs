def lutas(demonios, vidaDenji, vidaDemonio, initVidaDemonio, ataqueDenji, ataqueDemonio, initAtaqueDemonio, contadorMortos, duplicou):

  # imprime informacoes dos lutadores
  print(f'DENJI')
  print(f'Vida: {vidaDenji}')
  print(f'Ataque atual: {ataqueDenji}')

  print(f'DEMÔNIO')
  print(f'Vida: {vidaDemonio}')
  print(f'Ataque atual: {ataqueDemonio}')

  # recebe os bonus
  entrada_denji = input()
  if (entrada_denji == 'Denji ganhou um beijo de Makima'):
    vidaDenji += 50
  elif (entrada_denji == 'Pochita chegou para a batalha!'):
    ataqueDenji += 50
  elif (entrada_denji == 'Makima disse que ME AMA!!!'):
    vidaDenji = int(vidaDenji * 1.5)
  entrada_demon = input()
  if (entrada_demon == 'O demônio achou um escudo no chão!'):
    vidaDemonio += 25
  elif (entrada_demon == 'Onde ele arrumou essa espada?'):
    ataqueDemonio += 20
  elif (entrada_demon == 'Como assim ele se duplicou??!!'):
    duplicou = True
    vidaDemonio = 2 * vidaDemonio
    ataqueDemonio = 2 * ataqueDemonio

  # verifica se o demonio morreu
  vidaDemonio -= ataqueDenji
  if (vidaDemonio <= 0):
    demonios -= 1
    if (duplicou == True):
      contadorMortos += 2
      duplicou = False
    else:
      contadorMortos += 1

    if (demonios > 0):
      print('Matei um!!!')
      vidaDemonio = initVidaDemonio
      ataqueDemonio = initAtaqueDemonio
      if (demonios > 0):
        vidaDenji -= ataqueDemonio
  else:
    if (demonios > 0):
      vidaDenji -= ataqueDemonio

  return demonios, vidaDenji, vidaDemonio, initVidaDemonio, ataqueDenji, ataqueDemonio, initAtaqueDemonio, contadorMortos, duplicou


# variaveis auxiliares
duplicou = False
demonios = int(input())
qtdInicialDemonios = demonios
contadorMortos = 0
terminou = False

if (demonios == 0):
  print('Uhuuul um dia só para relaxar!')
  terminou = True
else:
  # inputs iniciais
  vidaDenji = int(input())
  vidaDemonio = int(input())
  initVidaDemonio = vidaDemonio
  ataqueDenji = int(input())
  ataqueDemonio = int(input())
  initAtaqueDemonio = ataqueDemonio

  # executa enquanto nenhum dos dois morrer
  while (demonios > 0 and vidaDenji > 0):
    demonios, vidaDenji, vidaDemonio, initVidaDemonio, ataqueDenji, ataqueDemonio, initAtaqueDemonio, contadorMortos, duplicou = lutas(demonios, vidaDenji, vidaDemonio, initVidaDemonio, ataqueDenji, ataqueDemonio, initAtaqueDemonio, contadorMortos, duplicou)


if (terminou == False):
  if (vidaDenji <= 0):
    print('Infelizmente Denji foi de comes e bebes :(')
  elif (contadorMortos > qtdInicialDemonios):
    print('Foi mais do que eu esperava mas finalmente terminei…')
  else:
    print('Ufa, agora posso descansar em paz!')