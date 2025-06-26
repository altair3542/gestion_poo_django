from django import forms
from .models import OrdenServicio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrdenServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenServicio
        fields = ['descripcion', 'estado', 'comentario_final']

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get('estado')
        comentario = cleaned_data.get('comentario_final')

        if estado == 'finalizada' and not comentario:
            raise forms.ValidationError("Para poder cerrar una orden, debes ingresar un comentario final.")
        return cleaned_data

class RegistroTecnicoForm(UserCreationForm):
    cargo = forms.ChoiceField(choices=[
        ('tecnico', 'Técnico'),
        ('supervisor', 'Supervisor'),
    ])
    especialidad = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'cargo', 'especialidad']
