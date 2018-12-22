import time
nomes = ['Joao', 'Eduardo', 'Alex', 'Julia']
print(nomes[0:len(nomes)+1])

#for item em coleção
for nome in nomes:
    print(nome)

#range
#lista_numeros = range(5)
lista_numeros = range(0, 20, 2)#com step
for i in lista_numeros:
    print(i)

for item in range(len(nomes)):
    print(nomes[item])

frase= 'Hello World!'
for letra in frase:
    print(letra)

i=0
while i < 10:
    print(i)
    i+=1
    time.sleep(1)

i=0
while i < 10:
    print(i)
    if i == 5:
        break
    i+=1