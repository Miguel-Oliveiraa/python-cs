# variaveis basicas
proximaAcao = input()
passouProtetor = False
dinheiroNaCarteira = 0
clima = "ensolarado"

# tratando os inputs enquanto a proxima acao nao eh ir para a praia
while proximaAcao != "ir para a praia":
    if proximaAcao == "separar dinheiro":
        dinheiro = float(input())
        dinheiroNaCarteira += dinheiro
    elif proximaAcao == "passar protetor":
        passouProtetor = True
    elif proximaAcao == "choveu":
        clima = "chuvoso"
    elif proximaAcao == "parou de chover":
        clima = "ensolarado"
    proximaAcao = input()

# verificando se choveu ou nao
if clima == "chuvoso":
    print("Hoje não vai dar pra ir, chuvinha barrou")
elif clima == "ensolarado":
    print("Hoje tem sol e mar!")
    # vericando os dinhero quando ele passou protetor
    if passouProtetor:
        if dinheiroNaCarteira < 10:
            print("Só faltou uma aguinha de coco...")
        else:
            print("Aí sim! Hoje rendeu!")
    # verificando o dinhero quando ele nao passou protetor
    else:
        if (dinheiroNaCarteira < 10):
            print("Você não chegou muito bem, chame um médico!")
        else:
            print("O novo camarão do CIn foi criado")
