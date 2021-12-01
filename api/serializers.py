from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import EmailField

from django.contrib.auth.hashers import make_password

from .models import Account, User

# Serialización de usuarios y validación de datos que se envian al ESB
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

# Serialización de la cuenta que se envia al ESB
class AccountSerializer(serializers.ModelSerializer):
    account_id = serializers.CharField(
        required=True)
    money_amount = serializers.CharField(
        required=True)

    class Meta:
        model = Account
        fields = ('account_id', 'money_amount')