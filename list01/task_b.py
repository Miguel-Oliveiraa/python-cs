selecaoUm = str(input())
selecaoDois = str(input())
valorApostado = int(input())
probabilidade = float(input())
resultado = str(input())

retorno = int(valorApostado * (1+(0.5 - probabilidade)**2 * 100))

if probabilidade >= 0.5:
    print("Pedro, você está proibido de apostar nos favoritos, só em zebra, lembra?")
else:
  if resultado == "Ganhou":
      if probabilidade > 0.4:
        print(f"Não foi um palpite tão arriscado, todos sabiam que {selecaoUm} não estava muito atrás de {selecaoDois}")
      elif probabilidade > 0.3:
        print(f"Eu pensava que {selecaoDois} iria ganhar, mas nunca duvidei que a {selecaoUm} pudesse ganhar essa partida")
      elif probabilidade > 0.2:
        print(f"Meu Deus! que jogo foi esse?? {selecaoUm} surpreendeu a todos nós…")
      elif probabilidade > 0.1:
        print(f"Essa é a copa das zebras?? O impossível aconteceu hoje nessa partida, como que {selecaoUm} ganhou de {selecaoDois}, alguém me explica?")
      elif probabilidade <= 0.1:
        print(f"PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na {selecaoUm}, somente você!")
      print(f"Parabéns, você apostou R${valorApostado} e recebeu R${retorno} nessa aposta")
  else:
    print("Pedro, infelizmente você está no fundo do poço, se endividou completamente e não temos o que fazer…")
    print(f"Você poderia ter ganhado R${retorno}, mas perdeu R${valorApostado}")