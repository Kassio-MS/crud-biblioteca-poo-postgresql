class Livro:
    def __init__(self, titulo, autor, ano, id_livro = None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.id_livro = id_livro
    def __str__(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}'