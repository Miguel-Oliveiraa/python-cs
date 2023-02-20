qtdPalavras = int(input())

# array para receber todas as palavras a serem decodificadas
mensagemDecodificada = []
for i in range(0, qtdPalavras):

    # recebendo os inputs
    quebraLinha = input()
    decodificador = input()
    quebraLinha = input()
    palavraCodificada = input()

    if decodificador == "Portal":
        palavraDecodificada = ""
        for j in range(0, len(palavraCodificada)):

            # transforma as letras em codigo ascii e soma 1
            if palavraCodificada[j].isalpha():
                codigoLetra = ord(palavraCodificada[j]) + 1

                # caso o codigo seja da letra z transforma em a
                if codigoLetra == 123:
                    codigoLetra = 97
                palavraDecodificada += chr(codigoLetra)
        mensagemDecodificada.append(palavraDecodificada)

    elif decodificador == "Experimento":
        palavraDecodificada = 0
        for j in range(0, len(palavraCodificada)):

            # soma os digitos pares
            if palavraCodificada[j].isdigit() and int(palavraCodificada[j]) % 2 == 0:
                palavraDecodificada += int(palavraCodificada[j])
        mensagemDecodificada.append(palavraDecodificada)

    elif decodificador == "Realidade":
        palavraDecodificada = 0
        for j in range(0, len(palavraCodificada)):

            # soma os digitos impares
            if palavraCodificada[j].isdigit() and int(palavraCodificada[j]) % 2 == 1:
                palavraDecodificada += int(palavraCodificada[j])
        mensagemDecodificada.append(palavraDecodificada)

    else:
        palavraDecodificada = 1

        # multiplica todos os numeros
        for j in range(0, len(palavraCodificada)):
            if palavraCodificada[j].isdigit():
                palavraDecodificada *= int(palavraCodificada[j])
        mensagemDecodificada.append(palavraDecodificada)

validade = True
mensagemFinal = ""
for i in range(0, len(mensagemDecodificada)):

    # concatena mensagem final
    if i != len(mensagemDecodificada) - 1:
        mensagemFinal += str(mensagemDecodificada[i]) + " "
    else:
        mensagemFinal += str(mensagemDecodificada[i])

    # verifica se os valores não são numero os char
    if not(str(mensagemDecodificada[i]).isdigit() or str(mensagemDecodificada[i]).isalpha()):
        validade = False
        break

if validade:
    print(f"Consegui! A mensagem decodificada de Bill Cipher é: {mensagemFinal}")
else:
    print("Esse formato de mensagem nem Bill Cipher entenderia!")
