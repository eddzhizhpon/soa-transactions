"""soa_transaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

# Para SchemaView
from rest_framework import permissions, routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib.auth.views import LoginView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

'''Rutas definidas para la conexión de la api
admin -> ruta establecida para configuracion de usuarios usando django
api -> ruta establecida para manejo de las transacciones en base a la api creada
/ -> ruta establecida para el inicio o index de la api
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('', include('api.routers')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('api/', include(router.urls)),
    path('',
        LoginView.as_view(template_name='api/login.html'), name='auth_login'),
]

'''
urls para la comunicación con el ESB mediante usos de json y distintos parametros
'''
urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
