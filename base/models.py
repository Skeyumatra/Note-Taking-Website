from django.db import models
from accounts.models import User
# Create your models here.

class Note(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title=models.CharField(max_length=10)
    content=models.TextField(max_length=500)
