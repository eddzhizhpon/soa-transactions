import requests
from django.conf import settings

def generate_transaction_request(url, data, headers={}):
    '''
    Genera un request de transacción enviando todos los datos
    en formato Json.
    '''
    response = requests.post(url, json=data, headers=headers)

    print(response)
    
    if response.status_code == 201:
        return response.json()

def transaction_request(data):
    '''
    Construye la request para el proceso de transacción.
    En este se establecen los headers necesarios para
    conectarse y enviar los datos al ESB.
    '''
    headers = {
        'Content-Type': 'application/json',
        # 'Accept': 'application/json',
        'X-IBM-Client-Id': settings.IBM_CLIENT
    }
    url = settings.IBM_CLIENT_URL + '/transaction'
    data['debitBank'] = settings.BANK_ID
    response = generate_transaction_request(url, data, headers)
    if response:
        return True
    else: 
        return False

def generate_password_request(url, headers={}):
    '''
    Realizar un request al generador aleatorio de contraseñas 
    usando api externa para el registro de los usuarios.
    '''
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

def password_request():
    '''
    Construye la request con los headers y atributos necesarios
    para realizar la solicitud del generador de contraseñas
    al ESB.
    '''
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-IBM-Client-Id': settings.IBM_CLIENT
    }
    url = settings.IBM_CLIENT_URL + '/password/generate'

    response = generate_password_request(url, headers)

    if response:
        return response