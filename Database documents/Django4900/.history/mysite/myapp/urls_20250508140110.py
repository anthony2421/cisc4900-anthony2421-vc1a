from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("county(admin)", views.counties, name = "list"),
    path("county/", views.county, name = "home"),
    path("county/kings", views.kings, name = "King's County"),
    path("county/schools(admin)", views.schools, name = "list2"),
    path("county/school/pathways(admin)", views.pathways, name=  "list3"),
    path("county/school/Brooklyn-College", views.brooklynCollege, name = "BrooklynCollege")
]