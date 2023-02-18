numeroLetras = int(input())

mensagemDecodificada = ""
for i in range(0, numeroLetras):
    mensagemCodificada = input()
    mensagemCodificada = mensagemCodificada.split(" ")
    mensagemCodificada[1] = mensagemCodificada[1].split("-")
    mensagemCodificada[0], mensagemCodificada[1][0], mensagemCodificada[1][1] = int(mensagemCodificada[0]), int(mensagemCodificada[1][0]), int(mensagemCodificada[1][1])
    primeiroNumero = 0
    segundoNumero = 1
    for j in range(1, mensagemCodificada[0]):
        terceiroNumero = primeiroNumero+segundoNumero
        primeiroNumero, segundoNumero = segundoNumero, terceiroNumero
    terceiroNumero = str(terceiroNumero)
    primeiroDigito = terceiroNumero[mensagemCodificada[1][0]]
    segundoDigito = terceiroNumero[mensagemCodificada[1][1]]
    codigo = primeiroDigito + segundoDigito
    mensagemDecodificada += chr(int(codigo))

print(mensagemDecodificada)