letraSorteado = input()
quantidadeAmigos = int(input())
estadoPreferido = input()

# recebendo nome e cidade dos amigos n vezes
for i in range (0, quantidadeAmigos):
    nomeAmigo = input()
    estadoAmigo = input()

    # contando quantas vezes o a letra sorteada aparece
    contadorLetraSorteada = 0
    for j in range (0, len(estadoAmigo)):
        if estadoAmigo[j] == letraSorteado:
            contadorLetraSorteada += 1

    # caso seja o primeiro estado colocando como estado escolhido
    if i == 0:
        estadoEscolhido = estadoAmigo
        amigoEscolhido = nomeAmigo
        quantidadesLetrasEscolhido = contadorLetraSorteada
    # comparando a quantidade de letras sorteadas do nome atual com o vencedor
    else:
        if contadorLetraSorteada > quantidadesLetrasEscolhido:
            estadoEscolhido = estadoAmigo
            amigoEscolhido = nomeAmigo
            quantidadesLetrasEscolhido = contadorLetraSorteada

# comparando o estado vencedor com o estado preferido
if estadoEscolhido == estadoPreferido:
    print(f"UHUL!!! Victor vai começar por {estadoEscolhido} que é o estado que ele queria e ficara la por {quantidadesLetrasEscolhido} dias.")
else:
    print(f"Eita!!! infelizmente, Victor terá que fazer uma viagem maior e começar pelo estado {estadoEscolhido} e ficara la por {quantidadesLetrasEscolhido} dias.")