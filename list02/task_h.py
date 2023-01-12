print("Roteiro emitido!")

print("DIA:")
# iniciando um contador de quantos acoes serao feitas e recebendo a primeira acao
acao = input()
contadorDia = 0

# criando uma variavel para disponibilidade de cada lugar e colocando como true
praiaAmor = True
passeioLancha = True
surfPipa = True
porDoSol = True
passeioBuggy = True
tirolesa = True

# Verificando os locais recebidos e caso esteja disponivel, contabilizando e mudando disponibilidade
while acao != "NOITE":
    if acao == "Ir para a Praia do Amor" and praiaAmor:
        praiaAmor = False
        contadorDia += 1
        print(acao)
    elif acao == "Passeio de Lancha" and passeioLancha:
        passeioLancha = False
        contadorDia += 1
        print(acao)
    elif acao == "Surf na Praia de Pipa" and surfPipa:
        surfPipa = False
        contadorDia += 1
        print(acao)
    elif acao == "Por do sol no chapadão" and porDoSol:
        porDoSol = False
        contadorDia += 1
        print(acao)
    elif acao == "Passeio de buggy" and passeioBuggy:
        passeioBuggy = False
        contadorDia += 1
        print(acao)
    elif acao == "Arborismo e Tirolesa" and tirolesa:
        tirolesa = False
        contadorDia += 1
        print(acao)
    else:
        print("[INVALIDO]")
    acao = input()


print("NOITE:")
contadorNoite = 0

# criando uma variavel para disponibilidade de cada lugar e colocando como true
jantarGastronomico = True
passeioCentro = True
luau = True
festa = True

# verificando se as acoes do dia foram par ou impar
if contadorDia % 2 == 0:
    acaoNoite = input()
    # Verificando os locais recebidos e caso esteja disponivel, contabilizando e mudando disponibilidade
    while acaoNoite != "Oba, Tudo planejado!!":
        if acaoNoite == "Jantar gastronômico" and jantarGastronomico:
            jantarGastronomico = False
            contadorNoite += 1
            print(acaoNoite)
        elif acaoNoite == "Passear pelo centrinho" and passeioCentro:
            passeioCentro = False
            contadorNoite += 1
            print(acaoNoite)
        elif acaoNoite == "Luau" and luau:
            luau = False
            contadorNoite += 1
            print(acaoNoite)
        elif acaoNoite == "Festa com DJ" and festa:
            festa = False
            contadorNoite += 1
            print(acaoNoite)
        else:
            print("[INVALIDO]")
        acaoNoite = input()
else:
    # Verificando os locais recebidos e caso esteja disponivel, contabilizando e mudando disponibilidade
    for i in range(2):
        acaoNoite = input()
        if acaoNoite == "Jantar gastronômico" and jantarGastronomico:
            jantarGastronomico = False
            contadorNoite += 1
            print(acaoNoite)
        elif acaoNoite == "Passear pelo centrinho" and passeioCentro:
            passeioCentro = False
            contadorNoite += 1
            print(acaoNoite)
        elif acaoNoite == "Luau" and luau:
            luau = False
            contadorNoite += 1
            print(acaoNoite)
        elif acaoNoite == "Festa com DJ" and festa:
            festa = False
            contadorNoite += 1
            print(acaoNoite)
        else:
            print("[INVALIDO]")

# printando mensagem final com numero de atividades
numeroAtividades = contadorDia + contadorNoite
print(f"Venha curtir esse dia em Pipa com um roteiro com {numeroAtividades} atividade(s)!")
