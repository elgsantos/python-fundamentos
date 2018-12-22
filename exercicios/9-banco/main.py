'''
EXERCICIO: Crie um software de gerenciamento baancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar, e consultar saldo
'''
from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Joao', '123455', 30)
conta1 = Conta(cliente1, 2000, 1000)

print('Nome:',conta1.cliente)
print('Saldo:',conta1.consulta_saldo())
print('Deposito de 1000,5:')
conta1.depositar(1000.5)
print('Saldo:',conta1.consulta_saldo())
print('Deposito de 0:')
conta1.depositar(0)
print('Saldo:',conta1.consulta_saldo())
print('saque de 3000:')
conta1.sacar(3000)
print('Saldo:',conta1.consulta_saldo())
print('saque de 500:')
conta1.sacar(500)
print('Saldo:',conta1.consulta_saldo())