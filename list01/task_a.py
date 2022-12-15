nomeJogador = str(input())

if nomeJogador == "Alisson":
  posicao = "goleiro"
elif nomeJogador == "Ederson":
  posicao = "goleiro"
elif nomeJogador == "Weverton":
  posicao = "goleiro"
elif nomeJogador == "Marquinhos":
  posicao = "zagueiro"
elif nomeJogador == "Thiago Silva":
  posicao = "zagueiro"
elif nomeJogador == "Éder Militão":
  posicao = "zagueiro"
elif nomeJogador == "Bremer":
  posicao = "zagueiro"
elif nomeJogador == "Daniel Alves":
  posicao = "lateral"
elif nomeJogador == "Danilo":
  posicao = "lateral"
elif nomeJogador == "Alex Sandro":
  posicao = "lateral"
elif nomeJogador == "Alex Telles":
  posicao = "lateral"
elif nomeJogador == "Casemiro":
  posicao = "meia"
elif nomeJogador == "Fabinho":
  posicao = "meia"
elif nomeJogador == "Fred":
  posicao = "meia"
elif nomeJogador == "Bruno Guimarães":
  posicao = "meia"
elif nomeJogador == "Lucas Paquetá":
  posicao = "meia"
elif nomeJogador == "Everton Ribeiro":
  posicao = "meia"
elif nomeJogador == "Neymar":
  posicao = "atacante"
elif nomeJogador == "Raphinha":
  posicao = "atacante"
elif nomeJogador == "Vini Jr.":
  posicao = "atacante"
elif nomeJogador == "Antony":
  posicao = "atacante"
elif nomeJogador == "Richarlison":
  posicao = "atacante"
elif nomeJogador == "Rodrygo":
  posicao = "atacante"
elif nomeJogador == "Pedro":
  posicao = "atacante"
elif nomeJogador == "Gabriel Jesus":
  posicao = "atacante"
elif nomeJogador == "Gabriel Martinelli":
  posicao = "atacante"
else:
  posicao = False


if posicao:
  print(f"{nomeJogador} foi convocado e jogará como {posicao}!")
else:
  print(f"{nomeJogador} não foi convocado, mas quem sabe na próxima?")
