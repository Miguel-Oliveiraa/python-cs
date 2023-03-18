def comprimirMensagem(mensagem):
  contador = 1
  mensagemFinal = ""
  resultadoSoma = 0
  for i in range(0, len(mensagem)-1):
    if mensagem[i] == mensagem[i+1]:
      print(mensagem[i], mensagem[i + 1])
      contador += 1
    else:
      mensagemFinal += f"{contador}" + mensagem[i]
      resultadoSoma += contador
      contador = 1
  return mensagemFinal, resultadoSoma

def ajudaChat():
  mensagem = input()
  while mensagem != "Não tô entendendo nada":
    mensagemComprimida, resultadoSoma = comprimirMensagem(mensagem)
    print(mensagemComprimida)
    mensagem = input()


mensagem = input()
if mensagem == "Vou pedir ajuda pro meu amigo ChatGPT":
  ajudaChat()