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
    print(data.json())
    if len(data.json()['result']) > 0: # result está no arquivo json gerado
        if apenas_ultima_mensagem == True:
            update_id = data.json()['result'][-1]['update_id'] # pegar o ultimo resultado da chave update_id
            requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}')
            print(data.json()) # obter o formado json da resposta
        else:
            print(data.json())    

#chat_id, text, disable_notifications eu sei pra que serve através da documentação
def enviar_mensagem(chat_id, text, disable_notification=False):  # link da doc: https://core.telegram.org/bots/api#sendmessage
    token = '6784879599:AAGP2MTGyujuEJc61-jpN7M-qOQywUyRIes'
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&disable_notification{disable_notification}')
    

#while True abaixo foi usado na função obter_mensagens
#while True:
#   obter_mensagens(apenas_ultima_mensagem=True) # Quero todas as mensagens a partir do momento da execução do bot
# Se colocar em True, re
# torna apenas a ultima

def enviar_imagem(links_imagens, chat_id, caption):
    token = '6784879599:AAGP2MTGyujuEJc61-jpN7M-qOQywUyRIes'
    for link in links_imagens:
        requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')
        sleep(2)
 
 
# enviar_mensagem(chat_id='-4019639147', text='aproveite!')
# o número do chat_id está no arquivo json e conseguimos quando colocamos a função obter mensagem pra rodar.

# Para subir fotos, precisamos de um site de hospedagem de imagens..
# Neste caso, podemos usar o imgbb e faça o upload das imagens.
# Após fazer o upload, será criado um link da imagem. Copie o link.

# link das imagens
# https://ibb.co/KNmFBzV
# https://ibb.co/vVCNGXB
imagens = ['https://ibb.co/KNmFBzV', 'https://ibb.co/vVCNGXB']
#enviar_imagem(links_imagens=imagens, chat_id='-4019639147', caption='Proximo carro?')


# Para envio de audios, primeiro ache um site que guarde esse audio, tipo, mediafire
def enviar_audio(links_audios, chat_id, caption):
    token = '6784879599:AAGP2MTGyujuEJc61-jpN7M-qOQywUyRIes'
    for link in links_audios:
        data = requests.get(f'https://api.telegram.org/bot{token}/sendAudio?chat_id={chat_id}&audio={link}&caption={caption}')
        print(data.json())

audios = ['https://download856.mediafire.com/xve1l0g18vygblWzCSM4EG-J4jpv8LYsVHL5STASWhYZfdnVbeoygonX5P3PFWb52q6jUPTbkVjkwVCiIBVAKzLAemZSor2z9WmMGZ33j99aWURphYRGOJBTB_E8t7GObkSS5_fGSUmCuvAY71AIIaTFUiGwUnk55ixSemBMHxs-9w/kzup508w5ybp0w5/Gravando.m4a']
#enviar_audio(links_audios=audios, chat_id='-4019639147', caption='audio de teste')        

def enviar_documentos(links_documentos, chat_id, caption):
    token = '6784879599:AAGP2MTGyujuEJc61-jpN7M-qOQywUyRIes'
    for link in links_documentos:
        requests.get(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}&document={link}&caption={caption}')
    

# A função acima de enviar documentos está pronta, mas precisamos dos links dos documentos.
# No caso, estamos usando o google drive para os documentos. 
# para isso, existe uma maneira. Pegue o link do arquivo e cole:
# https://drive.google.com/file/d/10wkR9-GNU_75kHRWk4Tc18lpxF-xIlyy/view?usp=sharing
# o código é o seguinte: drive.google.com/uc?id=####&export=download
# Dai você pega a maior sequencia de caracteres do link, neste caso> 10wkR9-GNU_75kHRWk4Tc18lpxF-xIlyy
# E cola no código, no lugar de ####, ficando assim:

# drive.google.com/uc?id=10wkR9-GNU_75kHRWk4Tc18lpxF-xIlyy&export=download

documentos = ['drive.google.com/uc?id=10wkR9-GNU_75kHRWk4Tc18lpxF-xIlyy&export=download']
enviar_documentos(links_documentos=documentos, chat_id='-4019639147', caption='documento de teste')

"""Dependendo do bot, vc pode querer somente a ultima mensagem do usuario.
para isso: No arquivo json gerado ao apertar pra rodar o programa, a variável
update_id vai gerar uma numeração a cada nova mensagem(sempre aumenta um numero). 
Para evitar erros, vamos criar uma forma de
verificar: Linha 25 deste codigo 
"""       

