from django.urls import path
from .views import *

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view()),
    path("register/", RegisterView.as_view(), name='register'),
    path("profil/", ProfilView.as_view()),
    path("seller/", SellerView.as_view()),

]