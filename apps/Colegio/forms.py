from django import forms

class sedeForm(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    telefono=forms.CharField()
    correo=forms.CharField()
