class Pessoa:
    def __init__(self, cod, nome, endereco, telefone):
        self.__codigo = cod
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        print(self.nome)

    def __imprimeTelefone(self):
        print(self.__telefone)
