from django import forms

class ContactoFormulario(forms.Form):

    nombre = forms.CharField()
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()