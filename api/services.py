import requests
from django.conf import settings
import json

def generate_transaction_request(url, data, headers={}):

    response = requests.post(url, json=data, headers=headers)

    print(response)
    
    if response.status_code == 201:
        return response.json()

def transaction_request(data):
    headers = {
        'Content-Type': 'application/json',
        # 'Accept': 'application/json',
        'X-IBM-Client-Id': settings.IBM_CLIENT
    }
    url = settings.IBM_CLIENT_URL + '/transaction'
    data['debitBank'] = settings.BANK_ID
    # print(data)
    response = generate_transaction_request(url, data, headers)
    if response:
        return True
    else: 
        return False

def generate_password_request(url, headers={}):

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

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