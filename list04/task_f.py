def transformaAscii(nome):
  c = 0
  for i in nome:
    c += ord(i)
  return c

def alocarPrisioneiro(celas, posicao, nomePrisioneiro, quantidade_celas):
  if celas[posicao] == " ":
    celas[posicao] = nomePrisioneiro
  else:
    while celas[posicao] != " ":
      posicao = (posicao+1)%quantidade_celas
    celas[posicao] = nomePrisioneiro

mensagem = input().split(" ")
quantidade_celas, quantidade_ordens = int(mensagem[0]), int(mensagem[1])
celas = [" "]*quantidade_celas
qtdPrisioneiros = 0

for i in range(0, quantidade_ordens):
  ordem = input().split(" ")
  comando = ordem[0]
  nomePrisioneiro = ordem[1]
  codigoPrisioneiro = transformaAscii(nomePrisioneiro)
  posicao = codigoPrisioneiro%quantidade_celas

  if comando == "ADICIONAR":
      if qtdPrisioneiros==quantidade_celas:
        print("CHEIO")
      else:
        alocarPrisioneiro(celas, posicao, nomePrisioneiro, quantidade_celas)
        qtdPrisioneiros += 1
  else:
    if nomePrisioneiro not in celas:
      print("NAO EXISTE")
    else:
      if celas[posicao] == nomePrisioneiro:
        celas[posicao] = " "

ordemPrisioneiros = []
for i in range(len(celas)):
  if celas[i] != " ":
    ordemPrisioneiros.append(celas[i])

print(*ordemPrisioneiros, sep=" ")
