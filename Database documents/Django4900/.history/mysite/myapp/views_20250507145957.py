from django.shortcuts import render, HttpResponse
from .models import County
from .models import School

# Create your views here.
def home(request):
    return render(request, "base.html")

def counties(request):
    items = County.objects.all()
    items2 = School.objects.all()
    return render(request, "list.html", {"names": items})

def county(request):
    return render(request, "home.html")

def schools(request):
    schoolList - School.objects.all()
    return render(request, "list2.html", {"names": schoolList})