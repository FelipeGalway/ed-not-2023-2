"""
    1) Identifique o algoritmo abaixo.
        Resposta ~> Algoritmo de ordenação Selection Sort

    2) Registre em comentário o propósito de cada uma das variáveis (de m a q).
        m ~> função selection_sort
        n ~> lista a ser ordenada (lista)
        o ~> posição do elemento selecionado (pos_sel)
        p ~> posição do menor elemento (pos_menor)
        q ~> posição da lista no for interno (pos)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        A variável o representa o elemento selecionado e a variável p
        repesenta a posição do menor elemento. Portanto, a linha
            if n[q] < n[o]:
        deve ser corrigida para
            if n[q] < n[p]:

""" 

def m(n):
    for o in range(len(n) - 1):
        p = o + 1
        for q in range(o + 2, len(n)):
            # if n[q] < n[o]:
            # CORREÇÃO
            if n[q] < n[p]:
                p = q
        if n[p] < n[o]:
            n[o], n[p] = n[p], n[o]