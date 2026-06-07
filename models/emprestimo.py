class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro

    def __str__(self):
        return f'Usuario: {self.usuario} - Livro: {self.livro}'