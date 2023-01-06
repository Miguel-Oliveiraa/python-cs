quantidadeJogosPromocao = int(input())

# recebendo os nomes e numeros de sequencia n vezes
for i in range(0, quantidadeJogosPromocao):
    nomeJogo = input()
    numeroSequencia = int(input())
    prequels = "2"
    # imprimindo caso o jogo seja um sequel direto, ou os jogos entre ele e o 1 caso seja um sequel indireto
    if numeroSequencia == 2:
        print("Achei a sequel! Hora da diversão!")
    else:
        for i in range(3, numeroSequencia):
            prequels = prequels + f", {i}"
        print(f"Achamos {nomeJogo} {numeroSequencia}, mas você ainda precisa jogar o {prequels} antes desse.")