from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=50, validators=[MinLengthValidator(8)])