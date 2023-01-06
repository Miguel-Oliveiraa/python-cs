vidasCalegario = 3
vidasApostador = 3

# executando o codigo enquanto algum ate que a vida de algum deles chegue a 0
while (vidasCalegario != 0 and vidasApostador !=0):
    palavraRodada = input()
    acaoRodada = int(input())

    # invertendo a palavra
    palavraInvertida = ""
    for i in palavraRodada:
        palavraInvertida = i + palavraInvertida

    # transformando a palavra em binaria
    palavraBinaria = ""
    for i in palavraRodada:
        # transformando letra por letra no codigo ascii
        codigoAscii = ord(i)

        # transformando o codigo ascii em binario
        numero = codigoAscii
        quociente = 1
        casaBinaria = ""
        while quociente >= 1:
            resto = codigoAscii%2
            casaBinaria = str(resto) + casaBinaria
            quociente = codigoAscii//2
            codigoAscii = quociente

        palavraBinaria = palavraBinaria + "0" + casaBinaria

    print("Rodada Concluída!")
    # Caso a rodada seja para inverter a palavra
    if acaoRodada == 1:
        palpiteRodada = input()
        if palpiteRodada == palavraInvertida:
            vidasApostador -= 1
            print("apostador perdeu uma vida")
        else:
            vidasCalegario -= 1
            print("calegario perdeu uma vida")
    # Caso seja para transformar em binario
    else:
        palpiteRodada = input()
        if palpiteRodada == palavraBinaria:
            vidasApostador -= 1
            print("apostador perdeu uma vida")
            print("Como alguém consegue fazer isso de cabeça?")
        else:
            vidasCalegario -= 1
            print("calegario perdeu uma vida")


# printando quando a partida termina
print("Partida Concluída!")
if vidasCalegario == 0:
    print("Vencedor: apostador")
    print("HAHAHA, acha mesmo que preciso trapacear para ganhar de você?")
else:
    print("Vencedor: calegario")
    print("Droga, não acredito que eu perdi essa partida, achei que seria uma vitória fácil...")