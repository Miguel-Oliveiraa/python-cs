numeroSorteado = input()
sorteadoDecimal = 0

acertou = False

# transformando o numero sorteado em decimal
for i in range(0, len(numeroSorteado), 1):
    casaBinaria = int(numeroSorteado[i]) * 2**(len(numeroSorteado)-i-1)
    sorteadoDecimal += casaBinaria

# pedindo um palpite 3 vezes e comparando com o sorteado em Decimal
for i in range(1, 4):
    palpite = int(input())
    # parando o loop e atribuindo true a variavel caso ele acerte
    if palpite == sorteadoDecimal:
        acertou = True
        break
    # printando quantas chances o usuario ainda tem
    if i != 3:
        print(f"Resposta incorreta. Mas não desista! Você ainda tem {3-i} chance(s)")

# verificando se ele acertou ou nao
if acertou:
    # se acertou
    print("Parabéns!! Você acertou!")
    # 1 Porto de galinha
    if sorteadoDecimal == 1:
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Porto de Galinhas (BRA).")
        print("Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!")
    # 2 Fernando de noronha
    elif sorteadoDecimal == 2:
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Fernando de Noronha (BRA).")
        print("Belíssimas praias estão por vir.")
        print("Não esqueça o protetor solar.")
    # 3 Gramado
    elif sorteadoDecimal == 3:
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Gramado (BRA).")
        print("Aproveite passeios e paisagens espetaculares no sul do país!")
    # 4 Berlim
    elif sorteadoDecimal == 4:
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Berlim (ALE).")
        print("Desfrute de muita cultura e de experiências incríveis!")
        print("Prepare os casacos de frio!")
    # 5 Toquio
    elif sorteadoDecimal == 5:
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Tóquio (JPN).")
        print("Viva uma experiência inesquecível explorando um país do outro lado do mundo.")
        print("Prepare-se para muitas horas de voo!")
    # Caso o numero sorteado nao for premiado
    else:
        print("Mas, infelizmente, hoje não é o seu dia de sorte.")
        print("Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.")
        print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")
else:
    # se errou
    print("Infelizmente mais uma resposta incorreta.")
    print("Agradecemos sua participação!")
    # caso o numero sorteado fosse premiado
    if sorteadoDecimal == 1 or sorteadoDecimal == 2 or sorteadoDecimal == 3 or sorteadoDecimal == 4 or sorteadoDecimal == 5:
        print("Seu bilhete era premiado. Que pena!")
    # caso o numero sorteado nao fosse premiado
    else:
        print("Pelo menos seu bilhete não era premiado.")
        print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")