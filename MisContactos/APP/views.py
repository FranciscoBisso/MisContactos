from django.shortcuts import render

# Create your views here.
def inicio(req):
    # futura carátula de la página
    return render(req, 'index.html')