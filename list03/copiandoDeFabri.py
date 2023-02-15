objetobuscado = input()
objetosencontrados = input()
objetosencontrados = objetosencontrados.split(', ')
encontrei = None
nome_mais_repetido = None
quantidade_mais_repetida = 0
repetidos = []

for i in range(len(objetosencontrados)):
    nome = objetosencontrados[i]
    if nome in objetosencontrados[:i]:
        continue
    quantidade = 1
    for j in range(i + 1, len(objetosencontrados)):
        if objetosencontrados[j] == nome:
            quantidade += 1
            repetidos.append(nome)
    if quantidade > 1:
        print(f'Após análises, percebi que {nome} foi coletado mais de uma vez...')
    if quantidade > quantidade_mais_repetida:
        quantidade_mais_repetida = quantidade
    if nome == objetobuscado: 
       encontrei = nome

if quantidade_mais_repetida >= 2:
    coeficiente = len(objetosencontrados) / quantidade_mais_repetida
    print(f'Certo, o coeficiente de erros de viagens interdimensionais é {coeficiente:.2f}')
if encontrei == objetobuscado and objetobuscado not in repetidos:
   print(f'Você encontrou o item necessário para me ajudar a voltar para minha dimensão! Finalmente voltarei para Gravity Falls!')
if encontrei != objetobuscado or objetobuscado in repetidos:
   print(f'Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...')
print(f'(Como prometido, você retorna ao DA do CIn. Mas, por razões desconhecidas, você se esquece do ocorrido)') 
print(f'O walkie-talkie está na sua mão. Depois de um tempo, você diz: "Que aparelho velho!"')
print(f'(Após pensar sobre o que fazer com o walkie-talkie, você resolve jogá-lo no banheiro do CIn)')
