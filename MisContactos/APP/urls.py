from django.urls import path
from APP.views import inicio,buscar_contacto,buscar_contactoEspecifico



urlpatterns = [
    path('', inicio, name='inicio'),
    path('buscar_contacto/', buscar_contacto, name='buscar_contacto'),
    path('buscar/', buscar_contactoEspecifico, name='buscar'),
]
