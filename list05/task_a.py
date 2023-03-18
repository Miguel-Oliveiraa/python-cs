numeros = input().split(" ")
alvo = int(input())
razao = int(numeros[1]) - int(numeros[0])

def calcularNumero(numero, alvo, contador, razao):
  if contador == alvo:
    return numero
  else:
    return calcularNumero(numero + razao, alvo, contador+1, razao)

print(f"Na progressão aritmética cujos três primeiros números são {numeros[0]}, {numeros[1]} e {numeros[2]}, o {alvo}º "
      f"elemento é {calcularNumero(int(numeros[0]), alvo, 1, razao)} e a razão da progressão é {razao}.")