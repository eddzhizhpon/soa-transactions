from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import EmailField

from django.contrib.auth.hashers import make_password

from .models import Account, User

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True)
    last_name = serializers.CharField(
        required=True)
    username = serializers.CharField(
        required=True)
    email = serializers.EmailField(
        required=True)
    dni = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'dni', 'password')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')