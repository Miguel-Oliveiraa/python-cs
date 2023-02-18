objetoProcurado = input()
listaItems = input()
# criando um array com o input
listaItems = listaItems.split(", ")

# variaveis auxiliares para caso o item seja encontrado ou caso ele repita
itemEncontrado = False
itensRepetidos = []
maxRepeticoes = 0

# passando por todos as posicoes
for i in range(0, len(listaItems)):
    # pulando caso o item já tenha sido contado
    if listaItems[i] not in itensRepetidos:
        qtdItem = 1
        # contando quantas vezes o item aparece
        for j in range(i+1, len(listaItems)):
            if listaItems[j] == listaItems[i]:
                qtdItem += 1
                itensRepetidos.append(listaItems[i])
        if qtdItem > 1:
            print(f"Após análises, percebi que {listaItems[i]} foi coletado mais de uma vez...")
        if qtdItem > maxRepeticoes:
            maxRepeticoes = qtdItem
        if listaItems[i] == objetoProcurado:
            itemEncontrado = True

if maxRepeticoes > 1:
    errorDimensional = '{0:.2f}'.format(len(listaItems) / maxRepeticoes)
    print(f'Certo, o coeficiente de erros de viagens interdimensionais é {errorDimensional}')

if itemEncontrado and objetoProcurado not in itensRepetidos:
    print("Você encontrou o item necessário para me ajudar a voltar para minha dimensão! Finalmente voltarei para Gravity Falls!")
else:
    print("Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...")
print("(Como prometido, você retorna ao DA do CIn. Mas, por razões desconhecidas, você se esquece do ocorrido)")
print('O walkie-talkie está na sua mão. Depois de um tempo, você diz: "Que aparelho velho!"')
print("(Após pensar sobre o que fazer com o walkie-talkie, você resolve jogá-lo no banheiro do CIn)")