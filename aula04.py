

idadeAluno: int = 11
nomeAluno: str = "cleito"



def exibeDadosAluno(prNomeAluno:str, prIdadeALuno: int, prStatusProva: bool, prTelefone: str):
    
    telefone: str = "49 9 88888888"
    statusProva: bool = False
    resposta: str = "OK"
    if idadeAluno < 18:
        return "erro001"
    elif statusProva == False:
        return "erro002"

    
    print(f"a idade do aluno é {prIdadeAluno}, e seu nome é {prNomeAluno} e seus telefone de contato é {prTelefone}")
    
    return resposta


resultadoFunção = exibeDadosAluno("cleito", 11 , False, "49 9 88888888"  )

if resultadoFunção == "OK":
    print("sucesso")
elif resultadoFunção == "erro001":
    print("menor de idade")
elif resultadoFunção == "erro002":
    print("Aluno não passou na prova")
else:
    print("Ocorreu um erro")

#não recebe e nao devolve nenhum retorno
def exibeNome():
    print("nome")

#recebe parametro e não devolve nenhum retorno 
def exibeNome(nome: str):
    print("nome")

#recebe o parametro nome que é do tipo string e 
# retorna um parametro tambem doi tipo string    
def exibeNome(nome: str) -> str:
    print("nome")
    return "OK"

#nao recebe parametro e retorna um parametro
def exibeNome() -> str:
    print("nome")
    return "OK"

#esse tipo de função variadica que recebe uma lista de parametros
def mostrarNumero(*numeros: int) -> bool:
    
    print(numeros)

    for nAtual in numeros[0]:
        print("o numero atual lido foi", nAtual)

    return True

#passa uma Tupla por parametro para a função mostraNumero = Tupla(10,20,30,40,50,60,71)

tuplaNumeros = (10,20,30,40,50,60,70,80,90,100)

print("Resultado foi:", mostrarNumero(tuplaNumeros))

listaDados = ["Teste", "Debug", "Compilar", "Python"]

print(listaDados[3][0])
