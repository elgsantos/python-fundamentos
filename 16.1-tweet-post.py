import oauth2
import json
import pprint
import urllib.parse
#crie uma conta no twitter developers
#crie um app para acessar o twitter
#crie um arquivo twitter-auth.py com as variaveis contendo seu próprio token
#da seguinte forma: (insira suas chaves dentro das aspas)
# consumer_key = ''
# secret_key = ''
#
# token_key = ''
# token_secret = ''
exec(open('twitter-auth.py').read())

consumer = oauth2.Consumer(consumer_key, secret_key)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Novo tweet: ")
#codificar para usar o # como caracter normal
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

#objeto veio em bytes, decodificar
decodificar = requisicao[1].decode()
#transformar em dicionario
objeto = json.loads(decodificar)

#imprimir estruturado pprint
pprint.pprint(objeto)
