def transformaHora(numero, sufixo):
  if numero == 0:
    return False
  if sufixo == "am":
    if numero == 12:
      return 12
    return numero
  if sufixo == "pm":
    if numero == 12:
      return 12
    return numero + 12


def calcProbabilidade(hora, qtdPessoas):
  if hora == 5:
    return 5.0
  elif 6 <= hora <= 15:
    if hora % 2 == 0:
      return calcProbabilidade((hora - 1)%24, qtdPessoas) + qtdPessoas / 2
    else:
      return calcProbabilidade((hora - 1)%24, qtdPessoas) + calcProbabilidade((hora - 1)%24, qtdPessoas) % 7
  else:
    if hora % 2 == 0:
      return calcProbabilidade((hora - 1)%24, qtdPessoas) + qtdPessoas
    else:
      return calcProbabilidade((hora - 1)%24, qtdPessoas) + calcProbabilidade((hora - 1)%24, qtdPessoas) % 10


horario = input().split(" ")
horario[0] = int(horario[0])
qtdPessoas = int(input())

hora = transformaHora(horario[0], horario[1])

if hora and qtdPessoas >= 0:
  probabilidade = calcProbabilidade(hora, qtdPessoas)
  print(f"A chance de aparecimento de Tubarao e de {probabilidade}%.")
  if probabilidade >= 100:
    print("E hoje que ele aparece.")
else:
  print("Dados Invalidos.")