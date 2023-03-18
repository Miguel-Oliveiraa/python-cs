def probabilidadebilidade(nome):
  global lista
  global qtdMorte
  global qtdVivo
  if (len(nome) > 7):
    print(f'Er {nome[0]}{nome[1]}.. errr... nao consigo lembrar, melhor deixar para la')
  else:
    if (nome == 'Makima'):
      print(f"Woof Woof")
      probabilidade = int(input())
      print(f"Beleza {nome}!! Essa é uma boa pretendente!")
      qtdVivo += 1
    else:
      probabilidade = int(input())
      if (probabilidade > 50):
        print(
          f"{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?")
        qtdMorte += 1
        if (lista == ''):
          lista += f'nome: {nome} - chances de morrer: {probabilidade}%'
        else:
          lista += f'\nnome: {nome} - chances de morrer: {probabilidade}%'
      elif (probabilidade <= 50):
        print(f"Beleza {nome}!! Essa é uma boa pretendente!")
        qtdVivo += 1
        if (lista == ''):
          lista += f'nome: {nome} - chances de morrer: {probabilidade}%'
        else:
          lista += f'\nnome: {nome} - chances de morrer: {probabilidade}%'


qtdMorte = 0
qtdVivo = 0
lista = ''
entrada = input()
while (entrada != 'cabo'):
  probabilidadebilidade(entrada)
  entrada = input()

if (qtdVivo > qtdMorte):
  print("Epa ai sim! E hoje pochita!!")
else:
  print("Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos")

if (qtdMorte == 0):
  print(lista)
