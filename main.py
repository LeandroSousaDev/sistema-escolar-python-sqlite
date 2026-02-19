import menu
from rotas import curso, aluno


while True:
    menu.menu_principal()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu.menu_alunos()
        operacao = input("Escolha a operação: ")
        if operacao == "1":
            aluno.criar_aluno()
        if operacao == "2":
            aluno.listar_aluno()
        if operacao == "3":
            aluno.atualizar_aluno()
        if operacao == "4":
            aluno.deletar_aluno()
        if operacao == "0":
            break

    if opcao == "2":
        menu.menu_cursos()
        operacao = input("Escolha a operação: ")
        if operacao == "1":
            curso.criar_curso()
        if operacao == "2":
            curso.listar_cursos()
        if operacao == "3":
            curso.atualizar_curso()
        if operacao == "4":
            curso.deletar_curso()
        if operacao == "0":
            break


    if opcao == "3":
        menu.menu_professores()
    if opcao == "4":
        menu.menu_contratos()
    if opcao == "5":
        menu.menu_prontuarios()
    if opcao == "0":
        break