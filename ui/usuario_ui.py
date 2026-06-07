from models.usuario import Usuario
from services.biblioteca import biblioteca

def cadastrar_usuario():
    try:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))

        usuario = Usuario(nome, idade)

        resultado = biblioteca.adicionar_usuario(usuario)

        if resultado:
            print('Usuario adicionado com sucesso!')
        else:
            print('Erro ao adicionar usuario!')

    except Exception as e:
        print(f'Erro ao cadastrar usuario: {e}')


def listar_usuarios():
    try:
        resultado = biblioteca.listar_usuarios()

        if resultado:
            for usuario in resultado:
                print(f'Matricula: {usuario.matricula}, Nome: {usuario.nome}, idade: {usuario.idade}')
        else:
            print('Nenhum usuário cadastrado!')

    except Exception as e:
        print(f'Erro ao listar usuarios: {e}')


def buscar_usuario():
    try:
        matricula = int(input('Digite a matricula do usuario: '))

        resultado = biblioteca.buscar_usuario(matricula)

        if resultado:
            print(f'Matricula: {resultado.matricula}, Nome: {resultado.nome}, idade: {resultado.idade}')
        else:
            print('Usuario não encontrado!')

    except Exception as e:
        print(f'Erro ao buscar usuario: {e}')


def remover_usuario():
    try:
        matricula = int(input('Matricula do usuario que deseja remover: '))
        resultado = biblioteca.remover_usuario(matricula)

        if resultado:
            print('Usuario removido com sucesso!')
        else:
            print('Matricula inexistente!')

    except Exception as e:
        print(f'Erro ao remover usuario: {e}')


def atualizar_usuario():
    try:
        matricula = int(input('Matricula do usuario que deseja atualizar: '))
        nome = input('Digite novo nome: ')
        idade = int(input('Digite nova idade: '))

        resultado = biblioteca.atualizar_usuario(matricula, nome, idade)
        if resultado:
            print('Usuario atualizado com sucesso!')
        else:
            print('Matricula inexistente!')

    except Exception as e:
        print(f'Erro ao atualizar usuario: {e}')