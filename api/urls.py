from django.urls import path, include

from .views import LoginView, LogoutView, SignupView, CreditView, DebitView

urlpatterns = [
    path('auth/login/',
        LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
        LogoutView.as_view(), name='auth_logout'),

    path('auth/signup/',
        SignupView.as_view(), name='auth_signup'),

    path('transfer/debit/',
        DebitView.as_view(), name='transfer_debit'),

    path('transfer/credit/',
        CreditView.as_view(), name='transfer_credit'),
]
