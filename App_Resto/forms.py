from django import forms

class ConsultaFormulario(forms.Form):

    nombre = forms.CharField()
    pregunta = forms.CharField()