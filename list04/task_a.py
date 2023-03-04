def verificaPrimo(numero):
  contador = 0
  # conta os multiplos de n
  for i in range(1, numero + 1):
    if numero % i == 0:
      contador += 1
  # se os multiplos = 2 é primo
  if contador == 2:
    return True
  return False


numero = int(input())

if verificaPrimo(numero):
  print(f"O número {numero} é primo.")
else:
  print(f"O número {numero} não é primo.")
  # verifica quais são os primos antes dele
  resultado = []
  for i in range(2, numero):
    if verificaPrimo(i):
      resultado.append(i)
  if len(resultado) == 0:
    print(f"Além disso, não temos primos no intervalo de 1 à {numero}.")
  else:
    print(f"Entretanto, temos primos no intervalo de 1 à {numero}. Estes são:")
    print(*resultado, sep=", ")

print("AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!")