from django.urls import path
from APP.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar_familiar', agregarFamiliar, name='agregarFamiliar'),
    path('agregar_amigo', agregarAmigo, name='agregarAmigo'),
    path('agregar_colega', agregarColega, name='agregarColega'),
]
