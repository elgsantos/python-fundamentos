'''
EXERCICIO: Escreva uma funcao que recebe um objeto de coleção e retorna o valor do maior numero dentro dessa coleção
faça outra função que retorna o menor numero dessa coleção
'''

def maior_interacao(colecao):
    maior = colecao[0]
    for item in colecao:
        if item > maior:
            maior = item
    return maior

def menor_interacao(colecao):
    menor = colecao[0]
    for item in colecao:
        if item < menor:
            menor = item
    return menor

def maior(colecao):
    return max(colecao)

def menor(colecao):
    return min(colecao)

lista = [12, 5, 3, 9, 50, 46, 10]

print(maior(lista))
print(maior_interacao(lista))
print(menor(lista))
print(menor_interacao(lista))