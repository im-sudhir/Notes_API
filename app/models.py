from django.db import models

# Create your models here.

class Notes(models.Model):
    note=models.CharField(max_length=300)
    author=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)