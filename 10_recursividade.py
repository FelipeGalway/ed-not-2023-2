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

##########################################################################
print(f"Fatorial de 6: "{fatorial_inter(6)})
