def verificaRotas(relacionamentos, gatoInicial, gatoAlvo, rotas=[]):
  rotas = rotas + [gatoInicial]
  rotas = []
  for amigo in relacionamentos[gatoInicial]["Bons"]:
    if amigo not in rotas:
      novaRota = verificaRotas(relacionamentos, amigo, gatoAlvo, rotas)
      for novaRota in novaRota:
        rotas.append(novaRota)
  return rotas



def main():
  relacionamentos = {}
  qtdGatos = int(input())
  for i in range(qtdGatos):
    nomeGato = input()
    bonsRelacionamentos = input().split(" ")
    mausRelacionamentos = input().split(" ")
    relacionamentos[nomeGato] = {}
    relacionamentos[nomeGato]["Bons"] = bonsRelacionamentos
    relacionamentos[nomeGato]["Maus"] = mausRelacionamentos
  gatoInicial = input()
  gatoAlvo = input()

  rotas = []
  if gatoAlvo in relacionamentos[gatoInicial]["Maus"]:
    print(f"Eu não falo com {gatoAlvo}! Mas fico feliz por ter sido edificado com essa fofoca")
  elif gatoAlvo in relacionamentos[gatoInicial]["Bons"]:
    print("Fofoca? Aceito. Vou contar agora mesmo, miau miau")
  else:
    rotas = verificaRotas(relacionamentos, gatoInicial, gatoAlvo)
    rotas.sort(key=len)


  if rotas:
    mensagem = ""
    for i in range(len(rotas)-1):
      if i == 0:
        mensagem += rotas[0]
      mensagem += " que acontou a " + rotas[i]
    print(f"Finalmente recebi a fofoca! Ela começou em {mensagem} e chegou em mim")

main()