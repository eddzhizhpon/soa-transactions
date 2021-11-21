from django.db import models

# Create your models here.
class User(models.Model):

    id = models.IntegerField(primary_key=True)
    firstname = models.TextField()
    lastname = models.TextField()
    username = models.TextField()
    dni = models.TextField(default='None')
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Account(models.Model):

    id = models.IntegerField(primary_key=True)
    account_id = models.TextField()
    money_amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)

class Transaction(models.Model):

    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    transmitter_account = models.ForeignKey(Account, related_name='transaction_transmiter_account', on_delete=models.DO_NOTHING, null=False)
    receiver_account = models.ForeignKey(Account, related_name='transaction_receiver_account', on_delete=models.DO_NOTHING, null=False)