from collections import deque
from collections import OrderedDict

class FIFO:
    """
    Implementa o algoritmo de substituição de páginas FIFO (First-In, First-Out).

    Atributos:
    - tamanho (int): Tamanho máximo da cache.
    - cache (deque): Estrutura de dados que armazena as páginas na cache.
    - conjunto_cache (set): Conjunto para verificação rápida de páginas na cache.
    - acertos (int): Contador de acertos na cache.
    - faltas (int): Contador de faltas na cache.
    - substituicoes (int): Contador de substituições de páginas na cache.

    Métodos:
    - acessar_pagina(pagina): Simula o acesso a uma página na cache.
    """
    def __init__(self, tamanho):
        """
        Inicializa a cache FIFO.

        Parâmetros:
        - tamanho (int): Tamanho máximo da cache.
        """
        self.tamanho = tamanho
        self.cache = deque()
        self.conjunto_cache = set()
        self.acertos = 0
        self.faltas = 0
        self.substituicoes = 0

    def acessar_pagina(self, pagina):
        """
        Simula o acesso a uma página na cache FIFO.

        Parâmetros:
        - pagina (int): Página a ser acessada.

        Comportamento:
        - Se a página já está na cache, incrementa o contador de acertos.
        - Se a página não está na cache:
            - Se a cache estiver cheia, remove a página mais antiga (FIFO).
            - Adiciona a nova página à cache e incrementa o contador de faltas.
            - Se houve remoção, incrementa o contador de substituições.
        """
        if pagina in self.conjunto_cache:
            self.acertos += 1
        else:
            self.faltas += 1
            if len(self.cache) >= self.tamanho:
                removida = self.cache.popleft()
                self.conjunto_cache.remove(removida)
                self.substituicoes += 1
            self.cache.append(pagina)
            self.conjunto_cache.add(pagina)
'''           
class LRU:
    """
    Implementa o algoritmo de substituição de páginas LRU (Least Recently Used).

    Atributos:
    - tamanho (int): Tamanho máximo da cache.
    - cache (list): Lista que armazena as páginas na cache.
    - indices (dict): Dicionário para verificação rápida de páginas na cache.
    - acertos (int): Contador de acertos na cache.
    - faltas (int): Contador de faltas na cache.
    - substituicoes (int): Contador de substituições de páginas na cache.

    Métodos:
    - acessar_pagina(pagina): Simula o acesso a uma página na cache LRU.
    """
    def __init__(self, tamanho):
        """
        Inicializa a cache LRU.

        Parâmetros:
        - tamanho (int): Tamanho máximo da cache.
        """
        self.tamanho = tamanho
        self.cache = []
        self.indices = {}
        self.acertos = 0
        self.faltas = 0
        self.substituicoes = 0

    def acessar_pagina(self, pagina):
        """
        Simula o acesso a uma página na cache LRU.

        Parâmetros:
        - pagina (int): Página a ser acessada.

        Comportamento:
        - Se a página já está na cache, incrementa o contador de acertos e move a página para o final da lista (recente).
        - Se a página não está na cache:
            - Se a cache estiver cheia, remove a página menos recentemente usada (primeira da lista).
            - Adiciona a nova página ao final da lista e incrementa o contador de faltas.
            - Se houve remoção, incrementa o contador de substituições.
        """
        if pagina in self.indices:
            self.acertos += 1
            self.cache.remove(pagina)
        else:
            self.faltas += 1
            if len(self.cache) >= self.tamanho:
                removida = self.cache.pop(0)
                del self.indices[removida]
                self.substituicoes += 1
        self.cache.append(pagina)
        self.indices[pagina] = True
        
'''        
class LRU:
     """
    Implementa o algoritmo de substituição de páginas LRU (Least Recently Used) usando `OrderedDict`.

    Atributos:
    - tamanho (int): Tamanho máximo da cache.
    - cache (OrderedDict): Estrutura de dados que armazena as páginas na cache e mantém a ordem de uso.
    - acertos (int): Contador de acertos na cache.
    - faltas (int): Contador de faltas na cache.
    - substituicoes (int): Contador de substituições de páginas na cache.

    Métodos:
    - acessar_pagina(pagina): Simula o acesso a uma página na cache LRU.
    """
    def __init__(self, tamanho):
        """
        Inicializa a cache LRU.

        Parâmetros:
        - tamanho (int): Tamanho máximo da cache.
        """
        self.tamanho = tamanho
        self.cache = OrderedDict()
        self.acertos = 0
        self.faltas = 0
        self.substituicoes = 0

    def acessar_pagina(self, pagina):
        """
        Simula o acesso a uma página na cache LRU.

        Parâmetros:
        - pagina (int): Página a ser acessada.

        Comportamento:
        - Se a página já está na cache, incrementa o contador de acertos e move a página para o final (recente).
        - Se a página não está na cache:
            - Se a cache estiver cheia, remove a página menos recentemente usada (primeira da `OrderedDict`).
            - Adiciona a nova página ao final e incrementa o contador de faltas.
            - Se houve remoção, incrementa o contador de substituições.
        """
        if pagina in self.cache:
            self.acertos += 1
            self.cache.move_to_end(pagina)  # Move para o final (recente)
        else:
            self.faltas += 1
            if len(self.cache) >= self.tamanho:
                self.cache.popitem(last=False)  # Remove o mais antigo (primeiro)
                self.substituicoes += 1
            self.cache[pagina] = True  # Adiciona no final
