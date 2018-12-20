#o input espera a entrada do usuário
nome = input('Escreva seu nome: ')
idade = input('Escreva sua idade: ')
altura = input('Escreva sua altura: ')

#o input guarda a entrada como string
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print('Nome:',nome,'\tIdade:',idade,'\tAltura:',altura)
print(tipo_nome)
print(tipo_idade)
print(tipo_altura)