# python-analise

# Comparação entre as Políticas de Cache LRU e FIFO

# Alunos:
João Bruno Tavares Uchoa - 123210302 (joao.bruno.tavares.uchoa@ccc.ufcg.edu.br)

João Vitor Moitinho Barbosa - 123210551 (joao.vitor.moitinho.barbosa@ccc.ufcg.edu.br)

Matheus Costa Chaves - 123210283 (matheus.costa.chaves@ccc.ufcg.edu.br)

Marcos Gabriel Zeferino da Silva - 123210793 (marcos.gabriel.zeferino.silva@ccc.ufcg.edu.br)

# Instituição:

Universidade Federal de Campina Grande (UFCG)
Centro de Engenharia Elétrica e Informática
Campina Grande - PB, 2025

# Resumo 
O trabalho busca como principal objetivo a comparação das duas políticas de cache,  sendo elas a FIFO (First in, First out) e a LRU (Least Recently Used), políticas que  são cruciais ao manejo de dados. Para a sua elaboração, haverá a necessidade de  realizar um simulador que irá permitir a observação do impacto de cada uma delas em  um sistema demonstrando a comparação gráfica das duas, permitindo a observação  dos momentos em que uma política aparentemente cria maior benefício em relação a  outra, bem como entendendo os seus os pontos fracos e fortes de cada política de  cache. Nele, serão analisados como critérios o custo computacional, o desempenho  e o uso de memória. 

# Objetivo do Trabalho

O foco principal é o estudo da eficiência das políticas de cache LRU e FIFO para o tratamento de dados em situações específicas. Ao procurar entender a quais situações é melhor preferir uma política ao invés da outra é importante para uma aplicação mais eficiente delas no contexto prático.

# Metodologia

  Implementação: Desenvolvimento de um simulador em Python para testar as políticas de cache.

  Testes: Geração de sequências de acesso à memória usando padrões como Zipf, aleatório uniforme e hotspot.

  Análise: Comparação gráfica das métricas de desempenho entre FIFO e LRU.

# Estrutura do Projeto

  main.py: Script principal para execução dos testes.

  algoritmos.py: Implementação das políticas de cache (FIFO e LRU).

  simulacao.py: Funções para gerar sequências de acesso (Zipf, aleatório, hotspot).

  graficos.py: Geração de gráficos comparativos.

  gerar_graficos.py: Define os padrões usados para a comparação e gera o arquivo resultados.png.

