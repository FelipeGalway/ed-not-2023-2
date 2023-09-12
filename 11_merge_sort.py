def merge_sort(lista):
    """
    ALGORITMO DE OR DENAÇÃO MERGE SORT
    No processo de ordenação, esse algoritmo "desmonta" a lista original, 
    contendo N elementos, até obter N listas com apenas um elemento cada uma.
    Em seguida, usando a técnica de mesclagem (merging), "remonta" a lista, 
    desta vez com os elemento já em ordem.
    """
    
    # PARTE 1: DIVISÃO DA LISTA ORIGINAL EM LISTAS MENORES

    # Para que possa haver divisão da lista, esta deve ter mais de um elemento
    if len(lista)>1:
        # Encontra a posição do meio da lista para fazer a divisão em duas metades
        meio= len(lista)//2

        # Tira uma cópia da primeira metade da lista
        sublista_esq = lista[:meio]
        # Tira uma cópia da segunda metade da lista
        sublista_dir = lista[meio:]

        # Chamamos recursividade a própria função para que ela continue repartindo
        # cada sublista em duas parte menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

    # PARTE 2: REMONTAGEM DA LISTA ORDENADAMENTE
    pos_esq= pos_dir=0
    ordenada = []
    
    # Compara os elementos das sublistas entre di e insere na lista ordenada a menor 
    # entre


