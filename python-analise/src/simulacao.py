import time
from src.algoritmos import FIFO, LRU
from src import geradores

def simular_acessos(algoritmo, paginas, tamanho_cache):
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

def executar_teste(tamanhos_cache, quantidade_paginas, intervalo_paginas, repeticoes=5, tipo_sequencia="uniforme", **kwargs):
    if tipo_sequencia == "zipf":
        gerar_sequencia = lambda q, i: geradores.gerar_zipf(q, i, kwargs.get("fator_zipf", 1.2))
    elif tipo_sequencia == "hotspot":
        gerar_sequencia = lambda q, i: geradores.gerar_hotspot(
            q, i,
            fracao_hot=kwargs.get("fracao_hot", 0.4),
            prob_hot=kwargs.get("prob_hot", 0.6)
        )
    else:
        gerar_sequencia = geradores.gerar_uniforme

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

