from Aluno import Aluno

class AluEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre= semestre

    def Imprimir(self):
        Aluno.Imprimir(self)
        print(str('Semestre: ' + self.semestre))
