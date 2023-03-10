from django.shortcuts import render
from django.views import View
from .models import *
from userapp.models import *
from django.db.models import *

class SavatView(View):
    def get(self, request):
        return render(request, "page-shopping-cart.html")

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