#Programa que retorna dados de cotação de moedas por uma api
# api utilizada: https://docs.awesomeapi.com.br/api-de-moedas
import requests
import json
import time
import datetime

while True:
    try:
        requisicao = requests.get('https://economia.awesomeapi.com.br/all')
        cotacao = json.loads(requisicao.text)
        print('#### COTAÇÃO ####', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #lib para data e hora
        print('Dolar:', cotacao['USD']['ask'])
        print('Euro:', cotacao['EUR']['ask'])
        print('BTC:', cotacao['BTC']['ask'])
    except:
        print('erro de conexão')
    time.sleep(5)