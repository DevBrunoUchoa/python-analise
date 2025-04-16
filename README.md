# Simulador de Políticas de Cache (FIFO e LRU)

## Instituição  
Universidade Federal de Campina Grande (UFCG)  
Centro de Engenharia Elétrica e Informática (CEEI) 
Campina Grande - PB, 2025  

---

## Membros

João Bruno Tavares Uchoa - 123210302 (joao.bruno.tavares.uchoa@ccc.ufcg.edu.br)

João Vitor Moitinho Barbosa - 123210551 (joao.vitor.moitinho.barbosa@ccc.ufcg.edu.br)

Matheus Costa Chaves - 123210283 (matheus.costa.chaves@ccc.ufcg.edu.br)

Marcos Gabriel Zeferino da Silva - 123210793 (marcos.gabriel.zeferino.silva@ccc.ufcg.edu.br)

---

## Resumo  
O trabalho busca como principal objetivo a comparação das duas políticas de cache, sendo elas a FIFO (First in, First out) e a LRU (Least Recently Used), políticas que são cruciais ao manejo de dados. Para a sua elaboração, haverá a necessidade de realizar um simulador que irá permitir a observação do impacto de cada uma delas em um sistema demonstrando a comparação gráfica das duas, permitindo a observação dos momentos em que uma política aparentemente cria maior benefício em relação a outra, bem como entendendo os seus os pontos fracos e fortes de cada política de cache. Nele, serão analisados como critérios o custo computacional, o desempenho e o uso de memória.

---

## Objetivo do Trabalho  
O foco principal é o estudo da eficiência das políticas de cache LRU e FIFO para o tratamento de dados em situações específicas. Ao procurar entender a quais situações é melhor preferir uma política ao invés da outra é importante para uma aplicação mais eficiente delas no contexto prático.

---

## Metodologia

1. **Implementação**  
   - Desenvolvimento de um simulador em Python que incorpora as políticas de cache FIFO e LRU.

2. **Testes**  
   - **Sequência de Acesso:** Geração de sequências para testar os acessos à memória:
     - **Uniforme:** Probabilidade igual para todas as páginas.
     - **Zipt:** Define um fator que controla a frequência dos acessos.
     - **Hotspot:** Grupo de páginas com maior frequência de acesso.

3. **Análise**  
   - Comparação dos resultados dos testes considerando:
     - Taxa de acertos e falhas do cache;
     - Eficiência sobre o tamanho do cache;
     - Frequência de substituições;
     - Custo de substituições;
     - Tempo de execução.
   - Visualização gráfica dos dados para identificar os pontos fortes e limitações de cada política.

---

## Estrutura do Projeto

```plaintext
.
├── interface.py                          # Script principal para execução dos testes
├── graficos/
│   └── resultados.png		         # Arquivo de imagem gerado com os gráficos de comparação dos algoritmos
└── src/
    ├── algoritmos.py                     # Implementa os algoritmos de substituição de páginas (LRU e FIFO)
    ├── geradores.py                      # Gera sequências de acesso
    ├── graficos.py                       # Realiza a criação dos gráficos
    └── simulacao.py                      # Executa os testes de substituição de página, coleta métricas e organiza os resultados

```

---

## Guia de Uso


### 1. Executando via Terminal

Para usuários que preferem a linha de comando, siga os passos abaixo:

1. **Clone ou baixe** este repositório:
```bash
git clone https://github.com/DevBrunoUchoa/python-analise
cd python-analise/python-analise
```

2. **Instale as dependências**:
```bash
pip install matplotlib numpy
```

3. **Execute o script principal**:
```bash
python interface.py
```

---

### 2. Executando Interface Gráfica

- **Tipo de Sequência de Acesso**  
  Escolha o padrão para a geração dos acessos à memória:
  - `Uniforme`: Probabilidade igual para todas as páginas.
  - `Zipf`: Define um fator que controla a frequência dos acessos.
  - `Hotspot`: Grupo de páginas com maior frequência de acesso.

- **Quantidade de Páginas**  
  Define o número total de páginas geradas na simulação.

- **Intervalo de Páginas**  
  Determina o intervalo dos identificadores de página.

- **Repetições**  
  Número de vezes que a simulação será repetida para cada configuração.

- **Tamanho Máximo do Cache**  
  Define o limite máximo de páginas que o cache pode armazenar.

- **Fator Zipf** *(aparece apenas quando a sequência Zipf é selecionada)*  
  Controla a concentração de acessos a páginas mais populares.

- **Parâmetros Hotspot** *(aparecem apenas quando a sequência Hotspot é selecionada)*  
  - **Fração Hot**: Percentual de páginas consideradas “hot”.
  - **Probabilidade Hot**: Probabilidade de que o acesso seja direcionado a essas páginas.

Após configurar os parâmetros desejados, clique no botão **"Executar Simulação"**.

Os resultados serão exibidos no navegador padrão e salvos automaticamente no arquivo `resultados.png`.

---
