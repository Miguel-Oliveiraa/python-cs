entradaUsuario = input()
suspeitos = []

# executando as regras enquanto a lista não está completa
while entradaUsuario != "ja temos nossa lista de suspeitos":
  if entradaUsuario == "novo suspeito - altissima periculosidade":
    nomeSuspeito = input()
    # adcionando um elemento a primeira posicao do array
    suspeitos.insert(0, nomeSuspeito)
  elif entradaUsuario == "novo suspeito - pouco perigoso":
    nomeSuspeito = input()
    # adcionando um elemento ao final do array
    suspeitos.append(nomeSuspeito)
  elif entradaUsuario == "livre de suspeita, pode remover":
    nomeSuspeito = input()
    # removendo um elemento do array
    suspeitos.remove(nomeSuspeito)
  elif entradaUsuario == "sujeito mais perigoso do que pensavamos":
    posicaoSuspeito = int(input())
    novaPosicao = int(input())
    # trocando os valores de duas posicoes em um array
    suspeitos[posicaoSuspeito], suspeitos[novaPosicao] = suspeitos[novaPosicao],suspeitos[posicaoSuspeito]
  elif entradaUsuario == "que estranho, esses dois meliantes… troque-os de lugar":
    primeiroSuspeito = suspeitos.index(input())
    segundoSuspeito = suspeitos.index(input())
    # trocando os valores de duas posicoes em um array
    suspeitos[primeiroSuspeito], suspeitos[segundoSuspeito] = suspeitos[segundoSuspeito],suspeitos[primeiroSuspeito]
  elif entradaUsuario == "essa posicao nao esta de acordo, ele nao e tao perigoso assim":
    nomeSuspeito = input()
    # remove um elemento do array e adciona na ultima posicao
    suspeitos.remove(nomeSuspeito)
    suspeitos.append(nomeSuspeito)
  elif entradaUsuario == "como a lista esta ficando?":
    # printando todos elementos do array, separando eles com um espaço vazio
    print(*suspeitos, sep=' ')
  entradaUsuario = input()

# tratando o array para exibir da forma pedida
resultadoFinal = ""
for i in range(0, len(suspeitos)):
  if i != len(suspeitos)-1:
    resultadoFinal += str(suspeitos[i]) + ' '
  else:
    resultadoFinal += str(suspeitos[i])
print("O resultado final ficou assim:")
print(resultadoFinal)