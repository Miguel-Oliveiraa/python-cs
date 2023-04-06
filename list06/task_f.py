def verificaRotas(gatoInicial, alvo, dicionario, visitados=[], caminhoAtual=None):
  if caminhoAtual is None:
    caminhoAtual = [gatoInicial]

  # popula a lista de visitados
  visitados.append(gatoInicial)
  rotas = []

  for amigo in dicionario[gatoInicial]['amigos']:
    # verifica existem amigos, e se ja foram visitados
    if amigo not in visitados and amigo != '':
      if amigo == alvo:
        rotas.append(caminhoAtual + [amigo])
      else:
        # executa recursivamente, passando uma copia dos visitados e o novo caminho
        novaRota = verificaRotas(amigo, alvo, dicionario, visitados.copy(), caminhoAtual + [amigo])

        # verifica todas rotas encontradas
        for novaRota in novaRota:
          # adciona as rotas com o alvo procurado
          if alvo in novaRota:
            rotas.append(novaRota)

  return rotas

def main():
  relacionamentos = {}

  # recebe as informações dos gatos
  qtdGatos = int(input())
  for i in range(qtdGatos):
    nomeGato = input()
    relacionamentosBom = input().split(" ")
    relacionamentosRuim = input().split(" ")
    relacionamentos[nomeGato] = {}
    relacionamentos[nomeGato]["amigos"] = relacionamentosBom
    relacionamentos[nomeGato]["inimigos"] = relacionamentosRuim
  gatoInicial = input()
  gatoAlvo = input()

  if gatoAlvo in relacionamentos[gatoInicial]["inimigos"]:
    print(f"Eu não falo com {gatoAlvo}! Mas fico feliz por ter sido edificado com essa fofoca")
  elif gatoAlvo in relacionamentos[gatoInicial]["amigos"]:
    print("Fofoca? Aceito. Vou contar agora mesmo, miau miau")
  else:
    rotas = verificaRotas(gatoInicial, gatoAlvo, relacionamentos)
    rotas.sort(key=len)

    if rotas:
      mensagem = ""
      for i in range(len(rotas[0]) - 1):
        if i == 0:
          mensagem += rotas[0][0]
          continue
        mensagem += " que contou a " + rotas[0][i]
      print(f"Finalmente recebi a fofoca! Ela começou em {mensagem} e chegou em mim")
    else:
      print("Infelizmente não tem como fofocar, melhor procurar outro gato!")


main()
