#funcoes def para declarar, não precisa definir tipagem de argumentos
#metodo geralmente não tem retorno mas não existe um consenso
def soma(num1, num2):
    return num1 + num2


print(soma(1,2))

def tem_sete_itens(objeto):
    if len(objeto) == 7:
        return True
    else:
        return False


if tem_sete_itens('1234567'):
    print("tem sete itens")

if tem_sete_itens(["oi",2,6,5,3,10.1,"tchau"]):
    print("tem sete itens")