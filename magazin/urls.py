from django.urls import path
from .views import *

urlpatterns = [
    path("home/", HomeView.as_view(), name='home'),
    path("bolim/", BolimlarView.as_view()),
    path("bolim/<int:pk>/", BittaBolimView.as_view()),
    path("bolim/mahsulot/<int:pk>/", BittaMahsulotView.as_view(), name="product")
]