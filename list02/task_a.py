# recebendo inputs
frase = str(input())
aliensDerrotados = 0

# excecutando o codigo enquanto as regras de execucao sao validas
while(frase != "O relógio descarregou!" and frase != "Por hoje já deu"):
  aliensDerrotados += 1
  frase = str(input())

# verificando qual das duas regras de execucao foi quebrada para printar o resultado
if frase == "O relógio descarregou!":
  print(f'Corra Ben! Você já derrotou {aliensDerrotados} aliens')
elif frase == "Por hoje já deu":
  print(f'Muito Ben Ben! hehe você derrotou {aliensDerrotados} aliens hoje')