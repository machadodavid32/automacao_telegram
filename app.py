import requests
from rich import print
from time import sleep

# Para criar um bot precisamos de
# token: 6784879599:AAGP2MTGyujuEJc61-jpN7M-qOQywUyRIes
# URL do API: https://core.telegram.org/bots/api
# ao abrir o link acima, vá em making requests e copie o link em vermelho
# URL do API: https://api.telegram.org/bot<token>/METHOD_NAME

# Qual tipo de requisição quer fazer - existem varios metodos. Vamos escolher o GetUpdates

# Monte dessa forma, confome a linha 5, no link, dentro de token, coloque o token. E em
# METHOD_NAME, coloque o nome do metodo, conforme abaixo:

# https://api.telegram.org/bot6784879599:AAGP2MTGyujuEJc61-jpN7M-qOQywUyRIes/getUpdates

# Faça a instalação de duas bibliotecas, requests e rich. Requests para fazer requisições e 
# rich que mostra essas requisições de forma mais clara

def obter_mensagens(apenas_ultima_mensagem=False):
    update_id = None # identificador da ultima mensagem enviada no grupo (numero das mensagens)
    token = '6784879599:AAGP2MTGyujuEJc61-jpN7M-qOQywUyRIes'
    data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates') # Fazendo a requisição
    if len(data.json()['result']) > 0: # result está no arquivo json gerado
        if apenas_ultima_mensagem == True:
            update_id = data.json()['result'][-1]['update_id'] # pegar o ultimo resultado da chave update_id
            requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}')
            print(data.json()) # obter o formado json da resposta
        else:
            print(data.json())    

while True:
    obter_mensagens(apenas_ultima_mensagem=True) # Quero todas as mensagens a partir do momento da execução do bot
# Se colocar em True, retorna apenas a ultima


'''Dependendo do bot, vc pode querer somente a ultima mensagem do usuario.
para isso: No arquivo json gerado ao apertar pra rodar o programa, a variável
update_id vai gerar uma numeração a cada nova mensagem(sempre aumenta um numero). 
Para evitar erros, vamos criar uma forma de
verificar: Linha 25 deste codigo 
 '''        