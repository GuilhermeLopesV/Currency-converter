import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

brl = {'EUR': 0.16, 'ARS': 277.78, 'USD': 0.19}
eur = {'ARS': 1702.73, 'USD': 1.15, 'BRL': 6.18}
usd = {'EUR': 0.87, 'ARS': 1480.25, 'BRL': 5.38}
ars = {'EUR': 0.00059, 'USD': 0.00068, 'BRL': 0.0036}

def conversor(moeda_origem, moeda_destino, valor):
    taxas = {'BRL': brl, 'EUR': eur, 'USD': usd, 'ARS': ars}

    if moeda_origem not in taxas:
        print(f"A moeda de origem '{moeda_origem}' não é suportada.")
        return
    if moeda_destino not in taxas[moeda_origem]:
        print(f"Não há taxa de conversão de {moeda_origem} para {moeda_destino}.")
        return

    taxa = taxas[moeda_origem][moeda_destino]
    convertido = valor * taxa
    print(f"{valor:.2f} {moeda_origem} = {convertido:.4f} {moeda_destino}")

def conversor_de_moeda():
    while True:
        limpar_tela()
        print('-' * 40)
        print(' BEM-VINDO AO CONVERSOR DE MOEDAS '.center(40, '-'))
        print('-' * 40)
        print('(Exemplo: BRL, USD, EUR, ARS)')

        try:
            valor = float(input('Digite o valor a converter: '))
            moeda_origem = input('Digite a moeda de origem: ').upper()
            moeda_destino = input('Digite a moeda de destino: ').upper()
        except ValueError:
            print('Valor digitado está incorreto. Use apenas números.')
            input("Pressione Enter para tentar novamente...")
            continue

        conversor(moeda_origem, moeda_destino, valor)

        sair = input('Deseja sair? [S/N] ').upper()
        if sair == 'S':
            break