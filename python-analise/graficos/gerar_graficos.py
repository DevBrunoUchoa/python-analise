from src.simulacao import executar_teste
from src.graficos import plotar_graficos
import os

def gerar_e_salvar_graficos():
    """
    Gera e salva gráficos comparando os algoritmos FIFO e LRU para diferentes tamanhos de cache.

    Esta função realiza os seguintes passos:
    1. Define os parâmetros para a simulação:
       - Número de páginas a serem geradas.
       - Intervalo de valores possíveis para as páginas.
       - Número de repetições para cada tamanho de cache.
       - Tamanhos de cache a serem testados.
    2. Executa os testes usando a função `executar_teste` para obter os resultados dos algoritmos FIFO e LRU.
    3. Cria uma pasta chamada "graficos" (se não existir) para armazenar os gráficos gerados.
    4. Salva o gráfico comparativo na pasta "graficos" com o nome "resultados.png".
    """
    quantidade_paginas = 10000  
    intervalo_paginas = 5000
    repeticoes = 10
    tamanhos_cache = list(range(1, 301))

    resultados_fifo, resultados_lru = executar_teste(tamanhos_cache, quantidade_paginas, intervalo_paginas, repeticoes)

    # Criar a pasta de gráficos se não existir
    os.makedirs("graficos", exist_ok=True)
    
    # Salvar o gráfico dentro da pasta "graficos"
    caminho_arquivo = "graficos/resultados.png"
    plotar_graficos(tamanhos_cache, resultados_fifo, resultados_lru, salvar=True, nome_arquivo=caminho_arquivo)

if __name__ == "__main__":
    gerar_e_salvar_graficos()
    print("Gráficos gerados com sucesso!") 
    print("Salvos em 'graficos/resultados.png'")
    
