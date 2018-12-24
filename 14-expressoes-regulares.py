import re #lib regex

string_teste = 'O gato é bonito, a gata é bonita, as gatinhas são bonitas, gat'

#criar o padrao - consultar documentacao
padrao = re.search(r'gat\w+', string_teste) #r antes das aspas transforma em RAW string
# . = significa qualquer caracter ate o espaco
# \w = substitui por uma letra nao considera espacos( procurar por uma palavra com 4 letras consecutivas \w\w\w\w)
# + = repete a ultima re mas deve ter pelo menos uma letra depois (gat\w+ = encontra as palavras com radical gat mas nao a palavra 'gat')
# * = repete a ultima re pode ter de 0 a infinitas letras depois (gat\w* = encontra as palavras com radical gat e o proprio radical 'gat*)

if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')

#pesquisar todas as ocorrências
padrao = re.findall(r'gat\w+', string_teste) #r antes das aspas transforma em RAW string

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')

string_email = 'o meu email é email@email.com.br, o seu é email@gmail.com'
#padrao de email
padrao = re.findall(r'[\w-]+@[\w-]+\.[\w\.-]+', string_email) #r antes das aspas transforma em RAW string

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')