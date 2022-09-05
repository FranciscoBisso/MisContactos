from django.urls import path
from APP.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar_contacto', agregar_contacto, name='agregarContacto'),
    path('agregar_familiar', agregar_familiar, name='agregarFamiliar'),
    path('agregar_amigo', agregar_amigo, name='agregarAmigo'),
    path('agregar_colega', agregar_colega, name='agregarColega'),
    path('busqueda_nombre', busqueda_nombre, name="busquedaFormulario"),
    path('busqueda_nombre_post', busqueda_nombre_post, name="busquedaFormulario_Post"),
    path('busqueda_nombre_post_amigo', busqueda_nombre_post_amigo, name="busquedaFormulario_Post_Amigo"),
    path('busqueda_nombre_post_colega', busqueda_nombre_post_colega, name="busquedaFormulario_Post_colega"),
]
