import sqlite3
conexao = sqlite3.connect("baco-de-dados.db")
cursor = conexao.cursor()


def criar_curso():
    nome = input("Digite o nome do curso: ")
    carga_horaria = input("Digite a carga horaria")

    cursor.execute("""INSERT INTO Curso (nome, carga_horaria) VALUES (?,?)""",
                       (nome, carga_horaria))
    conexao.commit()

def listar_cursos():
    cursor.execute("""SELECT * FROM Curso""")
    cursos = cursor.fetchall()
    for curso in cursos:
        print(curso)


def atualizar_curso():
    id_curso = input("Digite o id do curso: ")
    nome = input("Digite o nome do curso: ")
    carga_horaria = input("Digite a carga horaria: ")
    cursor.execute("""UPDATE Curso SET nome = ?, carga_horaria= ? WHERE id = ?""",
                       (nome, carga_horaria, id_curso))
    conexao.commit()

def deletar_curso():
    id_curso = input("Digite o id do curso: ")
    cursor.execute("""DELETE FROM Curso WHERE id = ?""", (id_curso,))
