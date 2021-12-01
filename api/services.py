import requests
from django.conf import settings
import json

# Genera una transacción enviando todos los datos necesarios
def generate_transaction_request(url, data, headers={}):

    response = requests.post(url, json=data, headers=headers)

    print(response)
    
    if response.status_code == 201:
        return response.json()

# Identifica el tipo de consumo que se da con el ESB para asi realizar una transacción
def transaction_request(data):
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

# Generador aleatorio de contraseñas usando api externa para usuarios
def generate_password_request(url, headers={}):

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

# Envio de la contraseña generada hacia la el ESB
def password_request():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-IBM-Client-Id': settings.IBM_CLIENT
    }
    url = settings.IBM_CLIENT_URL + '/password/generate'

    response = generate_password_request(url, headers)

    if response:
        return response