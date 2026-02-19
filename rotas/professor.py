import sqlite3
conexao = sqlite3.connect("baco-de-dados.db")
cursor = conexao.cursor()

def criar_professor():
    nome = input("Digite o nome do professor: ")
    formacao = input("Digite a formação do professor: ")

    cursor.execute("""INSERT INTO Professor (nome, formacao) VALUES (?, ?)""",
                   (nome, formacao))
    conexao.commit()

def listar_professor():
    cursor.execute("""SELECT * FROM Professor""")
    cursor.fetchall()
    professores = cursor.fetchall()
    for prof in professores:
        print(prof)

def alterar_professor():
    id_prof = input("Digite o id do professor: ")
    nome = input("Digite o nome do professor: ")
    formacao = input("Digite a formação do professor: ")

    cursor.execute("""UPDATE Professor SET nome = ? , formacao = ? WHERE id_professor = ?""",
                   (nome, formacao, id_prof))
    conexao.commit()

def deletar_professor():
    id_prof = input("Digite o id do professor: ")

    cursor.execute("""DELETE FROM Professor WHERE id_professor = ?""",
                   (id_prof))