from django.urls import path
from .views import *

urlpatterns = [
    path("savat/", SavatView.as_view()),
    path("", BuyurtmaView.as_view()),
    path("tanlangan/", TanlanganView.as_view()),
    path("savat_q/<int:pk>/", MiqdorQoshView.as_view()),
    path("savat_k/<int:pk>/", MiqdorKamView.as_view()),
    path("tanlangan_qosh/<int:pk>/", TanlanganQoshishView.as_view())
]