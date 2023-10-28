# Modificar los formularios de la aplicación
# home que aparecen por defecto en la pagina html
from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )

        widgets = {
            'cantidad': forms.NumberInput(
                attrs = {
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }

    # Validacion de los campos del formulario
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad

