from src.simulacao import executar_teste
from src.graficos import plotar_graficos
from tkinter import ttk, messagebox

import tkinter as tk

import os
import webbrowser

class AppSimulador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Substituição de Páginas")
        self.geometry("600x500")
        self.configure(bg="#f5f5f5")

        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')
        self.estilo.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
        self.estilo.configure("TLabel", background="#f5f5f5", font=("Arial", 11))
        self.estilo.configure("TEntry", font=("Arial", 11))
        self.estilo.configure("TCombobox", font=("Arial", 11))

        self.tipo_sequencia = tk.StringVar(value="Zipf")
        self.quantidade = tk.IntVar(value=10000)
        self.intervalo = tk.IntVar(value=5000)
        self.repeticoes = tk.IntVar(value=10)
        self.tamanho_max_cache = tk.IntVar(value=301)
        self.fator_zipf = tk.DoubleVar(value=1.2)
        self.fracao_hot = tk.DoubleVar(value=0.4)
        self.prob_hot = tk.DoubleVar(value=0.6)

        self._construir_interface()

    def _construir_interface(self):
        ttk.Label(self, text="Tipo de Sequência:").pack(pady=(10, 0))
        ttk.Combobox(self, textvariable=self.tipo_sequencia, values=["Uniforme", "Zipf", "Hotspot"]).pack()

        self._adicionar_entrada("Quantidade de Páginas:", self.quantidade)
        self._adicionar_entrada("Intervalo de Páginas:", self.intervalo)
        self._adicionar_entrada("Repetições:", self.repeticoes)
        self._adicionar_entrada("Tamanho Máximo do Cache:", self.tamanho_max_cache)

        self.zipf_frame = ttk.LabelFrame(self, text="Parâmetros Zipf", padding=10)
        self._adicionar_entrada("Fator Zipf:", self.fator_zipf, master=self.zipf_frame)

        self.hotspot_frame = ttk.LabelFrame(self, text="Parâmetros Hotspot", padding=10)
        self._adicionar_entrada("Fração Hot:", self.fracao_hot, master=self.hotspot_frame)
        self._adicionar_entrada("Probabilidade Hot:", self.prob_hot, master=self.hotspot_frame)

        self.zipf_frame.pack(pady=5, fill="x", padx=10)
        self.hotspot_frame.pack(pady=5, fill="x", padx=10)

        ttk.Button(self, text="Executar Simulação", command=self.executar).pack(pady=15)

    def _adicionar_entrada(self, texto, var, master=None):
        if master is None:
            master = self
        frame = ttk.Frame(master)
        frame.pack(pady=5, fill="x", padx=10)
        ttk.Label(frame, text=texto).pack(side="left")
        ttk.Entry(frame, textvariable=var, width=10).pack(side="right")

    def executar(self):
        tipo = self.tipo_sequencia.get().lower()
        qtd = self.quantidade.get()
        intervalo = self.intervalo.get()
        repeticoes = self.repeticoes.get()
        max_cache = self.tamanho_max_cache.get()
        tamanhos_cache = list(range(1, max_cache + 1))

        try:
            kwargs = {}
            if tipo == "zipf":
                kwargs["fator_zipf"] = self.fator_zipf.get()
            elif tipo == "hotspot":
                kwargs["fracao_hot"] = self.fracao_hot.get()
                kwargs["prob_hot"] = self.prob_hot.get()

            resultados_fifo, resultados_lru = executar_teste(
                tamanhos_cache, qtd, intervalo, repeticoes, tipo, **kwargs
            )

            os.makedirs("graficos", exist_ok=True)
            caminho_arquivo = os.path.abspath("graficos/resultados.png")
            plotar_graficos(tamanhos_cache, resultados_fifo, resultados_lru, salvar=True, nome_arquivo=caminho_arquivo)

            webbrowser.open(caminho_arquivo)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    app = AppSimulador()
    app.mainloop()

