import requests
import csv
from datetime import datetime

# Lista de moedas a serem consultadas
moedas = ["USD", "EUR", "BTC"]

# Data de hoje para referência
data_hoje = datetime.now().strftime('%Y-%m-%d')

# Fazer requisição para cada moeda
dados = []

for moeda in moedas:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        par = f"{moeda}BRL"
        cotacao = json_data[par]
        dados.append({
            "moeda": moeda,
            "cotacao": cotacao["bid"],
            "data": datetime.fromtimestamp(int(cotacao["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        print(f"Erro ao buscar dados para {moeda}")

# Salvar em CSV
nome_arquivo = "cotacoes.csv"

with open(nome_arquivo, mode="w", newline="") as arquivo:
    writer = csv.DictWriter(arquivo, fieldnames=["moeda", "cotacao", "data"])
    writer.writeheader()
    writer.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
