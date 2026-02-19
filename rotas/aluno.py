import sqlite3
conexao = sqlite3.connect("baco-de-dados.db")
cursor = conexao.cursor()

def criar_aluno():
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o cpf do aluno: ")
    data_nascimento = input("Digite o data de nascimento do aluno: ")
    curso = input("Digite o codigo do curso do aluno: ")

    cursor.execute("""INSERT INTO Aluno (nome, cpf, data_nascimento, Curso_id_curso) VALUES (?,?,?,?)""",
                   (nome, cpf, data_nascimento, curso))
    conexao.commit()

def listar_aluno():
    cursor.execute("""SELECT * FROM Aluno""")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)

def atualizar_aluno():
    id_aluno = input("Digite o id do aluno: ")
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o cpf do aluno: ")
    data_nascimento = input("Digite o data de nascimento: ")
    curso = input("Digite o codigo do curso do aluno: ")

    cursor.execute("""UPDATE Aluno SET nome = ?, cpf = ?, data_nascimento = ?, Curso_id_curso = ? WHERE id_aluno = ?""",
                   (nome, cpf, data_nascimento,curso ,id_aluno))
    conexao.commit()

def deletar_aluno():
    id_aluno = input("Digite o id do aluno: ")
    cursor.execute("""DELETE FROM Aluno WHERE id_aluno = ?""",
                   (id_aluno))
    conexao.commit()