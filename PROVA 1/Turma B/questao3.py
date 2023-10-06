"""
    1) Identifique o algoritmo abaixo.
        Resposta ~> algoritmo de busca sequencial.

    2) Registre em comentário o propósito de cada uma das variáveis (de a a d).
        a ~> função busca_sequencial
        b ~> a lista a ser pesquisada (lista)
        c ~> o valor a ser encontrado (val)
        d ~> posição do elemento na lista (pos)

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        A variável d representa a posição e é ela quem deve ser retornada
        quando o elemento é encontrado. Portanto, a linha
            if c == b[d]: return c
        deve ser corrigida para
            if c == b[d]: return d
"""    

def a(b, c):
    for d in range(len(b)):
        # if c == b[d]: return c
        # CORREÇÃO
        if c == b[d]: return d
    return -1