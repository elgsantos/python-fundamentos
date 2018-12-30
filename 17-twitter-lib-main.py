from twitter import Twitter

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

twitter = Twitter(consumer_key, secret_key, token_key, token_secret)

for i in range(1,3):
    query = input("Novo tweet: ")
    twitter.tweet(query+' '+str(i))