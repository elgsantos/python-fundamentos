#boolean
verdade = True
#operadores: == !=  >   <   >=  <=
#operadores: and    or
#operador de negação = not
a = 10
b = 20

#se a variável verdade for igual a True
if a>b:
    print(a, 'é maior do que',b)
else:
    print(a, 'não é maior do que',b)

print('Opções:\n1 = Escreve Hello\n2 = escreve World\n3 = escreve !')
opcao = input('Escolha uma opção: ')
if opcao == '1':
    print('Hello')
elif opcao == '2': #senão se
    print('World')
elif opcao == '3':
    print('!')
else:
    print('Opção inválida')