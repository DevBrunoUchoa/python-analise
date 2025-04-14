import matplotlib.pyplot as plt

def plotar_graficos(tamanhos_cache, resultados_fifo, resultados_lru, salvar=False, nome_arquivo="graficos/resultados.png"):
    metricas = [
        "Taxa de Acertos", "Taxa de Falhas", "Eficiência Relativa Sobre o Tamanho do Cache",
        "Frequência de Substituições", "Custo de Substituições", "Tempo Total de Execução"
    ]
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))
    axs = axs.flatten()

    for i, metrica in enumerate(metricas):
        axs[i].plot(tamanhos_cache, [r[i] for r in resultados_fifo], label='FIFO', color='blue')
        axs[i].plot(tamanhos_cache, [r[i] for r in resultados_lru], label='LRU', color='red')

        axs[i].set_title(metrica)
        axs[i].set_xlabel("Tamanho do Cache")
        axs[i].set_ylabel(metrica)
        axs[i].legend()
        axs[i].grid()

    plt.tight_layout()
    if salvar:
        plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
        print(f"Salvo em {nome_arquivo}")
    else:
        plt.show()

