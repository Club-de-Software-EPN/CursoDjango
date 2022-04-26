from django import forms
from .models import Denuncia
from django.contrib.auth.hashers import (PBKDF2PasswordHasher, SHA1PasswordHasher,)
import hashlib

class FormDenuncia(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ('titulo', 'tema', 'codigo', 'acusado', 'mensaje')

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        print(hash(codigo))
        if len(codigo) != 9:
            raise forms.ValidationError('El código único debe ser de 9 dígitos')
        else:
            print('Else del código')
            codigo = hashlib.sha256(codigo.encode('utf-8')).digest()
            # Deberín buscar si esta en la base de datos
            # si existe un registro que sea igual a codigo
        return codigo

    #def clean_acusado(self):
        #pass


