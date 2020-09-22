from Lista import Lista

lista = Lista()


print('Tamanho da lista: ' + str(lista.tamanho))

lista.adicionar(3)

print('Tamanho da lista: ' + str(lista.tamanho))

lista.imprimir()

valor = input('Digite um valor: ')
lista.adicionar(valor)
lista.imprimir()

valor = input('Digite um valor que deseja excluir: ')
lista.excluir(valor)
lista.imprimir()