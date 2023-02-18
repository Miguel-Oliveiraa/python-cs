# recebendo qtd n de locais
numeroLocais = int(input())

# criando uma variavel para caso ocorra empate e uma variavel -1 para checar se existe uma pior nota ou nao
empate = False
piorNota = -1

# executando um codigo n vezes
for i in range(0, numeroLocais):
    # recendo nome e nota do local
    nomeLugar = input()
    nota = 0
    notaRecebida = int(input())
    while notaRecebida > 0:
        nota = notaRecebida + nota
        notaRecebida = int(input())
    # caso seja a 1 execucao, atribuindo os valores do primeiro local como melhorLugar e melhorNota
    if i == 0:
        melhorLugar = nomeLugar
        melhorNota = nota
    # criando um fluxo para todas as outras execucoes
    else:
        # caso a nota atual seja pior que a melhor nota
        if nota > melhorNota:
            empate = False
            # verifico se a pior nota existe, se nao existir a melhor nota vira a pior nota
            if piorNota == -1:
                piorNota = melhorNota
                piorLugar = melhorLugar
            # transformo o valor atual na melhor nota
            melhorNota = nota
            melhorLugar = nomeLugar
        # caso a nota seja pior que a melhor nota
        elif nota < melhorNota:
            empate = False
            # verifico se a pior nota existe, se nao existir a nota atual vira a pior nota
            if piorNota == -1:
                piorNota = nota
                piorLugar = nomeLugar
            # se existir eu comparo a notal atual com a pior nota e atribuo um valor novo ou nao para a pior nota
            else:
                if nota < piorNota:
                    piorNota = nota
                    piorLugar = nomeLugar
        # caso a nota atual seja igual a melhor nota, eu atribuo empate como true e concateno a nota atual no final da melhor nota, assim ordenando pela ordem de input
        elif nota == melhorNota:
            empate = True
            melhorLugar = melhorLugar + ", " + nomeLugar

# executo os outputs
if empate == True:
    print(melhorLugar)
    print("Tantas opções")
else:
    print(f"{melhorLugar} ganhou de lavada de {piorLugar}, com {melhorNota} vs {piorNota}")