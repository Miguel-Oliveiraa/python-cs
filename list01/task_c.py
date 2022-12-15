nome = input()
disposicao = int(input())

if disposicao >= 85:
  posicao = input()
  chutes_passes = int(input())
  if posicao == "atacante":
    if chutes_passes > 10:
      print(f"{nome} esta com um bom desempenho")
    else:
      print(f"{nome} pode melhorar, coloque-o no segundo tempo")
  elif posicao != "atacante":
    if chutes_passes>=20:
      print(f"{nome} esta com um bom desempenho")
    else:
      print(f"{nome} pode melhorar, nao entrara no primeiro tempo")
elif disposicao > 50:
  desempenho_ultimo_jogo = int(input())
  if desempenho_ultimo_jogo>80:
    print(f"Jogador {nome} pode ser escalado")
  else:
    print(f"Analisar o desempenho do {nome} na partida")
else:
  desempenho_ultimo_treino = int(input())
  if desempenho_ultimo_treino>70:
    print(f"Voce deve colocar {nome} para treinar mais")
  else:
    print(f"{nome} nao deveria estar na copa")