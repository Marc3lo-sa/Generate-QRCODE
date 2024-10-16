import tkinter as tk
from tkinter import messagebox, filedialog
import pyqrcode

class GeradorCodigoDeBarrasApp:
    def __init__(self, master):
        self.master = master
        master.title("Gerador de Código de Barras")

        self.label = tk.Label(master, text="Digite os dados para gerar o código de barras:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Gerar Código de Barras", command=self.gerar_codigo)
        self.button.pack()

    def gerar_codigo(self):
        dados = self.entry.get()

        if dados:
            try:
                # Criar o código QR
                qr_code = pyqrcode.create(dados)

                # Salvar o código QR em um arquivo PNG
                nome_arquivo = f'codigo_de_barras_{dados}.png'
                qr_code.png(nome_arquivo, scale=10)

                messagebox.showinfo("Sucesso", "Código de barras gerado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o código de barras: {str(e)}")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira os dados para gerar o código de barras.")

root = tk.Tk()
app = GeradorCodigoDeBarrasApp(root)
root.mainloop()
