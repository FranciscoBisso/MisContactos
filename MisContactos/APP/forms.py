from django import forms

class FormularioPersonas(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()
    registro = forms.DateField()


class BusquedaFamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class BusquedaAmigoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class BusquedaColegaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)