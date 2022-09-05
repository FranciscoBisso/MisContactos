from django.urls import path
from APP.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar_familiar', agregarFamiliar, name='agregarFamiliar'),
    path('agregar_amigo', agregarAmigo, name='agregarAmigo'),
    path('agregar_colega', agregarColega, name='agregarColega'),
    path('busqueda_nombre', busqueda_nombre, name="busquedaFormulario"),
    path('busqueda_nombre_post', busqueda_nombre_post, name="busquedaFormulario_Post"),
    path('busqueda_nombre_post_amigo', busqueda_nombre_post_amigo, name="busquedaFormulario_Post_Amigo"),
    path('busqueda_nombre_post_colega', busqueda_nombre_post_colega, name="busquedaFormulario_Post_colega"),
]
