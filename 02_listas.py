# LISTAS
# Listas são uma forma de amrmazenar mais de um valor em uma única variável. Os valores podem
# ser de tipos diferentes

# Uma lista de numeros
valores = [2, 3, 5, 7, 9, 11]

# Uma lista com valores de tipos variáveis
mix = ["batata", 1.25, True, "tomate", 44]

# Lista de strings
legumes = ["batata", "tomate", "abobrinha", "cenoura"]

# OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO: significa percorrer a lista do primeiro ao último elemento, fazendo 
#              algo com cada um deles

#Imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)

print("-" * 40) #vai aparecer 40 ítens que estão dentro das "", ou seja, 40 hífens ----- etc

for x in valores: #vai multiplicar cada valor da lista valores por 2 e aparcer na dela 
    print(x * 2)

print("-" * 40)

# 2) INSERINDO NOVOS ELEMENTOS NO *FIM* DA LISTA (MÉTODO)

valores.append(13)
legumes.append("cebola")

print(valores)
print(legumes)

print("-" * 40)

# 3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECIFICADA (MÉTODO)
# Parâmetros:
# 1º: a posição onde será inserido o novo elemento
# 2º: o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "beterraba")
print(legumes)

print("-" * 40)

# 4) ACESSANDO UM VALOR EM UMA POSICAO ESPECIFICADA
print("Elemento na QUARTA posição: ", valores[3])
print("Elemento na PRIMEIRA posição: ", valores[0])
print("Elemento na ÚLTIMA posição: ", valores[-1])
print("Elemento na PENÚLTIMA posição: ", valores[-2])
