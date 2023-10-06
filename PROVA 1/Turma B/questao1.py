"""
    1) Identifique o algoritmo abaixo.
        Resposta ~> Algorimo de ordenação Merge Sort.

    2) Registre em comentário o propósito de cada uma das variáveis (de a a i).
        a ~> função merge_sort
        b ~> a lista ser ordenada (lista)
        c ~> meio calculado da lista (meio)
        d ~> sublista da esquerda (sublista_esq)
        e ~> sublista da direita (sublista_dir)
        f ~> posição da sublista da esquerda (pos_esq)
        g ~> posição da sublista da direita (pos_dir)
        h ~> lista ordenada (ordenada)
        i ~> lista de sobras (sobra)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        A variável h representa a lista ordenada, e i a lista de sobras.
        portanto, as linhas
            i.append(d[f])
            i.append(e[g])
        devem ser substituídas por:
            h.append(d[f])
            h.append(e[g])
"""

def a(b):
    if len(b) <= 1: return b
    c = len(b) // 2
    d = b[:c]
    e = b[c:]
    d = a(d)
    e = a(e)
    f = g = 0
    h = []
    i = []
    while f < len(d) and g < len(e):
        if d[f] < e[g]:
            # i.append(d[f])
            # CORREÇÃO
            h.append(d[f])
            f += 1
        else:
            # i.append(e[g])
            # CORREÇÃO
            h.append(e[g])
            g += 1
    if(f < g): i = d[f:]
    else: i = e[g:]
    return h + i