from django.shortcuts import render, redirect
from django.contrib import messages
from APP.models import *
from APP.forms import *

# Create your views here.
def inicio(req):
    # futura carátula de la página
    return render(req, 'index.html')

def agregarFamiliar(req):
    # 2) chequeo que la info venga por verbo POST
    if req.method == 'POST':
        formulario = FormularioPersonas(req.POST)
        
        # 3) chequeo validaciones de los datos que recibo del formulario
        if formulario.is_valid():
            # 4) limpio el formulario
            data = formulario.cleaned_data
            
            # 5) inserto datos y guardo en db
            familiar = Familiares(nombre=data.get('nombre'), email=data.get('email'), edad=data.get('edad'), registro=data.get('registro'))
            familiar.save(data)
            
            messages.info(req,
                  f'Se ha agregado a: {familiar.nombre} a tus familiares.')
            
            # 6) redirijo a 
            return redirect('inicio')
    
    # 1) cargo el formulario vacio para que sea completado por el usuario
    contexto = {
        'form': FormularioPersonas()
    }
    return render(req, 'formulario.html', contexto)

def agregarAmigo(req):
    # 2) chequeo que la info venga por verbo POST
    if req.method == 'POST':
        formulario = FormularioPersonas(req.POST)
        
        # 3) chequeo validaciones de los datos que recibo del formulario
        if formulario.is_valid():
            # 4) limpio el formulario
            data = formulario.cleaned_data
            
            # 5) inserto datos y guardo en db
            amigo = Amigos(nombre=data.get('nombre'), email=data.get('email'), edad=data.get('edad'), registro=data.get('registro'))
            amigo.save(data)
            
            messages.info(req,
                  f'Se ha agregado a: {amigo.nombre} a tus amigos.')
            
            # 6) redirijo a 
            return redirect('inicio')
    
    # 1) cargo el formulario vacio para que sea completado por el usuario
    contexto = {
        'form': FormularioPersonas()
    }
    return render(req, 'formulario.html', contexto)


def agregarColega(req):
    # 2) chequeo que la info venga por verbo POST
    if req.method == 'POST':
        formulario = FormularioPersonas(req.POST)
        
        # 3) chequeo validaciones de los datos que recibo del formulario
        if formulario.is_valid():
            # 4) limpio el formulario
            data = formulario.cleaned_data
            
            # 5) inserto datos y guardo en db
            colega = Colegas(nombre=data.get('nombre'), email=data.get('email'), edad=data.get('edad'), registro=data.get('registro'))
            colega.save(data)
            
            messages.info(req,
                  f'Se ha agregado a: {colega.nombre} a tus colegas.')
            
            # 6) redirijo a 
            return redirect('inicio')
    
    # 1) cargo el formulario vacio para que sea completado por el usuario
    contexto = {
        'form': FormularioPersonas()
    }
    return render(req, 'formulario.html', contexto)


def busqueda_nombre(request):

    contexto = {
        'form': BusquedaFamiliarFormulario(),
        'formAmigo': BusquedaAmigoFormulario(),
        'formColega': BusquedaColegaFormulario(),
    }
    return render(request, 'formulario_filtrado.html', contexto)


def busqueda_nombre_post(request):
    nombre  = request.GET.get('nombre')

    nombres = Familiares.objects.filter(nombre__icontains = nombre)



    contexto = {
        'nombres' : nombres
    }
    return render(request, 'formulario_filtrado_resultado.html', contexto)


def busqueda_nombre_post_amigo(request):
    nombre  = request.GET.get('nombre')

    nombres = Amigos.objects.filter(nombre__icontains = nombre)

    contexto = {
        'nombres' : nombres
    }
    return render(request, 'formulario_filtrado_resultado.html', contexto)

def busqueda_nombre_post_colega(request):
    nombre  = request.GET.get('nombre')

    nombres = Colegas.objects.filter(nombre__icontains = nombre)

    contexto = {
        'nombres' : nombres
    }
    return render(request, 'formulario_filtrado_resultado.html', contexto)


def mostrar_todo(request):

    familiares = Familiares.objects.all()
    amigos = Amigos.objects.all()
    colegas = Colegas.objects.all()



    contexto = {

        'familiares': familiares,
        'amigos': amigos,
        'colegas': colegas,


    }
    return render(request, 'mostrar_todo.html', contexto)

