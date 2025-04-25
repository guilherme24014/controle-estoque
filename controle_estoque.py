import tkinter as tk
from tkinter import messagebox

class ControleEstoque:
    def __init__(self, root):
        self.estoque = []

        root.title("Controle de Estoque")
        root.geometry("500x600")

        # Campos de entrada
        tk.Label(root, text="Nome do item:").pack()
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        tk.Label(root, text="Código:").pack()
        self.codigo_entry = tk.Entry(root)
        self.codigo_entry.pack()

        tk.Label(root, text="Quantidade:").pack()
        self.qtd_entry = tk.Entry(root)
        self.qtd_entry.pack()

        tk.Label(root, text="Categoria:").pack()
        self.categoria_entry = tk.Entry(root)
        self.categoria_entry.pack()

        tk.Button(root, text="Adicionar Item", command=self.adicionar_item).pack(pady=5)

        # Busca
        tk.Label(root, text="Buscar por nome ou código:").pack()
        self.busca_entry = tk.Entry(root)
        self.busca_entry.pack()
        tk.Button(root, text="Buscar", command=self.buscar_item).pack(pady=5)

        # Exibição do estoque
        self.resultado_texto = tk.Text(root, height=20, width=60)
        self.resultado_texto.pack(pady=10)

        tk.Button(root, text="Limpar Estoque", command=self.limpar_estoque).pack()

    def adicionar_item(self):
        nome = self.nome_entry.get()
        codigo = self.codigo_entry.get()
        qtd = self.qtd_entry.get()
        categoria = self.categoria_entry.get()

        if nome and codigo and qtd:
            try:
                qtd = int(qtd)
                self.estoque.append((nome, codigo, qtd, categoria))
                self.atualizar_resultado()
                self.nome_entry.delete(0, tk.END)
                self.codigo_entry.delete(0, tk.END)
                self.qtd_entry.delete(0, tk.END)
                self.categoria_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Erro", "Quantidade deve ser um número inteiro")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios")

    def buscar_item(self):
        termo = self.busca_entry.get().lower()
        resultados = [
            item for item in self.estoque
            if termo in item[0].lower() or termo in item[1].lower()
        ]

        self.resultado_texto.delete("1.0", tk.END)
        if resultados:
            for nome, codigo, qtd, cat in resultados:
                self.resultado_texto.insert(tk.END, f"{nome} | Código: {codigo} | Qtd: {qtd} | Categoria: {cat}\n")
        else:
            self.resultado_texto.insert(tk.END, "Nenhum item encontrado.\n")

    def atualizar_resultado(self):
        self.resultado_texto.delete("1.0", tk.END)
        for nome, codigo, qtd, cat in self.estoque:
            self.resultado_texto.insert(tk.END, f"{nome} | Código: {codigo} | Qtd: {qtd} | Categoria: {cat}\n")

    def limpar_estoque(self):
        confirmar = messagebox.askyesno("Confirmação", "Deseja apagar todo o estoque?")
        if confirmar:
            self.estoque = []
            self.resultado_texto.delete("1.0", tk.END)

# Iniciar o app
janela = tk.Tk()
app = ControleEstoque(janela)
janela.mainloop()

