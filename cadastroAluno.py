import sqlite3

##############################
#Definição de Variaveis Globais
##############################

##############################
#Definição de Funções
##############################
def mainMenu():
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar aluno")
    print("2. Listar Aluno")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao = input("Escolha uma opção:")
    return opcao

 
def createTable():
    conexao = sqlite3.connect("escola01.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    idade INTEGER
                   )                                             
        """)
    conexao.commit()
    conexao.close()


def register(nome,email,idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO aluno(nome,email,idade) VALUES (?,?,?)",
                       (nome,email,idade))
        conexao.commit()
        print("aluno cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("Email ja cadastrado")
    finally:
        conexao.close()

def display():
    conexao = sqlite3.connect("escola.db") #abrir conexao com banco
    cursor = conexao.cursor()

    cursor.execute("SELECTE * FROM aluno")
    alunos = cursor.fetchall()

    conexao.close() #fechei a conexao com banco

    print("Lista de alunos cadastrados")
    
    for aluno in alunos: 
        print(aluno)


if __name__ == "__main__":
    createTable()
    


    while True:
        opcao = mainMenu() 

        if opcao == "1":
            nome = input("Nome:")
            email = input("E-mail:")
            idade = int(input("Idade:"))
            register(nome,email,idade)
        elif opcao == "2":
            display()
        elif opcao == "5":
            break
        else:
            print("Opção invalida")