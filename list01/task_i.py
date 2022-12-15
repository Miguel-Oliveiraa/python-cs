FavoritismoBr = int(input())
faseBrasil = "Oitavas"

if faseBrasil == "Oitavas":
  NomeOponente1 = str(input())
  FavoritismoOponente1 = int(input())
  GolsBR1 = int(input())
  GolsOPO1 = int(input())
  if GolsBR1 == GolsOPO1:
      if FavoritismoBr > FavoritismoOponente1:
          print("No sufoco, o Brasil conseguiu ganhar!!!")
          faseBrasil="Quartas"
      else:
          print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
  elif GolsBR1 > GolsOPO1:
    if (GolsBR1 - GolsOPO1) >2:
      FavoritismoBr += 30
    elif (GolsBR1 - GolsOPO1) >1:
      FavoritismoBr += 20
    else:
      FavoritismoBr += 10
    print("Quem é que segura o Brasil???")
    faseBrasil="Quartas"
  else:
    print(f"Infelizmente essa seleção dx {NomeOponente1} era muito forte para o Brasil.")

if faseBrasil == "Quartas":
  NomeOponente2 = str(input())
  FavoritismoOponente2 = int(input())
  GolsBR2 = int(input())
  GolsOPO2 = int(input())
  if GolsBR2 == GolsOPO2:
    if FavoritismoBr > FavoritismoOponente2:
      print("No sufoco, o Brasil conseguiu ganhar!!!")
      faseBrasil="Semis"
    else:
      print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
  elif GolsBR2 > GolsOPO2:
    if (GolsBR2 - GolsOPO2) > 2:
      FavoritismoBr += 30
    elif (GolsBR2 - GolsOPO2) > 1:
      FavoritismoBr += 20
    else:
      FavoritismoBr += 10
    print("Quem é que segura o Brasil???")
    faseBrasil="Semis"
  else:
    print(f"Infelizmente essa seleção dx {NomeOponente2} era muito forte para o Brasil.")

if faseBrasil == "Semis":
  NomeOponente3 = str(input())
  FavoritismoOponente3 = int(input())
  GolsBR3 = int(input())
  GolsOPO3 = int(input())
  if GolsBR3 == GolsOPO3:
    if FavoritismoBr > FavoritismoOponente3:
      print("No sufoco, o Brasil conseguiu ganhar!!!")
      faseBrasil="Finais"
    else:
      print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
  elif GolsBR3 > GolsOPO3:
    if (GolsBR3 - GolsOPO3) > 2:
      FavoritismoBr += 30
    elif (GolsBR3 - GolsOPO3) > 1:
      FavoritismoBr += 20
    else:
      FavoritismoBr += 10
    print("Quem é que segura o Brasil???")
    faseBrasil="Finais"
  else:
    print(f"Infelizmente essa seleção dx {NomeOponente3} era muito forte para o Brasil.")

if faseBrasil == "Finais":
  NomeOponente4 = str(input())
  FavoritismoOponente4 = int(input())
  if FavoritismoBr > FavoritismoOponente4:
    print("O BRASIL VAI SER HEXAAAAAAAA")
    faseBrasil="Campeao"
  else:
    print(f"O nosso Brasil foi vice, não conseguindo bater a seleção dx {NomeOponente4} na simulação")

