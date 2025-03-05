from collections import deque

class FIFO:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cache = deque()
        self.conjunto_cache = set()
        self.acertos = 0
        self.faltas = 0
        self.substituicoes = 0

    def acessar_pagina(self, pagina):
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

class LRU:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cache = []
        self.indices = {}
        self.acertos = 0
        self.faltas = 0
        self.substituicoes = 0

    def acessar_pagina(self, pagina):
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

