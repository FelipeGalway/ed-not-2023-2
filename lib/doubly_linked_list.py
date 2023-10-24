class DoublyLinkedList:
    """
        ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
        Trata-se de uma lista linear, em que seus elementos (camadas nodos ou nós) 
        não estão fisicamente adjacentes uns dos outros, mas ligados logicamente por
        ponteiros que inicia, o nodo anterior e o nodo seguinte da sequência.
        Não possui restrição de acesso - inseções, exclusões e consultas podem ser
        executadas em qualquer posição da lista.
    """

    class Node:
        """
            Classe interna que representa a unidade de informação (nodo) armazenada
            pela lista duplamente encadeada.
        """
        def __init__(self, data):
            """ Construtor da classe interna Node """
            self.prev = None    # Ponteiro para o nodo anterior
            self.data = data    # Dado útil para o usuário
            self.next = None    # Ponteiro para o nodo seguintes

    def __init__(self):
        """
            Construtor da classe principal DoublyLinkedList
        """
        self.__head = None    # Ponteiro para o primeiro nodo
        self.__tail = None    # Ponteiro para o último nodo
        self.__count = 0    # Quantidade de nodos da lista
    
    def get_count(self):
        """
            Método que retorna a quantidade de nodos da lista
        """
        return self.__count

    def insert(self, pos, val):
        """
            Método que insere na posição "pos" o valor "val"
        """
        # Criamos um nodo para armazenar "val" e também os ponteiros "prev" e "next",
        # ambos apontando inicialmente para None
        new = self.Node(val)

        # 1º caso: a lista está vazia, e "new" será, ao mesmo tempo, o primeiro e o último nodo
        if self.get_count() == 0:   #Lista vazia
            self.__head = new
            self.__tail = new

        # 2º caso: iserção do início da lista (posição 0)
        elif pos == 0:  #FOTO 1-2 dia 23/10/2023
            new.next = self.__head
            self.__head.prev = new
            self.__head = new
        
        #3º caso: insersão no final da lista
        #Obs.: consideramos como posição final qualquer uma que seja >= self.get_count()
        elif pos >= self.get_count(): #FOTO 3-4 dia 23/10/2023
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new

        # 4º caso: 

        # Incrementa a contagem de nodos da lista
        self.__count += 1



