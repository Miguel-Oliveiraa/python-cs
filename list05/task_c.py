def comprimirMensagem(mensagem):
  contador = 1
  mensagemFinal = ""
  resultadoSoma = 0
  for i in range(0, len(mensagem)-1):
    if mensagem[i] == mensagem[i+1]:
      contador += 1
    else:
      mensagemFinal += f"{contador}" + mensagem[i]
      resultadoSoma += contador
      contador = 1
  mensagemFinal += f"{contador}" + mensagem[i+1]
  resultadoSoma += contador
  contador = 1

  if resultadoSoma > 0 and resultadoSoma <= 5:
    resposta = "1t3a1 1f1a1c3i1n1h1o1 1n3e"
  elif resultadoSoma>6 and resultadoSoma <= 20:
    resposta = "1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o"
  elif resultadoSoma>21 and resultadoSoma <= 30:
    resposta = "1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a"
  elif resultadoSoma>31 and resultadoSoma <= 40:
    resposta = "1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z"
  elif resultadoSoma>40:
    resposta = "3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r"
  return mensagemFinal, resposta

def descomprimirResposta(mensagem):
  resultado = ""
  for i in range(0, len(mensagem)-1, 2):
    for j in range(int(mensagem[i])):
      resultado += mensagem[i+1]
  return resultado

def ajudaChat():
  mensagem = input()
  while mensagem != "Não tô entendendo nada":
    mensagemComprimida, resposta = comprimirMensagem(mensagem)
    print(f"usuário:{mensagemComprimida}")
    print(f"ChatGPT:{resposta}")
    mensagem = input()
  return resposta


mensagem = input()
resposta = "naoExiste"
while mensagem != "Preciso parar de usar o ChatGPT":
  if mensagem == "Vou pedir ajuda pro meu amigo ChatGPT":
    resposta = ajudaChat()
  elif mensagem == "Qual era a tradução?":
    if resposta == "naoExiste":
      print("Não tem nada pra traduzir")
    else:
      resultado = descomprimirResposta(resposta)
      print(f"Descobri! É: {resultado}, tá de brincadeira né?")
  mensagem = input()
