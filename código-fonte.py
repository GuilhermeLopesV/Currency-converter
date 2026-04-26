# Conversor de moeda

"""
Ideias iniciais

Fazer um conversor de moedas que
converta vários tipos de moedas.

Cria uma 'interface' gráfica (GUI)
utilizando Tkinter

Regras do projeto
Crie funções para deixa o código mais limpo e versátil
Fazer o tratamento de exceções

"""
import requests

print("=== Conversor de Moedas ===")

valor = float(input("Digite o valor: "))
de = input("De qual moeda? (ex: BRL): ").upper()
para = input("Para qual moeda? (ex: USD): ").upper()

url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    convertido = list(dados['rates'].values())[0]
    print(f"{valor} {de} = {convertido:.2f} {para}")
else:
    print("Erro ao obter taxa de câmbio.")

