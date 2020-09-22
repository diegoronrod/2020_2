from No import No

class Lista:

    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar (self, valor):
        if self.inicio:
            aux = self.inicio
            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = No(valor)
        else:
            self.inicio = No(valor)
        self.tamanho = self.tamanho +1

    def imprimir(self):
        aux = self.inicio
        while (aux):
            print(aux.dado, '\n')
            aux = aux.proximo

    def excluir(self, valor):
        if self.tamanho  == 0:
            print('A lista esta vazia!!')
        elif self.tamanho == 1:
            if self.inicio.dado == valor:
                self.inicio = None
                self.tamanho -= 1
            else:
                print('Valor não encontrado!!')
        else:
            if self.inicio.dado == valor:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            else:
                ant = self.inicio
                aux = ant.proximo
                while (aux):
                    if aux.dado == valor:
                        ant.proximo = aux.proximo
                    ant = aux
                    aux = aux.proximo
                self.tamanho -= 1
