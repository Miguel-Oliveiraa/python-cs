def calcularPorcentagem(numero):
  return numero/10

def recebeStatus(denji, zombieDevil):
  nome = input()
  golpe = input()
  dano = input()

  if nome != "Denji" or nome != "ZombieDevil":
    print("Esse personagem não está lutando, escolha entre Denji ou Zombie Devil.")
  elif nome == "Denji":
    if golpe == "ataque":
      zombieDevil[2] -= dano
      if zombieDevil[2] < 0:
        zombieDevil[2] = 0
      print(f"Uhu, Denji atacou! A porcentagem de vida atual do Zombie Devil é de {calcularPorcentagem(denji[2])}%.")
    elif golpe == "defesa":
      print("Isso aê! O feitiço virou contra o feiticeiro. Denji defendeu o golpe do Zombie Devil e ganhou um bônus de vida.")
      denji[2] += dano
      if denji[2] > 1000:
        denji[2] = 1000
      zombieDevil[2] -= dano
      if zombieDevil[2] < 0:
        zombieDevil[2] = 0
  elif nome == "ZombieDevil":
    if golpe == "ataque":
      denji[2] -= dano
      if denji[2] < 0:
        denji[2] = 0
      print(f"Ah não, Denji foi atacado pelo Zombie Devil! A porcentagem de vida atual de Denji é de {calcularPorcentagem(denji[2])}%.")
    elif golpe == "defesa":
      print("Ops! O Zombie Devil defendeu o ataque de Denji e ganhou um bônus de vida.")
      zombieDevil[2] += dano
      if zombieDevil[2] > 1000:
        zombieDevil[2] = 1000
      denji[2] -= dano
      if denji[2] < 0:
        denji[2] = 0


denji = ["Denji", 0, 1000]
zombieDevil = ["Zombie Devil", 0, 1000]

print("Denji fez pacto com Pochita. Que comece a luta.")
while denji[2] > 0 and zombieDevil[2] > 0:
  recebeStatus(denji, zombieDevil)
  print(f"A porcentagem de vida atual de Denji é de {calcularPorcentagem(denji[2])}% e do Zombie Devil é de {calcularPorcentagem(zombieDevil[2])}%.")

if denji[2] == 0:
  print("Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.")
else:
  print(f"O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!")