import random
import time
import numpy as np
from src.algoritmos import FIFO, LRU
'''
## Uniformente aléatória ##
def gerar_sequencia(quantidade, intervalo):
   """
    Gera uma sequência de números inteiros uniformemente aleatórios.

    Parâmetros:
    - quantidade (int): Número de elementos na sequência.
    - intervalo (int): Intervalo de valores possíveis (de 1 a `intervalo`).

    Retorna:
    - list: Uma lista de inteiros gerados aleatoriamente.
    """
    return [random.randint(1, intervalo) for _ in range(quantidade)]
'''

## Padrão Zipf ##
def gerar_sequencia(quantidade, intervalo, fator=1.2):
    """
    Gera uma sequência de números inteiros seguindo a distribuição de Zipf.

    Parâmetros:
    - quantidade (int): Número de elementos na sequência.
    - intervalo (int): Intervalo de valores possíveis (de 1 a `intervalo`).
    - fator (float, opcional): Fator de forma da distribuição de Zipf. Padrão é 1.2.

    Retorna:
    - list: Uma lista de inteiros gerados aleatoriamente seguindo a distribuição de Zipf.
    """
    return list(np.random.zipf(fator, quantidade) % intervalo + 1)

'''
## Sequencial com repetição ##
def gerar_sequencia(quantidade, intervalo):
    """
    Gera uma sequência de números inteiros uniformemente aleatórios com possíveis repetições.

    Parâmetros:
    - quantidade (int): Número de elementos na sequência.
    - intervalo (int): Intervalo de valores possíveis (de 1 a `intervalo`).

    Retorna:
    - list: Uma lista de inteiros gerados aleatoriamente.
    """
    return [random.randint(1, intervalo) for _ in range(quantidade)]
'''
'''
## Padrão Hotspot
def gerar_sequencia(quantidade, intervalo, fracao_hot=0.4, prob_hot=0.6):
    """
    Gera uma sequência de números inteiros seguindo o padrão Hotspot.

    Parâmetros:
    - quantidade (int): Número de elementos na sequência.
    - intervalo (int): Intervalo de valores possíveis (de 1 a `intervalo`).
    - fracao_hot (float, opcional): Fração de páginas consideradas "hot". Padrão é 0.4.
    - prob_hot (float, opcional): Probabilidade de acessar uma página "hot". Padrão é 0.6.

    Retorna:
    - list: Uma lista de inteiros gerados seguindo o padrão Hotspot.
    """
    num_hot = max(1, int(intervalo * fracao_hot))
    hot_pages = list(range(1, num_hot + 1))
    cold_pages = list(range(num_hot + 1, intervalo + 1))
    
    sequencia = []
    for _ in range(quantidade):
        if random.random() < prob_hot:
            sequencia.append(random.choice(hot_pages))
        else:
            sequencia.append(random.choice(cold_pages) if cold_pages else random.choice(hot_pages))
    return sequencia
'''    
def simular_acessos(algoritmo, paginas, tamanho_cache):
    """
    Simula o acesso a páginas de memória usando um algoritmo de substituição de páginas.

    Parâmetros:
    - algoritmo (class): Classe que implementa o algoritmo de substituição de páginas (ex: FIFO, LRU).
    - paginas (list): Lista de páginas a serem acessadas.
    - tamanho_cache (int): Tamanho da cache.

    Retorna:
    - tuple: Uma tupla contendo:
        - taxa_acertos (float): Taxa de acertos na cache.
        - taxa_faltas (float): Taxa de faltas na cache.
        - eficiencia_relativa (float): Eficiência relativa da cache.
        - freq_substituicoes (float): Frequência de substituições na cache.
        - custo_substituicao (float): Custo de substituição na cache.
        - tempo_execucao (float): Tempo total de execução da simulação.
    """
    estrutura = algoritmo(tamanho_cache)
    inicio = time.perf_counter()
    for pagina in paginas:
        estrutura.acessar_pagina(pagina)
    tempo_execucao = time.perf_counter() - inicio
    
    taxa_acertos = estrutura.acertos / len(paginas)
    taxa_faltas = estrutura.faltas / len(paginas)
    eficiencia_relativa = taxa_acertos / tamanho_cache if tamanho_cache > 0 else 0
    freq_substituicoes = estrutura.substituicoes / estrutura.faltas if estrutura.faltas > 0 else 0
    custo_substituicao = estrutura.substituicoes * (tempo_execucao / len(paginas))
    
    return taxa_acertos, taxa_faltas, eficiencia_relativa, freq_substituicoes, custo_substituicao, tempo_execucao

def executar_teste(tamanhos_cache, quantidade_paginas, intervalo_paginas, repeticoes=5):
    """
    Executa testes de simulação de acesso a páginas para diferentes tamanhos de cache.

    Parâmetros:
    - tamanhos_cache (list): Lista de tamanhos de cache a serem testados.
    - quantidade_paginas (int): Número de páginas a serem geradas e acessadas.
    - intervalo_paginas (int): Intervalo de valores possíveis para as páginas.
    - repeticoes (int, opcional): Número de repetições para cada tamanho de cache. Padrão é 5.

    Retorna:
    - tuple: Uma tupla contendo duas listas:
        - resultados_fifo (list): Resultados médios para o algoritmo FIFO.
        - resultados_lru (list): Resultados médios para o algoritmo LRU.
    """
    resultados_fifo = []
    resultados_lru = []
    
    for tamanho in tamanhos_cache:
        resultados_fifo_tempo = []
        resultados_lru_tempo = []
        
        for _ in range(repeticoes):
            sequencia_paginas = gerar_sequencia(quantidade_paginas, intervalo_paginas)
            resultados_fifo_tempo.append(simular_acessos(FIFO, sequencia_paginas, tamanho))
            resultados_lru_tempo.append(simular_acessos(LRU, sequencia_paginas, tamanho))
        
        media_fifo = [sum(x) / repeticoes for x in zip(*resultados_fifo_tempo)]
        media_lru = [sum(x) / repeticoes for x in zip(*resultados_lru_tempo)]
        
        resultados_fifo.append(media_fifo)
        resultados_lru.append(media_lru)
    
    return resultados_fifo, resultados_lru

