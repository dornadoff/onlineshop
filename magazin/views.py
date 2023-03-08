from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth.models import User
from django.db.models import Avg

class Home2View(View):
    def get(self, request):
        return render(request, "page-index-2.html")

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:

            data = {
                "bolimlar":Bolim.objects.all()[:7],
                "chegirmalilar":Mahsulot.objects.filter(chegirma__gt=0).order_by("-chegirma")[:5]
            }
            return render(request, "page-index.html", data)
        return redirect("/")

class BolimlarView(View):
    def get(self, request):

        data = {
            "bolim":Bolim.objects.all(),
            "mahsulot":Mahsulot.objects.all()
        }
        return render(request, "page-category.html", data)

class BittaBolimView(View):
    def get(self, request, pk):
        data = {
            "mahsulot":Mahsulot.objects.filter(bolim__id=pk)
        }
        return render(request, "page-listing-grid.html", data)

class BittaMahsulotView(View):
    def get(self, request, pk):
        mahsulot1 = Mahsulot.objects.get(id=pk)
        izoh = Izoh.objects.filter(mahsulot=mahsulot1)
        ortachasi = izoh.aggregate(Avg("baho")).get("baho__avg")
        if ortachasi:
            ortachasi *= 20

        data = {
            "mahsulot":mahsulot1,
            "medialar":Media.objects.filter(mahsulot__id=pk),
            "izohlar":izoh,
            "ortacha":ortachasi
        }
        return render(request, "page-detail-product.html", data)

    def post(self, request, pk):
        user1 = request.user

        Izoh.objects.create(
            baho=request.POST.get("rating"),
            matn=request.POST.get("comment"),
            profil=Profil.objects.get(user=user1),
            mahsulot=Mahsulot.objects.get(id=pk)
        )
        return redirect(f"/magazin/bolim/mahsulot/{pk}/")
