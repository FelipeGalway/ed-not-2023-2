"""
    1) Identifique o algoritmo abaixo.
        Resposta ~> Algoritmo de ordenação Selection Sort

    2) Registre em comentário o propósito de cada uma das variáveis (de v a z).
        z ~> função selection_sort
        y ~> a lista a ser ordenada (lista)
        x ~> a posição de percurso na lista (pos_sel)
        w ~> a posição do menor elemento (pos_menor)
        v ~> a posição da lista no for interno (pos)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    A linha 
        if y[v] < y[x]:
    deve ser corrigida para
        if y[v] < y[w]:
    porque é a variável w que representa a posição do menor elemento.
"""

def z(y):
    for x in range(len(y) - 1):
        w = x + 1
        for v in range(x + 2, len(y)):
            # if y[v] < y[x]: # if lista[pos] < lista[pos_sel]
            # CORREÇÃO:
            if y[v] < y[w]:
                w = v
        if y[w] < y[x]:
            y[x], y[w] = y[w], y[x]