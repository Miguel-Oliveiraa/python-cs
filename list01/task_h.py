# dados do jogador Um
nomeJogadorUm = str(input())
bolasNaAreaJogadorUm = int(input())
finalizacoesJogadorUm = int(input())
golsJogadorUm = int(input())
resultadoJogadorUm = bolasNaAreaJogadorUm

# dados do jogador Dois
nomeJogadorDois = str(input())
bolasNaAreaJogadorDois = int(input())
finalizacoesJogadorDois = int(input())
golsJogadorDois = int(input())
resultadoJogadorDois = bolasNaAreaJogadorDois

# dados do jogador Tres
nomeJogadorTres = str(input())
bolasNaAreaJogadorTres = int(input())
finalizacoesJogadorTres = int(input())
golsJogadorTres = int(input())
resultadoJogadorTres = bolasNaAreaJogadorTres

# Comparando caso houve empate por bolas na area
if bolasNaAreaJogadorUm == bolasNaAreaJogadorDois and bolasNaAreaJogadorUm > bolasNaAreaJogadorTres:
  print("Tite está mais indeciso do que nunca!")
  resultadoJogadorUm = golsJogadorUm / finalizacoesJogadorUm
  resultadoJogadorDois = golsJogadorDois / finalizacoesJogadorDois
  resultadoJogadorTres = 0
elif bolasNaAreaJogadorDois == bolasNaAreaJogadorTres and bolasNaAreaJogadorDois > bolasNaAreaJogadorUm:
  print("Tite está mais indeciso do que nunca!")
  resultadoJogadorTres = golsJogadorTres / finalizacoesJogadorTres
  resultadoJogadorDois = golsJogadorDois / finalizacoesJogadorDois
  resultadoJogadorUm = 0
elif bolasNaAreaJogadorTres == bolasNaAreaJogadorUm and bolasNaAreaJogadorTres > bolasNaAreaJogadorDois:
  print("Tite está mais indeciso do que nunca!")
  resultadoJogadorUm = golsJogadorUm / finalizacoesJogadorUm
  resultadoJogadorTres = golsJogadorTres / finalizacoesJogadorTres
  resultadoJogadorDois = 0
elif bolasNaAreaJogadorTres == bolasNaAreaJogadorDois == bolasNaAreaJogadorUm:
  print("Tite está mais indeciso do que nunca!")
  resultadoJogadorUm = golsJogadorUm / finalizacoesJogadorUm
  resultadoJogadorDois = golsJogadorDois / finalizacoesJogadorDois
  resultadoJogadorTres = golsJogadorTres / finalizacoesJogadorTres
  # casos de empate menor
elif bolasNaAreaJogadorUm == bolasNaAreaJogadorDois and bolasNaAreaJogadorUm < bolasNaAreaJogadorTres:
  resultadoJogadorUm = golsJogadorUm / finalizacoesJogadorUm
  resultadoJogadorDois = golsJogadorDois / finalizacoesJogadorDois
elif bolasNaAreaJogadorDois == bolasNaAreaJogadorTres and bolasNaAreaJogadorDois < bolasNaAreaJogadorUm:
  resultadoJogadorTres = golsJogadorTres / finalizacoesJogadorTres
  resultadoJogadorDois = golsJogadorDois / finalizacoesJogadorDois
elif bolasNaAreaJogadorTres == bolasNaAreaJogadorUm and bolasNaAreaJogadorTres < bolasNaAreaJogadorDois:
  resultadoJogadorUm = golsJogadorUm / finalizacoesJogadorUm
  resultadoJogadorTres = golsJogadorTres / finalizacoesJogadorTres

# ordenando por pontos
if resultadoJogadorUm > resultadoJogadorDois:
  if resultadoJogadorDois > resultadoJogadorTres:
      jogadorEscolhido = 1
      print(f"{nomeJogadorUm}")
      print(f"{nomeJogadorDois}")
      print(f"{nomeJogadorTres}")
  else:
      if resultadoJogadorUm > resultadoJogadorTres:
          jogadorEscolhido = 1
          print(f"{nomeJogadorUm}")
          print(f"{nomeJogadorTres}")
          print(f"{nomeJogadorDois}")
      else:
          jogadorEscolhido = 3
          print(f"{nomeJogadorTres}")
          print(f"{nomeJogadorUm}")
          print(f"{nomeJogadorDois}")
else:
  if resultadoJogadorTres > resultadoJogadorDois:
      jogadorEscolhido = 3
      print(f"{nomeJogadorTres}")
      print(f"{nomeJogadorDois}")
      print(f"{nomeJogadorUm}")
  else:
      if resultadoJogadorTres > resultadoJogadorUm:
          jogadorEscolhido = 2
          print(f"{nomeJogadorDois}")
          print(f"{nomeJogadorTres}")
          print(f"{nomeJogadorUm}")
      else:
          jogadorEscolhido = 2
          print(f"{nomeJogadorDois}")
          print(f"{nomeJogadorUm}")
          print(f"{nomeJogadorTres}")

# armazenando o 1 jogador
if jogadorEscolhido == 1:
    nomeJogadorEscolhido = nomeJogadorUm
    bolasNaAreaJogadorEscolhido = bolasNaAreaJogadorUm
elif jogadorEscolhido == 2:
    nomeJogadorEscolhido = nomeJogadorDois
    bolasNaAreaJogadorEscolhido = bolasNaAreaJogadorDois
elif jogadorEscolhido == 3:
    nomeJogadorEscolhido = nomeJogadorTres
    bolasNaAreaJogadorEscolhido = bolasNaAreaJogadorTres

# printando o final
print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")

# printando caso o jogador escolhido seja bom ou nao
if bolasNaAreaJogadorEscolhido <= 10:
    print(f"{nomeJogadorEscolhido}?! Sei não hein Galvão…")
else:
    print(f"{nomeJogadorEscolhido}! Dessa vez o hexa vem pra casa!!")