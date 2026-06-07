from database.connection import get_connection
from models.usuario import Usuario
from models.livro import Livro
from models.emprestimo import Emprestimo
import logging


class Biblioteca:
    def __init__(self):
        pass

    def adicionar_emprestimo(self, emprestimo):
       try:
           with get_connection() as conn:
               with conn.cursor() as cursor:
                   cursor.execute('''
                        INSERT INTO emprestimos (matricula_usuario, id_livro)
                        VALUES (%s, %s)
                   ''', (emprestimo.usuario.matricula, emprestimo.livro.id_livro))

                   conn.commit()
                   return cursor.rowcount > 0

       except Exception as e:
           logging.error(f'Erro ao adicionar emprestimo: {e}')
           raise

    def listar_emprestimos(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT e.id, e.data_emprestimo, u.matricula, u.nome, l.id_livro, l.titulo, e.data_devolucao, e.status
                        FROM emprestimos AS e
                        INNER JOIN usuarios AS u ON e.matricula_usuario = u.matricula 
                        INNER JOIN livros AS l ON e.id_livro = l.id_livro
                    ''')
                    rows = cursor.fetchall()
                    return rows

        except Exception as e:
            logging.error(f'erro ao listar emprestimos: {e}')
            raise

    def buscar_emprestimo(self, id_emprestimo):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT e.id, e.data_emprestimo, u.matricula, u.nome, l.id_livro, l.titulo, e.data_devolucao, e.status
                        FROM emprestimos AS e
                        INNER JOIN usuarios AS u ON e.matricula_usuario = u.matricula
                        INNER JOIN livros AS l ON e.id_livro = l.id_livro
                        WHERE e.id = %s
                    ''', (id_emprestimo,))
                    row = cursor.fetchone()
                    return row

        except Exception as e:
            logging.error(f'Erro ao buscar emprestimo: {e}')
            raise

    def devolucao_emprestimo(self, id_emprestimo):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        UPDATE emprestimos
                        SET status = 'devolvido',
                            data_devolucao = CURRENT_DATE
                        WHERE id = %s
                    ''', (id_emprestimo,))

                    conn.commit()
                    return cursor.rowcount > 0

        except Exception as e:
            logging.error(f'Erro ao registrar devolução: {e}')
            raise

    def adicionar_livro(self, livro: Livro):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        INSERT INTO livros (titulo, autor, ano)
                        VALUES (%s, %s, %s)
                    ''', (livro.titulo, livro.autor, livro.ano))

                    conn.commit()
                    return True

        except Exception as e:
            logging.error(f'Erro ao adicionar livro: {e}')
            raise

    def listar_livros(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT * FROM livros
                    ''')
                    rows = cursor.fetchall()

                    livros = []
                    for row in rows:
                        livro = Livro(
                            id_livro = row[0],
                            titulo = row[1],
                            autor = row[2],
                            ano = row[3]
                        )
                        livros.append(livro)
                    return livros

        except Exception as e:
            logging.error(f'Erro ao listar livros: {e}')
            raise

    def buscar_livro(self, id_livro):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT * FROM livros WHERE id_livro = %s
                    ''', (id_livro,))
                    row = cursor.fetchone()

                    if row:
                        return Livro(
                            id_livro = row[0],
                            titulo = row[1],
                            autor = row[2],
                            ano = row[3]
                        )
                    return None

        except Exception as e:
            logging.error(f'Erro ao buscar livro: {e}')
            raise

    def remover_livro(self, id_livro):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        DELETE FROM livros
                        WHERE id_livro = %s
                    ''', (id_livro,))

                    conn.commit()
                    return cursor.rowcount > 0

        except Exception as e:
            logging.error(f'Erro ao remover livro: {e}')
            raise

    def atualizar_livro(self, id_livro, titulo, autor, ano):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        UPDATE livros
                        SET titulo = %s, autor = %s, ano = %s
                        WHERE id_livro = %s 
                    ''', (titulo, autor, ano, id_livro))

                    conn.commit()
                    return cursor.rowcount > 0

        except Exception as e:
            logging.error(f'Erro ao atualizar livro: {e}')
            raise

    def adicionar_usuario(self, usuario: Usuario):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        INSERT INTO usuarios (nome, idade)
                        VALUES (%s, %s)
                    ''', (usuario.nome, usuario.idade))

                    conn.commit()
                    return True

        except Exception as e:
            logging.error(f'Erro ao adicionar usuario: {e}')
            raise

    def listar_usuarios(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT * FROM usuarios
                    ''')
                    rows = cursor.fetchall()

                    usuarios = []
                    for row in rows:
                        usuario = Usuario(
                            matricula = row[0],
                            nome = row[1],
                            idade = row[2]
                        )
                        usuarios.append(usuario)
                    return usuarios

        except Exception as e:
            logging.error(f'Erro ao listar usuarios: {e}')
            raise

    def buscar_usuario(self, matricula):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        SELECT * FROM usuarios WHERE matricula = %s
                    ''', (matricula,))
                    row = cursor.fetchone()

                    if row:
                        return Usuario(
                            matricula=row[0],
                            nome = row[1],
                            idade = row[2]
                        )
                    return None

        except Exception as e:
            logging.error(f'Erro ao buscar usuario: {e}')
            raise

    def remover_usuario(self, matricula):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        DELETE FROM usuarios WHERE matricula = %s
                    ''', (matricula,))

                    conn.commit()
                    return cursor.rowcount > 0

        except Exception as e:
            logging.error(f'Erro ao remover usuario: {e}')
            raise

    def atualizar_usuario(self, matricula, nome, idade):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('''
                        UPDATE usuarios
                        SET nome = %s, idade = %s
                        WHERE matricula = %s
                    ''', (nome, idade, matricula))

                    conn.commit()
                    return cursor.rowcount > 0

        except Exception as e:
            logging.error(f'Erro ao atualizar usuario: {e}')
            raise


biblioteca = Biblioteca()

