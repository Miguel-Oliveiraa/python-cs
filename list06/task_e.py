def vaquinha(quantidade, energia, energiaGasta):
  energiaGasta += min(int(quantidade), energia)
  energia -= int(quantidade)
  energia = max(energia, 0)
  print("Brinquedo da vaquinha! Vou chacoalhar")
  return energia, energiaGasta


def chupeta(quantidade, energia, energiaGasta):
  energiaInicial = energia
  menorEnergia = min(int(quantidade), maiorEnergia)
  energia = max(energia - 5, menorEnergia)
  energia = min(energia, maiorEnergia)
  menorEnergia = energiaInicial - energia
  energiaGasta += (menorEnergia + abs(menorEnergia)) / 2
  print("Minha pipeta! Vou morder")
  return energia, energiaGasta


def gotinha(quantidade, energia, energiaGasta):
  energiazinha = energia
  energia = energia / max(int(quantidade), 1)
  energiaGastaparcial = energiazinha - energia
  energiaGasta += energiaGastaparcial
  print("Meu preferido! Faz barulho e mordo")
  return energia, energiaGasta


def bolinha(quantidade, energia, energiaGasta):
  energiaGastaparcial = int(int(quantidade) / 4)
  energiaGasta += min(energiaGastaparcial, energia)
  energia -= energiaGastaparcial
  energia = max(energia, 0)
  print("ZOOOOOOOOOOOOOOOOOM")
  return energia, energiaGasta


def osso(quantidade, energia, energiaGasta):
  energiaGastaparcial = 2 * int(quantidade)
  energia += energiaGastaparcial
  energia = min(energia, maiorEnergia)
  print("Pausa para roer")
  return energia, energiaGasta


def comida(quantidade, energia, energiaGasta):
  maximapassiva = energia
  energiaGastaparcial = len(quantidade)
  energia += energiaGastaparcial * (-1) ** energiaGastaparcial
  energia = min(energia, maiorEnergia)
  energia = max(energia, 0)
  energiaGastaparcial = maximapassiva - energia
  energiaGasta += (energiaGastaparcial + energiaGastaparcial * (-1) ** (len(quantidade) + 1)) / 2
  print(f"Uhh, {quantidade} deve ser comestível")
  return energia, energiaGasta


energia = int(input())
status = {"energia": energia, "energiaGasta": 0}
maiorEnergia = status["energia"]

funcoes = {"Vaquinha": vaquinha, "Zé Gotinha": gotinha, "Chupeta": chupeta, "Bolinha": bolinha, "Osso": osso,
           "Comida": comida}

while status["energia"] > 0 and status["energiaGasta"] < 100:
  brincadeira, quantidade = input().split(": ")
  status["energia"], status["energiaGasta"] = funcoes[brincadeira](quantidade, status["energia"], status["energiaGasta"])

status["energiaGasta"] = min(status["energiaGasta"], 100)

num_a = 'a' * max(int(status["energiaGasta"] / 10), 1)

print(
  f"Mamãe chegou! Gastei {status['energiaGasta']:.0f} pontos da minha energia e estou c{num_a}nsada, mas vou correr para seus braços!")