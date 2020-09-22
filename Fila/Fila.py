from No import No

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def imprimir(self):
        if self.tamanho == 0:
            print('Fila Vazia!!!')
        else:
            texto = ''
            aux = self.primeiro
            while(aux):
                texto = texto + str(aux.dado) + ' - '
                aux = aux.proximo
            print(texto)

    def adicionar(self, dado):
        no = No(dado)
        if self.ultimo is None:
            self.ultimo = no
        else:
            self.ultimo.proximo = no
            self.ultimo = no
        if self.primeiro is None:
            self.primeiro = no
        self.tamanho += 1
        self.imprimir()

    def remover(self):
        if self.tamanho == 0:
            print('Fila Vazia!!!')
        elif self.tamanho == 1:
            self.primeiro = None
            self.ultimo = None
            self.tamanho -= 1
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
