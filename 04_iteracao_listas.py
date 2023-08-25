# Listas de frutas
frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer uma lista e exibir apenas seus elementos,
# usamos a estrutura for ... in, como já vimos no arquivo nº 02

for f in frutas:
    print(f)

#traço
print ("-"*40)

# Imprimindo uma lista de trás para frente: reversed()
for x in reversed(frutas):
    print(x)

#traço
print ("-"*40)

# No entanto, frequantemente precisamos exibir, além do valor do elemento, também 
# sua posição. Nesse caso, devemos usar a estrutura for ... in combinada com as funções range() e len()
# "len" conta a quantidade de elementos
# "range"  gera uma sequencia de 0 até o número passo à ele
for pos in range(len(frutas)):
    #print(frutas[pos], ":", pos)
    #print("a fruta ", frutas[pos], " está na posição ", pos,".")
#f-string - usada para escrever com interpolação de variáveis.
    print(f"A fruta {frutas[pos]} está na posição {pos}.")

#traço
print ("-"*40)

# Às vezes, é necessário percorrer a lista de trás para a frente, mas tendo 
# acesso também à posição dos elementos. Para isso, usamos a estrutura 
# for ... in, range() com três parâmetros e len()
#for i in range(len(lista) - 1 (vai buscar a posição do último elemento da lista), -1 ( se colocar até zero, o zero não aparece. então colocamos -1 que é menor que zero), -1 (passo, de quanto em quanto vai ser listado, tem que ser negativo para andar em decrescente):
for i in range(len(frutas) - 1, -1, -1):
    print(f"A fruta {frutas[i]} está na posição {i}.")

