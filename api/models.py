from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    '''
    Clase usuario que abstrae los datos
    '''
    email = models.EmailField(
        max_length=150, unique=True)
    dni = models.TextField(
        unique=True, max_length=10)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'dni']


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Account(models.Model):
    '''
    Clase cuenta que crea una cuenta usando los datos del usuario
    '''
    id = models.IntegerField(primary_key=True)
    account_id = models.CharField(
        unique=True, max_length=15)
    money_amount = models.FloatField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return f'{self.account_id} {self.money_amount}'

class Transaction(models.Model):
    '''
    Clase de transacción que recibe datos necesarios para realizar una transacción
    '''
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    transaction_amount = models.FloatField()

    transmitter_account = models.CharField(
        max_length=15)
    transmitter_bank = models.CharField(
        max_length=30)
    transmitter_name = models.CharField(
        max_length=100)
    transmitter_email = models.EmailField(
        max_length=150)

    receiver_account = models.CharField(
        max_length=15)
    receiver_bank = models.CharField(
        max_length=30)
    receiver_name = models.CharField(
        max_length=100)
    receiver_email = models.EmailField(
        max_length=150)

    def __str__(self):
        return f'{self.id} {self.transaction_amount}'