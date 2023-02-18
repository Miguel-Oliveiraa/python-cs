numeroLetras = int(input())

mensagemDecodificada = ""
for i in range(0, numeroLetras):
    letraCodificada = input()

    # transformando o input codificado em um array com o numero da sequencia de fibonacci e a posicao dos numeros
    letraCodificada = letraCodificada.split(" ")
    letraCodificada[1] = letraCodificada[1].split("-")
    letraCodificada[0], letraCodificada[1][0], letraCodificada[1][1] = int(letraCodificada[0]), int(letraCodificada[1][0]), int(letraCodificada[1][1])

    # calculando o numero da sequencia de fibonacci
    primeiroNumero = 0
    segundoNumero = 1
    for j in range(1, letraCodificada[0]):
        resultadoFibonacci = primeiroNumero+segundoNumero
        primeiroNumero, segundoNumero = segundoNumero, resultadoFibonacci

    # pegando as posicoes pedidas
    resultadoFibonacci = str(resultadoFibonacci)
    primeiroDigito = resultadoFibonacci[letraCodificada[1][0]]
    segundoDigito = resultadoFibonacci[letraCodificada[1][1]]

    # concatenando e transformando em string
    codigo = primeiroDigito + segundoDigito
    mensagemDecodificada += chr(int(codigo))

print(mensagemDecodificada)