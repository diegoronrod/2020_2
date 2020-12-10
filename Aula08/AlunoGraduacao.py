from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def Imprimir(self):
        Aluno.Imprimir(self)
        print(str('Ano: ' + self.ano))

