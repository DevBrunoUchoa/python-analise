from src.simulacao import executar_teste
from src.graficos import plotar_graficos
import os

def gerar_e_salvar_graficos():
    quantidade_paginas = 10000
    intervalo_paginas = 5000 #100, 750 e 5000
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
    
