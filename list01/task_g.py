nome_time_1 =  input()
pontosTime1 = 0
resultado_jogo_1_time_1 = input()
if resultado_jogo_1_time_1 == "Ganhou":
  pontosTime1 += 3
elif resultado_jogo_1_time_1 == "Empatou":
  pontosTime1 += 1
resultado_jogo_2_time_1 = input()
if resultado_jogo_2_time_1 == "Ganhou":
  pontosTime1 += 3
elif resultado_jogo_2_time_1 == "Empatou":
  pontosTime1 += 1

nome_time_2 =  input()
pontosTime2 = 0
resultado_jogo_1_time_2 = input()
if resultado_jogo_1_time_2 == "Ganhou":
  pontosTime2 += 3
elif resultado_jogo_1_time_2 == "Empatou":
  pontosTime2 += 1
resultado_jogo_2_time_2 = input()
if resultado_jogo_2_time_2 == "Ganhou":
  pontosTime2 += 3
elif resultado_jogo_2_time_2== "Empatou":
  pontosTime2 += 1

nome_time_3 = input()
pontosTime3 = 0
resultado_jogo_1_time_3 = input()
if resultado_jogo_1_time_3 == "Ganhou":
  pontosTime3 += 3
elif resultado_jogo_1_time_3 == "Empatou":
  pontosTime3 += 1
resultado_jogo_2_time_3 = input()
if resultado_jogo_2_time_3 == "Ganhou":
  pontosTime3 += 3
elif resultado_jogo_2_time_3 == "Empatou":
  pontosTime3 += 1

if pontosTime3 < pontosTime1 and pontosTime3 < pontosTime2:
  print(f"Parabéns aos países {nome_time_1} e {nome_time_2}, vocês estão classificados para as oitavas de finais!!!")

if pontosTime2 < pontosTime3 and pontosTime2 < pontosTime1:
  print(f"Parabéns aos países {nome_time_1} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!")

if pontosTime1 < pontosTime3 and pontosTime1 < pontosTime2:
  print(f"Parabéns aos países {nome_time_2} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!")
