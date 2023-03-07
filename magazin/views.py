from django.shortcuts import render, redirect
from django.views import View
from .models import *

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
        mahsulot = Mahsulot.objects.get(id=pk)
        data = {
            "mahsulot":mahsulot,
            "medialar":Media.objects.filter(mahsulot__id=pk)
        }
        return render(request, "page-detail-product.html", data)