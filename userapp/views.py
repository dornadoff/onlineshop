from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from userapp.models import Profil

class LoginView(View):
    def get(self, request):
        return render(request, "page-user-login.html")

    def post(self, request):
        user = authenticate(request, username=request.POST.get("username"),
                            password=request.POST.get("password"))
        if user is None:
            return redirect("login")
        login(request, user)
        return redirect("/magazin/home/")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class RegisterView(View):
    def post(self, request):
        if request.POST.get("password") == request.POST.get("password_2"):
            a = User.objects.create_user(
                username=request.POST.get("username"),
                password=request.POST.get("password"),
                email=request.POST.get("email")
            )
            Profil.objects.create(
                ism=request.POST.get("ism"),
                familia=request.POST.get("familia"),
                jins=request.POST.get("gender"),
                shahar=request.POST.get("shahar"),
                davlat=request.POST.get("davlat"),
                user=a
            )
            return redirect("/magazin/home/")
    def get(self, request):
        return render(request, "page-user-register.html")
