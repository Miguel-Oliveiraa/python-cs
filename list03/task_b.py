tamanho = int(input())

# recebendo a lista de nomes
listaCriaturas = []
for i in range(0, tamanho):
    nomeCriatura = input()
    if nomeCriatura not in listaCriaturas:
        listaCriaturas.append(nomeCriatura)

# ordenando por ordem lexigrafica utilizado bubble sort
for i in range(0, len(listaCriaturas)):
    for j in range(0, len(listaCriaturas)-1):
        if listaCriaturas[j] > listaCriaturas[j+1]:
            listaCriaturas[j], listaCriaturas[j+1] = listaCriaturas[j+1], listaCriaturas[j]

# tratando o array para exibir da forma pedida
resultado = ""
for i in range(0, len(listaCriaturas)):
    if i != len(listaCriaturas)-1:
        resultado += listaCriaturas[i] + ", "
    else:
        resultado += listaCriaturas[i]
print(resultado)