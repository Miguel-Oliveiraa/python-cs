def verificaInimigos(animais, animaisEscolhidos):
  inimigos = False

  # itera sobre cada animal
  for i in animaisEscolhidos:

      # itera para cada animal
      for j in animaisEscolhidos:

          # caso o segundo animal seja inimigo do primeiro
          if j in animais[i]["inimigos"]:
              print(f"Sérgio, o(a) {i} tem o(a) {j} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos")
              inimigos = True


  return inimigos


def imprimeNecessidades(animais, animaisEscolhidos, recemNascido):
  if recemNascido:
    print("Como os animais são recém nascidos, eles podem ser adotados juntos!")
    print("Segue aqui as necessidades dos animais:")
  else:
    print("Segue aqui as necessidades dos animais:")

  # imprime as necessidades do animais
  for i in animaisEscolhidos:
    print(f"As necessidades do(a) {i} são:")
    for j in animais[i]["necessidades"]:
      print(f"- {j};")
  print("Dito isso, vamos adotá-los!!!")


def verificaAnimais(animaisEscolhidos):
  animais = ["cachorro", "gato", "hamster", "peixe"]
  animaisInvalidos = []

  # coloca os animais invalidos na lista
  for i in animaisEscolhidos:
    if i not in animais:
      animaisInvalidos.append(i)
  return animaisInvalidos


def main():
  animais = {
    "cachorro": {"inimigos": ["gato"], "necessidades": ["coleira", "ração", "ursinho de pelúcia"]},
    "gato": {"inimigos": ["cachorro", "hamster", "peixe"],
             "necessidades": ["bola de lã", "caixa de areia", "ração", "ratinho de brinquedo"]},
    "hamster": {"inimigos": ["cachorro", "gato"], "necessidades": ["ração", "roda para hamster", "serragem"]},
    "peixe": {"inimigos": ["gato"], "necessidades": ["aquário", "filtro", "ração"]},
  }

  # recebe os inputs e verifica eles
  animaisEscolhidos = input().split(" e ")
  recemNascido = True if input() == "sim" else False
  animaisInvalidos = verificaAnimais(animaisEscolhidos)

  if animaisInvalidos:
    for i in animaisInvalidos:
      print(f"Sérgio, o animal {i} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.")
  else:
    if recemNascido:
      imprimeNecessidades(animais, animaisEscolhidos, recemNascido)
    else:
      if not verificaInimigos(animais, animaisEscolhidos):
        imprimeNecessidades(animais, animaisEscolhidos, recemNascido)


main()
