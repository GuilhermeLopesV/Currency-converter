from tkinter import *
from conversor import ConversorMoeda

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas")
        self.root.geometry('500x400')

        self.conversor = ConversorMoeda()

        self.criar_widgets()

    def criar_widgets(self):
        Label(self.root, text="Conversor de Moedas", font=('Arial', 18)).pack(pady=10)

        self.valor_entry = Entry(self.root)
        self.valor_entry.pack(pady=5)

        self.origem_entry = Entry(self.root)
        self.origem_entry.pack(pady=5)

        self.destino_entry = Entry(self.root)
        self.destino_entry.pack(pady=5)

        Button(self.root, text="Converter", command=self.converter).pack(pady=10)

        self.resultado_label = Label(self.root, text="", font=('Arial', 12))
        self.resultado_label.pack(pady=10)

        Button(self.root, text="Sair", command=self.root.destroy, bg='red', fg='white').pack(pady=10)

    def converter(self):
        try:
            valor = float(self.valor_entry.get())
            origem = self.origem_entry.get()
            destino = self.destino_entry.get()

            resultado = self.conversor.converter(origem, destino, valor)

            self.resultado_label.config(
                text=f"{valor:.2f} {origem.upper()} = {resultado:.2f} {destino.upper()}"
            )

        except ValueError as e:
            self.resultado_label.config(text=str(e))


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()