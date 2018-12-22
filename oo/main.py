from veiculo import Veiculo #importa do veiculo a classe Veiculo
from carro import Carro

caminhao = Veiculo('azul', 6, 'fiat', 10)

print(type(caminhao))

print('Cor: ',caminhao.cor)
print('Marca:', caminhao.marca)
print('Tanque: ',caminhao.tanque)

#classe carro filha de veiculo
carro = Carro('preto', 'ford', 28)

print('Cor: ',carro.cor)
print('Marca:', carro.marca)
print('Tanque: ',carro.tanque)
carro.abastecer(10)
print('Tanque: ',carro.tanque)
carro.abastecer(30)
print('Tanque: ',carro.tanque)