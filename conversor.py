class ConversorMoeda:
    def __init__(self):
        self.taxas = {
            'BRL': {'EUR': 0.16, 'ARS': 277.78, 'USD': 0.19},
            'EUR': {'ARS': 1702.73, 'USD': 1.15, 'BRL': 6.18},
            'USD': {'EUR': 0.87, 'ARS': 1480.25, 'BRL': 5.38},
            'ARS': {'EUR': 0.00059, 'USD': 0.00068, 'BRL': 0.0036}
        }

    def converter(self, origem, destino, valor):
        origem = origem.upper()
        destino = destino.upper()

        if origem not in self.taxas:
            raise ValueError(f"Moeda inválida: {origem}")

        if destino not in self.taxas[origem]:
            raise ValueError(f"Conversão não disponível de {origem} para {destino}")

        return valor * self.taxas[origem][destino]