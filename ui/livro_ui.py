from models.livro import Livro
from services.biblioteca import biblioteca

def adicionar_livro():
    try:
        titulo = input('Digite o titulo do livro: ')
        autor = input('Digite o autor do livro: ')
        ano = int(input('Digite o ano do livro: '))

        livro = Livro(titulo, autor, ano)
        resultado = biblioteca.adicionar_livro(livro)

        if resultado:
            print('Livro adicionado com sucesso!')
        else:
            print('Erro ao adicionar livro!')

    except Exception as e:
        print(f'Erro ao adicionar livro: {e}')


def listar_livros():
    try:
        resultado = biblioteca.listar_livros()

        if resultado:
            for livro in resultado:
                print(f'ID: {livro.id_livro}. Livro: {livro.titulo}, autor: {livro.autor}, ano: {livro.ano}')
                print('-' * 30)
        else:
            print('Nenhum livro cadastrado!')
            return

    except Exception as e:
        print(f'Erro ao listar livros: {e}')


def buscar_livro():
    try:
        id_livro = int(input('Digite o id do livro: '))
        resultado = biblioteca.buscar_livro(id_livro)

        if resultado:
            print(f'ID: {resultado.id_livro}. Livro: {resultado.titulo}, autor: {resultado.autor}, ano: {resultado.ano}')
        else:
            print('ID de livro inexistente!')

    except Exception as e:
        print(f'Erro ao buscar livro: {e}')


def remover_livro():
    try:
        id_livro = int(input('Digite o id do livro: '))
        resultado = biblioteca.remover_livro(id_livro)

        if resultado:
            print('Livro removido com sucesso!')
        else:
            print('ID do livro inexistente!')

    except Exception as e:
        print(f'Erro ao remover livro: {e}')


def atualizar_livro():
    id_livro = int(input('Digite o id do livro: '))
    try:
        titulo = input('Digite novo titulo: ')
        autor = input('Digite autor do livro: ')
        ano = int(input('Digite ano do livro: '))

        resultado = biblioteca.atualizar_livro(id_livro, titulo, autor, ano)
        if resultado:
            print('Livro atualizado com sucesso!')
        else:
            print('ID do livro inexistente!')

    except Exception as e:
        print(f'Erro ao atualizar livro: {e}')