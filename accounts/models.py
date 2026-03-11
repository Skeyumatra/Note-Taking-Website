from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20, unique=True)
    password=models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    isOnline=models.BooleanField(default=False)  #this is for login page-home page transitions