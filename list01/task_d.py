nome_narrador_1 = str(input())
bordao_narrador_1 = str(input())
eh_carismatico_narrador_1 = bool(input() == "sim")
if eh_carismatico_narrador_1:
    pontuacaoNarrador1 = 10
else:
    pontuacaoNarrador1 = 0
emocao_narrador_1 = int(input())
pontuacaoNarrador1 += emocao_narrador_1

if bordao_narrador_1 == "PROOOO FUNDO DO GOOOL":
    pontuacaoNarrador1 += 15
elif bordao_narrador_1 == "EU QUERO É GRITAR GOL":
    pontuacaoNarrador1 -= 10
elif bordao_narrador_1 == "VOCÊ. É. RIDÍCULO":
    pontuacaoNarrador1 += 18
elif bordao_narrador_1 == "QUEM SABE NA BOLA PARADA":
    pontuacaoNarrador1 -= 5
else:
    pontuacaoNarrador1 += 10

nome_narrador_2 = str(input())
bordao_narrador_2 = str(input())
eh_carismatico_narrador_2 = bool(input() == "sim")
if eh_carismatico_narrador_2:
    pontuacaoNarrador2 = 10
else:
    pontuacaoNarrador2 = 0
emocao_narrador_2 = int(input())
pontuacaoNarrador2 += emocao_narrador_2

if bordao_narrador_2 == "PROOOO FUNDO DO GOOOL":
    pontuacaoNarrador2 += 15
elif bordao_narrador_2 == "EU QUERO É GRITAR GOL":
    pontuacaoNarrador2 -= 10
elif bordao_narrador_2 == "VOCÊ. É. RIDÍCULO":
    pontuacaoNarrador2 += 18
elif bordao_narrador_2 == "QUEM SABE NA BOLA PARADA":
    pontuacaoNarrador2 -= 5
else:
    pontuacaoNarrador2 += 10

if pontuacaoNarrador1 > pontuacaoNarrador2:
    print(
        f"O(a) narrador(a) escolhido(a) é {nome_narrador_1}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.")
else:
    print(
        f"O(a) narrador(a) escolhido(a) é {nome_narrador_2}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.")