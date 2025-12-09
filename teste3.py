import os
from tkinter import *

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

brl = {'EUR': 0.16, 'ARS': 277.78, 'USD': 0.19}
eur = {'ARS': 1702.73, 'USD': 1.15, 'BRL': 6.18}
usd = {'EUR': 0.87, 'ARS': 1480.25, 'BRL': 5.38}
ars = {'EUR': 0.00059, 'USD': 0.00068, 'BRL': 0.0036}

def conversor(moeda_origem, moeda_destino, valor):
    taxas = {'BRL': brl, 'EUR': eur, 'USD': usd, 'ARS': ars}

    if moeda_origem not in taxas:
        mensagem2 = (
            f"Não há taxa de conversão de {moeda_origem} para {moeda_destino}."
        )
        texto_conversor["text"] = mensagem2
    if moeda_destino not in taxas[moeda_origem]:
        mensagem1 = (
            f"Não há taxa de conversão de {moeda_origem} para {moeda_destino}."
        )
        texto_conversor["text"] = mensagem1

    taxa = taxas[moeda_origem][moeda_destino]
    convertido = valor * taxa

    mensagem3 = f"{valor:.2f} {moeda_origem} = {convertido:.4f} {moeda_destino}"
    texto_conversor["text"] = mensagem3


def conversor_de_moeda():


        valor = float(pegar_valor())
        moeda_origem = pegar_moeda_origem()
        moeda_destino = pegar_moeda_destino()

        conversor(moeda_origem, moeda_destino, valor)



def pegar_valor():
    valor = entrada1.get()
    return valor


def pegar_moeda_origem():
    moeda_origem = entrada2.get()
    return moeda_origem


def pegar_moeda_destino():
    moeda_destino = entrada3.get()
    return moeda_destino


mensagem = """
----------------------------------------
------- BEM-VINDO AO CONVERSOR DE MOEDAS -------
----------------------------------------
(Exemplo: BRL, USD, EUR, ARS)
"""



janela = Tk()
janela.title("Conversor de moeda")
janela.geometry('1500x750')

texto_cpf1 = Label(janela, text='-------------------------------------------', font=('Arial', 18))
texto_cpf1.grid(column=0, row=9, padx=25, pady=25)


texto_cpf = Label(janela, text='', font=('Arial', 18))
texto_cpf.grid(column=1, row=1, padx=25, pady=25)
texto_cpf["text"] = mensagem

texto_de_orintacao1 = Label(janela, text='Digite o valor a converter: ', font=('Arial', 10))
texto_de_orintacao1.grid(column=1, row=2, padx=25, pady=25)
entrada1 = Entry(janela)
entrada1.grid(column=1, row=3, padx=25, pady=25)

texto_de_orintacao2 = Label(janela, text='Digite a moeda de origem: ', font=('Arial', 10))
texto_de_orintacao2.grid(column=1, row=4, padx=25, pady=25)
entrada2 = Entry(janela)
entrada2.grid(column=1, row=5, padx=25, pady=25)

texto_de_orintacao3 = Label(janela, text='Digite a moeda de destino: ')
texto_de_orintacao3.grid(column=1, row=6, padx=25, pady=25)
entrada3 = Entry(janela)
entrada3.grid(column=1, row=7, padx=25, pady=25)

botao = Button(janela, text="Aperte para iniciar", command=conversor_de_moeda, font=('Arial', 20))
botao.grid(column=1, row=8, padx=25, pady=25)

texto_conversor = Label(janela, text='')
texto_conversor.grid(row=9, column=1)

janela.mainloop()