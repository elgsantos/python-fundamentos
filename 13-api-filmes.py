import requests
import json

req = None

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=67842d93&type=movie&t='+titulo)
        #print(req.text)
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as e:
        print('Erro na conexão', e)
        return None

def mostrar_detalhes(filme):
    try:
        print('Título:', filme['Title'])
        print('Ano:', filme['Year'])
        print('Diretor:', filme['Director'])
        print('Atores:', filme['Actors'])
        print('Nota:', filme['imdbRating'])
        print('Premios:', filme['Awards'])
        print('Posters:', filme['Poster'])
        print('')
    except Exception as e:
        print('Erro na aplicação, atributo nao encontrado: ', e)
sair = False
while not sair:
    op = input('Digite um filme ou SAIR para fechar: ')
    if op.lower() == 'sair':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            mostrar_detalhes(filme)