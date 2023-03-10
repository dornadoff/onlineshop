from django.db import models
from magazin.models import *
from django.contrib.auth.models import User
from userapp.models import *

class Tanlangan(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Buyurtma(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, null=True)
    sana = models.DateField(auto_now=True)

class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    umumiy = models.PositiveIntegerField(null=True)
    miqdor = models.PositiveIntegerField(null=True, default=1)




