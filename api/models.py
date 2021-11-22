from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser

from django.conf import settings

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    dni = models.TextField(
        unique=True, max_length=10)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'dni']


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    account_id = models.TextField()
    money_amount = models.FloatField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False)

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    transmitter_account = models.ForeignKey(Account, related_name='transaction_transmiter_account', on_delete=models.DO_NOTHING, null=False)
    receiver_account = models.ForeignKey(Account, related_name='transaction_receiver_account', on_delete=models.DO_NOTHING, null=False)