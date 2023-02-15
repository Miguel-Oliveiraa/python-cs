objetoProcurado = input()
listaItems = input()

listaItems = listaItems.split(", ")
novaLista = []
for i in listaItems:
    novaLista.append(i)

itemEncontrado = False
erroDimensional = 0
itensRepetidos = []

for i in range(0, len(novaLista)):
    for j in range(i, len(novaLista)):
        if novaLista[i] == novaLista[j]:
            if novaLista[i] == objetoProcurado:
                erroDimensional += 1
            itensRepetidos.append(novaLista[i])

print(itensRepetidos)
# nomesRepetidos = []
# for i in itensRepetidos:
#     if i not in nomesRepetidos:
#         nomesRepetidos.append(i)
#         print(i)
        # print(f"Após análises, percebi que {i} foi coletado mais de uma vez...")

if itensRepetidos != []:
    maxcount = 0
    element_having_max_freq = 0
    for i in range(0, len(itensRepetidos)):
      count = 0
      for j in range(0, len(itensRepetidos)):
        if(itensRepetidos[i] == itensRepetidos[j]):
          count += 1
      if (count > maxcount):
          maxcount = count
      element_having_max_freq = itensRepetidos[i]
    valor = round((len(novaLista)/maxcount),2)
    print(f"Certo, o coeficiente de erros de viagens interdimensionais é {valor}")

    if itemEncontrado and erroDimensional == 0:
        print(
            "Você encontrou o item necessário para me ajudar a voltar para minha dimensão! Finalmente voltarei para Gravity Falls!")
    else:
        print("Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...")

    print("(Como prometido, você retorna ao DA do CIn. Mas, por razões desconhecidas, você se esquece do ocorrido)")
    print('O walkie-talkie está na sua mão. Depois de um tempo, você diz: "Que aparelho velho!"')
    print("(Após pensar sobre o que fazer com o walkie-talkie, você resolve jogá-lo no banheiro do CIn)")