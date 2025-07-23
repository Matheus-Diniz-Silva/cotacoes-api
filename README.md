# Consulta de Cotações de Moedas via API

Este projeto realiza a consulta de cotações de moedas (USD, EUR e BTC) por meio de uma API pública e salva os dados em um arquivo CSV.

## API utilizada

As cotações foram obtidas via [AwesomeAPI - Currency](https://docs.awesomeapi.com.br/api-de-moedas).

## Arquivos incluídos

- `cotacoes.py`: Script Python responsável por consultar a API e salvar os dados.
- `cotacoes.csv`: Arquivo CSV gerado com as cotações mais recentes.

## Como executar localmente

1. Certifique-se de ter o Python 3 instalado.
2. Instale a biblioteca `requests` (caso não tenha):

   ```bash
   pip install requests
