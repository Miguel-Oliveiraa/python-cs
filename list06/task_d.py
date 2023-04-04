def verificaInimigos(animais, animaisEscolhidos):
  inimigos = False
  for i in animaisEscolhidos:
    for j in animais[i]["inimigos"]:
      if j in animaisEscolhidos:
        inimigos = True
        print(
          f"Sérgio, o(a) {i} tem o(a) {j} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos")
  return inimigos


def imprimeNecessidades(animais, animaisEscolhidos, recemNascido):
  if recemNascido:
    print("Como os animais são recém nascidos, eles podem ser adotados juntos!")
    print("Segue aqui as necessidades dos animais:")
  else:
    print("Segue aqui as necessidades dos animais:")

  for i in animaisEscolhidos:
    print(f"As necessidades do(a) {i} são:")
    for j in animais[i]["necessidades"]:
      print(f"- {j};")
  print("Dito isso, vamos adotá-los!!!")


def verificaAnimais(animaisEscolhidos):
  animais = ["cachorro", "gato", "hamster", "peixe"]
  animaisInvalidos = []
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

  animaisEscolhidos = input().split(" e ")
  recemNascido = input()
  recemNascido = True if recemNascido == "sim" else False
  animaisInvalidos = verificaAnimais(animaisEscolhidos)

  if animaisInvalidos == []:
    if recemNascido:
      imprimeNecessidades(animais, animaisEscolhidos, recemNascido)
    else:
      if not verificaInimigos(animais, animaisEscolhidos):
        imprimeNecessidades(animais, animaisEscolhidos, recemNascido)
  else:
    for i in animaisInvalidos:
      print(f"Sérgio, o animal {i} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.")


main()
