def calcularPorcentagem(numero):
  return int(numero / 10)


def ataque(vidaDenji, vidaDevil, atacante, dano):

  # decremente a vida do que não atacou
  if atacante == "Denji":
    vidaDevil -= dano
    if vidaDevil < 0:
      vidaDevil = 0
    if vidaDevil > 0 and vidaDenji > 0:
      print(f"Uhu, Denji atacou! A porcentagem de vida atual do Zombie Devil é de {calcularPorcentagem(vidaDevil)}%.")

  elif atacante == "ZombieDevil":
    vidaDenji -= dano
    if vidaDenji < 0:
      vidaDenji = 0
    if vidaDevil > 0 and vidaDenji > 0:
      print(f"Ah não, Denji foi atacado pelo Zombie Devil! A porcentagem de vida atual de Denji é de {calcularPorcentagem(vidaDenji)}%.")

  return vidaDenji, vidaDevil


def defesa(vidaDenji, vidaDevil, defensor, dano):

  # incrementa a vida de quem defendeu e decrementa a vida do outro
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
      print(f"A porcentagem de vida atual de Denji é de {calcularPorcentagem(vidaDenji)}% e do Zombie Devil é de {calcularPorcentagem(vidaDevil)}%.")

  elif defensor == "ZombieDevil":
    print("Ops! O Zombie Devil defendeu o ataque de Denji e ganhou um bônus de vida.")
    vidaDevil += dano
    vidaDenji -= dano
    if vidaDevil > 1000:
      vidaDevil = 1000
    if vidaDenji < 0:
      vidaDenji = 0
    if vidaDevil > 0 and vidaDenji > 0:
      print(f"A porcentagem de vida atual de Denji é de {calcularPorcentagem(vidaDenji)}% e do Zombie Devil é de {calcularPorcentagem(vidaDevil)}%.")

  return vidaDenji, vidaDevil


def batalha(vidaDenji, vidaDevil, nome, golpe, dano):

  # valida o nome
  if nome != "Denji" and nome != "ZombieDevil":
    print("Esse personagem não está lutando, escolha entre Denji ou Zombie Devil.")

  # valida o golpe
  if golpe != "ataque" and golpe != "defesa":
    print("Esse golpe não existe, escolha entre ataque ou defesa.")
  else:

    # atualiza a vida de acordo com o tipo de golpe
    if golpe == "ataque":
      vidaDenji, vidaDevil = ataque(vidaDenji, vidaDevil, nome, dano)

    else:
      vidaDenji, vidaDevil = defesa(vidaDenji, vidaDevil, nome, dano)

  return vidaDenji, vidaDevil


# inicio do codigo
vidaDenji = 1000
vidaDevil = 1000
print("Denji fez pacto com Pochita. Que comece a luta.")

# recebe os inputs e executa batalha ate um dos dois morrer
while (vidaDenji > 0 and vidaDevil > 0):
  nome = input()
  golpe = input()
  dano = int(input())

  # atualiza a vida dos personagens de acordo com a batalha
  vidaDenji, vidaDevil = batalha(vidaDenji, vidaDevil, nome, golpe, dano)

if vidaDenji <= 0:
  print("Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.")
elif vidaDevil <= 0:
  print(f"O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!")