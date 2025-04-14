import random
import numpy as np

def gerar_uniforme(quantidade, intervalo):
    return [random.randint(1, intervalo) for _ in range(quantidade)]

def gerar_zipf(quantidade, intervalo, fator=1.2):
    return list(np.random.zipf(fator, quantidade) % intervalo + 1)

def gerar_hotspot(quantidade, intervalo, fracao_hot=0.4, prob_hot=0.6):
    num_hot = max(1, int(intervalo * fracao_hot))
    hot_pages = list(range(1, num_hot + 1))
    cold_pages = list(range(num_hot + 1, intervalo + 1))

    sequencia = []
    for _ in range(quantidade):
        if random.random() < prob_hot and hot_pages:
            sequencia.append(random.choice(hot_pages))
        elif cold_pages:
            sequencia.append(random.choice(cold_pages))
        else:
            sequencia.append(random.choice(hot_pages))
    return sequencia

