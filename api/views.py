from django.db.models.fields import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.views import APIView
from rest_framework.decorators import api_view

import json

from .forms import SignUpForm
from .services import transaction_request, password_request
from .models import Account

class SignupView(LoginRequiredMixin, UserPassesTestMixin, APIView):
    '''
    Clase designada para registrar un usuario
    y persistirlo en la Base de Datos.
    '''
    login_url = '/api/auth/login/'

    def test_func(self):
        '''
        Verifica que el usuario logueado tenga
        permisos de administrador.
        '''
        return self.request.user.is_superuser

    def get(self, request):
        form = SignUpForm()
        return render(request, 'api/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(data={'reason': 'Usuario no creado.', 'errors': form.errors}, status=HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(('GET',))
def generate_password(request):
    '''
    Método para obtener las contraseñas generadas
    por la api: https://github.com/fawazsullia/password-generator
    '''
    if request.method == 'GET':
        response = password_request()
        if response:
            return JsonResponse(response, status=HTTP_200_OK)
        else:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@login_required
@api_view(('POST',))
def transaction_create(request):
    '''
    Método para realizar el proceso de transacción.
    En este se cargan las credenciales secretas dadas
    por IBM App Connect para utilizar sus servicios.
    '''    
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            with transaction.atomic():
                data = json.loads(json.dumps(request.POST))
                if transaction_request(data):
                    
                    transmiter_account = Account.objects.filter(account_id=data['transmiter_account'])
                    transmiter_account.update()
                    return Response(status=HTTP_201_CREATED)
                else:
                    raise Exception()
        except Exception as ex:
            print('Rollback')
            print(sid)
            transaction.savepoint_rollback(sid)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=HTTP_400_BAD_REQUEST)

@login_required
def transaction_create_render(request):
    user = request.user
    account_list = Account.objects.filter(user=user)
    account_list = list(account_list)
    return render(request, 'api/transaction_create.html', {'account_list': account_list})

class DebitView(APIView):
    '''
    Clase con el servicio para realizar un débito
    a una cuenta registrada.
    '''
    http_method_names = ['put']

    @csrf_exempt
    def put(self, request):

        data = json.loads(request.body)
        
        with transaction.atomic():
            transmiter_account = Account.objects.filter(account_id=data['transmiter_account'])

            if transmiter_account and transmiter_account[0].money_amount >= data['transaction_amount']:
                actual_account = transmiter_account[0].money_amount

                new_amount = actual_account - data['transaction_amount']
                Account.objects.filter(account_id=data['transmiter_account']).update(
                    money_amount=new_amount
                )

                return JsonResponse({'code': 200, 'message': 'Debit correct.'})
            else:
                return Response(status=HTTP_500_INTERNAL_SERVER_ERROR, 
                    data={'reason': 'Not enough money.'})

class CreditView(APIView):
    '''
    Clase con el servicio para realizar un crédito
    a una cuenta registrada.
    '''

    @csrf_exempt
    def put(self, request):
        data = json.loads(request.body)
        
        with transaction.atomic():
            receiver_account = Account.objects.filter(account_id=data['receiver_account'])

            if receiver_account:
                actual_account = receiver_account[0].money_amount

                new_amount = actual_account + data['transaction_amount']
                Account.objects.filter(account_id=data['receiver_account']).update(
                    money_amount=new_amount
                )

                return JsonResponse({'code': 200, 'message': 'Credit correct.'})
            else:
                return JsonResponse({'code': 400, 'message': 'Something went wrong!'})