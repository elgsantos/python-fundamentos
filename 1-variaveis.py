a = 'Hello World!'
#imprimir variável com quebra de linha
print(a,'\nVariáveis')
#imprimir variável com o tamanho dela ao lado
print(a,'\t',a.__len__())
n1=16
n2=20

print(n1**2) #potencia ao quadrado
print(n1**(1/2)) #raiz quadrada de n1

#string
nome = 'elgsantos'
#por convenção variáveis começam com letra minúscula e para juntar duas palavras no nome de variável se utiliza o _
idade = 22
#float
altura = 1.70

#retornar tipo da variável
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print('Nome:',nome,'\tIdade:',idade,'\tAltura:',altura)
print(tipo_nome)
print(tipo_idade)
print(tipo_altura)
