from veiculo import Veiculo

#herança
class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque) #carro sempre vai ter 4 rodas

    def abastecer(self, litros): #sobreposicao, abastecer com comportamentos diferentes
        if self.tanque + litros > 50:
            print("Tanque com capacidade inferior")
        else:
            self.tanque += litros