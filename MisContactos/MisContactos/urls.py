
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('APP/', include('APP.urls')),
    path('', lambda req: redirect('inicio')),
]
