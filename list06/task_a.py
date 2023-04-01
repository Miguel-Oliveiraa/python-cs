def main():
  numeroAnimais = int(input())
  dicionario = {"nomeAnimal": [], "especie": [], "dataNascimento": []}

  # recebendo dados dos animais
  for i in range(numeroAnimais):
    linha = input().split(" ")
    dicionario["nomeAnimal"].append(linha[0]), dicionario["especie"].append(linha[1]), dicionario[
      "dataNascimento"].append(linha[2])

  mesSelecionado = int(input())

  # cria um array com o nome e especie dos aniversariantes
  listaAniversariantes = []
  for i in range(numeroAnimais):
    date = dicionario["dataNascimento"][i].split("/")
    if int(date[1]) == mesSelecionado:
      listaAniversariantes.append([dicionario["nomeAnimal"][i], dicionario["especie"][i]])

  if not listaAniversariantes:
    print("Sem festa esse mes. :(")
  else:
    print("E os donos da festa do mes sao:")

    # ordena a lista pelo valor da posicao 0
    listaAniversariantes.sort(key=lambda valor: valor[0])
    for i in listaAniversariantes:
      print(i[0], "-", i[1])


main()