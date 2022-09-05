from django import forms

class FormularioPersonas(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()
    registro = forms.DateField()