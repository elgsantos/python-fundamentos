from veiculo import Veiculo
#importa do veiculo a classe Veiculo

caminhao = Veiculo('azul', 6, 'fiat', 10)

print(type(caminhao))

print('Cor: ',caminhao.cor)
print('Marca:', caminhao.marca)
print('Tanque: ',caminhao.tanque)

carro = Veiculo('preto', 4, 'ford', 5)

print('Cor: ',carro.cor)
print('Marca:', carro.marca)
print('Tanque: ',carro.tanque)