nomeInvencao = input()

# declarando variaveis importantes
custo = 0
etapasRealizadas = 0
etapasFalhas = 0

# executando um loop enquanto nao receber concluir ou desistir
nomeEtapa = input()
while nomeEtapa != "concluir" and nomeEtapa != "desistir":
    custoEtapa = int(input())

    if nomeEtapa == "dar um plus":
        custo += custoEtapa
        print(f"Agora o(a) {nomeInvencao} ficou ainda mais legal! Pena que precisei gastar R${custoEtapa}")
    else:
        tentativasEtapa = int(input())
        # verificando o status de n tentativas e calculando as etapas falhas e realizadas
        for i in range(0, tentativasEtapa):
            status = input()
            custo += custoEtapa
            if status == "incorreto":
                etapasFalhas += 1
                print(f"Ainda não consegui {nomeEtapa} corretamente, e essa tentativa me custou R${custoEtapa}")
            elif status == "correto":
                etapasRealizadas += 1
                print(f"Oba! consegui {nomeEtapa}, o que me custou R${custoEtapa}")
                break
        print(f"ANDAMENTO DO PROJETO: Etapas realizadas - {etapasRealizadas} ; Tentativas falhas - {etapasFalhas}")

    nomeEtapa = input()

print(f"A jornada da construção do(a) {nomeInvencao} acaba aqui.")
if nomeEtapa == "concluir":
    print(f"Uhuuu, finalmente o(a) {nomeInvencao} tá pronto(a)! Esse projeto me custou R${custo}")
elif nomeEtapa == "desistir":
    print(f"Infelizmente, o sonho do(a) {nomeInvencao} foi interrompido e levou junto com ele R${custo}")
