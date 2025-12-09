# Dicionários com as taxas de conversão
brl = {
    'EUR': 0.16,
    'ARS': 277.78,
    'USD': 0.19,
}
eur = {
    'ARS': 1702.73,
    'USD': 1.15,
    'BRL': 6.18,
}
usd = {
    'EUR': 0.87,
    'ARS': 1480.25,
    'BRL': 5.38,
}
ars = {
    'EUR': 0.00059,
    'USD': 0.00068,
    'BRL': 0.0036,
}

# Função para converter
def conversor(moeda_origem, moeda_destino, valor):
    taxas = {
        'BRL': brl,
        'EUR': eur,
        'USD': usd,
        'ARS': ars,
    }

    if moeda_origem not in taxas or moeda_destino not in taxas[moeda_origem]:
        print('Moeda não suportada ou combinação inválida.')
        return

    taxa = taxas[moeda_origem][moeda_destino]
    convertido = valor * taxa

    print(f'{valor:.2f} {moeda_origem} = {convertido:.2f} {moeda_destino}')

# Programa principal
print('--- Bem-vindo ao Conversor de Moedas ---')
print('-' * 40)
print('Moedas disponíveis: BRL, USD, EUR, ARS')
print()

valor = float(input('Digite o valor a converter: '))
de = input('De qual moeda você quer converter: ').upper()
para = input('Para qual moeda você quer converter: ').upper()

conversor(de, para, valor)
