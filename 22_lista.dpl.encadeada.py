from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

lista.insert(0, 'abacate')
lista.insert(0, 'mamão')
lista.insert(0, 'maçã')
lista.insert(0, 'abacaxi')

print(lista)

# inserção intermediária
lista.insert(2, 'ameixa')
print(lista)

# inserção na primeira posição
lista.insert(0, 'morango')
print(lista)
