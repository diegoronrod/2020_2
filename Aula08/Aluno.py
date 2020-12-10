class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def Imprimir(self):
        print(str('\nCódigo: ' + self.codigo + '\nNome: ' + self.nome + '\nMatricula: ' + self.matricula))
