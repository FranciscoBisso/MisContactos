from django import forms

class FamiliaresForms(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()
    registro = forms.DateField()
