from django.http import response
import requests
import json
from requests.api import request
from requests.models import Response


#consumo de api tbk
def generate_request_tbk(url, body):
    try:
        response = requests.post(url, body,
        headers = { "Tbk-Api-Key-Id": "597055555532", "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C", "Content-Type": "application/json"}, timeout=None)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError as e:
        response = "No hay respuesta" 
        return response
def get_initTrxTBK():

    body = json.dumps({"buy_order": "ordencompra", "session_id": "sesion1234557545", "amount": 10 , "return_url": "http://localhost:8000/tbkRes/" })
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.0/transactions"
    response = generate_request_tbk(url, body)
    if response:
       return response

def get_status_trx(url, token_ws):
    try:
        response = requests.get(url+"/"+token_ws,  headers = { "Tbk-Api-Key-Id": "597055555532", "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C", "Content-Type": "application/json"}, timeout=None)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError as e:
        response = "No hay respuesta"
        return response

def get_statusTBK(request):
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.0/transactions"
    response = get_status_trx(url, request.POST['token_ws'])
    if response:
<<<<<<< HEAD
       return response
=======
       return response



#Consumo de apis Django
def generate_request(url, params={}):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError as e:
        response = "Error: No existe respuesta del servidor"
        return response
>>>>>>> 0734714099ca445bd50b8e02e47935ab55bbd8cf
