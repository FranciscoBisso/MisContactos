from django.shortcuts import render
from APP.forms import FamiliaresForms
from APP.models import Familiares

# Create your views here.
def inicio(req):
    # futura carátula de la página
    return render(req, 'index.html')


def buscar_contacto(request):

    if request.method == 'POST':
       # mi_formulario = FamiliaresForms(request.POST)

       """ if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            familiar1 = Familiares(nombre=data.get('nombre'),camada=data.get('camada'))
            familiar1.save()

         return redirect('AppCoderCursoFormulario')  """

    familiares = Familiares.objects.all()

    contexto = {

       # 'form': CursoFormulario(),
        'familiares': familiares

    }
    return render(request, 'APP/BuscarContacto.html', contexto)

def buscar_contactoEspecifico(request):
    familia = request.GET.get('buscar', None)

    familiares = Familiares.objects.filter(nombre__icontains=familia)

    contexto = {
        'familiares': familiares
    }
    return render(request, 'APP/Buscar.html', contexto)

def busqueda_camada(request):

    contexto = {
        'form' : BusquedaCamadaFormulario(),
    }
    return render(request, 'AppCoder/busquedaCamada.html', contexto)