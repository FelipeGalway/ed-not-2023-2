from lib.stack import Stack

# Criando um nova pilha
pilha = Stack()

palavra = 'LARANJA'

#Empilhando as letras da palavra
for letra in palavra:
    pilha.push(letra)
    print(pilha)


print('-' * 80)


inverso = ""

#Desempilhando e colocando cada letr retirada dentro da string inverso
while not pilha.is_empty():
    inverso += pilha.pop()
    print(pilha)

print('-' * 80)

print(f"Palavra original: {palavra}")
print(f"Palavra invertida: {inverso}")