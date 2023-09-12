"""
    RECURSIVIDADE

    Trata-se de uma técnica de programação pela qual um função
    chama a si mesma, em uma condição diferente da inicial, O
    principal objetivo do uso da recursividade é diminuir a 
    complexidade de algoritmos.
"""

def fatorial_inter(num):
    """
    Calcula o fatorial de um número, usando um algoritmo
    ITERATIVO (não recursivo)
    """
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")
    resposta=1
    for n in range(num, 0, -1): resposta *= n
    return resposta

def fatorial_rec(num):
    """
    Cálculo do fatorial, usando um algoritmo RECURSIVO
    """
    #Não é possível valcular o fatorial de um número negativo]
    if num<0:
        raise Exception("ERRO: número negativo, cálculo impossível")

    if num<=1: return 1         #o fatoral de 0 e 1 é igual a 1
    else: return num*fatorial_rec(num-1) #chama recursiva à função


##########################################################################
print(f"Fatorial de 6 (interativo): {fatorial_inter(6)}")
print(f"Fatorial de 6 (recursivo): {fatorial_rec(6)}")



