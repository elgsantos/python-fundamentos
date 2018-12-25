import re
import requests

requisicao = requests.get('https://www.unilasalle.edu.br/rj/fale-conosco/')

padrao = re.findall(r'[\w-]+@[\w-]+\.[\w\.-]+', requisicao.text) #r antes das aspas transforma em RAW string

if padrao:
    conjunto = set()
    for item in padrao:
        conjunto.add(item)
    print(conjunto)
else:
    print('Padrão não encontrado')