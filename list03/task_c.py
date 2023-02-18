quantidadeDiarios = int(input())

# variaveis auxiliares
diarios = []
numeroDiarios = []

# recebendo n diarios
for i in range (0, quantidadeDiarios):
    diarioArmazenado = input()
    diarioArmazenado = diarioArmazenado.split(", ")
    # armazenando o nome do diario em um array e o numero dele em outro array com index igual
    diarios.append(diarioArmazenado[0])
    numeroDiarios.append(diarioArmazenado[1])

quantidadeBusca = int(input())
diariosBuscados = []
# recebendo n diarios para busca
for i in range (0, quantidadeBusca):
    diariosBuscados.append(input())

# verificando para cada diario a ser discado
for i in diariosBuscados:
    # caso o diario esteja no array de diarios!
    if diarios.count(i)>0:
        print(f"Informacoes sobre {i} estao no Diario {numeroDiarios[diarios.index(i)]}")
    else:
        print(f"Nenhum dos diarios possui informacoes sobre {i}")