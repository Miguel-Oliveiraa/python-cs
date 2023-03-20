def sequenciarIntervalos(numeros):
  # inicia um numero inicial
  inicio = numeros[0]
  final = inicio
  i = 1
  # executa até percorrer todo array ou o numero parar
  while i < len(numeros) and numeros[i] == final + 1:
    final = numeros[i]
    i += 1
  if inicio == final:
    stringDistancia = f"[{inicio}]"
  else:
    stringDistancia = f"[{inicio}-{final}]"
  if i < len(numeros):
    return stringDistancia + ", " + sequenciarIntervalos(numeros[i:])
  # condição de parada, i = tamanho do array
  else:
    return stringDistancia

numeros = input().split(", ")
for i in range(0, len(numeros)):
  numeros[i] = int(numeros[i])

print(sequenciarIntervalos(numeros))