def sequenciarIntervalos(numeros):

  # inicia um numero inicial
  inicio = numeros[0]
  final = inicio
  i = 1

  # executa até percorrer tudo ou o numero[i] ser diferente de numero[i+1]
  while i < len(numeros) and numeros[i] == final + 1:
    final = numeros[i]
    i += 1

  # concatena o numero sozinho ou o intervalo
  if inicio == final:
    stringDistancia = f"[{inicio}]"
  else:
    stringDistancia = f"[{inicio}-{final}]"

  if i < len(numeros):
    return stringDistancia + ", " + sequenciarIntervalos(numeros[i:])

  # condição de parada, i = tamanho do array
  else:
    return stringDistancia

# tranforma o array de string em arr de inteiros
numeros = input().split(", ")
for i in range(0, len(numeros)):
  numeros[i] = int(numeros[i])

print(sequenciarIntervalos(numeros))