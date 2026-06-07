from models.pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, idade, matricula = None):
        super().__init__(nome, idade)
        self.matricula = matricula

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Matricula: {self.matricula}'