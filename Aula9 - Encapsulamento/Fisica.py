from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, cod, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, cod, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimeCPF(self):
        print(self.__cpf)

    def __calculaIMC(self):
        return float(self.peso / (self.altura * self.altura))

    def getIMC(self):
        return (self.__calculaIMC())