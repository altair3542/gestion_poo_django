from django import forms
from .models import OrdenServicio

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
