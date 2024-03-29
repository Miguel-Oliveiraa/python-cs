# recebe as coordenadas do jogador
inicio = input()
inicio = inicio.split(" ")
coordenada = []
for i in inicio:
    coordenada.append(int(i))

# recebe as coordenadas do squad e indica a direcao
inicioSquad = input()
inicioSquad = inicioSquad.split(" ")
coordenadaSquad = []
for i in inicioSquad:
    coordenadaSquad.append(int(i))
if coordenadaSquad[0] == 7:
    movimentacaoSquad = "esquerda"
else:
    movimentacaoSquad = "direita"

sucesso = True
for m in range(0, 3):
    nomeLocal = input()

    # caso seja a ultima rodada, recebe as coordenadas dos policiais
    if m == 2:
        inicioPoliciais = input()
        inicioPoliciais = inicioPoliciais.split(" ")
        coordenadaPoliciais = []
        for i in inicioPoliciais:
            coordenadaPoliciais.append(int(i))


    tamanhoMatrizes = int(input())
    matrizes = []

    # recebe a primeira matriz
    primeiraMatriz = []
    for i in range(tamanhoMatrizes):
        linha = input()
        linha = linha.split(" ")
        primeiraMatriz.append(linha)
    matrizes.append(primeiraMatriz)


    # recebe a segunda matriz
    segundaMatriz = []
    for i in range(tamanhoMatrizes):
        linha = input()
        linha = linha.split(" ")
        segundaMatriz.append(linha)
    matrizes.append(segundaMatriz)


    # soma as matrizes
    somaMatrizes = []
    for i in range(tamanhoMatrizes):
        somaLinha = []
        for j in range(tamanhoMatrizes):
            somaLinha.append(int(matrizes[0][i][j]) + int(matrizes[1][i][j]))
        somaMatrizes.append(somaLinha)

    # soma todos elementos da matriz resultante
    resultadoSoma = 0
    for i in range(tamanhoMatrizes):
        for j in range(tamanhoMatrizes):
            resultadoSoma += somaMatrizes[i][j]


    # multiplica as matrizes
    produtoMatrizes = []
    for i in range(tamanhoMatrizes):
        produtoLinha = []
        for j in range(tamanhoMatrizes):
            resultado = 0
            for k in range(tamanhoMatrizes):
                resultado += int(matrizes[0][i][k])*int(matrizes[1][k][j])
            produtoLinha.append(resultado)
        produtoMatrizes.append(produtoLinha)

    # soma todos elementos da diagonal principal do produto
    resultadoProduto = 0
    for i in range(tamanhoMatrizes):
        resultadoProduto += produtoMatrizes[i][i]

    # cria as coordenadas do objetivo com base nas operações das matrizes
    coordenadasObjetivo = [resultadoSoma, resultadoProduto]

    # calcula a qtd de Passos para o objetivo
    qtdPassos = abs(coordenadasObjetivo[0]-coordenada[0]) + abs(coordenadasObjetivo[1]-coordenada[1])

    # calcula as distancias para o objetivo
    distanciaVertical = coordenadasObjetivo[1]-coordenada[1]
    distanciaHorizontal = coordenadasObjetivo[0] - coordenada[0]

    if m == 2:
        distanciaVerticalPoliciais = coordenadasObjetivo[1] - coordenadaPoliciais[1]
        distanciaHorizontalPoliciais = coordenadasObjetivo[0] - coordenadaPoliciais[0]

    # movimentacao dos protagonistas na vertical
    while coordenada[1] != coordenadasObjetivo[1]:
        # if m == 2:
        #     print(coordenada, coordenadaPoliciais)
        if not sucesso:
            break

        # verifica se tem que andar para cima ou para baixo
        if distanciaVertical > 0:
            coordenada[1] = coordenada[1]+1
        else:
            coordenada[1] = coordenada[1]-1

        # faz a movimentação do Squad
        if movimentacaoSquad == "direita":
            if coordenadaSquad[0] == 7:
                movimentacaoSquad = "esquerda"
            else:
                coordenadaSquad[0] = coordenadaSquad[0]+1
        if movimentacaoSquad == "esquerda":
            if coordenadaSquad[0] == 0:
                movimentacaoSquad = "direita"
                coordenadaSquad[0] = coordenadaSquad[0] + 1
            else:
                coordenadaSquad[0] = coordenadaSquad[0]-1

        # faz a movimentacao dos policiais
        if m == 2:
            if coordenadaPoliciais[0] != coordenadasObjetivo[0]:
                if distanciaHorizontalPoliciais > 0:
                    coordenadaPoliciais[0] = coordenadaPoliciais[0] + 1
                else:
                    coordenadaPoliciais[0] = coordenadaPoliciais[0] - 1
            elif coordenadaPoliciais[1] != coordenadasObjetivo[1]:
                if distanciaVerticalPoliciais > 0:
                    coordenadaPoliciais[1] = coordenadaPoliciais[1] + 1
                else:
                    coordenadaPoliciais[1] = coordenadaPoliciais[1] - 1

        # caso os policiais chegem na coordenada antes dos protagonistas eles ganham
        if m == 2:
            if coordenadaPoliciais == coordenadasObjetivo and coordenada != coordenadasObjetivo:
                sucesso = False

        if m == 2:
            if coordenada != coordenadasObjetivo:
                # caso os protagonistas se encontrem com o policiais e nao for no objetivo, eles perdem
                if coordenada[0] == coordenadaPoliciais[0] and coordenada[1] == coordenadaPoliciais[1]:
                    sucesso = False
                    break

        # caso os protagonistas se encontrem com o Squad, eles perdem
        if coordenada[0] == coordenadaSquad[0] and coordenada[1] == coordenadaSquad[1]:
            print("Parado! Está cercado pelo Esquadrão De Segurança para Evitar o Paradoxo do Tempo. O que quer que você diga pode ou já foi usado contra você no Tribunal do Futuro.")
            print("Talvez não foi uma boa ideia ajudar o Ford…")
            sucesso = False
            break

    if not sucesso:
        break

    # movimentacao dos protagonistas na vertical
    while coordenada[0] != coordenadasObjetivo[0]:
        # if m == 2:
        #     print(coordenada, coordenadaPoliciais)
        if not sucesso:
            break

        # verifica se tem que andar para direita ou esquerda
        if distanciaHorizontal > 0:
            coordenada[0] = coordenada[0] + 1
        else:
            coordenada[0] = coordenada[0] - 1

        # faz a movimentação do Squad
        if movimentacaoSquad == "direita":
            if coordenadaSquad[0] == 7:
                movimentacaoSquad = "esquerda"
            else:
                coordenadaSquad[0] = coordenadaSquad[0] + 1
        if movimentacaoSquad == "esquerda":
            if coordenadaSquad[0] == 0:
                movimentacaoSquad = "direita"
                coordenadaSquad[0] = coordenadaSquad[0] + 1
            else:
                coordenadaSquad[0] = coordenadaSquad[0] - 1

        # faz a movimentacao dos policiais
        if m == 2:
            if coordenadaPoliciais[0] != coordenadasObjetivo[0]:
                if distanciaHorizontalPoliciais > 0:
                    coordenadaPoliciais[0] = coordenadaPoliciais[0] + 1
                else:
                    coordenadaPoliciais[0] = coordenadaPoliciais[0] - 1
            elif coordenadaPoliciais[1] != coordenadasObjetivo[1]:
                if distanciaVerticalPoliciais > 0:
                    coordenadaPoliciais[1] = coordenadaPoliciais[1] + 1
                else:
                    coordenadaPoliciais[1] = coordenadaPoliciais[1] - 1

        # caso os policiais chegem na coordenada antes dos protagonistas eles ganham
        if m == 2:
            if coordenadaPoliciais == coordenadasObjetivo and coordenada != coordenadasObjetivo:
                sucesso = False

        if m == 2:
            if coordenada != coordenadasObjetivo:
                # caso os protagonistas se encontrem com o policiais e nao for no , eles perdem
                if coordenada[0] == coordenadaPoliciais[0] and coordenada[1] == coordenadaPoliciais[1]:
                    sucesso = False
                    break

        # caso os protagonistas se encontrem com o Squad, eles perdem
        if coordenada[0] == coordenadaSquad[0] and coordenada[1] == coordenadaSquad[1]:
            print("Parado! Está cercado pelo Esquadrão De Segurança para Evitar o Paradoxo do Tempo. O que quer que você diga pode ou já foi usado contra você no Tribunal do Futuro.")
            print("Talvez não foi uma boa ideia ajudar o Ford…")
            sucesso = False
            break

    if not sucesso:
        break
    print(f"{nomeLocal} está na coluna {coordenadasObjetivo[0]} e na linha {coordenadasObjetivo[1]}. Foram dados {qtdPassos} passos para chegar lá.")

if sucesso:
    print("IUHU, VOCÊ SALVOU O FORD!! Agora, todos podem voltar para casa!")
else:
    print("Oh, não! O Ford vai ter que achar outro jeito de voltar para casa.")