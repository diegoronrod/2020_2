from No import No


class Pilha:

    def __init__(self):
        self.primeiro = None
        self.topo = None
        self.tamanho = 0

    def imprimir(self):
        if self.tamanho == 0:
            print('Pilha Vazia!!!')
        else:
            texto = ''
            aux = self.primeiro
            while (aux):
                texto = texto + str(aux.dado) + ' - '
                aux = aux.proximo
            print(texto)

    def adicionar(self, dado):
        no = No(dado)
        if self.topo is None:
            self.topo = no
        else:
            self.topo.proximo = no
            self.topo = no
        if self.primeiro is None:
            self.primeiro = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho == 0:
            print('Pilha Vazia!!!')
        elif self.tamanho == 1:
            self.primeiro = None
            self.topo = None
            self.tamanho -= 1
        else:
            self.topo = self.topo.anterior
            self.topo.proximo = None
            self.tamanho -= 1
