import time

try:
    a = 2/0
except: #tratando qualquer erro
    print('Aconteceu algum erro')

try:
    asdasd()
except ZeroDivisionError: #erro de divisão por 0
    print('Divisão por 0!')
except NameError: #erro de nome
    print('Você digitou algo errado')

try:
    a = 2/0
except Exception as erro:
    print("Aconteceu algum erro:", erro)

def abre_arquivo():
    try:
        arquivo = open('arquivo1.txt')
        return True
    except Exception as erro:
        print("aconteceu algum erro", erro)
        return False

#enquanto não for criado o arquivo vai ser retornado erro
#maximo de 5 tentativas
i=1
while not abre_arquivo():
    print('Tentando abrir o arquivo')
    if i == 5:
        print('Após as tentativas não foi possível abrir o arquivo.')
        break
    time.sleep(5)
    i+=1
if i < 5:
    print('Consegui abrir o arquivo')