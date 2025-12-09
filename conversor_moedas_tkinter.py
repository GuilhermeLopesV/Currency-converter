from tkinter import *

brl = {'EUR': 0.16, 'ARS': 277.78, 'USD': 0.19}
eur = {'ARS': 1702.73, 'USD': 1.15, 'BRL': 6.18}
usd = {'EUR': 0.87, 'ARS': 1480.25, 'BRL': 5.38}
ars = {'EUR': 0.00059, 'USD': 0.00068, 'BRL': 0.0036}

def conversor(moeda_origem, moeda_destino, valor):
    taxas = {'BRL': brl, 'EUR': eur, 'USD': usd, 'ARS': ars}

    if moeda_origem not in taxas:
        texto_conversor["text"] = f"Moeda de origem inválida: {moeda_origem}"
        return

    if moeda_destino not in taxas[moeda_origem]:
        texto_conversor["text"] = (
            f"Não há taxa de conversão de {moeda_origem} para {moeda_destino}."
        )
        return

    taxa = taxas[moeda_origem][moeda_destino]
    convertido = valor * taxa
    texto_conversor["text"] = f"{valor:.2f} {moeda_origem} = {convertido:.4f} {moeda_destino}"

def conversor_de_moeda():

    try:
        valor = float(pegar_valor())
    except ValueError:
        texto_conversor["text"] = "Valor inválido! Digite um número."
        return

    moeda_origem = pegar_moeda_origem().upper()
    moeda_destino = pegar_moeda_destino().upper()

    conversor(moeda_origem, moeda_destino, valor)

def pegar_valor():
    return entrada1.get()

def pegar_moeda_origem():
    return entrada2.get()

def pegar_moeda_destino():
    return entrada3.get()

mensagem = """
 BEM-VINDO AO CONVERSOR DE MOEDAS 
(Exemplo: BRL, USD, EUR, ARS)
"""

janela = Tk()
janela.title("Conversor de moeda")
janela.geometry('1500x750')


janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

texto_mensagem = Label(janela, text=mensagem, font=('Arial', 15))
texto_mensagem.grid(column=1, row=1, padx=5, pady=5)

texto_de_orintacao1 = Label(janela, text='Digite o valor a converter: ', font=('Arial', 15))
texto_de_orintacao1.grid(column=1, row=2, padx=25, pady=25)
entrada1 = Entry(janela)
entrada1.grid(column=1, row=3, padx=5, pady=5)

texto_de_orintacao2 = Label(janela, text='Digite a moeda de origem: ', font=('Arial', 15))
texto_de_orintacao2.grid(column=1, row=4, padx=25, pady=25)
entrada2 = Entry(janela)
entrada2.grid(column=1, row=5, padx=5, pady=5)

texto_de_orintacao3 = Label(janela, text='Digite a moeda de destino: ', font=('Arial', 15))
texto_de_orintacao3.grid(column=1, row=6, padx=25, pady=25)
entrada3 = Entry(janela)
entrada3.grid(column=1, row=7, padx=5, pady=5)

botao = Button(janela, text="Aperte para converter", command=conversor_de_moeda, font=('Arial', 15))
botao.grid(column=1, row=8, padx=25, pady=25)

texto_conversor = Label(janela, text='', font=('Arial', 15))
texto_conversor.grid(row=9, column=1)

botao_sair = Button(
    janela,
    text="Encerrar",
    command=janela.destroy,
    font=('Arial', 10),
    bg='red',
    fg='white'
)
botao_sair.grid(column=1, row=10, padx=25, pady=25)

janela.mainloop()
