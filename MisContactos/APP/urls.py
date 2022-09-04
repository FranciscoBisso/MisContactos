from django.urls import path
from APP.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
]
