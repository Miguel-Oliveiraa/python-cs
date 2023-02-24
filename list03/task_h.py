nomes = input()
nomes = nomes.split(" ")

# cria um array de arrays
inventarios = []
for i in range(0, len(nomes)):
    inventarios.append([nomes[i], "lanterna"])

listaDesafios = ["portal", "criaturas", "energia", "carro"]

# itens para realizar cada desafio
portal = ["paginaPortal", "lanterna", "bobina", "martelo"]
criaturas = ["paginaCriaturas", "lanterna", "espada"]
energia = ["paginaEnergia", "lanterna", "fios", "martelo"]
carro = ["paginaPneus", "lanterna", "compressor"]

ultimoItem = None
ultimaAcao = None
posicaoJogador = None
mensagem = input()

while mensagem != "END":
    # armazena o input em 2 ou 3 variaveis diferentes
    mensagem = mensagem.split(" ")
    nomeJogador, acao = mensagem[0], mensagem[1]
    if len(mensagem) == 3:
        item = mensagem[2]

    if nomeJogador not in nomes:
        print(f"{nomeJogador} não faz parte da equipe!")
    else:
        if acao == "achou":

            # procura pelo jogador
            for i in range(0, len(inventarios)):
                if inventarios[i][0] == nomeJogador:

                    # caso o item ja exista
                    if item in inventarios[i]:
                        print(f"{item} já encontrado por {nomeJogador}.")
                    else:
                        # caso o inventario nao esteja lotado
                        if len(inventarios[i]) < 5:
                            print(f"{nomeJogador} coletou {item}!!")
                            inventarios[i].append(item)

                        # caso o inventario esteja lotado
                        else:
                            print(f"{nomeJogador} está com o máximo de itens! {item} foi descartado.")

        elif acao == "realizou":

            # procura pelo jogador e armazena a posicao dele
            for i in range(0, len(inventarios)):
                if inventarios[i][0] == nomeJogador:
                    posicaoJogador = i
            if item == "portal":

                # verifica os itens da missao sao um subconjunto no inventario
                if set(portal).issubset(set(inventarios[posicaoJogador])):

                    # remove todos os itens da missao, menos a lanterna e a pagina
                    for i in portal:
                        if i != "lanterna" and i != "paginaPortal":
                            inventarios[posicaoJogador].remove(i)
                    print(f"{nomeJogador} conseguiu consertar o portal!!!")
                    listaDesafios.remove("portal")
                else:
                    print(f"{nomeJogador} não possui os itens necessários para fazer essa tarefa! Colete mais itens e tente novamente.")

            elif item == "criaturas":

                # verifica os itens da missao sao um subconjunto no inventario
                if set(criaturas).issubset(set(inventarios[posicaoJogador])):
                    for i in criaturas:

                        # remove todos os itens da missao, menos a lanterna e a pagina
                        if i != "lanterna" and i != "paginaCriaturas":
                            inventarios[posicaoJogador].remove(i)
                    print(f"{nomeJogador} conseguiu exterminar todas as criaturas!!!")
                    listaDesafios.remove("criaturas")
                else:
                    print(f"{nomeJogador} não possui os itens necessários para fazer essa tarefa! Colete mais itens e tente novamente.")

            elif item == "energia":

                # verifica os itens da missao sao um subconjunto no inventario
                if set(energia).issubset(set(inventarios[posicaoJogador])):

                    # remove todos os itens da missao, menos a lanterna e a pagina
                    for i in energia:
                        if i != "lanterna" and i != "paginaEnergia":
                            inventarios[posicaoJogador].remove(i)
                    print(f"{nomeJogador} conseguiu restabelecer a energia do local. Ufa!!!")
                    listaDesafios.remove("energia")
                else:
                    print(f"{nomeJogador} não possui os itens necessários para fazer essa tarefa! Colete mais itens e tente novamente.")

            elif item == "carro":

                # verifica os itens da missao sao um subconjunto no inventario
                if set(carro).issubset(set(inventarios[posicaoJogador])):

                    # remove todos os itens da missao, menos a lanterna e a pagina
                    for i in carro:
                        if i != "lanterna" and i != "paginaPneus":
                            inventarios[posicaoJogador].remove(i)
                    print(f"{nomeJogador} conseguiu consertar o carro!!! Entrem todos!")
                    listaDesafios.remove("carro")
                else:
                    print(f"{nomeJogador} não possui os itens necessários para fazer essa tarefa! Colete mais itens e tente novamente.")

        elif acao == "desistiu":
            # procura o jogador e remove ele
            for i in range(0, len(inventarios)):
                if inventarios[i][0] == nomeJogador:
                    inventarios.pop(i)
                    print(f"{nomeJogador} abandonou a equipe! Não é porque somos menos que seremos mais fracos!!")
                    break


        elif acao == "perde":
            # caso criaturas ja tenha sido exterminadas e a ultima acao foi um desafio realizado
            if "criaturas" not in listaDesafios and ultimaAcao == "realizou":

                # procura o jogador e remove a lanterna do inventario
                for i in range(0, len(inventarios)):
                    if inventarios[i][0] == nomeJogador:
                        inventarios[i].remove("lanterna")
        ultimaAcao = mensagem[1]
    mensagem = input()


if len(listaDesafios) == 0:
    print("OBA! Stanford Pines conseguiu retornar à sua dimensão!!!")
elif "portal" in listaDesafios and len(listaDesafios) == 1:
    print("Apenas o portal... Que pena! Stanford Pines preso para sempre??")
elif len(listaDesafios) == 4:
    print("Nenhum avanço! Que fracasso, o Stanford ficará preso para sempre.")
else:
    print("Quase lá...")

print("(Você retorna ao banheiro do CIn, mas não se lembra do ocorrido. Vê um walkie-talkie na sua mão e decide voltar ao grad com ele, mas acaba esquecendo lá...)")