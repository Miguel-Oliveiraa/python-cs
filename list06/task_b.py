def formataListaPets(lista):
  listaPets = ""
  for i in range(len(lista)):
    if i == len(lista) - 1:
      listaPets += " e " + lista[i]
    elif i == 0:
      listaPets += lista[i]
    else:
      listaPets += ", " + lista[i]
  return listaPets

def main():
  numeroPets = int(input())
  dictPets = {"nome": [], "situacao": [],"amigos": []}

  # armazena nome, situacao e uma tupla de amigos do pet no dict
  for i in range(numeroPets):
    dados = input().split(", ")
    dictPets["nome"].append(dados[0]), dictPets["situacao"].append(dados[1]),  dictPets["amigos"].append(tuple(dados[2:len(dados)]))


  petsBagunceiros = []

  # verifica os animais que bagucam e coloca na lista
  for i in range(len(dictPets["situacao"])):
    if (dictPets["situacao"][i] == "agitado" and len(dictPets["amigos"][i]) <= 3) or len(dictPets["amigos"][i]) == 1:
      petsBagunceiros.append(dictPets["nome"][i])


  if not petsBagunceiros:
    print("Todos estão se divertindo tranquilamente! Os queridos cuidadores podem relaxar!")
  elif len(petsBagunceiros) == 1:
    print(f"Apenas {petsBagunceiros[0]} está querendo bagunçar, deem carinho e atenção imediatamente!")
  else:
    print(f"Vai ser um trabalho difícil, mas {formataListaPets(petsBagunceiros)} podem acabar atrapalhando os alunos do CIn!")

main()
