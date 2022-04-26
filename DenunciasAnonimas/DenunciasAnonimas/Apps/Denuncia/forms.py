from django import forms
from .models import Denuncia
from django.contrib.auth.hashers import (PBKDF2PasswordHasher, SHA1PasswordHasher,)
import hashlib
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings


def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY)  # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        # log the error if any
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

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

    def clean_acusado(self):
        acusado = self.cleaned_data['acusado']
        acusado = encrypt(acusado)
        #print(acusado)
        #print('Profesor encriptado: ',encrypt(acusado))
        return acusado


