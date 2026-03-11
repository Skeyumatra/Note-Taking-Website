from django.forms import ModelForm,PasswordInput
from . import models

class LoginForm(ModelForm):
    class Meta:
        model=models.User
        fields=["name","password"]
        widgets= {"password":PasswordInput()}

