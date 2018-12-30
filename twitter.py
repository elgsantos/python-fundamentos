import oauth2
import urllib.parse
import json
#biblioteca twitter
class Twitter:
    def __init__(self, consumer_key, secret_key, token_key, token_secret):
        self.conexao(consumer_key, secret_key, token_key, token_secret)

    def conexao(self, consumer_key, secret_key, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, secret_key)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def tweet(self, texto):
        # codificar para usar o # como caracter normal
        query_codificada = urllib.parse.quote(texto, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada,
                                     method='POST')
        # objeto veio em bytes, decodificar
        decodificar = requisicao[1].decode()
        # transformar em dicionario
        objeto = json.loads(decodificar)