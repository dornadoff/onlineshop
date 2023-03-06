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