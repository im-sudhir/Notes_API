from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    note=models.CharField(max_length=300)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
