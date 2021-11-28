from django.db.models.fields import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.serializers import Serializer

from . models import User, Account
from . serializers import UserSerializer

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


from django.db import transaction
import json

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response(UserSerializer(user).data, status=HTTP_200_OK)

        return Response(status=HTTP_404_NOT_FOUND)     

class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return Response(status=HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer


# ¿Interno y externo? ¿Solo uno?
# class IsAccountValid(APIView):
#     pass

# class DebitView(APIView):
#     pass

# class CreditView(APIView):
#     pass


class DebitView(APIView):
    http_method_names = ['put']

    @csrf_exempt
    def put(self, request):
        
        data = json.loads(request.body)

        print(data)
        
        with transaction.atomic():
            transmiter_account = Account.objects.filter(account_id=data['transmiter_account'])

            print(transmiter_account)

            if transmiter_account and transmiter_account[0].money_amount >= data['transaction_amount']:
                actual_account = transmiter_account[0].money_amount
                transmiter_account[0].money_amount = actual_account - data['transaction_amount']
                transmiter_account.update()

                return JsonResponse({'code': 200, 'message': 'Debit correct.'})
            else:
                return JsonResponse({'code': 400, 'message': 'Not enough money.'})


class CreditView(APIView):
    @csrf_exempt
    def put(self, request):
        data = json.loads(request.body)
        
        with transaction.atomic():
            receiver_account = Account.objects.filter(account_id=data['receiver_account'])

            if receiver_account:
                actual_account = receiver_account.money_amount
                receiver_account.money_amount = actual_account + data['transaction_amount']
                receiver_account.update()

                return JsonResponse({'code': 200, 'message': 'Credit correct.'})
            else:
                return JsonResponse({'code': 400, 'message': 'Something went wrong!'})