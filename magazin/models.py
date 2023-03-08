from django.db import models
from userapp.models import Profil

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=500)
    narx = models.FloatField()
    brend = models.CharField(max_length=500)
    davlat = models.CharField(max_length=100)
    kafolat = models.CharField(max_length=100)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    min_miqdor = models.PositiveIntegerField(default=1)
    tasdiqlangan = models.BooleanField(default=True)
    yetkazish = models.CharField(max_length=15)
    mavjud = models.BooleanField(default=True)
    chegirma = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Media(models.Model):
    rasm = models.FileField(upload_to="mahsulotlar")
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Izoh(models.Model):
    baho = models.FloatField(max_length=5)
    matn = models.CharField(max_length=1000)
    sana = models.DateField()
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, null=True)



