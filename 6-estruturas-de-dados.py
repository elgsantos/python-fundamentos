lista = ['Joao', 'Maria'] #lista (list)
tupla = ('Joao', 'Maria') #tupla (tuple) - não mutável
dicionario = {'nome': 'João', 'idade':30} #dicionario (dict) tem chave e valor (hashmap)
conjunto = {'Joao', 'Maria'} #Conjunto (set) mutável, no conjunto não se insere itens repetidos, e o conjunto não é ordenado

print(tupla[0])

#se item está na coleção
if 'Joao' in tupla:
    print('Joao esta na colecao')


print(dicionario['idade'])

if 'Joao' in dicionario.values():
    print('Joao esta no dicionario')

#imprimir chaves
for item in dicionario.keys():
    print(item)

#conjunto tem a busca rapida, muito mais rapida do que a lista
if 'Joao' in conjunto:
    print('Foi encontrado dentro do conjunto')

'''
Inicializar vazio
lista = []
tupla = ()
dicionario = {}
conjunto = set()
'''