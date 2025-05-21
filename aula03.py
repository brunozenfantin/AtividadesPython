def exibirInformações(**dados):

    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibirInformações(ender = "rua das pitanga", cpf = "009966775", nome = "cleito rasta")

def somar(a, b):
    return a + b

X = somar

resultadoDaSoma = somar(10, 200)

print(resultadoDaSoma)

print(X(30, 40))