import requests
import json

def requisicao(titulo):
    lista = []
    for i in range(1,101):
        try:
            url = 'http://www.omdbapi.com/?apikey=67842d93&type=movie&s='+titulo+'&page='+str(i)
            req = requests.get(url)
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    lista.append(filme)
            else:
                break

        except Exception as e:
            print('erro na conexão', e)
            return None
    return lista

def listar(lista):
    i = 0
    for item in lista:
        print(i+1, '-', lista[i]['Title'] + ' (' + lista[i]['Year'] + ') ')
        i += 1

def mostrar_detalhes(filme):
    try:
        print('Título:', filme['Title'])
        print('Ano:', filme['Year'])
        print('imbdID:', filme['imdbID'])
    except Exception as e:
        print('Erro na aplicação, atributo nao encontrado: ', e)

sair = False
while not sair:
    print('\n.:Pesquisa de Filmes:.')
    op = input('Digite um filme ou SAIR para fechar: ')
    if op.lower() == 'sair':
        sair = True
    else:
        lista_filmes = requisicao(op)
        print('Filmes encontrados: ', len(lista_filmes))
        if(len(lista_filmes)>0):
            listar(lista_filmes)
            try:
                escolha = input('Escolha um numero de filme acima para exibir detalhes:')
                mostrar_detalhes(lista_filmes[int(escolha)-1])
            except Exception as e:
                print('escolha inválida', e)