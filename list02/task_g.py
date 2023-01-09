quantidadeRodadas = int(input())

saldoArtur = 0
saldoGuga = 0
saldoFrej = 0
saldoMisheldon = 0

for i in range (1, quantidadeRodadas + 1):
    print(f"Rodada numero {i}")
    nomeJogador = input()
    valorJogador = int(input())
    acertosEstimados = int(input())

    print(f"Jogador: {nomeJogador}")
    print(f"Valor apostado: {valorJogador}")
    print(f"Acreditando que acerta {acertosEstimados} vezes em 3 tentativas")

    apostasContra = int(input())
    print(f"{apostasContra} amigos apostaram contra")

    if apostasContra == 3:
        print(f"Parece que {nomeJogador} está sendo subestimado!")

    apostaArtur = 0
    apostaGuga = 0
    apostaFrej = 0
    apostaMisheldon = 0

    for j in range (0, apostasContra):
        nomeAmigo = input()
        apostaAmigo = int(input())
        print(f"{nomeAmigo} apostou {apostaAmigo}")
        if nomeAmigo == "Artur":
            apostaArtur += apostaAmigo
        elif nomeAmigo == "Guga":
            apostaGuga += apostaAmigo
        elif nomeAmigo == "Frej":
            apostaFrej += apostaAmigo
        elif nomeAmigo == "Misheldon":
            apostaMisheldon += apostaAmigo
    apostadoContra = apostaArtur + apostaGuga + apostaFrej + apostaMisheldon
    possivelPerda = valorJogador * apostasContra

    pontuacaoJogador = 0
    for k in range (1, 4):
        expressao = input()
        if expressao == "Receba!":
            pontuacaoJogador += 1
        else:
            print(f"Errou! Restam {3-k} tentativas")

    if acertosEstimados == pontuacaoJogador:
        if nomeJogador == "Artur":
            saldoArtur += apostadoContra
        elif nomeJogador == "Guga":
            saldoGuga += apostadoContra
        elif nomeJogador == "Frej":
            saldoFrej += apostadoContra
        elif nomeJogador == "Misheldon":
            saldoMisheldon += apostadoContra

        if apostaArtur > 0:
            saldoArtur -= apostaArtur
        if apostaGuga > 0:
            saldoGuga -= apostaGuga
        if apostaFrej > 0:
            saldoFrej -= apostaFrej
        if apostaMisheldon > 0:
            saldoMisheldon -= apostaMisheldon
    else:
        if nomeJogador == "Artur":
            saldoArtur -= possivelPerda
        elif nomeJogador == "Guga":
            saldoGuga -= possivelPerda
        elif nomeJogador == "Frej":
            saldoFrej -= possivelPerda
        elif nomeJogador == "Misheldon":
            saldoMisheldon -= possivelPerda

        if apostaArtur > 0:
            saldoArtur += valorJogador
        if apostaGuga > 0:
            saldoGuga += valorJogador
        if apostaFrej > 0:
            saldoFrej += valorJogador
        if apostaMisheldon > 0:
            saldoMisheldon += valorJogador

print("Fim de jogo, o resultado foi:")
print(f"Artur ficou com {saldoArtur} de saldo")
print(f"Frej ficou com {saldoFrej} de saldo")
print(f"Guga ficou com {saldoGuga} de saldo")
print(f"Misheldon ficou com {saldoMisheldon} de saldo")

