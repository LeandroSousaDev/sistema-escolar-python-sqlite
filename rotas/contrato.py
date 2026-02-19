import sqlite3
conexao = sqlite3.connect("baco-de-dados.db")
cursor = conexao.cursor()

def criar_contrato():
    vinculo = input("Digite o vinculo do professor: ")
    carga_horaria_semanal = input("Digite a carga horaria semanal do professor: ")
    id_professor = input("Digite o id do professor: ")

    cursor.execute("""INSERT INTO Contrato (vinculo, carga_horaria_semanal, Professor_id_professor) VALUES (?,?,?)""",
                   (vinculo, carga_horaria_semanal,id_professor))
    conexao.commit()

def listar_contratos():
    cursor.execute("""SELECT * FROM Contrato""")
    contratos = cursor.fetchall()
    for contrato in contratos:
        print(contrato)

def alterar_contrato():
    id_contrato = input("Digite o id do contrato: ")
    vinculo = input("Digite o vinculo do professor: ")
    carga_horaria_semanal = input("Digite a carga horaria semanal do professor: ")
    id_professor = input("Digite o id do professor: ")

    cursor.execute("""UPDATE Contrato SET vinculo = ?, carga_horaria_semanal = ?, Professor_id_professor = ? WHERE id_contrato = ?""",
                   (vinculo, carga_horaria_semanal,id_professor,id_contrato))

def deletar_contrato():
    id_contrato = input("Digite o id do contrato: ")

    cursor.execute("""DELETE FROM Contrato WHERE id_contrato = ?""",
                   (id_contrato,))

def designar_professor_curso():
    id_professor = input("Digite o id do professor: ")
    id_curso = input("Digite o id do curso: ")

    cursor.execute("""INSERT INTO Professor_Curso (Professor_id_professor, Curso_id_curso) VALUES (?,?)""",
                   (id_professor, id_curso))
    conexao.commit()
