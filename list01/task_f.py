anoCopa = input()

nome_selecao1 = input()
vitorias_time1 = int(input())
empates_time1 = int(input())
pontos_time1 = vitorias_time1 * 3 + empates_time1

nome_selecao2 = input()
vitorias_time2 = int(input())
empates_time2 = int(input())
pontos_time2 = vitorias_time2 * 3 + empates_time2

nome_selecao3 = input()
vitorias_time3 = int(input())
empates_time3 = int(input())
pontos_time3 = vitorias_time3 * 3 + empates_time3

tipo_consulta = input()

if tipo_consulta == "Critério Geral":
  print(f"A classificação na copa de {anoCopa} foi:")
  if pontos_time1 > pontos_time2:
    if pontos_time2 > pontos_time3:
        print(f"{nome_selecao1} - {pontos_time1}")
        print(f"{nome_selecao2} - {pontos_time2}")
        print(f"{nome_selecao3} - {pontos_time3}")
    else:
        if pontos_time1 > pontos_time3:
            print(f"{nome_selecao1} - {pontos_time1}")
            print(f"{nome_selecao3} - {pontos_time3}")
            print(f"{nome_selecao2} - {pontos_time2}")
        else:
            print(f"{nome_selecao3} - {pontos_time3}")
            print(f"{nome_selecao1} - {pontos_time1}")
            print(f"{nome_selecao2} - {pontos_time2}")
  else:
    if pontos_time3 > pontos_time2:
        print(f"{nome_selecao3} - {pontos_time3}")
        print(f"{nome_selecao2} - {pontos_time2}")
        print(f"{nome_selecao1} - {pontos_time1}")
    else:
        if pontos_time3 > pontos_time1:
            print(f"{nome_selecao2} - {pontos_time2}")
            print(f"{nome_selecao3} - {pontos_time3}")
            print(f"{nome_selecao1} - {pontos_time1}")
        else:
            print(f"{nome_selecao2} - {pontos_time2}")
            print(f"{nome_selecao1} - {pontos_time1}")
            print(f"{nome_selecao3} - {pontos_time3}")
else:
  print(f"O times por ordem Lexicográfica da copa de {anoCopa} são:")
  if nome_selecao1 < nome_selecao2:
    if nome_selecao2 < nome_selecao3:
        print(f"{nome_selecao1} - {pontos_time1}")
        print(f"{nome_selecao2} - {pontos_time2}")
        print(f"{nome_selecao3} - {pontos_time3}")
    else:
        if nome_selecao1 < nome_selecao3:
            print(f"{nome_selecao1} - {pontos_time1}")
            print(f"{nome_selecao3} - {pontos_time3}")
            print(f"{nome_selecao2} - {pontos_time2}")
        else:
            print(f"{nome_selecao3} - {pontos_time3}")
            print(f"{nome_selecao1} - {pontos_time1}")
            print(f"{nome_selecao2} - {pontos_time2}")
  else:
    if nome_selecao3 < nome_selecao2:
        print(f"{nome_selecao3} - {pontos_time3}")
        print(f"{nome_selecao2} - {pontos_time2}")
        print(f"{nome_selecao1} - {pontos_time1}")
    else:
        if nome_selecao3 < nome_selecao1:
            print(f"{nome_selecao2} - {pontos_time2}")
            print(f"{nome_selecao3} - {pontos_time3}")
            print(f"{nome_selecao1} - {pontos_time1}")
        else:
            print(f"{nome_selecao2} - {pontos_time2}")
            print(f"{nome_selecao1} - {pontos_time1}")
            print(f"{nome_selecao3} - {pontos_time3}")