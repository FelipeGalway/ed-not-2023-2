"""
    1) Identifique o algoritmo abaixo.
        Resposta ~> Algoritmo de ordenação Bubble Sort

    2) Registre em comentário o propósito de cada uma das variáveis (de a a d).
        a ~> função bubble_sort
        b ~> lista a ser ordenada (lista)
        c ~> indicador de trocas (trocou)
        d ~> posição de percurso da lista (pos)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        Na linha
            b[d + 1], b[c] = b[c], b[d + 1]
        a vaiável d não representa a posição da lista, e sim o indicador
        de trocas. A linha corrigida é 
            b[d + 1], b[d] = b[d], b[d + 1]
"""

def a(b):
    while True:
        c = False
        for d in range(len(b) - 1):
            if b[d + 1] < b[d]:
                # b[d + 1], b[c] = b[c], b[d + 1]
                # Correção
                b[d + 1], b[d] = b[d], b[d + 1]
                c = True
        if not c:
            break