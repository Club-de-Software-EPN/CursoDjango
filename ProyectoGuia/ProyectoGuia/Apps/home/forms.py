from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese texto aquí'})
        }

    def clean_cantidad(self):
        titulo = self.cleaned_data['titulo']
        subtitulo = self.cleaned_data['subtitulo']
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            #cantidad = 12
            raise forms.ValidationError('Ingrese un número mayor a 10')
        #cantidad = 50
        return cantidad

    #def _post_clean(self):
     #   cantidad = 150


