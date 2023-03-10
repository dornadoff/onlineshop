from django.shortcuts import render
from django.views import View
from .models import *
from userapp.models import *
from django.db.models import *

class SavatView(View):
    def get(self, request):
        pr = Profil.objects.get(user=request.user)
        savat = Savat.objects.filter(profil=pr)
        data = {
            "savat":savat,
            "sum": savat.aggregate(Sum("mahsulot__narx"))["mahsulot__narx__sum"]
        }
        print(savat.aggregate(Sum("mahsulot__narx")))
        return render(request, "page-shopping-cart.html", data)

class BuyurtmaView(View):
    def get(self, request):
        buyurtma = Buyurtma.objects.filter(user=request.user)
        SUM = 0
        for i in buyurtma:
            SUM += i.mahsulot.narx
        data = {
            "mahsulot":buyurtma,
            "profil":Profil.objects.get(user=request.user),
            "hammasi":SUM
        }
        return render(request, "page-profile-orders.html", data)

class TanlanganView(View):
    def get(self, request):
        data = {
            "mahsulot":Tanlangan.objects.filter(user=request.user)
        }
        return render(request, "page-profile-wishlist.html", data)