import sys

argumentos = sys.argv #arg1 method // arg 2 - n1 // arg 3 - n2 (arg 1 é sempre o arquivo)

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumentos[1] == "--soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "--sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)

'''resultado no cmd  
E:\Documentos\PyCharmProjects\python>python 8-passagem_de_argumentos_cmd.py --soma 2 10
210
'''