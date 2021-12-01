from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.serializers import Serializer

from . models import User
from . serializers import UserSerializer

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.views import APIView

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
