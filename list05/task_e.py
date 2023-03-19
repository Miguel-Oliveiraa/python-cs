def sequenciarIntervalos(numeros):
  if not numeros:
    return ""
  inicio = numeros[0]
  final = inicio
  i = 1
  while i < len(numeros) and numeros[i] == final + 1:
    final = numeros[i]
    i += 1
  if inicio == final:
    stringDistancia = f"[{inicio}]"
  else:
    stringDistancia = f"[{inicio}-{final}]"
  if i < len(numeros):
    return stringDistancia + ", " + sequenciarIntervalos(numeros[i:])
  else:
    return stringDistancia

numeros = input().split(", ")
for i in range(0, len(numeros)):
  numeros[i] = int(numeros[i])

print(sequenciarIntervalos(numeros))