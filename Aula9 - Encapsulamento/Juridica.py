from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, cod, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, cod, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print(self.__cnpj)

    def __emitirNotaFiscal(self):
        print(self.__inscricaoEstadual)

    def getNotaFiscal(self):
        return (self.__emitirNotaFiscal())