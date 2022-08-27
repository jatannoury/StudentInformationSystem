from django.db import models

# Create your models here.
from django.db import models

class sisUser(models.Model):
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    isAdmin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    