def calcularPorcentagem(numero):
  return int(numero / 10)


def ataque(atacante, dano):
  global vidaDenji
  global vidaDevil
  if atacante == "Denji":
    vidaDevil -= dano
    if vidaDevil < 0:
      vidaDevil = 0
    if vidaDevil > 0 and vidaDenji > 0:
      print(f"Uhu, Denji atacou! A porcentagem de vida atual do Zombie Devil é de {calcularPorcentagem(vidaDevil)}%.")
  else:
    vidaDenji -= dano
    if vidaDenji < 0:
      vidaDenji = 0
    if vidaDevil > 0 and vidaDenji > 0:
      print(
        f"Ah não, Denji foi atacado pelo Zombie Devil! A porcentagem de vida atual de Denji é de {calcularPorcentagem(vidaDenji)}%.")


def defesa(defensor, dano):
  global vidaDenji
  global vidaDevil
  if defensor == "Denji":
    print(
      "Isso aê! O feitiço virou contra o feiticeiro. Denji defendeu o golpe do Zombie Devil e ganhou um bônus de vida.")
    vidaDenji += dano
    vidaDevil -= dano
    if vidaDenji > 1000:
      vidaDenji = 1000
    if vidaDevil < 0:
      vidaDevil = 0
    if vidaDevil > 0 and vidaDenji > 0:
      print(
        f"A porcentagem de vida atual de Denji é de {calcularPorcentagem(vidaDenji)}% e do Zombie Devil é de {calcularPorcentagem(vidaDevil)}%.")
  else:
    print("Ops! O Zombie Devil defendeu o ataque de Denji e ganhou um bônus de vida.")
    vidaDevil += dano
    vidaDenji -= dano
    if vidaDevil > 1000:
      vidaDevil = 1000
    if vidaDenji < 0:
      vidaDenji = 0
    if vidaDevil > 0 and vidaDenji > 0:
      print(
        f"A porcentagem de vida atual de Denji é de {calcularPorcentagem(vidaDenji)}% e do Zombie Devil é de {calcularPorcentagem(vidaDevil)}%.")


def batalha(nome, golpe, dano):
  global vidaDenji
  global vidaDevil

  if (nome != "Denji" and nome != "ZombieDevil"):
    print("Esse personagem não está lutando, escolha entre Denji ou Zombie Devil.")
  elif golpe != "ataque" and golpe != "defesa":
    print("Esse golpe não existe, escolha entre ataque ou defesa.")
  else:
    if golpe == "ataque":
      ataque(nome, dano)
    else:
      defesa(nome, dano)


vidaDenji = 1000
vidaDevil = 1000
print("Denji fez pacto com Pochita. Que comece a luta.")

while (vidaDenji > 0 and vidaDevil > 0):
  nome = input()
  golpe = input()
  dano = int(input())
  resultado = batalha(nome, golpe, dano)

if vidaDenji <= 0:
  print("Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.")

if vidaDevil <= 0:
  print(f"O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!")