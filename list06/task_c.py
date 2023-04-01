def imprimirResultado(dicionarioDogs):
  if dicionarioDogs["Aprovados"]:
    print("Estao aprovados e de parabens os seguintes coleguinhas:")
    for i in range(len(dicionarioDogs["Aprovados"])):
      print(f'{dicionarioDogs["Aprovados"][i]["nome"]} - {dicionarioDogs["Aprovados"][i]["raca"]} - media: {dicionarioDogs["Aprovados"][i]["media"]}')

  if dicionarioDogs["Reprovado"]:
    print("Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):")
    for i in range(len(dicionarioDogs["Reprovado"])):
      print(f'{dicionarioDogs["Reprovado"][i]["nome"]} - {dicionarioDogs["Reprovado"][i]["raca"]} - media: {dicionarioDogs["Reprovado"][i]["media"]}')

  if dicionarioDogs["Recuperacao"]:
    print("Esses queridos terao uma nova chance e prometem melhorar:")
    for i in range(len(dicionarioDogs["Recuperacao"])):
      print(f'{dicionarioDogs["Recuperacao"][i]["nome"]} - {dicionarioDogs["Recuperacao"][i]["raca"]} - media: {dicionarioDogs["Recuperacao"][i]["media"]}')


def calcularMedia(listaStrings):
  for i in range(len(listaStrings)):
    listaStrings[i] = float(listaStrings[i])
  # mediaFinal = "{:.2f}".format((listaStrings[0] + listaStrings[1] + listaStrings[2])/3)
  mediaFinal = format((listaStrings[0] + listaStrings[1] + listaStrings[2])/3, ".2f")
  return mediaFinal


def avaliaDog(dicionarioDogs):
  dados = input().split(", ")
  informacoesDog = {"nome": dados[0], "raca": dados[1], "media": calcularMedia(dados[2:])}
  if float(informacoesDog["media"]) >= 3:
    dicionarioDogs["Aprovados"].append(informacoesDog)
  elif float(informacoesDog["media"]) >= 2:
    dicionarioDogs["Recuperacao"].append(informacoesDog)
  else:
    dicionarioDogs["Reprovado"].append(informacoesDog)
  return dicionarioDogs


def main():
  numeroDog = int(input())

  resultadoDog = {"Aprovados": [], "Recuperacao": [], "Reprovado": []}
  for i in range(numeroDog):
    resultadoDog = avaliaDog(resultadoDog)
  imprimirResultado(resultadoDog)

main()