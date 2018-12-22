class Veiculo:
    #metodos
    def __init__(self, cor, rodas, marca, tanque):    #construtor
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros