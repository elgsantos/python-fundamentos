'''
EXERCICIO: Faça um programa que leia a qtd de pessoas para uma festa
após isso o programa irá perguntar o nome de todas as pessoas
e colocar numa lista de convidados
Após isso imprimir todos os nomes da lista
'''

qtd = int(input('Quantidade de pessoas para a festa: '))
i=0
lista_convidados = []
while i < qtd:
    lista_convidados.append(input('Digite o nome do convidado '+str(i)+': '))
    i+=1

print('\nLista de convidados para a festa')
for pessoa in lista_convidados:
    print(pessoa)