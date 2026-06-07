from ui.usuario_ui import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario
)
from ui.livro_ui import (
    adicionar_livro,
    listar_livros,
    buscar_livro,
    atualizar_livro,
    remover_livro
)
from ui.emprestimo_ui import (
    adicionar_emprestimo,
    listar_emprestimos,
    buscar_emprestimo,
    devolucao_emprestimo
)

while True:
    print('\n===== BIBLIOTECA =====')
    print('1 - Cadastrar / Adicionar')
    print('2 - Listar')
    print('3 - Buscar')
    print('4 - Atualizar')
    print('5 - Remover')
    print('6 - Empréstimos')
    print('0 - Sair')

    opcao = input('\nEscolha uma opção: ')

    match opcao:

        case '1':
            while True:
                print('\n===== CADASTRAR / ADICIONAR =====')
                print('1 - Cadastrar usuário')
                print('2 - Adicionar livro')
                print('3 - Adicionar empréstimo')
                print('0 - Voltar')

                sub_opcao = input('\nEscolha uma opção: ')

                match sub_opcao:
                    case '1':
                        cadastrar_usuario()

                    case '2':
                        adicionar_livro()

                    case '3':
                        adicionar_emprestimo()

                    case '0':
                        break

                    case _:
                        print('Opção inválida!')

        case '2':
            while True:
                print('\n===== LISTAR =====')
                print('1 - Listar usuários')
                print('2 - Listar livros')
                print('3 - Listar empréstimos')
                print('0 - Voltar')

                sub_opcao = input('\nEscolha uma opção: ')

                match sub_opcao:
                    case '1':
                        listar_usuarios()

                    case '2':
                        listar_livros()

                    case '3':
                        listar_emprestimos()

                    case '0':
                        break

                    case _:
                        print('Opção inválida!')

        case '3':
            while True:
                print('\n===== BUSCAR =====')
                print('1 - Buscar usuário')
                print('2 - Buscar livro')
                print('3 - Buscar empréstimo')
                print('0 - Voltar')

                sub_opcao = input('\nEscolha uma opção: ')

                match sub_opcao:
                    case '1':
                        buscar_usuario()

                    case '2':
                        buscar_livro()

                    case '3':
                        buscar_emprestimo()

                    case '0':
                        break

                    case _:
                        print('Opção inválida!')

        case '4':
            while True:
                print('\n===== ATUALIZAR =====')
                print('1 - Atualizar usuário')
                print('2 - Atualizar livro')
                print('0 - Voltar')

                sub_opcao = input('\nEscolha uma opção: ')

                match sub_opcao:
                    case '1':
                        atualizar_usuario()

                    case '2':
                        atualizar_livro()

                    case '0':
                        break

                    case _:
                        print('Opção inválida!')

        case '5':
            while True:
                print('\n===== REMOVER =====')
                print('1 - Remover usuário')
                print('2 - Remover livro')
                print('0 - Voltar')

                sub_opcao = input('\nEscolha uma opção: ')

                match sub_opcao:
                    case '1':
                        remover_usuario()

                    case '2':
                        remover_livro()

                    case '0':
                        break

                    case _:
                        print('Opção inválida!')

        case '6':
            while True:
                print('\n===== EMPRÉSTIMOS =====')
                print('1 - Registrar devolução')
                print('0 - Voltar')

                sub_opcao = input('\nEscolha uma opção: ')

                match sub_opcao:
                    case '1':
                        devolucao_emprestimo()

                    case '0':
                        break

                    case _:
                        print('Opção inválida!')

        case '0':
            print('Sistema encerrado.')
            break

        case _:
            print('Opção inválida!')