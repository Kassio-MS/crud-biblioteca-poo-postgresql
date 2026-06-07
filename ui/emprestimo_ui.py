from models.emprestimo import Emprestimo
from services.biblioteca import biblioteca

def adicionar_emprestimo():
    try:
        matricula_usuario = int(input('Digite a matricula do usuario: '))
        usuario = biblioteca.buscar_usuario(matricula_usuario)

        id_livro = int(input('Digite o id do livro: '))
        livro = biblioteca.buscar_livro(id_livro)

        if not usuario:
            print('Usuário inexistente!')
            return
        if not livro:
            print('Livro inexistente!')
            return

        emprestimo = Emprestimo(usuario, livro)
        resultado = biblioteca.adicionar_emprestimo(emprestimo)

        if resultado:
            print('Emprestimo adicionado com sucesso!')
        else:
            print('Erro ao adicionar emprestimo!')

    except Exception as e:
        print(f'Erro ao adicionar emprestimo: {e}')

def listar_emprestimos():
    try:
        resultado = biblioteca.listar_emprestimos()

        if resultado:
           for row in resultado:
               print(f'ID: {row[0]} |'
                     f'Data Emprestimo: {row[1]} |'
                     f'Matricula: {row[2]} |'
                     f'Nome: {row[3]} |'
                     f'Livro: {row[5]} |'
                     f'ID Livro: {row[4]} |'
                     f'Data Devolução: {row[6]} |'
                     f'Status: {row[7]}')
               print('-' * 30)
        else:
            print('Nenhum emprestimo existente!')

    except Exception as e:
        print(f'Erro ao listar emprestimos: {e}')

def buscar_emprestimo():
    try:
        id_emprestimo = int(input('Digite o ID do emprestimo: '))
        resultado = biblioteca.buscar_emprestimo(id_emprestimo)

        if resultado:
            print(f'ID: {resultado[0]} |'
                  f'Data Emprestimo: {resultado[1]} |'
                  f'Matricula: {resultado[2]} |'
                  f'Nome: {resultado[3]} |'
                  f'Livro: {resultado[5]} |'
                  f'ID Livro: {resultado[4]} |'
                  f'Data Devolução: {resultado[6]} |'
                  f'Status: {resultado[7]}')
        else:
            print('Emprestimo não encontrado!')

    except Exception as e:
        print(f'Erro ao buscar emprestimo: {e}')

def devolucao_emprestimo():
    try:
        id_emprestimo = int(input('Digite o ID do emprestimo para devolução: '))
        emprestimo_status = biblioteca.buscar_emprestimo(id_emprestimo)
        if not emprestimo_status:
            print('ID do emprestimo inexistente!')
            return
        elif emprestimo_status[7] == 'devolvido':
            print('Esse emprestimo ja foi devolvido')
            return

        resultado = biblioteca.devolucao_emprestimo(id_emprestimo)

        if resultado:
            print(f"Status alterado para 'devolvido'!")
        else:
            print('Não foi possível registrar a devolução.')

    except Exception as e:
        print(f'Erro ao alterar status do emprestimo: {e}')