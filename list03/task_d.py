tamanho = int(input())
chave = int(input())
sequencia = input()


# transformando a sequencia do input num array de strings
sequencia = sequencia.split(", ")
nova_sequencia = []
for i in sequencia:
  nova_sequencia.append(int(i))

resultado = []
soma = 0
# percorrendo todos os itens do array
for i in range(0, tamanho):
    if chave > 0:
        # percorrendo todos os items de forma circular entre a proxima posição ate a proxima + k
        for j in range(i+1, i+chave+1):
          posicao = j%tamanho
          soma += nova_sequencia[posicao]
        resultado.append(soma)
        soma = 0
    elif chave < 0:
        # percorrendo todos os items de forma circular entre a posição anterior ate a anterior menos a chave
        for j in range(i-1, i+chave-1, -1):
            posicao = j%tamanho
            soma += nova_sequencia[posicao]
        resultado.append(soma)
        soma = 0
    else:
        resultado.append(0)

# tratando o array para exibir da forma pedida
nomeFinal = ""
for i in range(0, len(resultado)):
  if i != len(resultado)-1:
    nomeFinal += str(resultado[i]) + ', '
  else:
    nomeFinal += str(resultado[i])

if chave == 0:
    print(f"Não foi dessa vez Gideãozinho a chave corrompeu e a sequencia ficou assim: {nomeFinal}")
else:
    print(f"Vamos lá Gideãozinho a sequencia final é {nomeFinal}")