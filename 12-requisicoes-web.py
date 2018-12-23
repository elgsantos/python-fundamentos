import requests
#beautiful soup 4 bs4 pip install bs4 pra page parsing

cabecalho = {'User-agent': 'Windows 20',
             'Referer': 'https://google.com'}

meus_cookies = {'Ultima-visita': '10-10-2018'}

texto = None
try:
    requisicao = requests.post('https://putsreq.com/7fmeywWOIvZIdiEqjhG1',
                               headers=cabecalho,
                               cookies=meus_cookies)
    texto = requisicao.text
except Exception as e:
    print('Erro na requisição', e)

print(texto)