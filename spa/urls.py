from django.urls import path, include
from .views import HomeTemplateView, AppointmantTemplateView


urlpatterns = [
    path("",HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/",AppointmantTemplateView.as_view(), name="appointment"),
]
 