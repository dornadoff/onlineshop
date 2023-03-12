from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import *
from django.db.models import Sum

class SavatView(View):
    def get(self, request):
        profil1 = Profil.objects.get(user=request.user)
        savatlar = Savat.objects.filter(profil=profil1)
        summa = savatlar.aggregate(Sum('umumiy'))['umumiy__sum']
        chegirmalar = 0
        for savat in savatlar:
            chegirmalar += savat.miqdor*(savat.mahsulot.chegirma*savat.mahsulot.narx)/100
        data = {
            'savat': savatlar,
            'sum': summa,
            'chg': round(chegirmalar, 2),
            'yakuniy': summa - round(chegirmalar, 2)
        }
        return render(request, 'page-shopping-cart.html', data)

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


class MiqdorQoshView(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user:
            savat.miqdor += 1
            savat.umumiy = savat.miqdor * savat.mahsulot.narx
            savat.save()
        return redirect("/buyurtma/savat/")

class MiqdorKamView(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user and savat.miqdor != 1:
            savat.miqdor -= 1
            savat.umumiy -= savat.mahsulot.narx
            savat.save()
        return redirect("/buyurtma/savat/")

class TanlanganQoshishView(View):
    def get(self, request, pk):
        Tanlangan.objects.create(
            user=request.user,
            mahsulot=Mahsulot.objects.get(id=pk)
        )
        return redirect("/buyurtma/tanlangan/")

