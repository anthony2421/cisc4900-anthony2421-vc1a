from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("county/admin", views.counties, name = "list"),
    path("county/", views.county, name = "home")
]