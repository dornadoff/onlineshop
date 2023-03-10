from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=10)
    shahar = models.CharField(max_length=100)
    davlat = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.ism