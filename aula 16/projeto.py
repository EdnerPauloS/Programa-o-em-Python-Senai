import tkinter as tk
from tkinter import ttk

class CRUDApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CRUD App")
        self.geometry("400x300")
        self.configure(bg="black")

        # Criar lista para armazenar os dados
        self.dados = []

        # Criar entrada para adicionar novos dados
        self.entrada_dado = tk.Entry(self, bg="white", fg="black")
        self.entrada_dado.pack(pady=10)

        # Botões CRUD
        self.frame_botoes = ttk.Frame(self, padding=(10, 0))
        self.frame_botoes.pack()

        self.botao_adicionar = ttk.Button(self.frame_botoes, text="Adicionar", command=self.adicionar_dado)
        self.botao_adicionar.grid(row=0, column=0, padx=5)

        self.botao_atualizar = ttk.Button(self.frame_botoes, text="Atualizar", command=self.atualizar_dado)
        self.botao_atualizar.grid(row=0, column=1, padx=5)

#criar botão deletar

        # Listar os dados
        self.lista_dados = tk.Listbox(self, bg="white", fg="black")
        self.lista_dados.pack(expand=True, fill="both", padx=10, pady=5)

    def adicionar_dado(self):
        dado = self.entrada_dado.get()
        if dado:
            self.dados.append(dado)
            self.lista_dados.insert(tk.END, dado)
            self.entrada_dado.delete(0, tk.END)

    def atualizar_dado(self):
        selecionado = self.lista_dados.curselection()
        if selecionado:
            novo_dado = self.entrada_dado.get()
            indice = selecionado[0]
            self.dados[indice] = novo_dado
            self.lista_dados.delete(indice)
            self.lista_dados.insert(indice, novo_dado)
            self.entrada_dado.delete(0, tk.END)

#criar função deletar

# Instanciar e executar a aplicação
app = CRUDApp()
app.mainloop()
