import requests
import json

try:
    cod = ""
    while cod != "200":
        cidade = input('Escreva sua cidade: ')
        #request enviada parametro q = cidade, units=metric para graus celsius ou pode ser utilizada a conversao de kelvin pra celsius float(temperatura-273.15)
        requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&APPID=bb3d893a00a351f980e9558070fc37e5&units=metric')
        resposta = json.loads(requisicao.text)
        cod = str(resposta['cod'])
        if cod == "404":
            print('Cidade não encontrada')
        else:
            # condicao atual
            condicao = resposta['weather'][0]['main']
            # descricao atual dict - list - dict
            descricao = resposta['weather'][0]['description']
            print('Condição:', condicao)
            print('Descrição:', descricao)
            # temperaturas
            temperatura = resposta['main']['temp']
            temp_min = resposta['main']['temp_min']
            temp_max = resposta['main']['temp_max']
            print('Temperatura:', temperatura)
            print('Mínima:', temp_min)
            print('Máxima:', temp_max)
except Exception as e:
    print('Erro de conexao',e)