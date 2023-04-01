def formataListaPets(listaNomes):
  listaPets = ""
  for i in range(len(listaNomes)):
    if i == len(listaNomes) - 1:
      listaPets += " e " + listaNomes[i]
    elif i == 0:
      listaPets += listaNomes[i]
    else:
      listaPets += ", " + listaNomes[i]
  return listaPets

def main():
  numeroPets = int(input())
  dicionarioPets = {"nome": [], "situacao": [],"amigos": []}

  # armazena nome, situacao e uma tupla de amigos do pet no dict
  for i in range(numeroPets):
    dados = input().split(", ")
    dicionarioPets["nome"].append(dados[0]), dicionarioPets["situacao"].append(dados[1]), dicionarioPets["amigos"].append(tuple(dados[2:len(dados)]))


  petsBagunceiros = []

  # verifica os animais que bagucam e coloca na lista
  for i in range(len(dicionarioPets["situacao"])):
    if (dicionarioPets["situacao"][i] == "agitado" and len(dicionarioPets["amigos"][i]) <= 3) or len(dicionarioPets["amigos"][i]) == 1:
      petsBagunceiros.append(dicionarioPets["nome"][i])


  if not petsBagunceiros:
    print("Todos estão se divertindo tranquilamente! Os queridos cuidadores podem relaxar!")
  elif len(petsBagunceiros) == 1:
    print(f"Apenas {petsBagunceiros[0]} está querendo bagunçar, deem carinho e atenção imediatamente!")
  else:
    print(f"Vai ser um trabalho difícil, mas {formataListaPets(petsBagunceiros)} podem acabar atrapalhando os alunos do CIn!")

main()
