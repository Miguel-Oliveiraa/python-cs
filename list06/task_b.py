numeroPets = int(input())
dictPets = {"nome": [], "situacao": [],"amigos": []}
for i in range(numeroPets):
  linha = input().split(", ")
  dictPets["nome"].append(linha[0]), dictPets["situacao"].append(linha[1]),  dictPets["amigos"].append(tuple(linha[2:len(linha)]))

petsAgitados = []
for i in range(len(dictPets["situacao"])):
  if dictPets["situacao"][i] == "agitado" and 1 < len(dictPets["amigos"][i]) <= 3:
    petsAgitados.append(dictPets["nome"][i])

if not petsAgitados:
  print("Todos estão se divertindo tranquilamente! Os queridos cuidadores podem relaxar!")
elif len(petsAgitados) == 1:
  print(f"Apenas {petsAgitados[0]} está querendo bagunçar, deem carinho e atenção imediatamente!")
else:
  listaPets = ""
  for i in range(len(petsAgitados)):
    if i == len(petsAgitados)-1:
      listaPets += " e " + petsAgitados[i]
    elif i == 0:
      listaPets += petsAgitados[i]
    else:
      listaPets += ", " + petsAgitados[i]
  print(f"Vai ser um trabalho difícil, mas {listaPets} podem acabar atrapalhando os alunos do CIn!")