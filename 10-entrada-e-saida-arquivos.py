# nome  modo de abertura(r,w) r é o default, w cria novamente o arquivo
# r+ leitura e escrita
# a append
arquivo = open('arquivo.txt', 'a+')
print(arquivo)

for i in range(1, 21):
    arquivo.write(str(i) + '\n')

arquivo.seek(0) #volta ao inicio
print(arquivo.read())

print('Arquivo:')
arquivo.seek(0) #volta ao inicio
for linha in arquivo:
    print(linha)

