'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do Exercito
Para entrar no exercito é preciso ter mais de 18 anos
pesar mais ou igual a 60 kg
e medir mais ou igual a 1,70
'''

idade = int(input('Informe a idade: '))
peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))

if idade>18 and peso>=60 and altura>=1.70:
    print('Apto para entrar no exército')
else:
    print('Não está apto para entrar no exército')