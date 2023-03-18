# recebe mensagem criptografada
codigo = input()

# invertendo a string recursivamente
def inverterString(codigo, contador):
    if contador == 0:
      return codigo[contador]
    else:
      return codigo[contador] + inverterString(codigo, contador-1)

print(inverterString(codigo, len(codigo)-1))