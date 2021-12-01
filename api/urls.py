from django.contrib.auth import logout
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    SignupView,
    CreditView, DebitView, transaction_create_render,
    transaction_create, generate_password
)

'''
Rutas definidas para identificar las diferentes funcionalides con las que cuenta la api de transacción
'''
urlpatterns = [
    path('auth/login/',
        LoginView.as_view(template_name='api/login.html'), name='auth_login'),

    path('auth/logout/',
        LogoutView.as_view(), name='auth_logout'),

    path('auth/signup/',
        SignupView.as_view(), name='auth_signup'),

    path('auth/genpassword',
        generate_password, name='auth_genpassword'),

    path('debit',
        DebitView.as_view(), name='transfer_debit'),

    path('credit',
        CreditView.as_view(), name='transfer_credit'),

    path('transaction',
        transaction_create_render, name='transaction_create_render'),

    path('transaction/create',
        transaction_create, name='transaction_create')
]
