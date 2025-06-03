import sqlite3

##############################
#Definição de Variaveis Globais
##############################

##############################
#Definição de Funções
##############################
def mainMenu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar aluno")
    print("2. Listar Aluno")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao: str = input("Escolha uma opção:")
    return opcao

 
def createTable():
    conexao = sqlite3.connect("C:/Projeto/Backend/escola01.db")
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


def register(nome: str,email: str,idade: int):
    conexao = sqlite3.connect("C:/Projeto/Backend/escola01.db")
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
    conexao = sqlite3.connect("C:/Projeto/Backend/escola01.db") #abrir conexao com banco
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    conexao.close() #fechei a conexao com banco

    print("Lista de alunos cadastrados")
    
    for aluno in alunos: 
        print(aluno)

def delete(id: str):
    conexao = sqlite3.connect("C:/Projeto/Backend/escola01.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM aluno WHERE id = ?",
                   (id))
    conexao.commit()
    
    print("Aluno deletado com sucesso")
    
    conexao.close() 
    

def update(id, newNome, newEmail ,newIdade):

    conexao = sqlite3.connect("C:/Projeto/Backend/escola01.db") #abrir conexao com banco
    cursor = conexao.cursor()

    cursor.execute("UPDATE aluno SET nome = ?, email = ?, idade = ? WHERE id = ?",
                   ( newNome, newEmail ,newIdade, id))
    
    conexao.commit()
    conexao.close()
    print("Aluno atualizado com sucesso")

if __name__ == "__main__":
    createTable()
    


    while True:
        opcao = mainMenu() 

        if opcao == "1":
            nome: str = input("Nome:")
            email: str = input("E-mail:")
            idade = int(input("Idade:"))
            register(nome,email,idade)
        elif opcao == "2":
            display()
        elif opcao == "3":
            id = int(input("Informe o id do aluno que vc deseja atualizar: "))
            newNome = input("novo nome: ")
            newEmail = input("novo email: ")
            newIdade = int(input("nova idade: "))            
            update(id,newNome,newEmail,newIdade)
        elif opcao == "4":
            id = input("Informe o id do aluno que vc quer excluir: ")
            delete(id)
        elif opcao == "5":
            break
        else:
            print("Opção invalida")