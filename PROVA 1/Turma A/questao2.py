"""
    1) Identifique o algoritmo abaixo.
        Resposta ~> Algoritmo de busca binária

    2) Registre em comentário o propósito de cada uma das variáveis (de a a f).
        a ~> função busca_binaria
        b ~> a lista onde será feita a busca (lista)
        c ~> o valor a ser encontrado (val)
        d ~> posição inicial da lista (ini)
        e ~> posição final da lista (fim)
        f ~> meio calculado da lista (meio)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        Quando o valor de busca é encotrado, deve-se retornar o valor
        do meio. Portanto, a linha
            if c == b[f]: e = f
        deve ser corrigida para
            if c == b[f]: return f
            
"""    

def a(b, c):
    d = 0
    e = len(b) - 1
    while d <= e: 
        f = (d + e) // 2
        # if c == b[f]: e = f
        # CORREÇÃO
        if c == b[f]: return f
        elif c < b[f]: e = f - 1
        else: d = f + 1
    return -1