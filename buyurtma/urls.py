from django.urls import path
from .views import *

urlpatterns = [
    path("savat/", SavatView.as_view()),
    path("", BuyurtmaView.as_view()),
    path("tanlangan/", TanlanganView.as_view()),
    path("savat_q/<int:pk>/", MiqdorQoshView.as_view()),
    path("savat_k/<int:pk>/", MiqdorKamView.as_view()),
    path("tanlangan_qosh/<int:pk>/", TanlanganQoshishView.as_view()),
    path("tanlangan/ochirish/<int:pk>/", TanlanganOchirishView.as_view()),
    path("savat/qoshish/<int:pk>/", SavatQoshishView.as_view()),
    path("mahsulot/qoshish/<int:pk>/", MahsulotMiqdorQoshish.as_view()),
    path("mahsulot/ayrish/<int:pk>/", MahsulotMiqdorAyrish.as_view()),
    path("savat/ochirish/<int:pk>/", SavatOchirishView.as_view())
]