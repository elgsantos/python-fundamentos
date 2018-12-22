class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite*-1

    def consulta_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if self.saldo - valor >= self.limite:
            self.saldo -= valor
            return valor
        print('Saldo insuficiente')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('valor depositado')
        else:
            print('você não depositou nada')