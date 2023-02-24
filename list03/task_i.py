nomeInimigo = input()
nomeAliado = input()
climaAtual = input()

mensagem = input()
listaCodigos = []

while mensagem != "Cansado":

    # cria um array de arrays de numeros
    mensagem = mensagem.split(" ")
    for i in range(0, len(mensagem)):
        mensagem[i] = int(mensagem[i])
    listaCodigos.append(mensagem)
    mensagem = input()



climaValido = True
if climaAtual == "Ensolarado":

    # percorre o array de arrays
    for i in range(0, len(listaCodigos)):

        # ordena os numeros do array interno
        for j in range(0, len(listaCodigos[i])):
            for k in range(0, len(listaCodigos[i])-j-1):
                if listaCodigos[i][k] > listaCodigos[i][k+1]:
                    listaCodigos[i][k], listaCodigos[i][k+1] = listaCodigos[i][k+1], listaCodigos[i][k]
    print(f"Caramba! Finalmente organizamos a mensagem secreta do {nomeInimigo} com esse clima Ensolarado! Vamos nessa {nomeAliado}!")

elif climaAtual == "Nublado":

    # percorre o array de arrays
    for i in range(0, len(listaCodigos)):

        # ordena os numeros do array interno
        for j in range(0, len(listaCodigos[i])):
            for k in range(0, len(listaCodigos[i])-j-1):
                if listaCodigos[i][k] < listaCodigos[i][k+1]:
                    listaCodigos[i][k], listaCodigos[i][k+1] = listaCodigos[i][k+1], listaCodigos[i][k]
    print(f"Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!")

elif climaAtual == "ChuvosoNormal":
    # percorre o array de arrays
    for i in range(0, len(listaCodigos)):

        # executa para todos os arrays que ainda faltam
        for j in range(0, len(listaCodigos) - i - 1):

            # compara a posicao k de um array com k do proximo array
            for k in range(0, len(listaCodigos[i])):
                if listaCodigos[j][k] < listaCodigos[i + 1][k]:
                    listaCodigos[i][k], listaCodigos[i + 1][k] = listaCodigos[i + 1][k], listaCodigos[i][k]
    print(f"Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!")

elif climaAtual == "ChuvosoComRaio":

    # percorre o array de arrays
    for i in range(0, len(listaCodigos)):

        # executa para todos os arrays que ainda faltam
        for j in range(0, len(listaCodigos) - i - 1):

            # compara a posicao k de um array com k do proximo array
            for k in range(0, len(listaCodigos[i])):
                if listaCodigos[i][k] > listaCodigos[i + 1][k]:
                    listaCodigos[i][k], listaCodigos[i + 1][k] = listaCodigos[i + 1][k], listaCodigos[i][k]
    print(f"Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nomeInimigo}! Vamos nessa {nomeAliado}!")

else:
    print("Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??")
    print(f"Tenho certeza que conseguiremos na próxima {nomeAliado}")
    climaValido = False

if climaValido:
    print(f"Agora decodificamos as {len(listaCodigos)} mensagens do {nomeInimigo} e sabemos seus {len(listaCodigos)} lugares de ataque.")
    print("Os lugares sao:")
    for i in range(len(listaCodigos)):
        print(f"{i + 1} lugar:")
        print(f"Coordenadas: {listaCodigos[i][0]}° {listaCodigos[i][1]}' {listaCodigos[i][2]}''")
        print(f"Horario: {listaCodigos[i][3]}h {listaCodigos[i][4]}m {listaCodigos[i][5]}s")
        print(f"Data: {listaCodigos[i][6]}/{listaCodigos[i][7]}/{listaCodigos[i][8]}")
    print(f"Vamos rapido {nomeAliado}!!")

