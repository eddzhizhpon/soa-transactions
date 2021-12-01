from django.conf import settings

def bank_setting_names(request):
    '''
    Identificador del tipo de proveedor o Banco
    '''
    return {
        'bank_name': settings.BANK_NAME
    }