nome_1 = str(input())
ataque_1 = int(input())
defesa_1 = int(input())
folego_1 = int(input())
gols_1 = 0
fator_canseira_1 = 1 - ((5 - folego_1) / 10)

nome_2 = str(input())
ataque_2 = int(input())
defesa_2 = int(input())
folego_2 = int(input())
fator_canseira_2 = 1 - ((5 - folego_2) / 10)
gols_2 = 0

print("Início de jogo!")
print("1° tempo:")
print(f"{nome_1} [{gols_1}-{gols_2}] {nome_2}")

sorte_1 = int(input())
if sorte_1 == 1:
    ataque_1 += 2
else:
    defesa_2 += 2
print(f"O time {nome_1} vem pressionando.")
if ataque_1 >= defesa_2:
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_1}!!!")
    gols_1 += 1
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_2}")
if sorte_1 == 1:
    ataque_1 -= 2
else:
    defesa_2 -= 2

sorte_2 = int(input())
ataque_1 *= fator_canseira_1
defesa_1 *= fator_canseira_1
ataque_2 *= fator_canseira_2
defesa_2 *= fator_canseira_2
if sorte_2 == 1:
    ataque_2 += 2
else:
    defesa_1 += 2
print(f"O time {nome_2} vem pressionando.")
if ataque_2 >= defesa_1:
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_2}!!!")
    gols_2 += 1
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_1}")
if sorte_2 == 1:
    ataque_2 -= 2
else:
    defesa_1 -= 2

print("2° tempo:")
print(f"{nome_1} [{gols_1}-{gols_2}] {nome_2}")

sorte_3 = int(input())
ataque_1 *= fator_canseira_1
defesa_1 *= fator_canseira_1
ataque_2 *= fator_canseira_2
defesa_2 *= fator_canseira_2
if sorte_3 == 1:
    ataque_2 += 2
else:
    defesa_1 += 2
print(f"O time {nome_2} vem pressionando.")
if ataque_2 >= defesa_1:
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_2}!!!")
    gols_2 += 1
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_1}")
if sorte_3 == 1:
    ataque_2 -= 2
else:
    defesa_1 -= 2

sorte_4 = int(input())
ataque_1 *= fator_canseira_1
defesa_1 *= fator_canseira_1
ataque_2 *= fator_canseira_2
defesa_2 *= fator_canseira_2
if sorte_4 == 1:
    ataque_1 += 2
else:
    defesa_2 += 2
print(f"O time {nome_1} vem pressionando.")
if ataque_1 >= defesa_2:
    print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_1}!!!")
    gols_1 += 1
else:
    print(f"O ataque é interrompido! Ótima defesa do time {nome_2}")
if sorte_4 == 1:
    ataque_1 -= 2
else:
    defesa_2 -= 2

print(f"{nome_1} [{gols_1}-{gols_2}] {nome_2}")
if gols_1 == gols_2:
    print("Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!")
elif gols_1 > gols_2:
    print(f"ACABOOOOU!! O TIME {nome_1} É O CAMPEÃO!!!")
else:
    print(f"Fim de jogo! O time {nome_2} é campeão.")