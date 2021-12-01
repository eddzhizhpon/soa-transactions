from django.conf import settings

def bank_setting_names(request):
    return {
        'bank_name': settings.BANK_NAME
    }