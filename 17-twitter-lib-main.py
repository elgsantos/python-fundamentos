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

sair = False
while not sair:
    print('1 - Novo tweet')
    print('2 - Pesquisar tweets')
    op = input('Digite a opcao ou SAIR para fechar: ')
    if op.lower() == 'sair':
        sair = True
    elif op == '1':
        query = input("Novo tweet: ")
        twitter.tweet(query)
    elif op == '2':
        query = input("Pesquisar: ")
        pesquisa = twitter.search(query, 'pt')
        print('____________________________________________')
        for resultado in pesquisa:
            print(resultado['user']['screen_name'])
            print(resultado['text'])
            print('____________________________________________')
    else:
        print('digite uma opção válida.')