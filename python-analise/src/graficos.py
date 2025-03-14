import matplotlib.pyplot as plt

def plotar_graficos(tamanhos_cache, resultados_fifo, resultados_lru, salvar=False, nome_arquivo="resultados.png"):
    """
    Plota gráficos comparando as métricas de desempenho dos algoritmos FIFO e LRU.

    Parâmetros:
    - tamanhos_cache (list): Lista de tamanhos de cache usados nos testes.
    - resultados_fifo (list): Lista de resultados médios do algoritmo FIFO para cada tamanho de cache.
    - resultados_lru (list): Lista de resultados médios do algoritmo LRU para cada tamanho de cache.
    - salvar (bool, opcional): Se True, salva o gráfico em um arquivo. Se False, exibe o gráfico na tela. Padrão é False.
    - nome_arquivo (str, opcional): Nome do arquivo para salvar o gráfico. Padrão é "resultados.png".

    Retorna:
    - None
    """
    metricas = ["Taxa de Acertos", "Taxa de Falhas", "Eficiência Relativa Sobre o Tamanho do Cache", "Frequência de Substituições", "Custo de Substituições", "Tempo Total de Execução"]
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))
    axs = axs.flatten()
    
    for i, metrica in enumerate(metricas):
        axs[i].plot(tamanhos_cache, [r[i] for r in resultados_fifo], linestyle='-', label='FIFO', color='blue')
        axs[i].plot(tamanhos_cache, [r[i] for r in resultados_lru], linestyle='-', label='LRU', color='red')

        axs[i].set_xlabel("Tamanho do Cache")
        axs[i].set_ylabel(metrica)
        axs[i].set_title(metrica)
        axs[i].legend()
        axs[i].grid()
    
    plt.tight_layout()
    
    if salvar:
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"Ação concluída com sucesso! Salvo como {nome_arquivo}")
    else:
        plt.show()

