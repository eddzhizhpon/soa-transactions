from django.conf import settings

# Identificador del tipo de proveedor o Banco
def bank_setting_names(request):
    return {
        'bank_name': settings.BANK_NAME
    }