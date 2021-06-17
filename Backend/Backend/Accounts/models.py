from django.db import models

# Create your models here.

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['created']