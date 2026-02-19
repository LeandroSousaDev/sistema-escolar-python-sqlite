import sqlite3
conexao = sqlite3.connect("baco-de-dados.db")
cursor = conexao.cursor()

def criar_prontuario():
    data_matricula = input("Digite o seu data de matricula: ")
    situacao = input("Digite o seu situacao da matricula: ")
    id_aluno = input("Digite o seu id aluno: ")

    cursor.execute("""INSERT INTO Prontuario (data_matricula, situacao_matricula, Aluno_id_aluno) VALUES (?, ?, ?)""",
                   (data_matricula, situacao, id_aluno))
    conexao.commit()

def listar_prontuario():
    cursor.execute("""SELECT * FROM Prontuario""")
    prontuarios = cursor.fetchall()
    for prontuario in prontuarios:
        print(prontuario)

def alterar_prontuario():
    id_prontuario = input("Digite o seu id prontuario: ")
    data_matricula = input("Digite o seu data de matricula: ")
    situacao = input("Digite o seu situacao da matricula: ")
    id_aluno = input("Digite o seu id aluno: ")

    cursor.execute("""UPDATE Prontuario SET data_matricula = ?, situacao_matricula = ?, Aluno_id_aluno = ? WHERE id_prontuario = ?""",
                   (data_matricula, situacao, id_aluno, id_prontuario))

def deletar_prontuario():
    id_prontuario = input("Digite o seu id prontuario: ")

    cursor.execute("""DELETE FROM Prontuario WHERE id_prontuario = ?""",
                   (id_prontuario))