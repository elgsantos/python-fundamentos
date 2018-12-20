lista_nomes = ['Joao', 'Maria', 'Jose']
#assim como em outras linguagens de programação a lista é indexada a partir do 0
#print(lista_nomes[0])
print(lista_nomes) #converte a lista para string e imprime
lista_nomes[1]='Mariana'
#adicionar itens
lista_nomes.append('Luiz')

print(lista_nomes[-1]) #imprime último item (indice negativo começa a contar do último)
#remover itens
lista_nomes.remove('Joao')
print(lista_nomes)
#limpar lista
#lista_nomes.clear()
#inserir em posição especifica
lista_nomes.insert(2,'Mariana')
print(lista_nomes)
contador_mariana = lista_nomes.count('Mariana') #contar itens
print(contador_mariana)
#funçao pop de pilha resgata ultimo obj e tira da lista (a lista é mutável)
print(lista_nomes.pop())
print(lista_nomes)

frase = 'Oi, tudo bem?'
frase+=' :)'
#imprime do indice 0 até o 7 (da primeira até a oitava letra)
#de 0 até < 8
print(frase[0:8])
#pode ser inserido mais um argumento para definir o step (padrão é 1)
print(frase[0:8:2])
#utilizando step negativo
print(frase[::-1])
#printar tamanho do obj
print(len(frase))
#passar para minúscula
print(frase.lower())
#transforma a string em uma lista
print(frase.split(','))