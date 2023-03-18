def comprimirMensagem(mensagem):
  # caso base é a string vazia
  if not mensagem:
    return ""

  char = mensagem[0]
  contador = 1
  i = 1
  # conta quantas vezes a letra foi repetida
  while i < len(mensagem) and mensagem[i] == char:
    contador += 1
    i += 1

  # retorna o numero de letras repetidas + a letra e executa a funcao para o resto da string novamente
  return str(contador) + char + comprimirMensagem(mensagem[i:])


def descomprimirResposta(mensagem, contador, tamanho):
  # caso base é a ultima string com codigo
  if contador == tamanho-2:
    # retorna o char n vezes
    return mensagem[contador+1]*int(mensagem[contador])
  else:
    return mensagem[contador+1]*int(mensagem[contador]) + descomprimirResposta(mensagem, contador + 2, tamanho)


def ajudaChat():
  mensagem = input()
  while mensagem != "Não tô entendendo nada":
    # comprimindo a mensagem e imprimindo mensagem do usuario e chatGPT
    mensagemComprimida = comprimirMensagem(mensagem)

    resultadoSoma = 0
    # somando todos numeros da string
    for i in mensagemComprimida:
      if ord(i) >= 48 and ord(i) <= 57:
        resultadoSoma = resultadoSoma + int(i)

    # retornando mensagem com base na soma
    if resultadoSoma > 0 and resultadoSoma <= 5:
      resposta = "1t3a1 1f1a1c3i1n1h1o1 1n3e"
    elif resultadoSoma > 6 and resultadoSoma <= 20:
      resposta = "1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o"
    elif resultadoSoma > 21 and resultadoSoma <= 30:
      resposta = "1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a"
    elif resultadoSoma > 31 and resultadoSoma <= 40:
      resposta = "1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z"
    elif resultadoSoma > 40:
      resposta = "3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r"

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
    # verificando se existiu resposta
    if resposta == "naoExiste":
      print("Não tem nada pra traduzir")
    else:
      resultado = descomprimirResposta(resposta, 0, len(resposta))
      print(f"Descobri! É: {resultado}, tá de brincadeira né?")
  mensagem = input()
