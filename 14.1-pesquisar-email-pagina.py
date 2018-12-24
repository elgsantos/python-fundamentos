import re
import requests

requisicao = requests.get('https://www.unilasalle.edu.br/rj/')

padrao = re.findall(r'[\w-]+@[\w-]+\.[\w\.-]+', requisicao.text) #r antes das aspas transforma em RAW string

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')